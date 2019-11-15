import win32print


def list_printers():
    printer_info = win32print.EnumPrinters(
        win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS
    )
    printer_names = [name for (flags, description, name, comment) in
                     printer_info]
    return printer_names
