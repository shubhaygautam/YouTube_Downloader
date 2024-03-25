from pytube import YouTube
from sys import argv

def display_menu():
    print("1. Download highest resolution video (MP4)")
    print("2. Download video in specific resolution (MP4)")
    print("3. Download audio only (MP3)")
    print("4. Exit")

def download_video(yt, resolution=None):
    if resolution:
        stream = yt.streams.filter(res=resolution, file_extension='mp4').first()
    else:
        stream = yt.streams.get_highest_resolution()
    try:
        stream.download('./YT Downloaded', filename=f'{yt.title}.mp4')  # Change file extension to 'mp4'
        print(f"Video downloaded successfully as {yt.title}.mp4")
    except Exception as e:
        print(f"Error downloading video: {e}")

def download_audio(yt):
    audio_stream = yt.streams.filter(only_audio=True).first()
    try:
        audio_stream.download(output_path='./YT Downloaded', filename='audio')
        print(f"Audio downloaded successfully as audio.mp4")
    except Exception as e:
        print(f"Error downloading audio: {e}")

def main():
    link = argv[1]
    try:
        yt = YouTube(link)
        print("Title: ", yt.title)
        print("Views: ", yt.views)

        while True:
            display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                download_video(yt)
            elif choice == '2':
                resolution = input("Enter desired resolution (e.g., 720p, 480p): ")
                download_video(yt, resolution)
            elif choice == '3':
                download_audio(yt)
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
