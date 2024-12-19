from chapters import chapters

def create_mp3_files(chapter_no):
    with open('quran.txt', 'a', encoding='UTF-8') as file:
        chapter_no_padded = f'00{chapter_no}'


def play(chapter: str, verse=0):
    chapter_no, verses = chapters[chapter]
    for ayat in range(verse-1, verses):
        print(ayat+1)
    print(chapter_no)
    

    

play('Hud')
