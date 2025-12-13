import reflex as rx
from ..Nav import navigation



def actionMenuItem2026():
    return rx.container(

        rx.text(
            "2026",
            size="9",
            weight="bold",
            margin_bottom="25px"

        ),

        rx.text(
            "Coming soon!",
            size="6",)
    )



@rx.page("/attendees2026", title="Attendees 2026")
def attendees2026():
 return (
     navigation.navbar_dropdown(),
     actionMenuItem2026()
 )