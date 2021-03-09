# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['tetris.py'],
             pathex=['C:\\Users\\AndreClerigo\\Desktop\\Git\\Games\\Python\\Tetris'],
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
a.datas += [('game_over.ttf','C:\\Users\\AndreClerigo\\Desktop\\Git\\Games\\Python\\Tetris\\assets\\fonts\\game_over.ttf', "DATA")]
a.datas += [('Premier2019-rPv9.ttf','C:\\Users\\AndreClerigo\\Desktop\\Git\\Games\\Python\\Tetris\\assets\\fonts\\Premier2019-rPv9.ttf', "DATA")]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='tetris',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
