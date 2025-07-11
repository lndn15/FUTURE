class CommandHistory:
    def __init__(self):
        self._hist = []
        self._max_size = 100

    def add(self, command: str):
        if command.strip():
            self._hist.append(command)
            if len(self._hist) > self._max_size:
                self._hist.pop(0)


