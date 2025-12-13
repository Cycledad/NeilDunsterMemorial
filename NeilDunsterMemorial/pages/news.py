import reflex as rx
from ..Nav import navigation



def brianWebsterRetirement():
    return(

                rx.text(
                    "Congratulations to Brian Webster on his retirement as of Oct 2025.",
                    size="6",
                    padding="10px",
                    background_color="var(--tomato-3)",


                ),

            #rx.separator(margin_top="25px"),
            #width="500px",
            #height="100px",
            #background_color="var(--tomato-3)",
            #border_radius="5px",
            #align="center",
            #justify="center",


    ),

def wayneGrandChildren():
    return(

                rx.text(
                    "Wayne and Chantal Davis welcome their third and fourth grandchildren, Arisa born in July 2025 and Onyx born in August 2025",
                    size="6",
                    padding="10px",
                    # background_color="var(--tomato-3)",
                ),


    )

def brianMaleGrandchild():
    return(

            rx.text(
                "Brian and Shelley Male welcome their first granchild in ?",
                size="6",
                padding="10px",
                background_color="var(--tomato-3)",
            ),


        #rx.separator(margin_top="10px", margin_bottom="25px"),
    )

def donationJune2025():
    return(
        rx.text(
            "A total of $750.00 for a donation contribution this year(2025) to the Royal Ottawa Hospital",
            size="6",
            padding="10px",
        )
    ),



@rx.page("/news", title="News")
def news():
 return (
     navigation.navbar_dropdown(),

     rx.container(
         rx.vstack(
            brianWebsterRetirement(),
             wayneGrandChildren(),
             brianMaleGrandchild(),
             donationJune2025(),
         )
     ),

 )