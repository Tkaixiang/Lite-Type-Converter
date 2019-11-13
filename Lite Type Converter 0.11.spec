# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Main.py'],
             pathex=['C:\\Users\\Tkaixiang\\Documents\\GitHub\\Lite-Type-Converter'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
			 
for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break

a.datas += [('hexa.ico','C:\\Users\\Tkaixiang\\Documents\\GitHub\\Lite-Type-Converter\\hexa.ico', 'Data')]			 


pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Lite Type Converter 0.11',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='hexa.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Lite Type Converter 0.11')
