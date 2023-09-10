# site-connectivity-checker

site-connectivity-checker is a command-line tool for checking the availability of websites. It allows users to check multiple websites either synchronously or asynchronously.

## Installation

1. Clone the repository:
   shell
    ```
    git clone https://github.com/Navid-JL/site-connectivity-checker
    ```
2. Install the dependencies:
    ```
    pip install pipenv
    ```
    ```
    pipenv install
    ```

## Usage

usage: src [-h] [-u URLs [URLs ...]] [-f FILE] [-a]

check the availability of web sites

options:
-h, --help show this help message and exit
-u URLs [URLs ...], --urls URLs [URLs ...]
enter one or more website URLs
-f FILE, --input-file FILE
read URLs from a file
-a, --asynchronous run the connectivity check asynchronously

### Options

-   `-u, --urls` : Specify one or more URLs to check.
-   `-f, --input-file` : Specify a file containing URLs to check.
-   `-a, --asynchronous` : Perform asynchronous checks (default: synchronous).

## Examples

1. Check a single website synchronously:

    ```python -m src -u python.org```
    
    The status of "python.org" is: "Online!"

2. Check multiple websites synchronously:

    ```python -u src -u python.org pypi.org docs.python.org```
    
    The status of "python.org" is: "Online!"

    The status of "pypi.org" is: "Online!"

    The status of "docs.python.org" is: "Online!"

3. Check websites asynchronously using an input file:
   
   ```python -m src -u python.org pypi.org docs.python.org -a```
    
    The status of "pypi.org" is: "Online!"

    The status of "docs.python.org" is: "Online!"
    
    The status of "python.org" is: "Online!"

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to customize the README.md file according to your project's specific details.
