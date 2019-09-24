# Simple http service for printing job
__version__ = '1.0.0'
from quart import Quart, make_response, request
from logging.config import fileConfig

from app.pdf_printer import PDFPrinter
from app.configuration import load_config, options
from multiprocessing import Process
import asyncio

loop = asyncio.get_event_loop()
app = Quart(__name__)


# fileConfig('../logging.cfg')


@app.route('/')
def index():
    """Index service"""
    return "Howdy, i'm running on port %s" % options['port']


@app.route('/print/barcode', methods=['GET', 'POST'])
async def print_barcode():
    url = request.args.get('reporturl')
    if not url:
        return await make_response('Report URL is missing !', 200)
    printer_name = request.args.get('printer', options['default_printer'])
    printer = PDFPrinter(width='1.97 in', height='1.18 in', name=printer_name)
    await asyncio.ensure_future(printer.print(url))
    return await make_response('OK', 200)


@app.route('/print', methods=['GET', 'POST'])
async def print_html():
    url = request.args.get('reporturl')
    if not url:
        return await make_response('Report URL is missing !', 200)
    printer_name = request.args.get('printer', options['default_printer'])
    # Default is A4
    width = request.args.get('width', '23.4 in')
    height = request.args.get('height', '33.1 in')
    printer = PDFPrinter(width=width, height=height, name=printer_name)
    await asyncio.ensure_future(printer.print(url))
    return await make_response('OK', 200)


def shutdown():
    """Shutdown the service"""
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


def main():
    """Start the service"""
    global server
    app.run(debug=True, port=int(options['port']))


if __name__ == '__main__':
    main()
