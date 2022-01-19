import os


def clean():
    for gender in os.listdir("D:\VocalSET\FULL"):
        for el in os.listdir("D:\VocalSET\FULL\\"+gender):
            for x in os.listdir("D:\VocalSET\FULL\\"+gender + "\\" + el):
                for audio in os.listdir("D:\VocalSET\FULL\\"+gender + "\\" + el + "\\" + x):
                    if audio == ".DS_Store" or audio == "_DS_Store":
                        os.remove("D:\VocalSET\FULL\\" + gender + "\\" + el + "\\" + x + "\\" + audio)


def mkdirs():
    pth = "D:\VocalSET\\embedded_train\\"
    for gender in os.listdir("D:\VocalSET\FULL"):
        os.mkdir(pth+gender)
        for el in os.listdir("D:\VocalSET\FULL\\"+gender):
            os.mkdir(pth + gender + "\\" + el)
            for x in os.listdir("D:\VocalSET\FULL\\"+gender + "\\" + el):
                os.mkdir(pth + gender + "\\" + el + "\\" + x)


if __name__ == "__main__":
    mkdirs()