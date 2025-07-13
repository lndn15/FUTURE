import psutil 

class ProcessManager:
    
    def own_htop():
        header ="PID | Name | CPU % | RAM (MB) | Disk (MB)"
        separator = "-" * len(header)

        print(header)
        print(separator)

        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info', 'io_counters']):
            try:
                pid = proc.info["pid"]
                name = proc.info["name"][:20]
                cpu = proc.info["cpu_percent"]
                ram = proc.info["memory_info"].rss / (1024**2)
                io = proc.info["io_counters"]
                disk = (io.read_bytes + io.write_bytes)
                
                print(f"{pid:>6} | {name:<20} | {cpu:>6.1f} | {ram:>8.1f} | {disk:>8.1f}")
            
            except psutil.NoSuchProcess:
                print("Процесс исчез")
            except psutil.AccessDenied:
                print("Нет прав доступа")
            except KeyError:
                print("Отсутствует ключ в данных")
