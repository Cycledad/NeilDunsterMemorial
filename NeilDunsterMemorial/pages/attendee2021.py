import reflex as rx
from ..Nav import navigation



def actionMenuItem2021():
    return rx.container(

        rx.text(
            "2021",
            size="9",
            weight="bold",
            margin_bottom="25px"

        ),
        rx.text(
            "Unfortunately, due to covid, the event was cancelled in 2021",
            size="6",
        )
    )


@rx.page("/attendees2021", title="Attendees 2021")
def attendees2021():
 return (
     navigation.navbar_dropdown(),
     actionMenuItem2021()
 )