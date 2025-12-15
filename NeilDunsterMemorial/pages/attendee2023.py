import reflex as rx
from ..Nav import navigation


def actionMenuItem2023():
    return rx.container(
        rx.desktop_only(
            rx.text(
                "2023",
                size="9",
                weight="bold",
                margin_bottom="25px"

            ),
            rx.text(
                "This years annual Neil Dunster Memorial was held on the same weekend as last year, June 16 - 17, 2023. ",
                size="6",
                margin_bottom="10px",
            ),

            rx.text(
                "Tee off times for June 16, 2023 are:",
                size="6",
            ),

            rx.list.unordered(
                rx.list.item("11:50 - Antonio Leal and Jeff Mulcock, Doug Corrigan and Steve Gallant"),
                rx.list.item("12:00 - Brian Male and Don Rowan, Al Scott and Johnny Stevens"),
                rx.list.item("12:10 - Steve Turner and Brian Gow, George Vadeboncouer and Dan Kalil"),
                rx.list.item("12:20 - Brian Webster and Steve Fournier, Ron Prosper and Bob Prosper"),
                list_style_type="none"
            ),

            rx.text(
                "The following participated:",
                size="6",
                margin_top="10px",
                margin_bottom="10px"
            ),

            rx.hstack(
                rx.list.unordered(
                    rx.list.item("Doug Corrigan"),
                    rx.list.item("Steve Fournier"),
                    rx.list.item("Steve Gallant"),
                    rx.list.item("Brian Gow"),
                    rx.list.item("Dan Kalil"),
                    rx.list.item("Tony Leal"),
                    rx.list.item("Brian Male"),
                    rx.list.item("Jeff Mulcock"),
                    rx.list.item("Rob Prosper"),
                    rx.list.item("Ron Prosper"),
                    rx.list.item("Don Rowan"),
                    rx.list.item("Allan Scott"),
                    rx.list.item("John Stevens"),
                    rx.list.item("Steve Turner"),
                    rx.list.item("George Vadeboncoeur"),
                    rx.list.item("Brian Webster"),
                    style={"font-size": "20px"},
                    list_style_type="none"
                ),

                rx.image(
                    src="/gallery/year2023.jpg",
                    alt="year2023",
                    width="400px",
                    height="400px",
                    margin_left="200px",
                )
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.text(
                    "2023",
                    size="9",
                    weight="bold",
                    margin_bottom="25px"

                ),
                rx.text(
                    "This years annual Neil Dunster Memorial was held on the same weekend as last year, June 16 - 17, 2023. ",
                    size="6",
                    margin_bottom="10px",
                ),

                rx.text(
                    "Tee off times for June 16, 2023:",
                    size="6",
                ),

                rx.list.unordered(
                    rx.list.item("11:50 - Antonio Leal and Jeff Mulcock, Doug Corrigan and Steve Gallant"),
                    rx.list.item("12:00 - Brian Male and Don Rowan, Al Scott and Johnny Stevens"),
                    rx.list.item("12:10 - Steve Turner and Brian Gow, George Vadeboncouer and Dan Kalil"),
                    rx.list.item("12:20 - Brian Webster and Steve Fournier, Ron Prosper and Bob Prosper"),
                    list_style_type="none"
                ),

                rx.text(
                    "The following participated:",
                    size="6",
                    margin_top="10px",
                    margin_bottom="10px"
                ),

                rx.image(
                    src="/gallery/year2023.jpg",
                    alt="year2023",
                    width="400px",
                    height="400px",

                ),

                rx.list.unordered(
                    rx.list.item("Doug Corrigan"),
                    rx.list.item("Steve Fournier"),
                    rx.list.item("Steve Gallant"),
                    rx.list.item("Brian Gow"),
                    rx.list.item("Dan Kalil"),
                    rx.list.item("Tony Leal"),
                    rx.list.item("Brian Male"),
                    rx.list.item("Jeff Mulcock"),
                    rx.list.item("Rob Prosper"),
                    rx.list.item("Ron Prosper"),
                    rx.list.item("Don Rowan"),
                    rx.list.item("Allan Scott"),
                    rx.list.item("John Stevens"),
                    rx.list.item("Steve Turner"),
                    rx.list.item("George Vadeboncoeur"),
                    rx.list.item("Brian Webster"),
                    style={"font-size": "20px"},
                    list_style_type="none"
                ),
        ),


        )
    )


@rx.page("/attendees2023", title="Attendees 2023")
def attendees2023():
 return (
     navigation.navbar_dropdown(),
     actionMenuItem2023()
 )