# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['PDFPrinting.pyw'],
             pathex=['C:\\Users\\Duong Long\\PycharmProjects\\print_service'],
             binaries=[],
             datas=[('icon.ico', '.'), ('.\\config', 'config'), ('.\\local-chromium', 'local-chromium'), ('.\\logs', 'logs'), ('.\\pdf', 'pdf'), ('.\\static', 'static'), ('.\\templates', 'templates'), ('.\\tools', 'tools')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='PDFPrinting',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='PDFPrinting')
