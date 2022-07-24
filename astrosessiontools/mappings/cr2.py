"""Metadata mappings for Canon RAW CR2 format"""

# Data formatters for Canon CR2

def temperature_formatter(value):
    """Formats temperature data from "float C" to a real float"""
    return float(value[:-2])

def focallength_formatter(value):
    """Formats focal length data from "float mm" to a real float"""
    return(float(value[:-3]))

def timestamp_formatter(value):
    """Formats date and time from "YYYY:MM:DD HH:MM:SS" to ISO format"""
    date, time = value.split()
    return "T".join([
        date.replace(":", "-"),
        time
    ])


# Metadata mapping
METADATA_MAPPINGS_CR2 = {
    # Grouping fields
    "file_type": {
        "fields": ["mimetype"],
    },
    "iso_gain": {
        "fields": [
            "iso"
        ],
    },
    "exposure": {
        "formatter": float,
        "fields": ["exposuretime"],
    },
    "temperature": {
        "formatter": temperature_formatter,
        "fields": ["cameratemperature"],
    },
    "filter": {
        "fields": [],
    },
    "image_type": {
        "fields": [],
    },
    # Non grouping fields
    "timestamp": {
        "formatter": timestamp_formatter,
        "fields": ["createdate"],
    },
    "camera": {
        "fields": ["model"],
    },
    "telescope": {
        "fields": [],
    },
    "focal_length": {
        "formatter": focallength_formatter,
        "fields": ["focallength"],
    },
    "aperture": {
        "fields": ["aperturevalue"],
    },
    "fnumber": {
        "fields": ["fnumber"],
    },
    "object": {
        "fields": [],
    },
    "width": {
        "fields": ["imagewidth"],
    },
    "height": {
        "fields": ["imageheight"],
    },
    "bits": {
        "fields": []
    },
    "pixel_width": {
        "fields": [],
    },
    "pixel_height": {
        "fields": [],
    },
    "bin_width": {
        # Binning is always 1 in RAW files
        "default": 1,
        "fields": [],
    },
    "bin_height": {
        # Binning is always 1 in RAW files
        "default": 1,
        "fields": [],
    },
    "ra": {
        "fields": [],
    },
    "dec": {
        "fields": [],
    },
}
