from urllib import request

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

my_url = 'https://www.youtube.com/'
otvet = request.urlopen(my_url)

text1 = otvet.readlines()
text2 = otvet.read()

# print(otvet)

for i in text1:
    print(i)
