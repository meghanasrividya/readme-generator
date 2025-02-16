from InquirerPy import inquirer
from rich.console import Console

# License information including badges and notices
LICENSE_INFO = {
    "MIT License": {
        "badge": "[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)",
        "notice": "This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details."
    },
    "Apache License 2.0": {
        "badge": "[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)",
        "notice": "Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for details."
    },
    "GNU General Public License (GPL v3)": {
        "badge": "[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)",
        "notice": "This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. See [LICENSE](LICENSE) for details."
    },
    "GNU Lesser General Public License (LGPL v3)": {
        "badge": "[![License: LGPL v3](https://img.shields.io/badge/License-LGPL_v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)",
        "notice": "This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version. See [LICENSE](LICENSE) for details."
    },
    "Mozilla Public License 2.0 (MPL 2.0)": {
        "badge": "[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)",
        "notice": "This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/."
    },
    "Creative Commons Licenses (CC0, CC BY, etc.)": {
        "badge": "[![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)",
        "notice": "This work is licensed under a Creative Commons license. See the specific license terms for more information."
    },
    "Unlicense": {
        "badge": "[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)",
        "notice": "This is free and unencumbered software released into the public domain. For more information, please refer to [UNLICENSE](UNLICENSE)."
    }
}

def main():
    console = Console()
    console.print("\n[bold cyan]🌟 README Generator 🌟[/bold cyan]", justify="center")
    console.print("[bold]Welcome! Let's create a professional README for your project.[/bold]\n")

    # Collect user inputs
    project_title = inquirer.text(message="Project Title:").execute()
    project_description = inquirer.editor(
        message="Project Description:",
        instruction="(Provide a brief overview of your project. Save and close the editor to continue.)"
    ).execute()
    installation = inquirer.editor(
        message="Installation Instructions:",
        instruction="(Describe how to install the project. Save and close the editor to continue.)"
    ).execute()
    usage = inquirer.editor(
        message="Usage Instructions:",
        instruction="(Explain how to use the project. Save and close the editor to continue.)"
    ).execute()
    license_choice = inquirer.select(
        message="Select License:",
        choices=list(LICENSE_INFO.keys())
    ).execute()
    author_info = inquirer.editor(
        message="Author/Contact Information:",
        instruction="(Provide your contact details. Save and close the editor to continue.)"
    ).execute()

    # Retrieve license details
    license_badge = LICENSE_INFO[license_choice]["badge"]
    license_notice = LICENSE_INFO[license_choice]["notice"]

    # Generate README content
    readme_content = f"""# {project_title} {license_badge}

{project_description}

## Installation

{installation}

## Usage

{usage}

## License

{license_notice}

## Author

{author_info}
"""

    # Write to README.md
    with open("README.md", "w") as file:
        file.write(readme_content)

    console.print("\n[bold green]✅ Success! README.md has been generated.[/bold green]")

if __name__ == "__main__":
    main()