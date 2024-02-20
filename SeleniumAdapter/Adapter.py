import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import typing as tp

WebDriverOrWebElement = tp.Union[WebDriver, WebElement]

class Adapter_common_By(By):
    pass

class SeleniumAdapter:
    def __init__(self, timeout:int=15) -> None:
        self.timeout=timeout
    
    def active_chrome(self):
        self.driver = uc.Chrome()

    def get_current_url(self):
        return self.driver.current_url

    def visit_web(self, URL: str):
        self.driver.get(URL)

    def wait_for_page_load(self,):
        WebDriverWait(self.driver, self.timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    def wait_for_element(self,
                         condition: tp.Callable[[tp.Tuple[Adapter_common_By, str]], bool],
                         strategy: Adapter_common_By,
                         keyword: str,
                         web_element: WebDriverOrWebElement =None, 
                         timeout: int=None) -> WebElement:
        if timeout is None:
            timeout = self.timeout
        if web_element is None:
            web_element = self.driver
        wait = WebDriverWait(web_element, timeout)
        element = wait.until(condition((strategy, keyword)))
        return element

    def find_element(self,
                     strategy: Adapter_common_By,
                     keyword: str,
                     web_element: WebDriverOrWebElement=None) -> WebElement:
        if web_element is None:
            web_element = self.driver
        element = web_element.find_element(strategy, keyword)
        return element
    
    def find_elements(self,
                      strategy: Adapter_common_By,
                      keyword: str, 
                      web_element: WebDriverOrWebElement=None) -> tp.List[WebElement]:
        if web_element is None:
            web_element = self.driver
        elements = web_element.find_elements(strategy, keyword)
        return elements

    def clear_value(self, element: WebElement):
        element.clear()

    def send_keys(self, element: WebElement, text: str):
        element.send_keys(text)

    def click_element(self, element: WebElement):
        element.click()

    def execute_script(self, script: str, element: WebElement=None):
        return self.driver.execute_script(script, element)
    
    def get_text(self, element: WebElement) -> tp.List[str]:
        return element.text