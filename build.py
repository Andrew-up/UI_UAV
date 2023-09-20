import PyInstaller.__main__

PyInstaller.__main__.run([
    'game.py', '-F',
    '--add-data=img/;img'
])

print('======================')
