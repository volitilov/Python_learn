from pytube import YouTube

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

yt = YouTube('https://www.youtube.com/watch?v=HZyyEpTTE2g')

# print(yt.video_id)
# QRg_8NNPTD8

# print(yt.title)
# Heilung | LIFA - Krigsgaldr LIVE

# print(yt.thumbnail_url)
# https://i.ytimg.com/vi/QRg_8NNPTD8/default.jpg

# for f in yt.streams.all():
	# print(f)
# <Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2">
# <Stream: itag="43" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp8.0" acodec="vorbis">
# <Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2">
# <Stream: itag="36" mime_type="video/3gpp" res="240p" fps="30fps" vcodec="mp4v.20.3" acodec="mp4a.40.2">
# <Stream: itag="17" mime_type="video/3gpp" res="144p" fps="30fps" vcodec="mp4v.20.3" acodec="mp4a.40.2">
# <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028">
# <Stream: itag="248" mime_type="video/webm" res="1080p" fps="30fps" vcodec="vp9">
# <Stream: itag="136" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.4d401f">
# <Stream: itag="247" mime_type="video/webm" res="720p" fps="30fps" vcodec="vp9">
# <Stream: itag="135" mime_type="video/mp4" res="480p" fps="30fps" vcodec="avc1.4d401e">
# <Stream: itag="244" mime_type="video/webm" res="480p" fps="30fps" vcodec="vp9">
# <Stream: itag="134" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.4d401e">
# <Stream: itag="243" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp9">
# <Stream: itag="133" mime_type="video/mp4" res="240p" fps="30fps" vcodec="avc1.4d4015">
# <Stream: itag="242" mime_type="video/webm" res="240p" fps="30fps" vcodec="vp9">
# <Stream: itag="160" mime_type="video/mp4" res="144p" fps="30fps" vcodec="avc1.4d400c">
# <Stream: itag="278" mime_type="video/webm" res="144p" fps="30fps" vcodec="vp9">
# <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2">
# <Stream: itag="171" mime_type="audio/webm" abr="128kbps" acodec="vorbis">
# <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus">
# <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus">
# <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus">


# for f in yt.streams.filter(progressive=True).all():
	# print(f)
# <Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2">
# <Stream: itag="43" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp8.0" acodec="vorbis">
# <Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2">
# <Stream: itag="36" mime_type="video/3gpp" res="240p" fps="30fps" vcodec="mp4v.20.3" acodec="mp4a.40.2">
# <Stream: itag="17" mime_type="video/3gpp" res="144p" fps="30fps" vcodec="mp4v.20.3" acodec="mp4a.40.2">

# for f in yt.streams.filter(adaptive=True).all():
# 	print(f)

# for f in yt.streams.filter(only_audio=True).all():
	# print(f)
# <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2">
# <Stream: itag="171" mime_type="audio/webm" abr="128kbps" acodec="vorbis">
# <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus">
# <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus">
# <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus">

m = yt.streams.filter(only_audio=True).first()
m.download()


# for f in yt.streams.filter(file_extension='mp4').all():
	# print(f)

# res = yt.streams.get_by_itag('22')
# print(res)

