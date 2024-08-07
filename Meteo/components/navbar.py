import reflex as rx

def navbar () -> rx.Component:
    return rx.hstack(
        rx.text("Home", height="40px", color="white"),
        rx.text("Reportes", height="40px",color="white"),
        position="sticky",
        bg="gray",
        padding="10px",
    )