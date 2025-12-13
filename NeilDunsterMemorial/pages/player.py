import reflex as rx
from NeilDunsterMemorial.Nav import navigation




listPlayers = [
    {"firstName": "Jeff", "lastName": "Mulcock", "img": "/imgPlayers/jeffMulcock.png"},
    {"firstName": "Steve", "lastName": "Gallant", "img": "/imgPlayers/steveGallant.jpg"},
    {"firstName": "Neil", "lastName": "Dunster", "img": "/imgPlayers/neilDunster.png"},
    {"firstName": "Steve", "lastName": "Arbuckle", "img": "/imgPlayers/steveArbuckle.jpg"},
    {"firstName": "Brian", "lastName": "Gow", "img": "/imgPlayers/brianGow.jpg"},
    {"firstName": "Steve", "lastName": "Fournier", "img": "/imgPlayers/steveFournier.jpg"},
    {"firstName": "Brian", "lastName": "Male", "img": "/imgPlayers/brianMale.jpg"},
    {"firstName": "Wayne", "lastName": "Davis", "img": "/imgPlayers/wayneDavis.jpg"},
    {"firstName": "Dan", "lastName": "Kalil", "img": "/imgPlayers/danKalil.jpg"},
    {"firstName": "Don", "lastName": "Rowan", "img": "/imgPlayers/donRowan.jpg"},
    {"firstName": "Tony", "lastName": "Leal", "img": "/imgPlayers/tonyLeal.jpg"},
    {"firstName": "John", "lastName": "Chatterton", "img": "/imgPlayers/johnChatterton.jpg"},
    {"firstName": "Doug", "lastName": "Corrigan", "img": "/imgPlayers/dougCorrigan.jpg"},
    {"firstName": "Mark", "lastName": "Campbell", "img": "/imgPlayers/markCampbell.jpg"},
    {"firstName": "Steve", "lastName": "Turner", "img": "/imgPlayers/steveTurner.jpg"},
    {"firstName": "John", "lastName": "Stevens", "img": "/imgPlayers/johnStevens.jpg"},
    {"firstName": "Brian", "lastName": "Webster", "img": "/imgPlayers/brianWebster.jpg"},
    {"firstName": "Alan", "lastName": "Scott", "img": "/imgPlayers/alanScott.jpg"},
    {"firstName": "Mike", "lastName": "Kehoe", "img": "/imgPlayers/mikeKehoe.jpg"},
    {"firstName": "Ron", "lastName": "Prosper", "img": "/imgPlayers/ronProsper.jpg"},
    {"firstName": "George", "lastName": "Vadeboncoeur", "img": "/imgPlayers/georgeVadeboncoeur.jpg"},
    {"firstName": "Tony", "lastName": "Bond", "img": "/imgPlayers/tonyBond.jpg"},
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
                         # align="center"
                    ),
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