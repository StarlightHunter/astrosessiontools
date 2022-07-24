#!/usr/bin/python3
"""
Main command line application for astrosessiontools
"""
import sys
import argparse

from astrosessiontools import Session


def parse_args():
    """Parses command line arguments"""
    parser = argparse.ArgumentParser(
        description="Astrophotography session metadata extraction tool"
    )

    parser.add_argument(
        "directory",
        metavar="DIRECTORY",
        type=str,
        help="astrophotography session directory",
    )

    parser.add_argument(
        "description",
        metavar="DESCRIPTION",
        type=str,
        help="description for this astrophotography session",
    )

    parser.add_argument(
        "location",
        metavar="LOCATION",
        type=str,
        help="astrophotography session location",
    )

    parser.add_argument(
        "-l",
        "--locdata",
        default=None,
        metavar="LOCDATA",
        type=str,
        help="location data file",
    )

    parser.add_argument(
        "-f",
        "--fullmetadata",
        action="store_true",
        help="include full metadata for each image",
    )


    return parser.parse_args(sys.argv[1:])


if __name__ == "__main__":
    args = parse_args()

    session = Session(args.directory, args.description, args.location)
    # Load location data if specified
    if args.locdata:
        session.load_location_data(args.locdata, args.location)
    # Set full metadata option
    session.include_full_metadata = args.fullmetadata
        
    session.analyze_session()
    session.save()
