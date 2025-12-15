import reflex as rx
import NeilDunsterMemorial.NeilDunsterMemorial

class sharedState(rx.State):

    @rx.event
    def eventMenuItem2017(self):
        return rx.redirect("./attendees2017")


    @rx.event
    def eventMenuItem2018(self):
        return rx.redirect("./attendees2018")

    @rx.event
    def eventMenuItem2019(self):
        return rx.redirect("./attendees2019")

    @rx.event
    def eventMenuItem2020(self):
        return rx.redirect("./attendees2020")

    @rx.event
    def eventMenuItem2021(self):
        return rx.redirect("./attendees2021")

    @rx.event
    def eventMenuItem2022(self):
        return rx.redirect("./attendees2022")

    @rx.event
    def eventMenuItem2023(self):
        return rx.redirect("./attendees2023")

    @rx.event
    def eventMenuItem2024(self):
        return rx.redirect("./attendees2024")

    @rx.event
    def eventMenuItem2025(self):
        return rx.redirect("./attendees2025")

    @rx.event
    def eventMenuItem2026(self):
        return rx.redirect("./attendees2026")


    @rx.event
    def eventMenuItemNews(self):
        return rx.redirect("/news")

    @rx.event
    def eventMenuItemPlayers(self):
        return rx.redirect("/players")

    @rx.event
    def eventMenuItemResults(self):
        return rx.redirect("/results")

    @rx.event
    def eventMenuItemGallery(self):
        return rx.redirect("/gallery")

    @rx.event
    def eventMenuItemSponsors(self):
        return rx.redirect("/sponsors")

    @rx.event
    def eventMenuItemHome(self):
        return rx.redirect("/")


