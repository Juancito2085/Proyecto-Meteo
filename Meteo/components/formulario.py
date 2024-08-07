import reflex as rx

class FormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit"""
        self.form_data = form_data

def formulario() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.hstack(
                rx.text("Lluvia: ", width="100px"),
                rx.select(
                    ["No hubo", "Débil", "Moderada", "Fuerte", "Torrencial"],
                    default_value="No hubo",
                    name="Lluvia",
                )
            ),
            rx.hstack(
                rx.text("Viento: ", width="100px"),
                rx.select(
                    ["No hubo", "Débil", "Moderado", "Fuerte", "Muy fuerte"],
                    default_value="No hubo",
                    name="Viento",
                )
            ),
            rx.hstack(
                rx.text("Granizo: ", width="100px"),
                rx.select(
                    ["No hubo", "Chico", "Mediano", "Grande", "Muy grande"],
                    default_value="No hubo",
                    name="Granizo",
                )
            ),
            rx.button("Submit", type="submit"),
            on_submit=FormState.handle_submit,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(FormState.form_data.to_string()),
    )