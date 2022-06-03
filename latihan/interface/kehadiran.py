from abc import ABC, abstractmethod

class Kehadiran(ABC):
    
    @abstractmethod
    def mencatat_kehadiran(self):
        pass
    
    