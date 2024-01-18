class Invoker:
    def __init__(self):
        self.history = []

    def store_and_execute(self, command):
        self.history.append(command)  # This could be used for undo functionality
        command.execute()
