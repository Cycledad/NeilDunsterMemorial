import reflex as rx
from ..Nav import navigation


def actionMenuItem2020():
    return rx.container(

        rx.text(
            "2020",
            size="9",
            weight="bold",
            margin_bottom="25px"

        ),

        rx.text(
            "Unfortunately, due to covid, the event was cancelled in 2020",
            size="6",
        )
    )

@rx.page("/attendees2020", title="Attendees 2020")
def attendees2020():
 return (
     navigation.navbar_dropdown(),
     actionMenuItem2020()
 )