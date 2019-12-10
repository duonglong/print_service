# Simple http service for printing job
__version__ = '1.0.0'
from quart import Quart, make_response, request, render_template, jsonify
from pdf_printer import PDFPrinter
from configuration import load_config, options, path
from list_printer import list_printers
import socket
import os
import asyncio
import random

loop = asyncio.get_event_loop()
app = Quart('PRINT_SERVICE')


def get_index_img():
    img_path = path + "\\static\\img\\"
    files = os.listdir(img_path)
    return "..\\static\\img\\" + files[random.randrange(len(files) - 1)]


@app.route('/')
def index():
    """Index service"""
    img = get_index_img()
    return render_template("index.html", img=img, port=options.get('port', 5000))


@app.route('/getPrinters')
def get_printers():
    """List all available printers"""
    printers = list_printers()
    return jsonify(printers)


@app.route('/print/barcode', methods=['GET', 'POST'])
async def print_barcode():
    try:
        if request.method == 'POST':
            data = await request.get_json(silent=True)
        else:
            data = request.args
        url = data.get('reporturl')
        if not url:
            return await make_response('Report URL is missing !', 200)
        printer_name = data.get('printer', options['default_printer'])
        printer = PDFPrinter(width='1.97 in', height='1.18 in', name=printer_name)
        asyncio.ensure_future(printer.print(url))
        return await make_response('OK', 200)
    except Exception as e:
        return await make_response(str(e), 200)


@app.route('/print', methods=['GET', 'POST'])
async def print_html():
    try:
        if request.method == 'POST':
            data = await request.get_json(silent=True)
        else:
            data = request.args
        url = data.get('reporturl')
        if not url:
            return await make_response('Report URL is missing !', 500)
        printer_name = data.get('printer', options['default_printer'])
        # Default is A4
        width = data.get('width', '23.4 in')
        height = data.get('height', '33.1 in')
        printer = PDFPrinter(width=width, height=height, name=printer_name)
        await asyncio.ensure_future(printer.print(url))
        return await make_response('OK', 200)
    except Exception as e:
        return await make_response(str(e), 500)


@app.route('/shutdown', methods=['GET', 'POST'])
def shutdown():
    pass


def main():
    """Start the service"""
    port = int(options.get('port', 5000))
    app.run(host='0.0.0.0', port=port, loop=loop)


def run():
    load_config()
    main()


if __name__ == '__main__':
    run()
