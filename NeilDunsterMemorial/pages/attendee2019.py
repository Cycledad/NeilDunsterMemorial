import reflex as rx
from ..Nav import navigation



def actionMenuItem2019():
    return rx.container(

        rx.text(
            "2019",
            size="9",
            weight="bold",
            margin_bottom="25px"

        ),

        rx.text(
            "The 3rd annual Neil Dunster Memorial was held June 21 - 22, 2019.",
            size="6",
            margin_bottom="10px",
        ),

        rx.text(
            "The first tee off time for June 21, 2019 is 1:20:",
            size="6",
            margin_bottom="25px"
        ),

        rx.list.unordered(
            rx.list.item("Antonio Leal and Jeff Mulcock, Doug Corrigan and Wayne Davis"),
            rx.list.item("Al Scott and Mark Campbell, Steve Arbuckle and John Stevens"),
            rx.list.item("Steve Gallant and Brian Male, Brian Gow and Steve Turner"),
            rx.list.item("Neil Dunster and George Vadebonceour, Mike Kehoe and Brian Webster"),
            rx.list.item("Tony Bond and Dan Kalil, John Chatterton"),
            #list_style_type="none",
            style={"font-size": "20px"},
        ),

    )


@rx.page("/attendees2019", title="Attendees 2019")
def attendees2019():
 return (
     navigation.navbar_dropdown(),
     actionMenuItem2019()
 )