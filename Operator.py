from Action import LoginPage, GPTMainPage
from SeleniumAdapter.Adapter import SeleniumAdapter
import typing as tp

class GPTHelper:
    def __init__(self, config: tp.Dict) -> None:
        """
        Initialize GPTHelper with the provided configuration.

        Args:
            config (dict): Configuration dictionary containing settings for LoginPage and GPTMainPage.
        """
        self.driver = SeleniumAdapter()
        self.driver.active_chrome()
        
        # Initialize LoginPage and GPTMainPage instances
        self.login_page = LoginPage(self.driver, config['LoginPage'])
        self.GPT = GPTMainPage(self.driver, config['GPTMainPage'])
    
    def login(self, username: str, password: str):
        """
        Perform the login process using the provided username and password.

        Args:
            username (str): The username for login.
            password (str): The password for login.
        """
        self.login_page.main(username, password)
        
    def ask_question(self, message: str) -> str:
        """
        Ask a question by sending a message to the GPT model and retrieve the response.

        Args:
            message (str): The message to be sent to the GPT model.

        Returns:
            str: The response from the GPT model.
        """
        answer = self.GPT.main(message)
        return answer
    
    def logout(self):
        """
        Logout from the application.
        """
        self.GPT.logout()