import PyInstaller.__main__
import os

package_name = 'PDFPrinting'
icon = 'icon.ico'
resources = [
    'config',
    'local-chromium',
    'logs',
    'pdf',
    'static',
    'templates',
    'tools',
]

options = [
    '-y',
    '--name=%s' % package_name,
    '--icon=%s' % os.path.join('.', 'icon.ico'),
    '--add-data=icon.ico;.',
]
for r in resources:
    options.append('--add-data=%s;%s' % (os.path.join('.', r), r))
options.append(os.path.join('.', 'PDFPrinting.pyw'))
PyInstaller.__main__.run(options)
