import reflex as rx
from .gallery import GalleryState

#from .SharedState import ImageState

@rx.page(route="/viewer", title="Viewer Page")
def viewer():
    return rx.center(
        rx.vstack(

            rx.image(
                src=GalleryState.selectedImage,
                width="100%",
                height="80vh",
                border="2px solid #ccc",
                alt="Where is my image"
            ),

            rx.button(
                "Back",
                on_click=rx.redirect("./gallery"),
                color="black"
            ),
            position="relative"
        )
    )