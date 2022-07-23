"""Metadata mappings for FITS format"""

METADATA_MAPPINGS_FITS = {
    # Grouping fields
    "file_type": {
        "fields": ["mimetype"],
    },
    "iso_gain": {
        "fields": [
            "gain",
            "iso",
        ],
    },
    "exposure": {
        "formatter": float,
        "fields": ["exptime"],
    },
    "temperature": {
        "fields": ["ccd-temp"],
    },
    "filter": {
        "fields": ["filter"],
    },
    "image_type": {
        "fields": ["imagetyp"],
    },
    # Non grouping fields
    "timestamp": {
        "fields": ["observationdate"],
    },
    "camera": {
        "fields": ["instrument"],
    },
    "telescope": {
        "fields": ["telescope"],
    },
    "focal_length": {
        "fields": ["focallen"],
    },
    "aperture": {
        "fields": [],
    },
    "fnumber": {
        "fields": [],
    },
    "object": {
        "fields": ["object"],
    },
    "width": {
        "fields": ["naxis1"],
    },
    "height": {
        "fields": ["naxis2"],
    },
    "bits": {
        "fields": ["bitpix"],
    },
    "pixel_width": {
        "fields": ["xpixsz"],
    },
    "pixel_height": {
        "fields": ["ypixsz"],
    },
    "bin_width": {
        "fields": ["xbinning"],
    },
    "bin_height": {
        "fields": ["ybinning"],
    },
    "ra": {
        "fields": ["ra"],
    },
    "dec": {
        "fields": ["dec"],
    },
}
