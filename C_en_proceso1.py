import reflex as rx

def Navbar_trasparente1() -> rx.Component:
    # Definimos los enlaces para evitar repetir código
    menu_items = [
        ("Nuestra cocina", "https://reflex.dev"),
        ("Queda aquí", "https://reflex.dev"),
        ("Horarios y Eventos", "https://reflex.dev"),
        ("Reserva tu mesa", "https://reflex.dev"),
    ]

    return rx.vstack(
        rx.center(
            # --- VERSIÓN ESCRITORIO ---
            rx.vstack(
                rx.hstack(
                    *[
                        rx.link(
                            rx.text(text, size="4", color="White", _hover={"opacity": 0.7}),
                            href=url
                        ) for text, url in menu_items
                    ],
                    spacing="9",
                    align="center",
                    display=["none", "none", "none", "flex"], # Solo visible en pantallas grandes
                ),
                rx.box(
                    height="1px",
                    width="100%",
                    bg="White",
                    margin_top="0.5em",
                    display=["none", "none", "none", "block"], # La línea también se oculta
                ),
                width="fit_content",
                align="center",
            ),

            # --- VERSIÓN MÓVIL (Menú Desplegable) ---
            rx.box(
                rx.menu.root(
                    rx.menu.trigger(
                        rx.button(
                            rx.icon("menu", color="white", size=30),
                            variant="ghost", # Mantiene la transparencia
                            cursor="pointer",
                        )
                    ),
                    rx.menu.content(
                        *[
                            rx.menu.item(
                                text, 
                                on_click=rx.redirect(url),
                                color_scheme="gray"
                            ) for text, url in menu_items
                        ],
                        background_color="rgba(0, 0, 51, 0.9)", # Fondo oscuro semi-transparente para leer el menú
                    ),
                ),
                display=["block", "block", "block", "none"], # Visible en móvil y tablet
                padding="1em",
            ),
            width="100%",
        ),
        background="transparent",
        position="fixed",
        top="0",
        z_index="999",
        width="100%",
        padding_top="1em",
    )

app = rx.App()
app.add_page(Navbar_trasparente1)
