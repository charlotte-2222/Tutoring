# begin here
# import the necessary modules

# This program is my first attempt at a YouTube video downloader

# This imports the module essential to our programme, pytube
import pytube

from pytube import YouTube


#This tells the user the premise of the programme
print("Welcome to my video downloading programme")


# This allows the user to select the video they wish to download
link = input("Please enter the link of your desired video")


# This allows us to use the module functions with the video link
vid = YouTube(link)

# This ensures the selected video is downloaded in the highest video resolution
res = vid.streams.get_highest_resolution()

# This downloads the video itself
res.download()

# This acts as confirmation to the user that the video has successfully downloaded
print("Video downloaded in the project file")