import reflex as rx
from ..Nav import navigation

def results2025():
    return rx.container(
        rx.vstack(
            rx.text(
                "2025 Winning team:",
                size="6",
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
                size="6"
            ),

            rx.list.unordered(
                rx.list.item("Closest to the Pin: Brian Webster"),
                rx.list.item("Longest Drive: Rob Prosper"),
                rx.list.item("Low Gross: Brian Webster"),
                rx.list.item("Most Honest: Brian Male 'I think we should call this trophy 'The Barnie Award'"),
                list_style_type="none",
            ),
        )
)

@rx.page("/results", title="Results / Stats")
def results():
 return (
     navigation.navbar_dropdown(),
     results2025()

 )