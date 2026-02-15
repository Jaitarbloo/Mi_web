import reflex as rx

def One_Page():
    return rx.center(
        rx.vstack(
            rx.heading(
                "Especialista en webs One Page",
                size="7",
                text_align="center",
                color="white",
            ),

            rx.text(
                "Mi especialidad es el diseño y desarrollo de webs One Page: "
                "sitios de una sola página donde toda la información importante "
                "está organizada de forma clara, visual y directa.",
                text_align="center",
                font_size="1.1em",
                color="gray.300",
                max_width="800px",
            ),

            rx.text(
                "Este enfoque permite reducir los tiempos de diseño y desarrollo "
                "a aproximadamente un mes, sin renunciar a una imagen profesional "
                "ni a una buena experiencia de usuario.",
                text_align="center",
                font_size="1.1em",
                color="gray.300",
                max_width="800px",
            ),

            rx.text(
                "Una web One Page guía al visitante de forma natural, de arriba abajo, "
                "llevando el mensaje justo a la persona adecuada en el momento adecuado. "
                "Es la forma más directa y eficaz de llegar a clientes potenciales.",
                text_align="center",
                font_size="1.1em",
                color="gray.300",
                max_width="800px",
            ),

            rx.vstack(
                rx.text("• Comunicación clara y directa"),
                rx.text("• Navegación sencilla (todo en un solo lugar)"),
                rx.text("• Experiencia optimizada para móviles"),
                rx.text("• Desarrollo más rápido y controlado"),
                rx.text("• Ideal para captar clientes y presentar servicios"),
                spacing="2",
                color="gray.200",
                font_size="1em",
                align="start",
            ),

            spacing="5",
            padding="4em",
            align="center",
        ),
        width="100%",
        bg="#1a1a2e",
    )
