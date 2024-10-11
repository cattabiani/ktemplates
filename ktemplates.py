import os
import argparse
import yaml


def create_project_structure(project_name, template):
    """Creates project structure based on the YAML template."""
    os.makedirs(project_name)
    for folder in template.get("folders", []):
        path = os.path.join(project_name, folder)
        os.makedirs(path)

    for file in template.get("files", []):
        path = os.path.join(project_name, file)
        with open(path, "w") as f:
            content = template["files"][file]
            f.write(content)


def load_template(template_file):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, template_file)

    """Loads template configuration from YAML file."""
    with open(template_path, "r") as file:
        return yaml.safe_load(file)


def sanitize(template, d):
    """Recursively replaces placeholders in the template with corresponding values from d."""

    if isinstance(template, dict):
        return {sanitize(key, d): sanitize(value, d) for key, value in template.items()}

    elif isinstance(template, list):
        return [sanitize(item, d) for item in template]

    elif isinstance(template, str):
        for key, value in d.items():
            template = template.replace(f"${{{key}}}", str(value))
        return template

    return template


def main():
    # Argument parser
    parser = argparse.ArgumentParser(description="Create project templates.")
    parser.add_argument(
        "--python", metavar="project_name", type=str, help="Create a Python project"
    )
    args = parser.parse_args()

    # Check for project type and create structure
    if args.python:
        project_name = args.python
        # Load template
        template = load_template("templates/python.yaml")
        template = sanitize(template, {"PROJECT_NAME": project_name})
        create_project_structure(project_name, template)
        print(f"Python project '{project_name}' created successfully!")


if __name__ == "__main__":
    main()
