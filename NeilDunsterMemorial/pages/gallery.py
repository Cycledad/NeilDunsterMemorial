import os

import reflex as rx
from ..Nav import navigation

def retrieveFolderFilenames(folderName: str):
    listFilenames: list = []
    for fileName in os.listdir(folderName):
        listFilenames.append(fileName)
        # print(fileName)

    return listFilenames





@rx.page("/gallery", title="Gallery")
def gallery():

    listImgFileNames: list = retrieveFolderFilenames("./assets/gallery")

    return (
        navigation.navbar_dropdown(),
        rx.grid(
            rx.foreach(
                listImgFileNames,
                lambda img: rx.image(src="./gallery/" + img)

            ),
            columns="5"
        )





 )