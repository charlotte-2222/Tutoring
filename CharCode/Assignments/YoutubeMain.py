import os
import pytube


class bcolors:  # This class is used to make the text in the terminal colourful
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# This is the main function of the program
def dlVideo(url, title, author):
    pytube.YouTube(url).streams.get_highest_resolution().download(
        output_path=f"C:\\Users\\{os.getlogin()}\\Pictures\\Youtube\\",
        filename=rename + ".mp4",
        skip_existing=True,
        timeout=180)
    # This prints a message to the user to confirm the video has been downloaded
    print(f"{bcolors.BOLD}{bcolors.OKCYAN}Downloaded successfully!{bcolors.ENDC}{bcolors.ENDC}")


url = input("Enter the URL of the video: ")  # This is the link of the video
title = pytube.YouTube(url).title
author = pytube.YouTube(url).author
print(
    f"This is {bcolors.OKGREEN}'{title}'{bcolors.ENDC} by {bcolors.OKCYAN}{author}{bcolors.ENDC}")  # This prints the title and author of the video

firstRename = input("\nWhat do you want to name the video? Enter: ")  # this is the rename of the video
rename = firstRename.replace(" ", "-")  # this replaces the spaces in the rename with dashes
print(
    "Is this correct? "f"C:\\Users\\{os.getlogin()}\\Pictures\\Youtube\\{rename}")  # this prints the rename of the video

if input("Y/N: ").upper() == "Y":  # this asks the user if the video is correct
    pass  # pass if the video is correct
else:
    print("Please try again")  # this prints if the video is not correct
    exit()  # this exits the program

dlReq = input(
    "Do you want to download the video? (Y/N): ").upper()  # this asks the user if they want to download the video

if dlReq == "Y":  # this if statement asks if the user wants to download the video
    dlVideo(url, title, author)  # this downloads the video
elif dlReq == "N":  # this if statement asks if the user does not want to download the video
    print(
        f"{bcolors.WARNING}Video will not be downloaded{bcolors.ENDC}")  # this prints if the user does not want to download the video
    exit(0)  # this exits the program
else:
    print(f"{bcolors.WARNING}Invalid input{bcolors.ENDC}")  # this prints if the user enters an invalid input
    exit(0)  # this exits the program
