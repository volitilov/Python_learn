from urllib import request, parse
import sys

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

my_url = 'https://www.google.by/search?'
value = {'q': 'ANDESA Soft'}

my_header = {}
my_header['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'

try:
    my_data = parse.urlencode(value)
    print(my_data)
    my_url += my_data
    req = request.Request(my_url, headers=my_header)
    otvet = request.urlopen(req)
    otvet = otvet.readlines()
    for line in otvet:
        print(line)
except:
    print('Error web request!!')
    print(sys.exc_info()[1])