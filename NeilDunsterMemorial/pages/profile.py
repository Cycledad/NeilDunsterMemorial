import reflex as rx
from NeilDunsterMemorial.Nav import navigation

def  courseProfile():
    return(

            rx.text(
                "Course Profile",
                size="6",
                padding_top="50px",
            ),

            rx.text(
                "Smuggler’s Glen Golf Course is a championship 18-hole facility that opened "
                "on July 21, 2005 for public and member play. The developers of Smuggler’s Glen, "
                "the Seal family, have owned and operated the Glen House Resort since 1962. "
                "The owners have over 50 years of experience in the hospitality industry and "
                "have invested a considerable amount of capital to create the area’s newest "
                "attraction, Smuggler’s Glen Golf Course. The Glen House is proud to offer yet "
                "another reason to visit the world-famous 1000 Islands, a region renowned for "
                "boating, fishing and vacationing amidst the St. Lawrence River’s natural beauty.",
                size="5",
                padding="20px",
                padding_bottom="25px",
                # font = "sans-serif",
                #font = "Helvetica",
            ),

    )

def hole1():
    return(

        rx.text(
            "Hole 1, The Gorge",
            size="5",
            padding_top="20px",
            padding_left="20px",
            padding_bottom="10px",
        ),
        rx.text(
            "Par 5 for all tees. Keep driver in the bag – not needed. Don’t miss right, everything slopes that way.",
            size="4",
            padding_left="20px",
        ),
        rx.image(src="/imgHoles/map1.jpg"),
    )

def hole2():
    return(

        rx.text(
            "Hole 2, Upper Ridge",
            size="5",
            padding_top="45px",
            padding_left="20px",
            padding_bottom="10px",
        ),
        rx.text(
            "Usually into wind, so take extra club. Short in bunker okay, but don’t miss long or right. Beware the slope off "
            "the back and the cliff’s edge on right side of green.",
            size="4",
            padding_left="20px",
        ),
        rx.image(src="/imgHoles/map2.jpg"),
    )

def hole3():
    return(

        rx.text(
            "Hole 3 - Settlers Field",
            size="5",
            padding_top="45px",
            padding_left="20px",
            padding_bottom="10px",
        ),
        rx.text(
            "Aim either short of centre bunker or right side. Beware the tree on right side of the green, "
            "comes into play. Smallest green on course, be below the hole.",
            size="4",
            padding_left="20px",
        ),
        rx.image(src="/imgHoles/map3.jpg"),
    )

def hole4():
    return(

        rx.text(
            "Hole 4 - Bio Challenge",
            size="5",
            padding_top="45px",
            padding_left="20px",
            padding_bottom="10px",
        ),
        rx.text(
            "Toughest hole on the course for most golfers, par is outstanding. Lay up and stay out of the environmental "
            "areas (creeks). Extra club to green (uphill), long won’t hurt you on approach shot to green.",
            size="4",
            padding_left="20px",
        ),
        rx.image(src="/imgHoles/map4.jpg"),
    )

def hole5():
    return(

        rx.text(
            "Hole 5 - Coyote",
            size="5",
            padding_top="45px",
            padding_left="20px",
            padding_bottom="10px",
        ),
        rx.text(
            "Longest & toughest par 3, be happy with par. Beware of the hazard left side. Centre of the green is "
            "target, short won’t hurt you.",
            size="4",
            padding_left="20px",
        ),
        rx.image(src="/imgHoles/map5.jpg"),
    )

def hole6():
    return(

        rx.text("Hole 6 - Wild Creek",
            size="5",
            padding_top="45px",
            padding_left="20px",
            padding_bottom="10px",
        ),
        rx.text(
            "Beware the “Wild Creek” on right side, stay left. Aim at fairway bunker left side, fairway slopes toward creek. "
            "Big rolling green so take note of pin position and choose correct club.",
            size="4",
            padding_left="20px",
        ),
        rx.image(src="/imgHoles/map6.jpg"),
    )

def hole7():
    return(

         rx.text(
            "Hole 7 - Rolling Meadows",
            size="5",
            padding_top="45px",
            padding_left="20px",
            padding_bottom="10px",
        ),
        rx.text(
            "Beware out-of-bounds left side of fairway. Position your second shot to left side of fairway bunkers. "
            "Take extra club to green (uphill).",
            size="4",
            padding_left="20px",
        ),
        rx.image(src="/imgHoles/map7.jpg"),
    )

def hole8():
    return(

        rx.text(
            "Hole 8 - Lower Ridge",
            size="5",
            padding_top="45px",
            padding_left="20px",
            padding_bottom="10px",
        ),
        rx.text(
            "Long narrow green, club selection is vital. Keep out of right side bunker, left is easier up and down. "
            "Usually into wind, take extra club.",
            size="4",
            padding_left="20px",
        ),
        rx.image(src="/imgHoles/map8.jpg"),
    )

def hole9():
    return(

        rx.text(
            "9 - River View",
            size="5",
            padding_top="45px",
            padding_left="20px",
            padding_bottom="10px",
        ),
        rx.text(
            "Another hole driver best kept in bag. Try to lay up to 125-150 mark in. Take extra club (uphill) but don’t be long.",
            size="4",
            padding_left="20px",
        ),
        rx.image(src="/imgHoles/map9.jpg"),
    )

def hole10():
    return(

        rx.text(
            "Hole 10 - Bullseye",
            size="5",
            padding_top="45px",
            padding_left="20px",
            padding_bottom="10px",
        ),
        rx.text(
            "Huge elevated tee off, take one less club. Small round green, centre of green target – the bullseye.",
            size="4",
            padding_left="20px",
        ),
        rx.image(src="/imgHoles/map10.jpg"),
    )

def hole11():
    return(

        rx.text(
            "11 - Hawks Valley",
            size="5",
            padding_top="45px",
            padding_left="20px",
            padding_bottom="10px",
        ),
        rx.text(
            "Position your drive just up to the fairway bunker or right side of it. Narrow green, tough to hold approach shot in. "
            "Green side front bunker is easy up & down.",
            size="4",
            padding_left="20px",
        ),
        rx.image(src="/imgHoles/map11.jpg"),
    )

def hole12():
    return(

        rx.text(
            "12 - The Gambler",
            size="5",
            padding_top="45px",
            padding_left="20px",
            padding_bottom="10px",
        ),
        rx.text(
            "A great risk/reward hole! If going for the green, beware right side rocks. Don’t be short, everything rolls down "
            "the slope of the hill.",
            size="4",
            padding_left="20px",
        ),
        rx.image(src="/imgHoles/map12.jpg"),
    )

def hole13():
    return(

        rx.text("13",
                size="5",
                padding_top="45px",
                padding_left="20px",
                padding_bottom="10px",
        ),
        rx.text(
            "Can’t miss left or right (creeks). Target is right-centre of fairway, short of bunker. Aim right side for lay up, "
            "everything kicks left.",
            size="4",
            padding_left="20px",
        ),
        rx.image(src="/imgHoles/map13.jpg"),

    )

def hole14():
    return(

        rx.text(
            "14 - Serenity Valley",
            size="5",
            padding_top="45px",
            padding_left="20px",
            padding_bottom="10px",
        ),
        rx.text(
            "Big wide fairway, aim at left trap. Raised green requires extra club.",
            size="4",
            padding_left="20px",
        ),
        rx.image(src="/imgHoles/map14.jpg"),
    )

def hole15():
    return(

        rx.text(
            "15 - Rugged",
            size="5",
            padding_top="45px",
            padding_left="20px",
            padding_bottom="10px",
        ),
        rx.text(
            "Long par 4 requires drive down left side. Don’t miss right on second shot. "
            "Big long green, select club according to pin position.",
            size="4",
            padding_left="20px",
        ),
        rx.image(src="/imgHoles/map15.jpg"),
    )

def hole16():
    return(

        rx.text(
            "16 - Shorty",
            size="5",
            padding_top="45px",
            padding_left="20px",
            padding_bottom="10px",
        ),
        rx.text(
            "Everything kicks right onto the green. Try to stay below the hole.",
            size="4",
            padding_left="20px",
        ),
        rx.image(src="/imgHoles/map16.jpg"),
    )

def hole17():
    return(

        rx.text(
            "17 - Cliffs Edge",
            size="5",
            padding_top="45px",
            padding_left="20px",
            padding_bottom="10px",
        ),
        rx.text(
            "Another risk/reward hole, but only for the long hitters. Beware OB right edge and behind green. "
            "Try to position your drive to 100-125 yards in.",
            size="4",
            padding_left="20px",
        ),
        rx.image(src="/imgHoles/map17.jpg"),
    )

def hole18():
    return(

        rx.text(
            "18 - Green Monster",
            size="5",
            padding_top="45px",
            padding_left="20px",
            padding_bottom="10px",
        ),
        rx.text(
            "600 yard par 5 requires 3 good shots. Aim drive right side of fairway bunker. "
            "To stay out of water, aim second shot at far right bunker.",
            size="4",
            padding_left="20px",
        ),
        rx.image(src="/imgHoles/map18.jpg"),
    )

@rx.page("/profile", title="Course Profile")
def profile():
    return (
        navigation.navbar_dropdown(),
        rx.container(
            courseProfile(),
            hole1(),
            hole2(),
            hole3(),
            hole4(),
            hole5(),
            hole6(),
            hole7(),
            hole8(),
            hole9(),
            hole10(),
            hole11(),
            hole12(),
            hole13(),
            hole14(),
            hole15(),
            hole16(),
            hole17(),
            hole18(),

            margin="0px",

        ),

    )


