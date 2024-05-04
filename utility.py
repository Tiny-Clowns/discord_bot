def read_token():
    try:
        file=open("token.txt", "r")
        return file.readline()

    except Exception as ex:
        print(ex)