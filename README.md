# ktemplates

*ktemplates* is a Python-based project that generates templates based on a YAML configuration file. This tool simplifies the creation of templates by allowing users to define their structure and content in a flexible, human-readable format.

## Features

- Generate templates from YAML configuration files.
- Easily customizable and extensible for different use cases.
- Lightweight and fast, suitable for automating template generation in various environments.

## Installation

To use *ktemplates*, simply clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/ktemplates.git
cd ktemplates
pip install -r requirements.txt
```

## Usage

1. Define your template configuration in a YAML file as the examples in the `templates` folder. (optional)

2. Adapt the `ktemplates.py` main to recofnize the new template (optional)
    
2. Run the template generation command. i.e. for python:

    ```bash
    ktemplates --python <new_project>
    ```

3. Your template will be generated based on the provided YAML configuration with the name of the project: `new_project` substituted in the appropriate places.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for discussion.

## License

This project is licensed under the [MIT License](LICENSE).