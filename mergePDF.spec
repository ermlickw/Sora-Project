# -*- mode: python -*-

block_cipher = None


a = Analysis(['mergePDF.py'],
             pathex=['C:\\Users\\BillyErmlick\\Desktop\\Workspace\\Python\\Sora-Project'],
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
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='mergePDF',
          debug=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=True , icon='C:\\Users\\BillyErmlick\\Downloads\\Cornmanthe3rd-Plex-Other-python.ico')
