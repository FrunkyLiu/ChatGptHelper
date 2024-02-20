from Action import LoginPage, GPTMainPage
from SeleniumAdapter.Adapter import SeleniumAdapter


class GPTHelper:
    def __init__(self, config) -> None:
        
        self.driver = SeleniumAdapter()
        self.driver.active_chrome()
        
        self.login_page = LoginPage(self.driver, config['LoginPage'])
        self.GPT = GPTMainPage(self.driver, config['GPTMainPage'])
    
    def login(self, username, password):
        self.login_page.main(username, password)
        
    def ask_question(self, message:str) -> str:
        answer = self.GPT.main(message)
        return answer
    
    def logout(self):
        self.GPT.logout()