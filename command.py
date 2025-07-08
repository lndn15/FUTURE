from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseCommand(ABC):
    @property
    @abstractmethod
    def name(self) -> str:  
        pass

    @abstractmethod
    def execute(self, args: Dict[str, Any]) -> None:  
        pass
