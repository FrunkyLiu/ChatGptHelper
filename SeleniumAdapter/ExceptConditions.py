from selenium.webdriver.support import expected_conditions as EC


class Conditions:

    @staticmethod
    def visibility_of_element_located():
        return EC.visibility_of_element_located

    @staticmethod
    def text_to_be_present_in_element():
        return EC.text_to_be_present_in_element

    @staticmethod
    def url_changes():
        return EC.url_changes
    
    @staticmethod
    def url_contains():
        return EC.url_contains
