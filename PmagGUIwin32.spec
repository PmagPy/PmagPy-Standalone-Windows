# -*- mode: python -*-

block_cipher = None


a = Analysis(['programs\pmag_gui.py'],
             pathex=['F:\PmagPy'],
             binaries=None,
             datas=[('.\pmagpy\data_model\*','.\data_model')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='PmagGUIwin32',
          debug=False,
          strip=False,
          upx=True,
          console=False , version='C:\Users\Kevin\Desktop\PmagGUI_version.txt' , icon='.\programs\images\PmagPy.ico')
