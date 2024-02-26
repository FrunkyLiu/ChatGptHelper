# ChatGPT Helper
ChatGPT Helper is designed based on Selenium to assist in quick retrieval and processing of responses.

# How to use
The main functions implement using ChatGPT.

```python
from Operator import GPTHelper
import yaml

# Loading web pages setting configuration
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Initialize GPTHelper
helper = GPTHelper(config)

# Input account and password
helper.login('MY_ACCOUNT', 'MY_PASSWORD')

# Ask questions and get responses
respose = helper.ask_question('hello gpt')

# Perform some processing on the response
...

# Logout
helper.logout()
``` 

If there are other custom web operations you'd like to add, you can refer to the methods in [Action.py](./Action.py) and add them yourself.

**Note:** Please ensure that the Chrome browser is up-to-date and when using this program, make sure that the Chrome browser opened for logging in is visible on the screen.

# Project Requirements

- `selenium`: A powerful library for web automation testing, providing a wide range of tools for interacting with web browsers.
- `undetected-chromedriver`: A package for using ChromeDriver with Selenium, which provides an undetected mode to prevent bot detection.
- `PyYAML`: A YAML parser and emitter for Python, used for reading and writing YAML files.
