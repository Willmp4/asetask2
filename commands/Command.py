from abc import ABC, abstractmethod

# A command is an object that encapsulates all the information needed to perform an action at a later time.
#   It is useful because it allows us to decouple the object that invokes the action from the object that knows how to perform it.
#   It also allows us to implement undo functionality.

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
