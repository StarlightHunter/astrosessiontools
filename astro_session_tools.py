#!/usr/bin/python3
"""
Main command line application for astrosessiontools
"""
import sys

from astrosessiontools import Session

if __name__ == "__main__":
    session_dir = sys.argv[1]
    session_name = sys.argv[2]
    session_location = sys.argv[3]

    session = Session(session_dir, session_name, session_location)

    session.analyze_session()
    session.save()
