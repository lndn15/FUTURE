class Komandir:
    def __init__(self):
        self._comd = {}
        self._hist = []

    def register(self, name: str, handler: callable):
        self._comnd[name] = {"handler": handler} 
        
