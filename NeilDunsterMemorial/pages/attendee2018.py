import reflex as rx
from ..Nav import navigation

def actionMenuItem2018():
    return rx.container(

        rx.text(
            "2018",
            size="9",
            weight="bold",
            margin_bottom="25px"

        ),

        rx.text(
            "The 2nd annual Neil Dunster Memorial was held June 22 - 23, 2018.",
            size="6",
            margin_bottom="10px",
        ),

        rx.text(
            "The following participated:",
            size="6",
            margin_bottom="10px"
        ),

        rx.list.unordered(
            rx.list.item("Steve Arbuckle"),
            rx.list.item("Tony Bond"),
            rx.list.item("Mark Campbell"),
            rx.list.item("Doug Corrigan"),
            rx.list.item("Wayne Davis"),
            rx.list.item("Neil Dunster"),
            rx.list.item("Steve Gallant"),
            rx.list.item("Brian Gow"),
            rx.list.item("Mike Kehoe"),
            rx.list.item("Dan Kalil"),
            rx.list.item("Tony Leal"),
            rx.list.item("Brian Male"),
            rx.list.item("Jeff Mulcock"),
            rx.list.item("Allan Scott"),
            rx.list.item("John Stevens"),
            rx.list.item("George Vadeboncoeur"),
            rx.list.item("Brian Webster"),
            style={"font-size": "20px"},
            list_style_type="none"
        )

    )


@rx.page("/attendees2018", title="Attendees 2018")
def attendees2018():
 return (
     navigation.navbar_dropdown(),
     actionMenuItem2018()
 )