import reflex as rx
from ..Nav import navigation

@rx.page("/gallery", title="Gallery")
def gallery():
 return (
     navigation.navbar_dropdown(),

 )