import reflex as rx

def Contactar() -> rx.Component:
    return rx.box(
        rx.vstack(
            # TÍTULO
            rx.heading(
                "Contacto",
                size="7",
                color="#f5f3ef",
            ),

            # TEXTO DESCRIPTIVO
            rx.text(
                "¿Quieres qué te ayude a impulsar tu negocio?",
                color="#d8d2c8",
                text_align="center",
                max_width="500px",
            ),

            # EMAIL DESTACADO
            rx.link(
                rx.text(
                    "jaitardev@gmail.com",
                    font_size="1.2rem",
                    font_weight="bold",
                    color="#e6dccf",
                ),
                href="jaitardev@gmail.com",
                _hover={"color": "#ffffff"},
            ),

            # BOTÓN OPCIONAL
            rx.link(
                rx.button(
                    "Enviar email",
                    bg_color="#e6dccf",
                    color="#4a3a32",
                    border_radius="full",
                    padding_x="2rem",
                    _hover={"bg_color": "#d2b48c"},
                ),
                href="jaitardev@gmail.com",
            ),

            # DIVISOR
            rx.divider(
                border_color="rgba(245,243,239,0.2)",
                margin_y="2rem",
                width="100%",
            ),

            # FOOTER INFERIOR
            rx.text(
                "© 2026 · Tu negocio",
                size="2",
                color="#d8d2c8",
            ),

            spacing="4",
            align="center",
            padding="4rem 2rem",
            max_width="800px",
            margin="0 auto",
        ),
        width="100%",
        #background_color="#d38832",
    )


app = rx.App()
app.add_page(Contactar)