import psutil

class System:
    @classmethod
    def run(cls):
        while True:
            print("(SystemFile)")
            print("\nДоступные команды: work, process_work, kill")
            command = input(">>> ").strip().lower()
            
            if command == "work":
                print(cls.whole_work())
            elif command == "process_work":
                cls.show_work() 
            elif command in ("exit", "quit", "finish"):
                break
            elif command in ("kill","murder","finish_prcs"):
                cls.kill_process(cls)
            elif command == "help":
                print("Неизвестная команда, доступные команд: work, process_work")
            else:
                print("Неизвестная команда, доступные команд: work, process_work") 
  
    def kill_process(cls):
        try:
            pid = int(input("Введите PID процесса для завершения: "))
            process = psutil.Process(pid)
            process.terminate()
            print(f"[✓] Процесс {pid} ({process.name()}) завершен")
        except ValueError:
            print("Ошибка: PID должен быть числом")
        except psutil.NoSuchProcess:
            print(f"[×] Процесс {pid} не найден")
        except psutil.AccessDenied:
            print(f"[×] Нет прав для завершения {pid}")

    @classmethod
    def show_work(cls):
        print("\nВыберите метрику: cpu; ram; disk;")
        metric = input(">>> ").strip().lower()
        
        if metric not in ['cpu', 'ram', 'disk']:
            print("Ошибка: допустимы только cpu, ram, disk")
            return

        n = 7

        try:
            if metric == 'cpu':
                field = 'cpu_percent'
                processes = []
                for p in psutil.process_iter(['pid', 'name', field]):
                    try:
                        if p.info[field] > 0:
                            processes.append(p)
                    except:
                        continue
                processes.sort(key=lambda p: p.info[field], reverse=True)
                print(f"\nТоп-{n} процессов по CPU (PID | Имя | Нагрузка):")
                for i, p in enumerate(processes[:n], 1):
                    print(f"{i}. {p.info['pid']} | {p.info['name']} | {p.info[field]:.1f}%")

            elif metric == 'ram':
                field = 'memory_percent'
                processes = []
                for p in psutil.process_iter(['pid', 'name', field]):
                    try:
                        if p.info[field] > 0:
                            processes.append(p)
                    except:
                        continue
                processes.sort(key=lambda p: p.info[field], reverse=True)
                print(f"\nТоп-{n} процессов по RAM (PID | Имя | Память):")
                for i, p in enumerate(processes[:n], 1):
                    print(f"{i}. {p.info['pid']} | {p.info['name']} | {p.info[field]:.1f}%")

            elif metric == 'disk':
                field = 'io_counters'
                processes = []
                for p in psutil.process_iter(['pid', 'name', field]):
                    try:
                        io = p.info[field]
                        if io.read_bytes + io.write_bytes > 0:
                            processes.append(p)
                    except:
                        continue
                processes.sort(key=lambda p: p.info[field].read_bytes + p.info[field].write_bytes, reverse=True)
                print(f"\nТоп-{n} процессов по Disk (PID | Имя | Чтение+Запись):")
                for i, p in enumerate(processes[:n], 1):
                    total = (p.info[field].read_bytes + p.info[field].write_bytes) / (1024 * 1024)
                    print(f"{i}. {p.info['pid']} | {p.info['name']} | {total:.2f} MB")

        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")
    
    
    #>>>
    #<<<
    #>>>
    
    
    @staticmethod
    def disk_work():
        disk = psutil.disk_usage("/")
        return (
            f"Диск:\n"
            f"  Всего: {disk.total / (1024**3):.1f} GB\n"
            f"  Использовано: {disk.used / (1024**3):.1f} GB\n"
            f"  Свободно: {disk.free / (1024**3):.1f} GB\n"
            f"  Заполнение: {disk.percent}%"
        )
    
    @staticmethod
    def cpu_work():
        return (
            f"Процессор:\n"
            f"  Нагрузка: {psutil.cpu_percent(interval=1)}%\n"
            f"  Ядра: {psutil.cpu_count(logical=False)}\n"
            f"  Частота: {psutil.cpu_freq().current:.1f} MHz"
        )

    @staticmethod
    def ram_work():
        mem = psutil.virtual_memory()
        return (
            f"Память:\n"
            f"  Использовано: {mem.used / (1024**3):.1f} GB\n"
            f"  Всего: {mem.total / (1024**3):.1f} GB\n"
            f"  Загрузка: {mem.percent}%"
        )

    @classmethod
    def whole_work(cls):
        return "\n\n".join([
            cls.disk_work(),
            cls.cpu_work(),
            cls.ram_work()
        ])

main
from modules.system import System
from modules.searcher import SearchAnswer
class AssistantCore:
    from modules.system import System
    from modules.searcher import SearchAnswer

    def __init__(self):
        self.commands = {
            "sysm": System,
            "search": SearchAnswer
        }
        self.run_program()

    def show_help(self):
        print("(CoreFile)")
        print("Доступные команды:")
        print("sysm; search")
        print("help")
        print("exit")

    def run_program(self):
        
        self.show_help()

        while True:
            user_input = input(">>> ").strip().lower()

            if user_input in ("exit", "quit", "finish"):
                print("Завершение работы программы...")
                break
            elif user_input == "sysm":
                self.System.run()  
            elif user_input == "search":
                self.SearchAnswer.run()
            elif user_input == "help":
                self.show_help()
            else:
                print(f"Ошибка: команда '{user_input}' не найдена")

if __name__ == "__main__":
    AssistantCore()
