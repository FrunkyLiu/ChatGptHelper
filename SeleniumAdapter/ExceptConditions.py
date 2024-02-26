from selenium.webdriver.support import expected_conditions as EC


class Conditions:

    @staticmethod
    def visibility_of_element_located():
        """
        Returns a condition that waits for an element to be present in the DOM and visible on the page.
        """
        return EC.visibility_of_element_located

    @staticmethod
    def text_to_be_present_in_element():
        """
        Returns a condition that waits for the specified text to be present in the element.
        """
        return EC.text_to_be_present_in_element

    @staticmethod
    def url_changes():
        """
        Returns a condition that waits for the URL to change.
        """
        return EC.url_changes
    
    @staticmethod
    def url_contains():
        """
        Returns a condition that waits for the URL to contain the specified string.
        """
        return EC.url_contains
