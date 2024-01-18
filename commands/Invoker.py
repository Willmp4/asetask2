#An invoker is an object that knows how to execute a given command but doesn't know how the command is implemented.
#It only knows the command's interface. It can also optionally store a history of commands that have been executed.
#This is the Invoker class
class Invoker:
    def __init__(self):
        self.history = []

    def store_and_execute(self, command):
        self.history.append(command)  # This could be used for undo functionality
        return command.execute()
