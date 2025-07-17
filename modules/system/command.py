import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from core.general import Komandir
from .hard_process_kill import HardProcessKiller
from .soft_process_kill import SoftProcessKiller
from .system_monitor import SystemMonitor
from .process_manager import ProcessManager

class SystemCommand:
    def setup(self, processor: Komandir):
        killer = HardProcessKiller()
        terminator = SoftProcessKiller()
        sys_monitor = SystemMonitor()
        process_manage = ProcessManager()

        processor.register(
            name = "убить",
            handler = killer.kill_process
        )
        processor.register(
            name = "завершить",
            handler = terminator.terminate_process
        )
        processor.register(
            name = "покажи нагрузку железа",
            handler = sys_monitor.whole_work
        )
        processor.register(
            name = "покажи нагрузку процессами",
            handler = process_manage.own_htop
        )
