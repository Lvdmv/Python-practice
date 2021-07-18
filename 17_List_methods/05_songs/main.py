violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

def index_song(song):
    for i in range(len(violator_songs)):
        if violator_songs[i][0] == song:
            return violator_songs[i][1]

song_amt = int(input('Сколько песен выбрать? '))
song_duration = 0
for i_song in range(song_amt):
    print('Название', i_song + 1, 'песни: ', end = ' ')
    song = input()
    index_song(song)
    song_duration += index_song(song)
print('\nОбщее время звучания песен: ', round(song_duration, 2), 'минут')

