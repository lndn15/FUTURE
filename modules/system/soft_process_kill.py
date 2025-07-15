import psutil

class SoftProcessKiller:
    
    def kill_process(identifier):

        try:
            if isinstance(identifier, int) or str(identifier).isdigit():
                psutil.Process(int(identifier)).terminate()
                return True
            
            for proc in psutil.process_iter(['pid', 'name']):
                if str(identifier).lower() in proc.info['name'].lower():
                    proc.terminate()
                    return True
            return False
        
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return False
