"""Utility functions."""

import json
import subprocess


def get_exif_info(filepath, bin_data=False, lowercase_keys=True):
    """Get EXIF information from file using exiftool command."""
    if bin_data:
        command = f'exiftool -b -json "{filepath}"'
    else:
        command = f'exiftool -json "{filepath}"'
    output = subprocess.getoutput(command)
    data = json.loads(output)[0]
    if lowercase_keys:
        return {k.lower(): v for k, v in data.items()}
    return data
