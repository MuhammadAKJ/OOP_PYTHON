from chapters import chapters

def create_mp3_files(surahs):
    with open('quran.txt', 'a', encoding='UTF-8') as file:
        for surah in surahs:
            chapter_no, chapter_ayats = surahs[surah]
            for i in range(chapter_ayats):
                chapter_no_padded = f'00{chapter_no}'
                ayat_padded = f'00{i+1}'
                file.write(f'{chapter_no_padded[-3:]}{ayat_padded[-3:]}\n')


def play(chapter: str, surat_repeat=1, ayat_repeat=0, start_ayat=1, stop_ayat=0):
    queue = []
    chapter_no, no_of_ayat = chapters[chapter]
    assert start_ayat <= no_of_ayat, 'Out of range'
    assert stop_ayat >= start_ayat, 'Range error'
    
    for i in range(start_ayat, stop_ayat):
        chapter_no_padded = f'00{chapter_no}'
        ayat_padded = f'00{i}'
        queue.append(f'{chapter_no_padded[-3:]}{ayat_padded[-3:]}')

    
    for i in range(surat_repeat):
        for file in queue:
            play_current(file)
    '''
    chapter >> provide chapter name to be played
    surat_repeat >> whether to repeat surah or not.
        options:
            0 > play once
            1 > keep playing the same surah
            2 > keep once and proceed to the next surah
    aya_repeat >> specify how many times to repeat ayah before proceeding to the next (0-N)
    start_ayat >> default is 1 but can be changed (1-No. of ayat in surah)
    stop_ayat >> default is last ayat of the surah but can change (1-No. ayat in surah)
    '''
    



def play_current(file_name):
    print(f'playing {file_name}...')
    



# play('Hud')

# create_mp3_files(chapters)

play('Hud', 2, 0, 1, 10)
