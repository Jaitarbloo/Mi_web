import reflex as rx


def Carrusel_peque() -> rx.Component:
    slides = [
        ("bmw-publicidad.webp", "Cocina responsable", "Producto local y de temporada"),
        ("Entrada_principal_Barron.jpg", "Compromiso sostenible", "Reducimos residuos"),
        ("giphy.gif", "Personas primero", "Respeto y condiciones justas"),
        ("Pared_fondo_Barron.jpg", "Menos desperdicio", "Aprovechamos todo"),
        ("unnamed.jpg", "Cuidar el planeta", "También se sirve en la mesa"),
    ]

    return rx.box(

        rx.hstack(
            *[
                rx.box(
                    rx.image(
                        src=image,
                        width=["140px", "180px", "240px"],
                        height=["100px", "130px", "170px"],
                        object_fit="cover",
                        border_radius="14px",
                        transition="transform 0.4s ease",
                        _hover={"transform": "scale(1.08)"},
                    ),

                    rx.vstack(
                        rx.heading(title, size="3", color="white"),
                        rx.text(subtitle, size="2", color="white"),
                        spacing='2',
                        position="absolute",
                        bottom="0.75rem",
                        left="0.75rem",
                        right="0.75rem",
                    ),

                    position="relative",
                    flex="0 0 auto",
                )
                for image, title, subtitle in slides * 2   # ← CLAVE
            ],

            gap=["1.5rem", "2rem", "2.5rem"],
            animation="carousel-move 30s linear infinite",
            _hover={"animationPlayState": "paused"},
        ),

        width="100%",
        overflow="hidden",
        padding_y=["2rem", "3rem", "4rem"],
        background_color="#5b3a29",

        # CSS embebido
        sx={
            "@keyframes carousel-move": {
                "from": {"transform": "translateX(0%)"},
                "to": {"transform": "translateX(-50%)"},
            }
        },
    )


app = rx.App()
app.add_page(Carrusel_peque)

