__author__ = 'tamvm'
import baskin_terminal.version
import threading 
import pip 
import re

terminal_version = baskin_terminal.version

def get_current_version():
    """ get current version of baskin_terminal """
    # read from file, maybe ? 
    with open(baskin_terminal.server.__file__) as f: 
        version = re.search(
            r"^__version__\s*=\s*'(.*)'", 
            f.read(), 
            re.M).group(1)

        return version

def check_for_update(): 
    threading.Timer(30.0, check_for_update).start()
    # check if a module available 
    pip.main(['install','-U','baskin-robbin-terminal'])
    current_ver = get_current_version()
    global terminal_version 
    if not current_ver == terminal_version: 
        terminal_version = current_ver
        baskin_terminal.server.stop_server()
        reload(baskin_terminal)
        baskin_terminal.server.start_server()

def main():
    """start the socket server and check for updated version"""
    # start thread checking new pypi version 
    check_for_update() 
    # start socket server 
    baskin_terminal.server.start_server()

if __name__ == '__main__':
    main()
