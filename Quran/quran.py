from chapters import chapters
import os
from pydub import AudioSegment
from pydub.playback import play as pyplay

file_path = os.path.dirname(__file__)
audio_base = os.path.join(file_path, '/audio/minshawi')

def create_mp3_files(surahs):
    with open('quran.txt', 'a', encoding='UTF-8') as file:
        for surah in surahs:
            chapter_no, chapter_ayats = surahs[surah]
            for i in range(chapter_ayats):
                chapter_no_padded = f'00{chapter_no}'
                ayat_padded = f'00{i+1}'
                file.write(f'{chapter_no_padded[-3:]}{ayat_padded[-3:]}\n')


def play(chapter: str, group_repeat=1, ayat_repeat=0, start_ayat=1, stop_ayat=0):
    '''
    chapter >> provide chapter name to be played
    group_repeat >> number of times to repeat group play
    surat_repeat >> whether to repeat surah or not.
        options:
            0 > play once
            1 > keep playing the same surah
            2 > keep once and proceed to the next surah
    aya_repeat >> specify how many times to repeat ayah before proceeding to the next (0-N)
    start_ayat >> default is 1 but can be changed (1-No. of ayat in surah)
    stop_ayat >> default is last ayat of the surah but can change (1-No. ayat in surah)
    '''
    queue = []
    chapter_no, no_of_ayat = chapters[chapter]
    assert start_ayat <= no_of_ayat, 'Out of range'
    assert stop_ayat >= start_ayat, 'Range error'
    
    # Create a queue list
    for i in range(start_ayat, stop_ayat + 1):
        chapter_no_padded = f'00{chapter_no}'
        ayat_padded = f'00{i}'
        queue.append(f'{chapter_no_padded[-3:]}{ayat_padded[-3:]}')

    
    for i in range(group_repeat): #loop through group repeat + 1 to make it human readable
        for file in queue: #loop through file
            if ayat_repeat == 0:
                play_current(file)
            elif ayat_repeat > 0:
                for _ in range(ayat_repeat):
                    play_current(file)
            else:
                raise 'invalid range'

def display_ayat(file_name):
    with open('quran-text.txt', 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            if line.startswith(file_name):
                print(line[6:])

def play_ayat(filename):
    mp3_filename = filename + '.mp3'
    path = os.path.join(audio_base, mp3_filename)
    audio = AudioSegment.from_file(path)
    pyplay(audio)

def play_current(file_name):
    print(f'playing {file_name}...')
    display_ayat(file_name)
    play_ayat(file_name)



# play('Hud')

# create_mp3_files(chapters)
play(chapter='An-Nas', group_repeat=1, ayat_repeat=0, start_ayat=1, stop_ayat=6)

# print(os.getcwd())