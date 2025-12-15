import reflex as rx
from NeilDunsterMemorial.Nav import navigation


class State(rx.State):

    listPlayers = [
        {"firstName": "Jeff", "lastName": "Mulcock", "img": "/imgPlayers/jeffMulcock.png", "city": "Ottawa, ON", "controlbreak": True},
        {"firstName": "Steve", "lastName": "Gallant", "img": "/imgPlayers/steveGallant.jpg", "city": "Ottawa, ON", "controlbreak": True},
        {"firstName": "Neil", "lastName": "Dunster", "img": "/imgPlayers/neilDunster.png", "city": "Ottawa, ON", "controlbreak": True},
        {"firstName": "Steve", "lastName": "Arbuckle", "img": "/imgPlayers/steveArbuckle.jpg", "city": "WestPort, ON", "controlbreak": True},
        {"firstName": "Brian", "lastName": "Gow", "img": "/imgPlayers/brianGow.jpg", "city": "Ottawa, ON", "controlbreak": True},
        {"firstName": "Steve", "lastName": "Fournier", "img": "/imgPlayers/steveFournier.jpg", "city": "Ottawa, ON", "controlbreak": True},
        {"firstName": "Brian", "lastName": "Male", "img": "/imgPlayers/brianMale.jpg", "city": "Orleans, ON", "controlbreak": True},
        {"firstName": "Wayne", "lastName": "Davis", "img": "/imgPlayers/wayneDavis.jpg", "city": "Orleans, ON", "controlbreak": True},
        {"firstName": "Dan", "lastName": "Kalil", "img": "/imgPlayers/danKalil.jpg", "city": "Ottawa, ON", "controlbreak": True},
        {"firstName": "Don", "lastName": "Rowan", "img": "/imgPlayers/donRowan.jpg", "city": "Ottawa, ON", "controlbreak": True},
        {"firstName": "Tony", "lastName": "Leal", "img": "/imgPlayers/tonyLeal.jpg", "city": "Alliston, ON", "controlbreak": True},
        {"firstName": "John", "lastName": "Chatterton", "img": "/imgPlayers/johnChatterton.jpg", "city": "Ottawa, ON", "controlbreak": True},
        {"firstName": "Doug", "lastName": "Corrigan", "img": "/imgPlayers/dougCorrigan.jpg", "city": "NC, USA", "controlbreak": True},
        {"firstName": "Mark", "lastName": "Campbell", "img": "/imgPlayers/markCampbell.jpg", "city": "Halifax, NS", "controlbreak": True},
        {"firstName": "Steve", "lastName": "Turner", "img": "/imgPlayers/steveTurner.jpg", "city": "Ottawa, ON", "controlbreak": True},
        {"firstName": "John", "lastName": "Stevens", "img": "/imgPlayers/johnStevens.jpg", "city": "Ottawa, ON", "controlbreak": True},
        {"firstName": "Brian", "lastName": "Webster", "img": "/imgPlayers/brianWebster.jpg", "city": "Ottawa, ON", "controlbreak": True},
        {"firstName": "Alan", "lastName": "Scott", "img": "/imgPlayers/alanScott.jpg", "city": "Ottawa, ON", "controlbreak": True},
        {"firstName": "Mike", "lastName": "Kehoe", "img": "/imgPlayers/mikeKehoe.jpg", "city": "Ottawa, ON", "controlbreak": True},
        {"firstName": "Ron", "lastName": "Prosper", "img": "/imgPlayers/ronProsper.jpg", "city": "Ottawa, ON", "controlbreak": True},
        {"firstName": "George", "lastName": "Vadeboncoeur", "img": "/imgPlayers/georgeVadeboncoeur.jpg", "city": "Wasaga Beach, ON", "controlbreak": True},
        {"firstName": "Tony", "lastName": "Bond", "img": "/imgPlayers/tonyBond.jpg", "city": "Ottawa, ON", "controlbreak": True},
        ]

    XsortedList = list(sorted(listPlayers, key=lambda Xplayer: Xplayer["lastName"]))
    lastNames = [d['lastName'] for d in XsortedList] #hack used to printinitial

    @rx.event
    def setControlBreak(self):
        for i in range(len(self.XsortedList)):
            if i == 0:
                self.XsortedList[i]["controlbreak"] = True
            else:
                if self.XsortedList[i]["lastName"][0] == self.XsortedList[i-1]["lastName"][0]:
                    self.XsortedList[i]["controlbreak"] = False
                else:
                    self.XsortedList[i]["controlbreak"] = True






def showInitial(initial: str):
    return (
        rx.text(
            f"{initial}",
            size="7",
        ),
        rx.separator(
            margin_bottom="15px"
        ),
    ),

def funcDoNothing():
    return()

def showImage(player: dict, i: int):

    return(

                rx.vstack(
                    rx.cond(
                        player["controlbreak"],
                        showInitial(State.lastNames[i][0]), #this is a hack as I couldn't use syntax dictionary player["lastname"][0], it just wouldn't work
                        funcDoNothing()
                    ),

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
                        style={"line_height": "1"},  # Adjust the value as needed
                        margin_bottom="15px"
                    ),
                    spacing="1", # Set spacing of the parent Vstack to 0
                    margin_left="50px"
                ),
    )


def showPlayer():

 return (
     #rx.desktop_only(
     #    #rx.center(

     #    rx.grid(

     #        rx.foreach(
     #            State.XsortedList,
     #            lambda player, index: showImage(player, index)
     #        ),
     #        columns="6",
     #        #flex_wrap="wrap",
     #        #justify="center",
     #        gap="30px",
     #        #width="100%"


      #   ),

     #),
     #rx.mobile_and_tablet(
         rx.vstack(
             rx.foreach(
                 State.XsortedList,
                 lambda player, index: showImage(player, index)
             ),
         )
     #)

 )

@rx.page("/players", title="Players", on_load=State.setControlBreak)
def players():
 return(
     navigation.navbar_dropdown(),
     showPlayer(),
 )