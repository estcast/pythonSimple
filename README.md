# Simple Python Project with Selenium

## Description
Are you familiar with Java and Selenium? This project is a great way to get started with Python and Selenium quickly and easily.

## Features

- **PyTest**: A testing framework similar to TestNG or JUnit.
- **UnitTest**: Another testing framework, also similar to TestNG or JUnit.
- **POM (Page Object Model)**: A popular design pattern in QA.

## Installation

1. Clone this repository.
2. Install Python on your machine from the [official website](https://www.python.org/).
3. We recommend using PyCharm. Download the Community Edition from [here](https://www.jetbrains.com/pycharm/).
4. Install the required libraries by running the following command in the directory where `requirements.txt` is located:
    ```bash
    pip install -r requirements.txt
    ```

## Notes

- To generate test reports, run the following command for any test, whether it uses UnitTest or PyTest:
    ```bash
    pytest ./Tests/Test2.py --html=./Reports/Test2-report.html
    ```
- Test2 uses `webdriver_manager` to automatically download the appropriate driver for each test. Test1 uses the `chromedriver.exe` file.
- This project is still under development, and additional improvements will be made in the future.

## License
MIT License

Copyright (c) 2024 Esteban Castro U.


