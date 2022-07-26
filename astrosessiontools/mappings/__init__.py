"""Metadata mappings module."""

from .cr2 import METADATA_MAPPINGS_CR2
from .fits import METADATA_MAPPINGS_FITS

METADATA_MAPPINGS = {
    "image/fits": METADATA_MAPPINGS_FITS,
    "image/x-canon-cr2": METADATA_MAPPINGS_CR2
}
