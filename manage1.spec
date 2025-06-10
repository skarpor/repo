# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['manage.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('D:/develop/Python38/Lib/site-packages/django/contrib/admin/templates/', 'django/contrib/admin/templates'),
        ('D:/develop/Python38/Lib/site-packages/jazzmin/static/**', 'static'),
        ('D:/develop/Python38/Lib/site-packages/jazzmin/templates/**', 'templates'),
        ('D:/develop/Python38/Lib/site-packages/import_export/templates/', 'import_export/templates'),
    ],
    hiddenimports=[
        'jazzmin',
        'jazzmin.templatetags',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'repo_app',
        'repo_app.admin',
        'repo_app.models',
        'repo_app.apps',
        'repo_app.resources',
        'import_export',
        'import_export.admin',
        'import_export.resources',
        'django.template.context_processors',
        'asset',
        'asset.admin',
        'asset.models',
        'asset.apps',
        'asset.resources',
],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='manage',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='manage',
)
