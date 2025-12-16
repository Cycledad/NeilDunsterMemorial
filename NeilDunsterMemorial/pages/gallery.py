import os

import reflex as rx
from ..Nav import navigation

class GalleryState(rx.State):
    selectedImage: str = ""


    def select(self, imgURL: str):
        """Set the selected image and redirect."""
        self.selectedImage = imgURL
        print(imgURL)
        return rx.redirect("/viewer")



def retrieveFolderFilenames(folderName: str):
    listFilenames: list = []
    for fileName in os.listdir(folderName):
        listFilenames.append(fileName)
        # print(fileName)

    return listFilenames

def showButtons(img: str):

    #imgURL = "./gallery/year2017.jpg"
        #imgURL = "./gallery/img"
    print(img)



    return(

        rx.button(
            rx.image(
                src=img,
                width="100%",
            ),
            on_click=GalleryState.select(img),
            background="transparent",
            color="black",
            height="100%",
            width="105%",  #removes excess column gaps
            cursor="pointer",
        )
        #GalleryState.select("./gallery/" + img)

        #rx.image(src="./gallery/" + img)

        # rx.button(
        #     "button",
        #     on_click=GalleryState.select("./gallery/" + img),
        #     position="absolute",
        #     top="80px",
        #     left="125px",
        #     background="transparent",
        #     # background="blue",
        #     color="black",
        #     height="100%",
        #     width="15%",
        #     cursor="pointer",
        # ),
    )


@rx.page("/gallery", title="Gallery")
def gallery():

    listImgFileNames: list = retrieveFolderFilenames("./assets/gallery")

    return (
        navigation.navbar_dropdown(),
        rx.grid(
            rx.foreach(
                listImgFileNames,
                #lambda img: rx.image(src="./gallery/" + img)
                lambda img: showButtons("./gallery/" + img)
            ),
            width="100%",
            columns="5",
            spacing="1",
            column_gap="0px",
            #margin="10px",
            style={"column-gap": "0px"}

        )
 )

