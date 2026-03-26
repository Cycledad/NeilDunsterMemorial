import reflex as rx
from NeilDunsterMemorial.Nav import navigation

def  courseProfile():
    return(

        rx.text("Course Profile"),
        rx.text(" "),
        rx.text("Smuggler’s Glen Golf Course is a championship 18-hole facility that opened "
        "on July 21, 2005 for public and member play. The developers of Smuggler’s Glen, "
        "the Seal family, have owned and operated the Glen House Resort since 1962. "
        "The owners have over 50 years of experience in the hospitality industry and "
        "have invested a considerable amount of capital to create the area’s newest "
        "attraction, Smuggler’s Glen Golf Course. The Glen House is proud to offer yet "
        "another reason to visit the world-famous 1000 Islands, a region renowned for "
        "boating, fishing and vacationing amidst the St. Lawrence River’s natural beauty."),
    )

@rx.page("/profile", title="Course Profile")
def profile():
    return (
        navigation.navbar_dropdown(),
        courseProfile(),
    )


