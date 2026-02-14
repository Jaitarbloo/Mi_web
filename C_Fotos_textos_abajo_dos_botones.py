import reflex as rx


def Fotos_textos_abajo_dos_botones() -> rx.Component:
    return rx.box(
        rx.vstack(
            # TÍTULO DE SECCIÓN
            rx.heading(
                "Componente para mostrar tus productos",
                size="8",
                text_align="center",
            ),

            rx.text(
                "Producto, técnica y respeto por el origen.",
                size="5",
                text_align="center",
                color="gray.600",
            ),

            # BLOQUES DE PRODUCTO / SERVICIO
            rx.hstack(
                # BLOQUE 1
                rx.vstack(
                    rx.image(
                        src="Ensalada_Barron.jpg",
                        width="100%",
                        height="260px",
                        object_fit="cover",
                        border_radius="10px",
                    ),
                    rx.heading("Producto local", size="5"),
                    rx.text(
                        "Trabajamos con productores cercanos y de temporada, "
                        "respetando el ritmo natural de cada ingrediente.",
                        size="4",
                        color="gray.600",
                    ),
                    spacing="3",
                    align_items="start",
                    max_width="260px",
                ),

                # BLOQUE 2
                rx.vstack(
                    rx.image(
                        src="Hamburguesa_Barron.jpg",
                        width="100%",
                        height="260px",
                        object_fit="cover",
                        border_radius="10px",
                    ),
                    rx.heading("Cocina honesta", size="5"),
                    rx.text(
                        "Una cocina reconocible, cuidada y sin artificios, "
                        "donde el sabor es el verdadero protagonista.",
                        size="4",
                        color="gray.600",
                    ),
                    spacing="3",
                    align_items="start",
                    max_width="260px",
                ),

                # BLOQUE 3
                rx.vstack(
                    rx.image(
                        src="Desayuno_Barron.png",
                        width="100%",
                        height="260px",
                        object_fit="cover",
                        border_radius="10px",
                    ),
                    rx.heading("Experiencia", size="5"),
                    rx.text(
                        "Un espacio pensado para disfrutar con calma, "
                        "en un ambiente cercano y acogedor.",
                        size="4",
                        color="gray.600",
                    ),
                    spacing="3",
                    align_items="start",
                    max_width="260px",
                ),

                # BLOQUE 4
                rx.vstack(
                    rx.image(
                        src="Terraza_Barron.jpg",
                        width="100%",
                        height="260px",
                        object_fit="cover",
                        border_radius="10px",
                    ),
                    rx.heading("Ambiente", size="5"),
                    rx.text(
                        "Un lugar donde compartir, relajarse y sentirse "
                        "como en casa, dentro y fuera.",
                        size="4",
                        color="gray.600",
                    ),
                    spacing="3",
                    align_items="start",
                    max_width="260px",
                ),

                spacing="5",
                justify="center",
                width="100%",
                wrap="wrap",
            ),

            # CTA DOBLE
            rx.flex(
                rx.button(
                    "Nuestra carta",
                    bg_color="#4a3a32",
                    color="#f5f3ef",
                    padding_x="3rem",
                    border_radius="md",
                    _hover={"bg_color": "#3b2f2a"},
                ),
                rx.button(
                    "Reservar mesa",
                    bg_color="#4a3a32",
                    color="#f5f3ef",
                    padding_x="3rem",
                    border_radius="md",
                    _hover={"bg_color": "#3b2f2a"},
                ),
                spacing="3",
                margin_top="3.5rem",
            ),

            spacing="6",
            max_width="1200px",
            margin="0 auto",
            padding="6rem 2rem",
            align_items="center",
        ),
        width="100%",
        background_color="#d38832",
    )


app = rx.App()
app.add_page(Fotos_textos_abajo_dos_botones, title="Fotos, textos abajo y dos botones")
