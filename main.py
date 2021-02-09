import crawlMedia

if __name__ == "__main__":
    # CLI Program

    print("Welcome to TweetSquirrel")
    print("1. Get Started")
    print("2. Exit")

    if(input() == "1"):
        print("\n[ Setting Scope ]")
        print("Select all to include. Separate by spaces.")
        print("1. Tweet\n2. Retweet\n3. Like")

        _include = input()
        print(_include)

        print("\n[ Setting Data Types ]")
        print("Select all to include. Separate by spaces.")
        print("1. Link\n2. Picture\n3. Video")

        _type = input()
        print(_type)

        crawlMedia.crawlMedia(_include, _type)

    else:
        print("\nBye Bye~")
        exit