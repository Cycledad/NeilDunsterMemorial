import reflex as rx
from ..Nav import navigation


def actionMenuItem2024():
    return rx.container(
        rx.desktop_only(
            rx.text(
                "2024",
                size="9",
                weight="bold",
                margin_bottom="25px"

            ),
            rx.text(
                "For the third time, this years annual Neil Dunster Memorial was held on June 16 - 17, 2024 ",
                "with the first tee off at 11:30 am on Friday",
                size="5",
                margin_bottom="10px",
            ),

            rx.text(
                "Special thanks to Jeff Mulcock for the hoodies, caps and golf ball gifts and awards.",
                size="5",
            ),
            rx.text(
                "Special thanks to Turbo for the cap gift awards. ",
                size="5",
            ),
            rx.text(
                "Special thanks to Webby the official safe keeper of our team trophy and individual trophy awards and for ",
                "annually getting our yearly winners engraved on our awards.",
                size = "5",
            ),
            rx.text(
                "Special thanks to Dougie our golf director and helping out with the tournament scores and playoff format. ",
                "The grill and sausages were a hit and many thanks for keeping us updated and our glasses full with the latest "
                "cocktail trends in today’s market.  The transfusions were great 🥃 ",
                size="5",
            ),
            rx.text(
                "Special thanks to Barnie……sorry about that Fournier…..I meant to say Earnie…… and Fournier for pulling out the Rolodex and ",
                "bringing in last minute players to fill in some empty spots.  Many thanks to Pat Higgins, Jim Cooper, Clarkey and Colin Vandyk for ",
                "joining us this year.  ",
                size="5",
                margin_bottom="10px",
            ),

            rx.text(
                "The following participated:",
                size="6",
                margin_bottom="10px"
            ),

            rx.hstack(

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
                ),

                rx.image(
                    src="./gallery/year2024.jpg",
                    margin_top="65px",
                    margin_left="135px",
                ),

            ),
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.text(
                    "2024",
                    size="9",
                    weight="bold",
                    margin_bottom="25px"

                ),
                rx.text(
                    "For the third time, this years annual Neil Dunster Memorial was held on June 16 - 17, 2024 ",
                    "with the first tee off at 11:30 am on Friday",
                    size="5",
                    margin_bottom="10px",
                ),

                rx.text(
                    "Special thanks to Jeff Mulcock for the hoodies, caps and golf ball gifts and awards.",
                    size="5",
                ),
                rx.text(
                    "Special thanks to Turbo for the cap gift awards. ",
                    size="5",
                ),
                rx.text(
                    "Special thanks to Webby the official safe keeper of our team trophy and individual trophy awards and for ",
                    "annually getting our yearly winners engraved on our awards.",
                    size="5",
                ),
                rx.text(
                    "Special thanks to Dougie our golf director and helping out with the tournament scores and playoff format. ",
                    "The grill and sausages were a hit and many thanks for keeping us updated and our glasses full with the latest "
                    "cocktail trends in today’s market.  The transfusions were great 🥃 ",
                    size="5",
                ),
                rx.text(
                    "Special thanks to Barnie……sorry about that Fournier…..I meant to say Earnie…… and Fournier for pulling out the Rolodex and ",
                    "bringing in last minute players to fill in some empty spots.  Many thanks to Pat Higgins, Jim Cooper, Clarkey and Colin Vandyk for ",
                    "joining us this year.  ",
                    size="5",
                    margin_bottom="10px",
                ),

                rx.text(
                    "The following participated:",
                    size="6",
                    margin_bottom="10px"
                ),

                rx.image(
                    src="./gallery/year2024.jpg",
                    #margin_top="65px",
                    #margin_left="135px",
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
            ),
            ),
        )
    )


@rx.page("/attendees2024", title="Attendees 2024")
def attendees2024():
 return (
     navigation.navbar_dropdown(),
     actionMenuItem2024()
 )