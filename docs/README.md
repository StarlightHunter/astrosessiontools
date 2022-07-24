# Astro session tools

astrosessiontools is a command line application that analyzes the contents of a
given folder and reads the images metadata to create a JSON
file with that metadata in an ordered way to be consumed by other apps.

## How to use it?

### Dependencies

astrosessiontools depends on the ***exiftool*** command to extract the metadata from
the image files.

### Usage

```bash
$ ./session_tools.py  path_to_session_directory/ "Session description" "Session location"
```

## Example output file

A file named session_data.json will be written in the session directory.

```json
{
{
  "description": "My session",
  "location": {
    "name": "Home"
  },
  "date": "2022-05-28",
  "object": "M16",
  "image_groups": [
    {
      "file_type": "image/fits",
      "iso_gain": 1600,
      "exposure": 60.0,
      "temperature": "20.",
      "filter": null,
      "image_type": "Light",
      "image_files": [
        {
          "path": "test_image_01.fit",
          "file_type": "image/fits",
          "iso_gain": 1600,
          "exposure": 60.0,
          "temperature": "20.",
          "filter": null,
          "image_type": "Light",
          "timestamp": "2022-05-28T01:06:49.078653",
          "camera": "Canon EOS 4000D",
          "telescope": "EQMod Mount",
          "focal_length": 129,
          "aperture": null,
          "fnumber": null,
          "object": "M16",
          "width": 5202,
          "height": 3465,
          "bits": 16,
          "pixel_width": 4.28999996185303,
          "pixel_height": 4.28999996185303,
          "bin_width": 1,
          "bin_height": 1,
          "ra": 275.3055,
          "dec": -14.7023
        }
      ]
    }
  ]
}
```

## Location data loading

You can specify a location data file to use that information
as part of the final session information.

The file must be a JSON file with location identifiers as keys
of the main JSON object.

This is a sample location data file

```json
{
    "location_a": {
        "name": "Location A",
        "desc": "Pico de las Nieves",
        "gps": "27°58'06.7\"N 15°33'55.2\"W",
        "gps_decimal": [27.968518, -15.565340],
        "map_url": "https://goo.gl/maps/sYfwgrnu77DTK5kcA",
    },
    "location_b": {
        "name": "Location B",
        "desc": "Llanos de la Pez",
        "gps": "27°58'33.4\"N 15°34'55.1\"W",
        "gps_decimal": [27.975933, -15.581974],
        "map_url": "https://goo.gl/maps/ZDDTBbxJ76eDojEp8",
    }
}
```

Save the contents to a json file. Let's call it locations.json

Then, you can execute astrosessiontools like this:

```bash
$ ./astro_session_tools.py session_dir "Weekend session for Orion Nebula" location_b --locdata locations.json
```

This will get all the information in the ***location_b*** object
and append it to the location in the final session_data.json file.

For example:

```json
{
  "description": "My session",
  "location": {
    "name": "Location B",
    "desc": "Llanos de la Pez",
    "gps": "27\u00b058'33.4\"N 15\u00b034'55.1\"W",
    "gps_decimal": [
      27.975933,
      -15.581974
    ],
    "maps_url": "https://goo.gl/maps/ZDDTBbxJ76eDojEp8"
  },
  "date": "2022-05-28",
  "object": "M16",
  "image_groups": [
    {
      "file_type": "image/fits",
      "iso_gain": 1600,
      "exposure": 60.0,
      "temperature": "20.",
      "filter": null,
      "image_type": "Light",
      "image_files": [
        {
          "path": "test_image_01.fit",
          "file_type": "image/fits",
          "iso_gain": 1600,
          "exposure": 60.0,
          "temperature": "20.",
          "filter": null,
          "image_type": "Light",
          "timestamp": "2022-05-28T01:06:49.078653",
          "camera": "Canon EOS 4000D",
          "telescope": "EQMod Mount",
          "focal_length": 129,
          "aperture": null,
          "fnumber": null,
          "object": "M16",
          "width": 5202,
          "height": 3465,
          "bits": 16,
          "pixel_width": 4.28999996185303,
          "pixel_height": 4.28999996185303,
          "bin_width": 1,
          "bin_height": 1,
          "ra": 275.3055,
          "dec": -14.7023
        }
      ]
    }
  ]
}
```

### Location file format

The only mandatory field is the ***name*** field. The rest of
the information is optional.

You can add whatever fields you want to be included, but the
recommended fields are the following:

* **name**: The name for that location
* **description**: A more detailed description of the location
* **gps**: GPS coordinates for the location
* **gps_decimal**: GPS coordinates in decimal format
* **map_url**: An URL for a map application (OpenStreetMap, Google maps...)