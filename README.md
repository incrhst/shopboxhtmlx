# Shopbox Flask HTMX Project Readme

## Project Overview

Welcome to our Flask project! This web application is built using Flask, a lightweight and versatile web framework for Python. This readme will guide you through the process of setting up a virtual environment on both Windows and Unix-like systems and installing the necessary dependencies from the included `requirements.txt` file.

## Getting Started

### Prerequisites

Before you begin, make sure you have the following installed:

- Python (3.x recommended)
- `pip` (Python package installer)

### Setting up Virtual Environment

#### Windows

1. Open a command prompt in the project directory.
2. Run the following command to create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    ```bash
    .\venv\Scripts\activate
    ```

    If you encounter issues with script execution, you may need to set the execution policy:

    ```bash
    Set-ExecutionPolicy Unrestricted -Scope Process
    ```

4. Your prompt should now show the virtual environment name, indicating it's active.

#### Unix-like Systems (Linux/MacOS)

1. Open a terminal in the project directory.
2. Run the following command to create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    ```bash
    source venv/bin/activate
    ```

    Your prompt should now show the virtual environment name, indicating it's active.

### Installing Dependencies

Once the virtual environment is active, install the project dependencies using `pip`:

```bash
pip install -r requirements.txt
```

This command reads the `requirements.txt` file and installs all the necessary packages.

### Configuring the environment

Copy the  `.env.sample` file to `.env` and put the correct access token

### Running the Application

With the virtual environment activated and dependencies installed, you can now run the Flask application. Make sure you are in the project directory and run:

```bash
python main.py
```

Visit `http://127.0.0.1:5000/` in your web browser to view the application.

## Contributing

If you'd like to contribute to this project, please follow our [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
