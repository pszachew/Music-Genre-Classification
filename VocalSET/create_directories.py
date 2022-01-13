import os


def clean():
    for gender in os.listdir("D:\VocalSET\FULL"):
        for el in os.listdir("D:\VocalSET\FULL\\"+gender):
            for x in os.listdir("D:\VocalSET\FULL\\"+gender + "\\" + el):
                for audio in os.listdir("D:\VocalSET\FULL\\"+gender + "\\" + el + "\\" + x):
                    if audio == ".DS_Store" or audio == "_DS_Store":
                        os.remove("D:\VocalSET\FULL\\" + gender + "\\" + el + "\\" + x + "\\" + audio)


def mkdirs():
    for gender in os.listdir("D:\VocalSET\FULL"):
        os.mkdir("D:\VocalSET\embedded\\"+gender)
        for el in os.listdir("D:\VocalSET\FULL\\"+gender):
            os.mkdir("D:\VocalSET\embedded\\" + gender + "\\" + el)
            for x in os.listdir("D:\VocalSET\FULL\\"+gender + "\\" + el):
                os.mkdir("D:\VocalSET\embedded\\" + gender + "\\" + el + "\\" + x)


if __name__ == "__main__":
    mkdirs()