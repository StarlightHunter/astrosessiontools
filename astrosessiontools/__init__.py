"""astrosessiontools module"""

import os
import sys
import json
import datetime

from . import utils
from . import mappings


class Session:
    """Session class"""

    def __init__(self, directory, description, location):
        self.directory = directory
        self.description = description
        self.location = {"name": location}
        self.date = None
        self.object = None
        self.image_groups = []
        self.filepath = os.path.join(self.directory, "session_data.json")
        # Options
        self.include_full_metadata = False

    def load_location_data(self, filepath, location):
        """Load location data for a location from a location data file"""
        if not os.path.exists(filepath):
            print(f"Error: Location data file {filepath}")
            sys.exit(1)
        with open(filepath, "r", encoding="utf-8") as file_pointer:
            location_data = json.load(file_pointer)
            if location in location_data:
                self.location = location_data[location]
            else:
                print("Warning: Specified location not found in location data file")

    def analyze_session(self):
        """Analyzes the session directory"""
        # Check session dir
        if not os.path.isdir(self.directory):
            print(f"Error: Directory {self.directory} does not exist")
            sys.exit(1)
        if os.path.exists(self.filepath):
            response = input(
                f"Session file {self.filepath} already exists. Overwrite? "
            )
            if response.lower() not in ["y", "yes"]:
                print("Aborting")
                sys.exit(1)
        # Find image files in directory
        for current_dir, _, file_list in os.walk(self.directory):
            for filename in file_list:
                extension = os.path.splitext(filename)[-1][1:].lower()
                if extension in ["fit", "fits", "cr2"]:
                    rel_dir = os.path.relpath(current_dir, self.directory)
                    if rel_dir != ".":
                        filepath = os.path.join(rel_dir, filename)
                    else:
                        filepath = filename
                    self.process_image(filepath)

    def process_image(self, filepath):
        """Process the image metadata and adds it to an image group"""
        print(f"Processing file {filepath}")
        image = ImageFile(self, filepath)
        image.analyze_image()
        # Update session date according image timestamp
        if image.timestamp:
            date = datetime.datetime.fromisoformat(
                image.timestamp  # pylint: disable=no-member
            )
            if self.date:
                if date > self.date:
                    self.date = date
            else:
                self.date = date
        # Update session object according to image object
        if image.object:
            if not self.object:
                self.object = image.object
            else:
                if self.object != image.object:
                    print(f"Warning: object {image.object} read from image {filepath} differs from {self.object}")
                    print(f"    Session directories should only contain files for the same object.")
        # Add image to the correct image group
        image_group = self.get_image_group(image.get_group_data())
        image_group.add_image(image)

    def get_image_group(self, image_group_data):
        """Gets an image group for given group data"""
        # Find an image group with all this specific fields
        for image_group in self.image_groups:
            if image_group.get_group_data() == image_group_data:
                return image_group
        # If there is no group for that information, return a new one with this grouping data
        image_group = ImageGroup(*image_group_data)
        self.image_groups.append(image_group)
        return image_group

    def save(self):
        """Dumps session data to the session_data.json file"""
        image_groups = []
        for image_group in self.image_groups:
            image_groups.append(image_group.serialize())
        data = {
            "description": self.description,
            "location": self.location,
            "date": self.date.date().isoformat(),
            "object": self.object,
            "image_groups": image_groups,
        }
        with open(self.filepath, "w", encoding="utf-8") as file_pointer:
            json.dump(data, file_pointer, indent=2)


class ImageGroup:
    """
    Image group class
    """

    def __init__(
        self,
        file_type,
        iso_gain,
        exposure,
        temperature,
        filter,  # pylint: disable=redefined-builtin
        image_type,
    ):  # pylint: disable=too-many-arguments
        self.file_type = file_type
        self.iso_gain = iso_gain
        self.exposure = exposure
        self.temperature = temperature
        self.filter = filter
        self.image_type = image_type
        self.image_files = []

    def add_image(self, image):
        """Adds an image to this image group"""
        self.image_files.append(image)

    def serialize(self):
        """Serialize this image group"""
        image_files = []
        for image in self.image_files:
            image_files.append(image.serialize())
        return {
            "file_type": self.file_type,
            "iso_gain": self.iso_gain,
            "exposure": self.exposure,
            "temperature": self.temperature,
            "filter": self.filter,
            "image_type": self.image_type,
            "image_files": image_files,
        }

    def get_group_data(self):
        """Gets the image group grouping data"""
        return [
            self.file_type,
            self.iso_gain,
            self.exposure,
            self.temperature,
            self.filter,
            self.image_type,
        ]


class ImageFile:
    """
    Image file class
    """

    def __init__(self, session, filepath):
        self.session = session
        self.filepath = filepath
        self.full_metadata = None
        self.mapping = None
        self.full_path = os.path.join(session.directory, filepath)

    def analyze_image(self):
        """Analyze this image to extract metadata"""
        # Extract metadata from file
        self.full_metadata = utils.get_exif_info(self.full_path)
        # Check file type
        mimetype = self.full_metadata["mimetype"]
        # Select metadata mapping for this file type
        self.mapping = mappings.METADATA_MAPPINGS[mimetype]
        # Load important information into fields
        self.load_metadata_fields()

    def load_metadata_fields(self):
        """Load metadata fields for the image according to this file type metadata mapping"""
        for field, field_info in self.mapping.items():
            # Set default value for field
            default_value = field_info.get("default", None)
            setattr(self, field, default_value)
            # Get value if the field exists
            for metadata_field in field_info["fields"]:
                value = self.full_metadata.get(metadata_field, None)
                if value is not None:
                    if "formatter" in field_info:
                        value = field_info["formatter"](value)
                    setattr(self, field, value)
                    break

    def get_group_data(self):
        """Get the image grouping data for this image"""
        return [
            # pylint: disable=no-member
            self.file_type,
            self.iso_gain,
            self.exposure,
            self.temperature,
            self.filter,
            self.image_type,
            # pylint: enable=no-member
        ]

    def serialize(self):
        """Serialize this image"""
        data = {
            "path": self.filepath
        }
        for field in self.mapping:
            data[field] = getattr(self, field)
        if self.session.include_full_metadata:
            data["full_metadata"] = self.full_metadata
        return data
