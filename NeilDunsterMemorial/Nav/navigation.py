import reflex as rx
from NeilDunsterMemorial.GlobalState import events
from NeilDunsterMemorial.pages import *


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(rx.text(text, size="4", weight="medium", color="black"), href=url)


def navbar_dropdown() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("Neil Dunster Memorial", size="7", weight="bold"),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/"),
                    navbar_link("News", "/news"),
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.button(
                                rx.text("Memorial Years", size="4", weight="medium", color="black"),
                                rx.icon("chevron-down"),
                                weight="medium",
                                variant="ghost",
                                size="3",
                                color="black",
                            ),
                        ),
                        rx.menu.content(
                            rx.menu.item("2017", on_click=events.sharedState.eventMenuItem2017),
                            rx.menu.item("2018", on_click=events.sharedState.eventMenuItem2018),
                            rx.menu.item("2019", on_click=events.sharedState.eventMenuItem2019),
                            rx.menu.item("2020", on_click=events.sharedState.eventMenuItem2020),
                            rx.menu.item("2021", on_click=events.sharedState.eventMenuItem2021),
                            rx.menu.item("2022", on_click=events.sharedState.eventMenuItem2022),
                            rx.menu.item("2023", on_click=events.sharedState.eventMenuItem2023),
                            rx.menu.item("2024", on_click=events.sharedState.eventMenuItem2024),
                            rx.menu.item("2025", on_click=events.sharedState.eventMenuItem2025),
                            rx.menu.item("2026", on_click=events.sharedState.eventMenuItem2026),
                        ),
                    ),
                    navbar_link("Participants", "/players"),
                    #navbar_link("Results", "/results"),
                    navbar_link("Gallery", "/gallery"),
                    navbar_link("Sponsors", "/sponsors"),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",


            ),

        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg", width="2em", height="auto", border_radius="25%"
                    ),
                    rx.heading("Neil Dunster Memorial", size="6", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.menu.item("Home", on_click=events.sharedState.eventMenuItemHome),
                        rx.menu.item("News", on_click=events.sharedState.eventMenuItemNews),
                        rx.menu.sub(
                            rx.menu.sub_trigger("Memorial Years"),
                            rx.menu.sub_content(
                                rx.menu.item("2017", on_click=events.sharedState.eventMenuItem2017),
                                rx.menu.item("2018", on_click=events.sharedState.eventMenuItem2018),
                                rx.menu.item("2019", on_click=events.sharedState.eventMenuItem2019),
                                rx.menu.item("2020", on_click=events.sharedState.eventMenuItem2020),
                                rx.menu.item("2021", on_click=events.sharedState.eventMenuItem2021),
                                rx.menu.item("2022", on_click=events.sharedState.eventMenuItem2022),
                                rx.menu.item("2023", on_click=events.sharedState.eventMenuItem2023),
                                rx.menu.item("2024", on_click=events.sharedState.eventMenuItem2024),
                                rx.menu.item("2025", on_click=events.sharedState.eventMenuItem2025),
                                rx.menu.item("2026", on_click=events.sharedState.eventMenuItem2026),
                            ),
                        ),
                        rx.menu.item("Participants", on_click=events.sharedState.eventMenuItemPlayers),
                        #rx.menu.item("Results", on_click=events.sharedState.eventMenuItemResults),
                        rx.menu.item("Gallery", on_click=events.sharedState.eventMenuItemGallery),
                        rx.menu.item("Sponsors", on_click=events.sharedState.eventMenuItemSponsors),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        #bg=rx.color("accent", 3),
        bg=rx.color("green"),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )