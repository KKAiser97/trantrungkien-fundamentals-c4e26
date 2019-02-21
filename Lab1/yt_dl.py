from youtube_dl import YoutubeDL
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=UwuAPyOImoI'])

options = {
    'format': 'bestaudio/audio' 
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=ffxKSjUwKdU'])

options = {
    'default_search': 'ytsearch',
    'max_downloads': 1 
}
dl = YoutubeDL(options)
dl.download(["As if it's your last"])

options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1, 
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Chiều nay không có mưa bay'])
