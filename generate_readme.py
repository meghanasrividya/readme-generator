from InquirerPy import inquirer
from rich.console import Console
import os

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
        "notice": "This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License."
    },
    "Unlicense": {
        "badge": "[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)",
        "notice": "This is free and unencumbered software released into the public domain. For more details, see [UNLICENSE](UNLICENSE)."
    }
}

def validate_input(value):
    if not value.strip():
        return "This field cannot be empty."
    return True

def get_multiline_input(prompt):
    """Helper function to collect multi-line input."""
    console = Console()
    console.print(prompt)
    lines = []
    while True:
        line = input()
        if line.strip().lower() == "end":
            break
        lines.append(line)
    return "\n".join(lines)

def main():
    console = Console()
    console.print("\n[bold cyan]🌟 README Generator 🌟[/bold cyan]", justify="center")
    console.print("[bold]Welcome! Let's create a professional README for your project.[/bold]\n")

    # Collect user inputs
    project_title = inquirer.text(message="Project Title:", validate=validate_input).execute()
    console.print("\nEnter Project Description (type 'END' on a new line to finish):")
    project_description = get_multiline_input("")
    console.print("\nEnter Installation Instructions (type 'END' on a new line to finish):")
    installation = get_multiline_input("")
    console.print("\nEnter Usage Instructions (type 'END' on a new line to finish):")
    usage = get_multiline_input("")
    
    license_choice = inquirer.select(
        message="Select License:",
        choices=list(LICENSE_INFO.keys())
    ).execute()
    
    author_info = inquirer.text(message="Author/Contact Information:", validate=validate_input).execute()

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
    try:
        with open("README.md", "w") as file:
            file.write(readme_content)
        console.print("\n[bold green]✅ Success! README.md has been generated.[/bold green]")
    except IOError as e:
        console.print(f"\n[bold red]❌ Error: {e}[/bold red]")

if __name__ == "__main__":
    main()