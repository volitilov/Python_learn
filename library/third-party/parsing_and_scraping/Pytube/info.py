Pytube ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Pytube это библиотека для скачивания видео с Youtube. Как сказано 
# в документации, у неё нет сторонних зависимостей и она построена 
# на стандартной библиотеке.

# Документация на английском:
# https://python-pytube.readthedocs.io/en/latest/index.html

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# установка
pip3 install pytube

import pytube

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

yt = pytube.YouTube(url)
# класс YouTube представляет экземпляр YouTube-сессии, поэтому его 
# нужно инициализировать. После этого в переменной yt будет храниться 
# вся информация о переданном видео

yt.video_id
# индетификатор видео

yt.streams.count()
# получение кол-во потоков

yt.thumbnail_url
# получение ссылки на изображение (thumbnail) к видео

yt.streams.all()
# возможные варианты для загрузки

yt.streams.last()
# получение последнего потока

v = yt.streams.first()
# получение первого потока

v.title
# получение названия файла

v.filesize
# получение размера файла в байтах 

v.download()
# загрузка видео


# filter :::::::::::::::::::::::::::::::::::::::::::::::::::

filter(fps=None, res=None, resolution=None, mime_type=None, 
	type=None, subtype=None, file_extension=None, abr=None, 
	bitrate=None, video_codec=None, audio_codec=None, 
	only_audio=None, only_video=None, progressive=None, 
	adaptive=None, custom_filter_functions=None)

yt.streams.filter(progressive=True).all()
# получаем список прогресовного видео

yt.streams.filter(adaptive=True).all()
# получаем список адаптивного видео

yt.streams.filter(only_audio=True).all()
# получаем список аудио потоков

yt.streams.filter(file_extension='mp4').all()
# получаем список видео и аудио потоков с расширением mp4

yt.streams.get_by_itag('22')
# получение конкретного потока


# subtitle ::::::::::::::::::::::::::::::::::::::::::::::::::

yt.captions.all()
# получение списка потоков с субтитрами

с = yt.captions.get_by_language_code('en')
# получение английских субтитров

c.xml_captions
# вывод субтитров в xml формате

c.generate_srt_captions()
# вывод субтитров в строчку