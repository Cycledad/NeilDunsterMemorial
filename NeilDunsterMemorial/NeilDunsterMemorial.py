"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from reflex import redirect

import NeilDunsterMemorial.pages.player

from .pages import attendee2017 as page2017
from .pages import attendee2018 as page2018
from .pages import attendee2019 as page2019
from .pages import attendee2020 as page2020
from .pages import attendee2021 as page2021
from .pages import attendee2022 as page2022
from .pages import attendee2023 as page2023
from .pages import attendee2024 as page2024
from .pages import attendee2025 as page2025
from .pages import attendee2026 as page2026
from .pages import gallery as gallery
from .pages import results as results
from .pages import sponsors as sponsors
from .pages import news as news


from .Nav import navigation
from .GlobalState import events
from .pages import *


@rx.page("/index", title="Home")
def index():

 return (
    navigation.navbar_dropdown(),

    rx.image(
        src="/gallery/neil1.jpg",
        width="100vw",
        height="90vh"    ),

 ),


app = rx.App()
app.add_page(index)
app.add_page(page2017.attendees2017)
app.add_page(page2018.attendees2018)
app.add_page(page2019.attendees2019)
app.add_page(page2020.attendees2020)
app.add_page(page2021.attendees2021)
app.add_page(page2022.attendees2022)
app.add_page(page2023.attendees2023)
app.add_page(page2024.attendees2024)
app.add_page(page2025.attendees2025)
app.add_page(page2026.attendees2026)
app.add_page(NeilDunsterMemorial.pages.player.players)
app.add_page(gallery.gallery)
app.add_page(results.results)
app.add_page(sponsors.sponsors)
app.add_page(news.news)
