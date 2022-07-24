"""Metadata mappings module"""

from .fits import METADATA_MAPPINGS_FITS
from .cr2 import METADATA_MAPPINGS_CR2

METADATA_MAPPINGS = {
    "image/fits": METADATA_MAPPINGS_FITS,
    "image/x-canon-cr2": METADATA_MAPPINGS_CR2
}
