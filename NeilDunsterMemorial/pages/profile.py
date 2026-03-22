import reflex as rx
from NeilDunsterMemorial.Nav import navigation


@rx.page("/profile", title="Course Profile")
def profile():
    return (

        rx.text(
            "Congratulations to Brian Webster on his retirement as of Oct 2025.",
            size="6",
            padding="10px",
            background_color="var(--tomato-3)",
        ),
    )
