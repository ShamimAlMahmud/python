import os
choice = input("Want to restart? (Y/N)")

if choice is "Y":
    os.system("restart /s /t /1")
else:
    exit()