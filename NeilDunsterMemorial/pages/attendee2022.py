import reflex as rx
from ..Nav import navigation

def actionMenuItem2022():
    return rx.container(

        rx.text(
            "2022",
            size="9",
            weight="bold",
            margin_bottom="25px"

        ),
        rx.text(
            "This years annual Neil Dunster Memorial was held June 16 - 17, 2022. ",
            "Of note, the weekend golf trip is renamed to honour our friend Neil. ",
            size="6",
            margin_bottom="10px",
        ),

        rx.text(
            "The following participated:",
            size="6",
            margin_bottom="10px"
        ),

        rx.list.unordered(
            rx.list.item("Brian Clarke"),
            rx.list.item("Doug Corrigan"),
            rx.list.item("Wayne Davis"),
            rx.list.item("Steve Fournier"),
            rx.list.item("Steve Gallant"),
            rx.list.item("Brian Gow"),
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
            rx.list.item("Brian Webster"),
            style={"font-size": "20px"},
            list_style_type="none"
        )
    )


@rx.page("/attendees2022", title="Attendees 2022")
def attendees2022():
 return (
     navigation.navbar_dropdown(),
     actionMenuItem2022()
 )