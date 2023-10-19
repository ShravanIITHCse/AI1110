import numpy as np

def myrandom(songs_list):
    songs_array = np.array(songs_list)
    np.random.shuffle(songs_array)
    shuffled_song_list = songs_array.tolist()

    return shuffled_song_list
