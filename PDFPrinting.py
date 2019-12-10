from infi.systray import SysTrayIcon
import multiprocessing
import server
import os
import subprocess
import signal

hover_text = "PDFPrinting Service"
multiprocessing.freeze_support()
proc = None


def kill_child_processes(parent_id):
    ps_command = subprocess.Popen("wmic process where (ParentProcessId=%s) get ProcessId" % parent_id, shell=True, stdout=subprocess.PIPE)
    ps_output = ps_command.stdout.read().decode('utf8')
    ps_command.wait()
    for pid_str in ps_output.strip().split("\r\r\n")[1:]:
        pid = int(pid_str.strip())
        os.kill(pid, signal.SIGTERM)


def start(sysTrayIcon):
    global proc
    proc = multiprocessing.Process(target=server.run)
    proc.daemon = True
    proc.start()


def stop(sysTrayIcon):
    kill_child_processes(proc.pid)
    proc.terminate()


def restart(sysTrayIcon):
    stop(None)
    start(None)


if __name__ == '__main__':
    menu_options = (('Start', None, start),
                    ('Stop', None, stop),
                    ('Restart', None, restart))
    sysTrayIcon = SysTrayIcon("icon.ico", hover_text, menu_options, on_quit=stop, default_menu_index=1)
    sysTrayIcon.start()
    start(None)
