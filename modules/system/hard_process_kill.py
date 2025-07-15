import psutil

class HardProcessKiller:

    def kill_process(identifier):

        try:
            if isinstance(identifier, int) or str(identifier).isdigit():
                psutil.Process(int(identifier)).kill()
                return True
            
            for proc in psutil.process_iter(['pid', 'name']):
                if str(identifier).lower() in proc.info['name'].lower():
                    proc.kill()
                    return True
            return False
        
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return False
