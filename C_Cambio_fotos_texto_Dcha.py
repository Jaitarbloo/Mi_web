import reflex as rx

def Cambio_fotos_texto_Dcha() -> rx.Component:
    return rx.box(
        rx.flex(
            # CONTENEDOR DE IMÁGENES (CAMBIO AUTOMÁTICO)
            rx.box(
                rx.image(
                    src="Naturaleza.jpg",
                    position="absolute",
                    top="0",
                    left="0",
                    width="100%",
                    height="100%",
                    object_fit="cover",
                    animation="fade1 15s infinite",
                ),
                rx.image(
                    src="Cascada.jpg",
                    position="absolute",
                    top="0",
                    left="0",
                    width="100%",
                    height="100%",
                    object_fit="cover",
                    animation="fade2 15s infinite",
                ),
                rx.image(
                    src="unnamed.jpg",
                    position="absolute",
                    top="0",
                    left="0",
                    width="100%",
                    height="100%",
                    object_fit="cover",
                    animation="fade3 15s infinite",
                ),
                # Responsive: 100% ancho en móvil, 50% en escritorio
                width=["100%", "100%", "50%"],
                height=["300px", "400px", "500px"],
                position="relative",
                overflow="hidden",
                border_radius="10px",
                sx={
                    "@keyframes fade1": {
                        "0%": {"opacity": "1"},
                        "30%": {"opacity": "1"},
                        "33%": {"opacity": "0"},
                        "100%": {"opacity": "0"},
                    },
                    "@keyframes fade2": {
                        "0%": {"opacity": "0"},
                        "33%": {"opacity": "0"},
                        "36%": {"opacity": "1"},
                        "63%": {"opacity": "1"},
                        "66%": {"opacity": "0"},
                        "100%": {"opacity": "0"},
                    },
                    "@keyframes fade3": {
                        "0%": {"opacity": "0"},
                        "66%": {"opacity": "0"},
                        "69%": {"opacity": "1"},
                        "100%": {"opacity": "1"},
                    },
                },
            ),

            # TEXTO
            rx.vstack(
                rx.image(
                    src="Icono_reciclaje.webp",
                    width="100px",
                    height="100px",
                    margin_bottom="1rem",
                ),
                rx.heading(
                    "Ejemplo componente de compromiso con el planeta",
                    size="8",
                    text_align="center", # Centrado para móvil
                ),
                rx.text(
                    "Trabajamos con producto local y de temporada, reducimos residuos, "
                    "reciclamos y tomamos decisiones responsables para minimizar "
                    "nuestro impacto ambiental.",
                    size="4",
                    color="gray.600",
                    text_align="center",
                ),
                rx.text(
                    "Porque creemos que cuidar del planeta también forma parte "
                    "de lo que servimos en la mesa.",
                    size="4",
                    font_style="italic",
                    text_align="center",
                ),
                spacing="4",
                align_items="center",
                width=["100%", "100%", "50%"],
                max_width="500px",
            ),

            # RESPONSIVE CORE:
            # column = móvil (imagen arriba), row = escritorio (lado a lado)
            flex_direction=["column", "column", "row"],
            spacing="8",
            align_items="center",
            justify="center",
            max_width="1200px",
            margin="0 auto",
            padding=["2rem 1rem", "4rem 2rem", "6rem 2rem"],
        ),
        width="100%",
        background_color="#d38832",
    )

app = rx.App()
app.add_page(Cambio_fotos_texto_Dcha)
