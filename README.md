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
          "object": null,
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

## Contributing to astrosessiontools

Thank you for wanting to contribute! I really appreciate your interest.

Please read the following guidelines for contributing.

## Reporting Bugs

### Before Submitting a Bug Report

- Check if your issue is already reported in our [bug tracker](https://github.com/StarlightHunter/astrosessiontools/issues)
  - If the issue is already reported and is marked as **OPEN**, comment on it
    and if possible and needed, share info about the issue just as if you were
    submitting a new issue
  - If the issue is marked as **CLOSED**, check if your version of astrosessiontools is
    up-to-date or if there are some steps, described in the closed issue, that
    you should follow. If you are still experiencing the issue, please file a
    new issue
- Sometimes a bug is not reported in our bug tracker but instead people ask for
  help somewhere else. In such cases we'd like you to still report the bug and
  share with us any info that could be gathered from those places

### Writing a Bug Report

Writing good bug reports is a nice way to make the job of the maintainers and
other contributors a bit easier.

When writing a bug report:

- **Use a clear and descriptive title**
- **Describe the problem** - Can you reproduce the bug reliably? What first
  triggered the problem? Did it start happening after upgrading your system?
- **Provide steps how to reproduce** - It's easier for us to fix a bug if we can
  reproduce it.
- **Describe the behavior you received and what you expected** - Sometimes it
  may not be clear what the *right* behavior should look like.
- **Provide info about the version of used software** - What version do you use?
- **Provide info about your system** - What distribution do you use?, Which
  version of exiftool do you have installed?


## Making Suggestions

astrosessiontools is not feature-complete and some of it's functionality is
not-there-yet.
We are thankful for all suggestions and ideas but be ready that your suggestion
may be rejected.

### Before Submitting a Suggestion

- Check if your suggestion has not already been made in our [bug tracker](https://github.com/StarlightHunter/astrosessiontools/issues)
  - If it has and is marked as **OPEN**, go ahead and share your own thoughts
    about the topic!
  - If it has and is marked as **CLOSED**, please read the ticket and depending
    on whether the suggestion was accepted or not consider if it is worth
    opening a new issue or not.
- Consider if the suggestion is not too out of scope of the project.

### Writing a Suggestion

When writing a suggestion:

- **Use a clear and descriptive title**
- **Describe the idea** - What parts of astrosessiontools does it affect?
  Is it a major functionality or a minor tweak?
- **Provide step-by-step description of the suggested behavior** so that we
  will understand.
- **Explain why would this idea be useful** - It sounds good to have a lot of
  options but sometimes less is more.

## First Contribution

astrosessiontools is written in [Python](https://python.org)
as it's buildsystem.

Here are some ideas of what you could contribute with:

- Check our [bug tracker](https://github.com/StarlightHunter/astrosessiontools/issues)
  and look for tickets to be fixed.
- Write tests to check astrosessiontools code.
- Write documentation to make easier to use, understand and develop astrosessiontools


## Pull Requests

All pull requests are welcome! Features, bug fixes, fixing of typos, tests,
documentation, code comments and much more.

### Creating a Pull Request

- Document well your changes - This applies to the description of your PR and to
  your commit messages.
- If possible add additional test cases - If there are no tests for the part of
  code you're contributing to, consider opening another PR if you want to
  implement it yourself or file an issue so that somebody else can pick it up.
- Update documentation to reflect your changes

### After Creating a Pull Request

It may take us some time to review your changes and sometimes even longer to
actually merge them. Please, don't interpret this as an act of not appreciating
your efforts! We really appreciate them! Sometimes we may be stuck in different
parts of our lives.

## Style Guide

astrosessiontools is written in [Python](https://python.org) and uses some tools
like pylint to check styling and errors

If you are using Visual Studio Code, there are [plugins](https://marketplace.visualstudio.com/items?itemName=python)
that include all this functionality and throw a warning if you're doing
something wrong.
