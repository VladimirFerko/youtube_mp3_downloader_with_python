import youtube_dl
import os
import sys
import time
from pydub import AudioSegment

# options for ytb dl

ydl_opts = {
    'format' : 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

# download method, it just take the link and options and download the video

def download(link, ydl_opts):
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    try:
        ydl.download([link])
    except:
        print('wrong link')

# recursive main function where the downlaod function is called, also you are imputting the link

def main():
    while True:
        try:
            link = input('Enter the link, if you dont want to download anymore, press enter: ')

            if link.strip() == '':
                raise ValueError('')

            download(link, ydl_opts)
            title = youtube_dl.YoutubeDL().extract_info(link, download=False)["title"]

            # this iterates through songs in the repository, if song titles are matching, then rename the song to get the pure title

            for f in os.listdir():
                if title in f:
                    os.rename(f, title)

                    # converting any file to .mp3

                    AudioSegment.from_file(title).export(title, format = 'mp3')
                    break

        except ValueError:
            print('Thank you for your downloading')
            for i in range(1,4):
                print(f'\t The system will shut down in {i}')
                time.sleep(0.5)
            sys.exit(1)

        except:
            pass

    main()

if __name__ == '__main__':
    while True:
        try:
            path = input('Enter the path : ')
            os.chdir(path.strip())
            print('ok')
            break
        except:
            print('Bad path')

    main()