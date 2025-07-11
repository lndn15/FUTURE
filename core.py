from .history import CommandHistory
from modules.searcher import SearchCommand
from modules.system import SystemCommand

class Core:
    def __init__(self):
        self._comnd = {
            "поиск": SearchCommand,
            "помощь": self.showhelp,
            "система": SystemCommand,
            "история": self.historyshow 
        }
        self._hist = CommandHistory()

    def historyshow(self) -> str:
        return "\n".join(self._hist[-10:]) if self._hist else "История пуста"
    def showhelp(self) -> str:
        return "В ядре доступны команды: search; system; history"
    def worka(self, user_input: str) -> str:
        self._hist.add(user_input)

        if not user_input.strip():
            return "Неизвестная команда"
        
        parts = user_input.split()
        mainc, args = parts[0], parts[1:]

        if mainc not in self._comnd:
            return "Неизвестная команда; Введите help для массива команд"
        try:
            return str(self._comnd[mainc](*args))
        except KeyError:
            return "Неизвестная команда"
        except Exception as e:
            return f"Ошибка: {str(e)}"    
        
