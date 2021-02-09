import os

def crawlMedia(_include, _type):
    if os.path.isdir(".\Media") == False:
        os.mkdir(".\Media")
        print("Media Directory Created")
    else:
        pass