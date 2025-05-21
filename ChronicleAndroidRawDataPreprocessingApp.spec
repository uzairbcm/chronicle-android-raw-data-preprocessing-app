# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path
import os
import sys
import PyInstaller.config

block_cipher = None

# Determine platform
is_windows = sys.platform.startswith('win')
is_macos = sys.platform.startswith('darwin')

# List all modules that need to be included
hidden_imports = [
    'pandas',
    'pytz',
    'dateutil',
    'dateutil.parser',
    'dateutil.tz',
    'openpyxl',
    'openpyxl.styles',
    'PyQt6',
    'PyQt6.QtCore',
    'PyQt6.QtGui',
    'PyQt6.QtWidgets',
    'matplotlib',
    'numpy',
    'datetime',
    'json',
    'shutil',
    'logging',
    'sys',
    're',
    'contextlib',
    'functools',
    'typing',
    'dataclasses',
    'pathlib',
]

# Include all module directories as data
datas = [
    ('app_codebook_files', 'app_codebook_files'),
    ('apps_to_filter_files', 'apps_to_filter_files'),
    ('config', 'config'),
    ('models', 'models'),
    ('plotting', 'plotting'),
    ('preprocessors', 'preprocessors'),
    ('ui', 'ui'),
    ('utils', 'utils')
]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['_tkinter', 'tcl', 'tk', 'test', 'unittest', 'pydoc', 'doctest'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(
    a.pure, 
    a.zipped_data,
    cipher=block_cipher,
    compress=True
)

# Windows EXE configuration
if is_windows:
    exe = EXE(
        pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name='ChronicleAndroidRawDataPreprocessingApp',
        debug=False,
        bootloader_ignore_signals=True,
        strip=True,
        upx=True,
        upx_exclude=['vcruntime140.dll', 'python*.dll', '*.pyd'],
        console=False,
        disable_windowed_traceback=False,
        argv_emulation=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
        icon='ui/resources/icon.ico' if Path('ui/resources/icon.ico').exists() else None,
        uac_admin=False,
    )

    coll = COLLECT(
        exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=True,
        upx_exclude=['vcruntime140.dll', 'python*.dll', '*.pyd'],
        name='ChronicleAndroidRawDataPreprocessingApp',
    )

# macOS App configuration
if is_macos:
    exe = EXE(
        pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name='ChronicleAndroidRawDataPreprocessingApp',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,  # Setting to False to avoid stripping symbols that might be needed
        upx=True,
        console=False,
        disable_windowed_traceback=False,
        argv_emulation=True,  # Enable argv emulation for macOS
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
        icon='ui/resources/icon.ico' if Path('ui/resources/icon.ico').exists() else None,
    )
    
    coll = COLLECT(
        exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=True,
        name='ChronicleAndroidRawDataPreprocessingApp',
    )
    
    app = BUNDLE(
        coll,
        name='ChronicleAndroidRawDataPreprocessingApp.app',
        icon='ui/resources/icon.ico' if Path('ui/resources/icon.ico').exists() else None,
        bundle_identifier='com.chronicle.rawdatapreprocessingapp',
        info_plist={
            'NSPrincipalClass': 'NSApplication',
            'NSAppleScriptEnabled': False,
            'NSHighResolutionCapable': True,
            'CFBundleDisplayName': 'Chronicle Android Raw Data Preprocessing App',
            'CFBundleName': 'ChronicleAndroidRawDataPreprocessingApp',
        },
    ) 