from datetime import datetime
from htmltopdf import converter
from configuration import FOXIT_READER, PDF_PATH
import subprocess
import logging


class PDFPrinter(object):
    """Print PDF File to Printer"""

    def __init__(self, name=None, width='', height='', **kwargs):
        # TODO: Support all puppeteer options
        self.directory = PDF_PATH
        self.filename = None
        self.name = name
        self.width = width
        self.height = height
        self.options = kwargs

    async def print(self, url):
        self.set_filename()
        _logger = logging.getLogger('quart.serving')
        options = self.print_options()
        response = await converter.html_to_pdf(url, options)
        if response == 200:
            _logger.info("Saved pdf to %s" % self.filename)
            command = [FOXIT_READER, '/t',  self.filename, self.name]
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
