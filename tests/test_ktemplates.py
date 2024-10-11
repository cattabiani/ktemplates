import os
import pytest
import yaml
from ktemplates import create_project_structure, load_template, sanitize

# Sample template for testing
sample_template = {
    "folders": ["src", "tests"],
    "files": {
        "README.md": "# Sample Project\nThis is a sample project.",
        "src/main.py": 'def main():\n    print("Hello, World!")',
    },
}


@pytest.fixture
def setup_project(tmpdir):
    """Fixture to create a temporary project directory."""
    project_name = tmpdir.join("test_project").strpath
    yield project_name
    # Cleanup after test
    for root, dirs, files in os.walk(project_name, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))


def test_create_project_structure(setup_project):
    """Test creating a project structure."""
    create_project_structure(setup_project, sample_template)

    # Check folders were created
    assert os.path.exists(os.path.join(setup_project, "src"))
    assert os.path.exists(os.path.join(setup_project, "tests"))

    # Check files were created
    assert os.path.isfile(os.path.join(setup_project, "README.md"))
    assert os.path.isfile(os.path.join(setup_project, "src/main.py"))


def test_load_template():
    """Test loading a template from a YAML file."""
    # Create a temporary YAML file
    template_path = "test_template.yaml"
    with open(template_path, "w") as file:
        yaml.dump(sample_template, file)

    loaded_template = load_template(template_path)
    assert loaded_template == sample_template

    # Cleanup
    os.remove(template_path)


def test_sanitize():
    """Test the sanitization of templates."""
    template = {
        "project_name": "MyProject",
        "files": {
            "README.md": "This is a project named ${PROJECT_NAME}.",
        },
    }
    sanitized_template = sanitize(template, {"PROJECT_NAME": "MyProject"})
    assert (
        sanitized_template["files"]["README.md"] == "This is a project named MyProject."
    )

    # Test empty input
    assert sanitize(None, {}) is None
    assert sanitize("", {}) == ""
