import zipfile, pprint

# :::::::::::::::::::::::::::::::::::::::::::::::

ex_zip = zipfile.ZipFile('experement.zip')
z = ex_zip.namelist()
pprint.pprint(z)
# ['experement/',
#  'experement/ex1/',
#  'experement/ex1/ex_1/',
#  'experement/ex1/ex_1/ex_file3.py',
#  'experement/ex1/ex_file2.py',
#  'experement/ex2/',
#  'experement/ex2/ex_file4.py',
#  'experement/ex_file.py']

ex_zip.extractall()

ex_zip.close()


ex_zip = zipfile.ZipFile('experement.zip', 'w')
ex_zip.write('filename.txt', compress_type=zipfile.ZIP_DEFLATED)
ex_zip.close()