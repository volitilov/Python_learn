import shutil

# ::::::::::::::::::::::::::::::::::::::::::::::::::

shutil.copy('src.py', 'new_file.py')
# файл src копируется в new_file

shutil.move('src.py', 'new_file.py')
# копирует, а затем удаляет аригинал (перемещает)

shutil.copytree(src, dst)
# копирует дерикторию целиком

shutil.rmtree(path)
# удаляет дерикторию со всем содержимым в ней
