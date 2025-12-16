import reflex as rx
from ..Nav import navigation

def actionMenuItem2025():
    return rx.container(

        rx.text(
            "2025",
            size="9",
            weight="bold",
            margin_bottom="25px"

        ),
        rx.text(
            "This years annual Neil Dunster Memorial was held on June 13 - 14, 2025.",
            size="6",
            margin_bottom="10px",
        ),

        rx.text(
            "Congratulations to this years winning group:",
            size="5"
        ),
        rx.list.unordered(
            rx.list.item("Captain: Brian Webster"),
            rx.list.item("Rob Prosper"),
            rx.list.item("Brian Gow"),
            rx.list.item("Brian Male"),
            list_style_type="none",

        ),

        rx.text(
            "Individual awards:",
            size="5",
        ),

        rx.list.unordered(
            rx.list.item("Closest to the pin: Brian Webster"),
            rx.list.item("Longest drive: Rob Prosper"),
            rx.list.item("Low gross: Brian Webster"),
            rx.list.item("Most honest: Brian Male"),
            list_style_type="none",

        ),

        rx.text(
            "The following participated:",
            size="6",
            margin_bottom="10px"
        ),

        rx.list.unordered(
            rx.list.item("Steve Arbuckle"),
            rx.list.item("Les Bell"),
            rx.list.item("Doug Corrigan"),
            rx.list.item("Wayne Davis"),
            rx.list.item("Steve Fournier"),
            rx.list.item("Steve Gallant"),
            rx.list.item("Brian Gow"),
            rx.list.item("Dan Kalil"),
            rx.list.item("Greg Laternus"),
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


@rx.page("/attendees2025", title="Attendees 2025")
def attendees2025():
 return (
     navigation.navbar_dropdown(),
     actionMenuItem2025()
 )