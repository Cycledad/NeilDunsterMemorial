import reflex as rx
from NeilDunsterMemorial.Nav import navigation


class PlayerState(rx.state):

    listPlayers = [
        {"firstName": "Jeff", "lastName": "Mulcock", "img": "/imgPlayers/jeffMulcock.png", "city": "Ottawa, ON"},
        {"firstName": "Steve", "lastName": "Gallant", "img": "/imgPlayers/steveGallant.jpg", "city": "Ottawa, ON"},
        {"firstName": "Neil", "lastName": "Dunster", "img": "/imgPlayers/neilDunster.png", "city": "Ottawa, ON"},
        {"firstName": "Steve", "lastName": "Arbuckle", "img": "/imgPlayers/steveArbuckle.jpg", "city": "WestPort, ON"},
        {"firstName": "Brian", "lastName": "Gow", "img": "/imgPlayers/brianGow.jpg", "city": "Ottawa, ON"},
        {"firstName": "Steve", "lastName": "Fournier", "img": "/imgPlayers/steveFournier.jpg", "city": "Ottawa, ON"},
        {"firstName": "Brian", "lastName": "Male", "img": "/imgPlayers/brianMale.jpg", "city": "Orleans, ON"},
        {"firstName": "Wayne", "lastName": "Davis", "img": "/imgPlayers/wayneDavis.jpg", "city": "Orleans, ON"},
        {"firstName": "Dan", "lastName": "Kalil", "img": "/imgPlayers/danKalil.jpg", "city": "Ottawa, ON"},
        {"firstName": "Don", "lastName": "Rowan", "img": "/imgPlayers/donRowan.jpg", "city": "Ottawa, ON"},
        {"firstName": "Tony", "lastName": "Leal", "img": "/imgPlayers/tonyLeal.jpg", "city": "Alliston, ON"},
        {"firstName": "John", "lastName": "Chatterton", "img": "/imgPlayers/johnChatterton.jpg", "city": "Ottawa, ON"},
        {"firstName": "Doug", "lastName": "Corrigan", "img": "/imgPlayers/dougCorrigan.jpg", "city": "NC, USA"},
        {"firstName": "Mark", "lastName": "Campbell", "img": "/imgPlayers/markCampbell.jpg", "city": "Halifax, NS"},
        {"firstName": "Steve", "lastName": "Turner", "img": "/imgPlayers/steveTurner.jpg", "city": "Ottawa, ON"},
        {"firstName": "John", "lastName": "Stevens", "img": "/imgPlayers/johnStevens.jpg", "city": "Ottawa, ON"},
        {"firstName": "Brian", "lastName": "Webster", "img": "/imgPlayers/brianWebster.jpg", "city": "Ottawa, ON"},
        {"firstName": "Alan", "lastName": "Scott", "img": "/imgPlayers/alanScott.jpg", "city": "Ottawa, ON"},
        {"firstName": "Mike", "lastName": "Kehoe", "img": "/imgPlayers/mikeKehoe.jpg", "city": "Ottawa, ON"},
        {"firstName": "Ron", "lastName": "Prosper", "img": "/imgPlayers/ronProsper.jpg", "city": "Ottawa, ON"},
        {"firstName": "George", "lastName": "Vadeboncoeur", "img": "/imgPlayers/georgeVadeboncoeur.jpg", "city": "Wasaga Beach, ON"},
        {"firstName": "Tony", "lastName": "Bond", "img": "/imgPlayers/tonyBond.jpg", "city": "Ottawa, ON"},
        ]

    sortedList = list(sorted(listPlayers, key=lambda player: player["lastName"]))



def doit(initial: str):

    return (

        rx.text(
            events.sharedState.prevLastNameInitial,
            size="9"
        ),

        rx.divider(
            size="4",
            margin_bottom="10px",

        )
    )
def showLastNameInitial(initial: str):

    rx.cond(
        events.sharedState.prevLastNameInitial != initial,
        doit(initial),
        rx.text("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
    ),




def showImage(player: dict):

    #events.sharedState.updatePreviousLastNameInitial(player["lastName"][0])

    return(


         #couldnt get this to work as i wanted


                #showLastNameInitial(player["lastName"][0]),

                #doit(player["lastName"][0]),

                rx.vstack(

                    rx.image(
                         src=player["img"],
                         width="100px",
                         height="100px",
                         border_radius="60px",
                         flex="1 1 auto"

                    ),

                    rx.text(
                         f"{player["firstName"]} {player["lastName"]}",

                         size="4",
                         style={"line_height": "1"}  # Adjust the value as needed
                         # align="center"
                    ),
                    rx.text(
                        f"{player['city']}",
                        size="1",
                        style={"line_height": "1"}  # Adjust the value as needed
                    ),
                    spacing="1" # Set spacing of the parent Vstack to 0
                ),
    )


def showPlayer():

 return (
     rx.desktop_only(
         #rx.center(

         rx.grid(


             rx.foreach(
                 sortedList,
                 lambda player: showImage(player)
             ),
             columns="6",
             #flex_wrap="wrap",
             #justify="center",
             gap="30px",
             #width="100%"


         ),

     ),
     rx.mobile_and_tablet(
         rx.vstack(
             rx.foreach(
                 sortedList,
                 lambda player: showImage(player)
             ),
         )
     )

 )

@rx.page("/players", title="Players")
def players():
 return(
     navigation.navbar_dropdown(),
     showPlayer(),
 )