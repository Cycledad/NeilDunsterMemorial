import reflex as rx
from ..Nav import navigation

def actionMenuItem2025():
    return rx.container(
        rx.desktop_only(
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
                "Friday tee off groups:",
                size="6",
                margin_bottom="10px",
            ),
            rx.text("Group 1"),
            rx.list.unordered(
                rx.list.item("Antonio Leal"),
                rx.list.item("Jeff Mulcock"),
                rx.list.item("Doug Corrigan"),
                rx.list.item("Wayne Davis"),
                list_style_type="none",
            ),
            rx.text("Group 2"),
            rx.list.unordered(
                rx.list.item("Al Scott"),
                rx.list.item("George Vadeboncouer"),
                rx.list.item("Dan Kalil"),
                rx.list.item("Steve Turner"),
                list_style_type="none",
            ),

            rx.text("Group 3"),
            rx.list.unordered(
                rx.list.item("Brian Gow"),
                rx.list.item("Greg Laturnus"),
                rx.list.item("John Stevens"),
                rx.list.item("Ron Prosper"),
                list_style_type="none",
            ),

            rx.text("Group 4"),
            rx.list.unordered(
                rx.list.item("Rob Prosper"),
                rx.list.item("Steve Arbuckle"),
                rx.list.item("Brian Male"),
                rx.list.item("Colin Van Dyk"),
                list_style_type="none",
            ),

            rx.text("Group 5"),
            rx.list.unordered(
                rx.list.item("Steve Fournier"),
                rx.list.item("Les Bell"),
                rx.list.item("Steve Gallant"),
                rx.list.item("Brian Webster"),
                list_style_type="none",
                margin_bottom="10px",
            ),

            rx.text(
                "Congratulations to this years winning group:",
                size="6",
                margin_bottom="10px",
            ),
            rx.list.unordered(
                rx.list.item("Captain: Brian Webster"),
                rx.list.item("Rob Prosper"),
                rx.list.item("Brian Gow"),
                rx.list.item("Brian Male"),
                list_style_type="none",
                margin_bottom="10px",
            ),

            rx.text(
                "Individual awards:",
                size="6",
                margin_bottom="10px",
            ),

            rx.list.unordered(
                rx.list.item("Closest to the pin: Brian Webster"),
                rx.list.item("Longest drive: Rob Prosper"),
                rx.list.item("Low gross: Brian Webster"),
                rx.list.item("Most honest: Brian Male"),
                list_style_type="none",
                margin_bottom="10px",
            ),

            rx.text(
                "Many thanks to Webby for keeping our treasured trophies safe and updated with engraved memories, for the Chemist who continues ",
                "to educate us in spirit etiquette and quality and supply us with amazing drinks. ",
                "Special thanks to Colin for bringing the keg and keeping the beer flowing.",
                margin_bottom="10px"
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
        ),
        rx.mobile_and_tablet(
            rx.vstack(
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
                    "Friday tee off groups:",
                    size="6",
                    margin_bottom="10px",
                ),
                rx.text("Group 1"),
                rx.list.unordered(
                    rx.list.item("Antonio Leal"),
                    rx.list.item("Jeff Mulcock"),
                    rx.list.item("Doug Corrigan"),
                    rx.list.item("Wayne Davis"),
                    list_style_type="none",
                ),
                rx.text("Group 2"),
                rx.list.unordered(
                    rx.list.item("Al Scott"),
                    rx.list.item("George Vadeboncouer"),
                    rx.list.item("Dan Kalil"),
                    rx.list.item("Steve Turner"),
                    list_style_type="none",
                ),

                rx.text("Group 3"),
                rx.list.unordered(
                    rx.list.item("Brian Gow"),
                    rx.list.item("Greg Laturnus"),
                    rx.list.item("John Stevens"),
                    rx.list.item("Ron Prosper"),
                    list_style_type="none",
                ),

                rx.text("Group 4"),
                rx.list.unordered(
                    rx.list.item("Rob Prosper"),
                    rx.list.item("Steve Arbuckle"),
                    rx.list.item("Brian Male"),
                    rx.list.item("Colin Van Dyk"),
                    list_style_type="none",
                ),

                rx.text("Group 5"),
                rx.list.unordered(
                    rx.list.item("Steve Fournier"),
                    rx.list.item("Les Bell"),
                    rx.list.item("Steve Gallant"),
                    rx.list.item("Brian Webster"),
                    list_style_type="none",
                    margin_bottom="10px",
                ),

                rx.text(
                    "Congratulations to this years winning group:",
                    size="6",
                    margin_bottom="10px",
                ),
                rx.list.unordered(
                    rx.list.item("Captain: Brian Webster"),
                    rx.list.item("Rob Prosper"),
                    rx.list.item("Brian Gow"),
                    rx.list.item("Brian Male"),
                    list_style_type="none",
                    margin_bottom="10px",
                ),

                rx.text(
                    "Individual awards:",
                    size="6",
                    margin_bottom="10px",
                ),

                rx.list.unordered(
                    rx.list.item("Closest to the pin: Brian Webster"),
                    rx.list.item("Longest drive: Rob Prosper"),
                    rx.list.item("Low gross: Brian Webster"),
                    rx.list.item("Most honest: Brian Male"),
                    list_style_type="none",
                    margin_bottom="10px",
                ),

                rx.text(
                    "Many thanks to Webby for keeping our treasured trophies safe and updated with engraved memories, for the Chemist who continues ",
                    "to educate us in spirit etiquette and quality and supply us with amazing drinks. ",
                    "Special thanks to Colin for bringing the keg and keeping the beer flowing.",
                    margin_bottom="10px"
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
        )

    )


@rx.page("/attendees2025", title="Attendees 2025")
def attendees2025():
 return (
     navigation.navbar_dropdown(),
     actionMenuItem2025()
 )