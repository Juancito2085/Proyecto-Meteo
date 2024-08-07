import reflex as rx
from Meteo.components.navbar import navbar
from Meteo.components.formulario import formulario

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        formulario()
    )


app=rx.App()
app.add_page(index)
app._compile()