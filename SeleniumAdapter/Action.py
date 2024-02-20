from .Adapter import SeleniumAdapter, Adapter_common_By
from .ExceptConditions import Conditions
from abc import ABC, abstractmethod
import typing as tp


class BaseAction(ABC):
    def __init__(self, driver: SeleniumAdapter, config: tp.Dict, *args, **kwargs) -> None:
        self.driver = driver
        self.config = config
        self.By = Adapter_common_By()
        if 'condition' in config:
            self.condition = getattr(Conditions, config['condition'])()
        for method_name in dir(self):
            if method_name in config:
                setattr(self, f"config_{method_name}", config[method_name])
    
    @abstractmethod
    def main(self, *args, **kwargs):
        pass
    
    def get_by(self, by):
        return getattr(self.By, by)
    
    def get_current_url(self):
        return self.driver.get_current_url()