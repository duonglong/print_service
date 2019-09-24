from datetime import datetime
from app.htmltopdf import converter
import subprocess
import logging

_logger = logging.getLogger(__name__)

GHOSTSCRIPT_PATH = r".\tools\GHOSTSCRIPT\bin\gswin32.exe"
GSPRINT_PATH = r".\tools\GSPRINT\gsprint.exe"


class PDFPrinter(object):
    """Print PDF File to Printer"""
    def __init__(self, name=None, width='', height='', **kwargs):
        # TODO: Support all puppeteer options
        self.directory = './app/pdf/'
        self.filename = None
        self.name = name
        self.width = width
        self.height = height
        self.options = kwargs

    async def print(self, url):
        self.set_filename()
        options = self.print_options()
        response = await converter.html_to_pdf(url, options)
        if response == 200:
            command = [GSPRINT_PATH, '-ghostscript', GHOSTSCRIPT_PATH, '-printer', self.name, self.filename]
            stdout, stderr = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            if stderr:
                _logger.info(stderr)
        return response

    def print_options(self):
        return {
            'path': self.filename,
            'width': self.width,
            'height': self.height
        }

    def set_filename(self):
        now = datetime.now().strftime('%d%m%Y%H%m%S')
        self.filename = self.directory + now + '.pdf'


def get_printer(name, width, height):
    return PDFPrinter(name=name, width=width, height=height)
