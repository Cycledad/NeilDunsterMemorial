import reflex as rx
from ..Nav import navigation


def actionMenuItem2024():
    return rx.container(

        rx.text(
            "2024",
            size="9",
            weight="bold",
            margin_bottom="25px"

        ),
        rx.text(
            "For the third time, this years annual Neil Dunster Memorial was held on June 16 - 17, 2024 ",
            "with the first tee off at 11:30 am on Friday",
            size="6",
            margin_bottom="10px",
        ),

        rx.text(
            "The following participated:",
            size="6",
            margin_bottom="10px"
        ),

        rx.list.unordered(
            rx.list.item("Mark Campbell"),
            rx.list.item("Brian Clarke"),
            rx.list.item("Jim Cooper"),
            rx.list.item("Doug Corrigan"),
            rx.list.item("Wayne Davis"),
            rx.list.item("Pat Higgins"),
            rx.list.item("Dan Kalil"),
            rx.list.item("Tony Leal"),
            rx.list.item("Brian Male"),
            rx.list.item("Jeff Mulcock"),
            rx.list.item("Rob Prosper"),
            rx.list.item("Ron Prosper"),
            rx.list.item("Allan Scott"),
            rx.list.item("John Stevens"),
            rx.list.item("Steve Turner"),
            rx.list.item("George Vadeboncoeur"),
            rx.list.item("Colin Vandyk"),
            rx.list.item("Brian Webster"),
            style={"font-size": "20px"},
            list_style_type="none"
        )
    )


@rx.page("/attendees2024", title="Attendees 2024")
def attendees2024():
 return (
     navigation.navbar_dropdown(),
     actionMenuItem2024()
 )