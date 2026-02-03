import reflex as rx


def El_Local() -> rx.Component:
    return rx.box(
        rx.vstack(
            # TÍTULO
            rx.heading(
                "Nuestro espacio",
                size="7",
                color="#4a3a32",
            ),

            rx.text(
                "Un lugar pensado para disfrutar con calma, "
                "cuidando cada detalle.",
                size="4",
                color="gray.700",
                max_width="600px",
                text_align="center",
            ),

            # GALERÍA
            rx.hstack(
                # FOTO GRANDE
                rx.box(
                    background_image="url('/Comedor_nuevo.jpg')",
                    background_size="cover",
                    background_position="center",
                    width="60%",
                    height="420px",
                    border_radius="xl",
                ),

                # FOTOS PEQUEÑAS
                rx.vstack(
                    rx.box(
                        background_image="url('/Terraza_Barron.jpg')",
                        background_size="cover",
                        background_position="center",
                        width="100%",
                        height="200px",
                        border_radius="xl",
                    ),
                    rx.box(
                        background_image="url('/Entrada_principal_Barron.jpg')",
                        background_size="cover",
                        background_position="center",
                        width="100%",
                        height="200px",
                        border_radius="xl",
                    ),
                    rx.box(
                        background_image="url('/Pared_fondo_Barron.jpg')",
                        background_size="cover",
                        background_position="center",
                        width="100%",
                        height="200px",
                        border_radius="xl",
                    ),
                    spacing="3",
                    width="40%",
                ),

                spacing="4",
                width="100%",
            ),

            spacing="4",
            align_items="center",
            max_width="1200px",
            margin="0 auto",
            padding="6rem 2rem",
        ),

        width="100%",
        background_color="#d38832",
    )


app = rx.App()
app.add_page(El_Local)
