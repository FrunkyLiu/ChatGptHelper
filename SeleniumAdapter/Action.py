from .Adapter import SeleniumAdapter, Adapter_common_By
from .ExceptConditions import Conditions
from abc import ABC, abstractmethod
import typing as tp


class BaseAction(ABC):
    def __init__(self, driver: SeleniumAdapter, config: tp.Dict, *args, **kwargs) -> None:
        """
        Initialize BaseAction with a SeleniumAdapter instance and a configuration dictionary.
        """
        self.driver = driver
        self.config = config
        self.By = Adapter_common_By()
        if 'condition' in config:
            # Set the condition based on the provided configuration.
            self.condition = getattr(Conditions, config['condition'])()
        for method_name in dir(self):
            if method_name in config:
                # Set configuration for each method based on the provided configuration.
                setattr(self, f"config_{method_name}", config[method_name])
    
    @abstractmethod
    def main(self, *args, **kwargs):
        """
        Abstract method that defines the main action to be performed.
        """
        pass
    
    def get_by(self, by):
        """
        Get the locator strategy from Adapter_common_By.
        """
        return getattr(self.By, by)
    
    def get_current_url(self):
        """
        Get the current URL from the SeleniumAdapter instance.
        """
        return self.driver.get_current_url()