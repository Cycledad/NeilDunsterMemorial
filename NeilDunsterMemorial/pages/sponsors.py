import reflex as rx
from ..Nav import navigation


@rx.page("/sponsors", title="Sponsors")
def sponsors():
    return (
        navigation.navbar_dropdown(),
        rx.container(
            rx.center(
                rx.desktop_only(
                    rx.grid(
                        rx.image(
                            src="/sponsors/taggart1.png"
                        ),
                        rx.image(
                            src="/sponsors/stantec1.png"
                        ),
                        rx.image(
                            src="/sponsors/scheel2.jpg"
                        ),
                        rx.image(
                            src="/sponsors/leal1.jpg"
                        ),
                        columns="3",
                        spacing="4"


                    )
                ),
                rx.mobile_and_tablet(
                    rx.vstack(
                        rx.image(
                            src="/sponsors/taggart1.png"
                        ),
                        rx.image(
                            src="/sponsors/stantec1.png"
                        ),
                        rx.image(
                            src="/sponsors/scheel2.jpg"
                        ),
                        rx.image(
                            src="/sponsors/leal1.jpg"
                        ),
                    )

                )
            )
        )

    )