import zipfile

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::

ex_zip = zipfile.ZipFile('experement.zip')
# получения объкта орхива

ex_zip.namelist()
# возвращает список строк, для всех файлов и 
# папок содержащихся в архиве

ex_info = ex_zip.getinfo('ex.py')
# возвращает объект ZipInfo, содержащий информацию о
# данном файле 
	ex_info.file_size()
	# целочисленное значение размера исходного файла
	ex_info.compress_size()
	# целочисленное значение размера зжатого файла

ex_zip.extractall()
# извлечение содержимого архива в текущую дерикторию

ex_zip.extract('info.py', 'ex_folder')
# извлекает одиночный файл из архива в ex_folder, если
# ex_folder не существует, то создаст.

ex_zip.close()
# закрытие файла

ex_zip2 = zipfile.ZipFile('new.zip', 'w')
	'w' # открыть объект ZipFile в режиме записи
	'a' # открыть объект в режиме дозаписи
	
ex_zip2.write('filename.txt', compress_type=zipfile.ZIP_DEFLATED)
# сжимает указаный файл и добавляет его в ZIP файл, вторым
# аргументом передаётся тип сжатия 
	zipfile.ZIP_DEFLATED
	# алгоритм сжатия без потерь