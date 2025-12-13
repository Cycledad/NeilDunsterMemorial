import reflex as rx

#import NeilDunsterMemorial.Nav.navigation as navx

from ..Nav import navigation as navx

def actionMenuItem2017():
    return rx.container(
        rx.desktop_only(
                rx.text(
                "2017",
                size="9",
                weight="bold",
                margin_bottom="25px"

            ),

            rx.text(
                "The inaugural year had a total of 12 people competing with the event taking place at Smugglers Glen Golf Course on June 17 - 18. "
                "Accommodations were located across the street from the golf course at the Glen House Resort. ",
                " The format to be used is the first round is our actual score to make up the best ball groups for the 2nd round.",
                size="6",
                margin_bottom="25px"
            ),


            rx.text(
                "The following participated:",
                size="6",
                margin_bottom="10px"

            ),

            rx.hstack(
                rx.list.unordered(
                    rx.list.item("Steve Arbuckle"),
                    rx.list.item("Mark Campbell"),
                    rx.list.item("Doug Corrigan"),
                    rx.list.item("Wayne Davis"),
                    rx.list.item("Neil Dunster"),
                    rx.list.item("Steve Gallant"),
                    rx.list.item("Tony Leal"),
                    rx.list.item("Brian Male"),
                    rx.list.item("Jeff Mulcock"),
                    rx.list.item("Allan Scott"),
                    rx.list.item("John Stevens"),
                    rx.list.item("Brian Webster"),
                    style={"font-size":"20px"},
                    list_style_type="none"
                ),

                rx.image(
                    src="/gallery/year2017.jpg",
                    width="400px",
                    height="400px",
                    margin_left="300px"
                )
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.text(
                    "2017",
                    size="9",
                    weight="bold",
                    margin_bottom="25px"

                ),

                rx.text(
                    "The inaugural year had a total of 12 people competing with the event taking place at Smugglers Glen Golf Course on June 17 - 18. "
                    "Accommodations were located across the street from the golf course at the Glen House Resort. ",
                    " The format to be used is the first round is our actual score to make up the best ball groups for the 2nd round.",
                    size="6",
                    margin_bottom="25px"
                ),

                rx.text(
                    "The following participated:",
                    size="6",
                    margin_bottom="10px"

                ),

                rx.image(
                    src="/gallery/year2017.jpg",
                    width="400px",
                    height="400px",

                ),

                rx.list.unordered(
                    rx.list.item("Steve Arbuckle"),
                    rx.list.item("Mark Campbell"),
                    rx.list.item("Doug Corrigan"),
                    rx.list.item("Wayne Davis"),
                    rx.list.item("Neil Dunster"),
                    rx.list.item("Steve Gallant"),
                    rx.list.item("Tony Leal"),
                    rx.list.item("Brian Male"),
                    rx.list.item("Jeff Mulcock"),
                    rx.list.item("Allan Scott"),
                    rx.list.item("John Stevens"),
                    rx.list.item("Brian Webster"),
                    style={"font-size": "20px"},
                    list_style_type="none"
                ),
            )
        )
    )


@rx.page("/attendees2017", title="Attendees 2017")
def attendees2017():
 return (
     navx.navbar_dropdown(),
     actionMenuItem2017()
 )