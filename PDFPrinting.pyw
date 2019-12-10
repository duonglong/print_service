from infi.systray import SysTrayIcon
import multiprocessing
import server

hover_text = "PDFPrinting Service"
multiprocessing.freeze_support()
proc = None


def start(sysTrayIcon):
    global proc
    proc = multiprocessing.Process(target=server.run)
    proc.start()


def stop(sysTrayIcon):
    proc.terminate()


def restart(sysTrayIcon):
    proc.terminate()
    start(None)


if __name__ == '__main__':
    menu_options = (('Start', None, start),
                    ('Stop', None, stop),
                    ('Restart', None, restart))
    sysTrayIcon = SysTrayIcon("icon.ico", hover_text, menu_options, on_quit=stop, default_menu_index=1)
    sysTrayIcon.start()
    print('BEFORE START')
    start(None)
    print('AFTER START')
