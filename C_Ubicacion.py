import reflex as rx


def UbicacionFooter() -> rx.Component:
    return rx.box(
        rx.vstack(
            # BLOQUE SUPERIOR
            rx.hstack(
                rx.vstack(
                    rx.heading(
                        "Dónde estamos",
                        size="8",
                        color="#f5f3ef",
                    ),

                    rx.text(
                        "Restaurante Barrón",
                        size="5",
                        font_weight="bold",
                        color="#f5f3ef",
                    ),

                    rx.text(
                        "Calle Mayor 25, 28013 Madrid",
                        size="4",
                        color="#d8d2c8",
                    ),

                    rx.text(
                        "Tel. 912 345 678",
                        size="4",
                        color="#d8d2c8",
                    ),

                    rx.text(
                        "Horario: Martes a Domingo · 13:00 – 23:00",
                        size="4",
                        color="#d8d2c8",
                    ),

                    rx.link(
                        rx.button(
                            "Cómo llegar",
                            bg_color="#e6dccf",
                            color="#4a3a32",
                            padding_x="2rem",
                            border_radius="md",
                            _hover={"bg_color": "#d2b48c"},
                        ),
                        href="https://www.google.com/maps?q=40.416775,-3.703790",
                        is_external=True,
                    ),

                    spacing="3",
                    align_items="start",
                ),

                rx.box(
                    rx.html(
                        """
                        <iframe
                            src="https://www.google.com/maps?q=40.416775,-3.703790&z=16&output=embed"
                            width="100%"
                            height="100%"
                            style="border:0;"
                            loading="lazy"
                            referrerpolicy="no-referrer-when-downgrade">
                        </iframe>
                        """
                    ),
                    width="100%",
                    height="350px",
                    border_radius="lg",
                    overflow="hidden",
                ),

                spacing="8",
                align_items="center",
                width="100%",
            ),

            rx.divider(
                border_color="rgba(245,243,239,0.2)",
                margin_y="3rem",
            ),

            rx.hstack(
                rx.text(
                    "© 2025 Restaurante Barrón",
                    size="3",
                    color="#d8d2c8",
                ),

                rx.hstack(
                    rx.link("Aviso legal", href="#", color="#d8d2c8"),
                    rx.link("Privacidad", href="#", color="#d8d2c8"),
                    rx.link("Cookies", href="#", color="#d8d2c8"),
                    spacing="4",
                ),

                justify="between",
                width="100%",
            ),

            spacing="6",
            max_width="1200px",
            margin="0 auto",
            padding="5rem 2rem 3rem 2rem",
        ),
        width="100%",
        background_color="#4a3a32",
    )


app = rx.App()
app.add_page(UbicacionFooter)
