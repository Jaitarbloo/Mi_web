import reflex as rx

# --- ESTADO PARA EL FORMULARIO ---
class State(rx.State):
    def enviar_email(self, form_data: dict):
        nombre = form_data.get("nombre")
        email = form_data.get("email")
        mensaje = form_data.get("comentario")
        # Aquí iría tu lógica smtplib para jaitarbloo@yahoo.es
        return rx.window_alert(f"Mensaje de {nombre} enviado correctamente.")

# --- NAVBAR CON SCROLL CORREGIDO ---
def navbar() -> rx.Component:
    menu_items = [
        ("Inicio", "#inicio"),
        ("Tecnologías", "#tecnologias"),
        ("Contacto", "#contacto"),
    ]

    return rx.box(
        rx.hstack(
            # Logo o Título
            rx.text("Mi Web", color="white", weight="bold", size="5"),
            rx.spacer(),
            
            # ESCRITORIO: Links directos
            rx.hstack(
                *[rx.link(text, href=url, color="white", size="3", _hover={"opacity": 0.7}) 
                  for text, url in menu_items],
                spacing="6",
                display=["none", "none", "flex"],
            ),

            # MÓVIL: Menú Desplegable (Cambiado rx.redirect por rx.link para que funcione el scroll)
            rx.box(
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", color="white", size=30, cursor="pointer")
                    ),
                    rx.menu.content(
                        *[
                            rx.link(
                                rx.menu.item(text, color="white"),
                                href=url,
                                text_decoration="none",
                            ) for text, url in menu_items
                        ],
                        background_color="rgba(0, 0, 51, 0.95)",
                    ),
                ),
                display=["block", "block", "none"],
            ),
            align="center",
            width="100%",
            max_width="1100px",
            margin="0 auto",
        ),
        position="fixed",
        top="0",
        z_index="999",
        width="100%",
        padding="1.5em",
        background="rgba(0,0,0,0.3)", # Fondo sutil para legibilidad
        backdrop_filter="blur(10px)",
    )

# --- COMPONENTE DE CONTACTO MINIMALISTA ---
def contacto_section() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Contacto", size="4", weight="bold"),
            rx.form(
                rx.vstack(
                    rx.input(placeholder="Nombre", name="nombre", required=True, variant="soft"),
                    rx.input(placeholder="Tu Email", name="email", type="email", required=True, variant="soft"),
                    rx.text_area(placeholder="Mensaje", name="comentario", required=True, height="80px", variant="soft"),
                    rx.center(
                        rx.button("Enviar", type="submit", width="120px", color_scheme="indigo"),
                        width="100%",
                    ),
                    spacing="3",
                ),
                on_submit=State.enviar_email,
                reset_on_submit=True,
            ),
            width=["90%", "320px"],
            align="center",
        ),
        id="contacto",
        padding_y="100px", # Espacio para que el scroll no quede pegado
        scroll_margin_top="80px",
    )

# --- PÁGINA PRINCIPAL ---
def navbar_prueba() -> rx.Component:
    return rx.box(
        navbar(),
        # SECCIÓN INICIO
        rx.center(
            rx.heading("Bienvenido a mi One Page", size="9", color="white"),
            id="inicio",
            height="100vh",
            background="linear-gradient(45deg, #1a1a2e, #16213e)",
        ),
        # SECCIÓN TECNOLOGÍAS (Relleno)
        rx.center(
            rx.heading("Mis Tecnologías", size="8"),
            id="tecnologias",
            height="80vh",
            background="white",
        ),
        # SECCIÓN CONTACTO
        contacto_section(),
    )

# --- CONFIGURACIÓN DE LA APP ---
app = rx.App(
    style={
        "html": {"scroll_behavior": "smooth"}, # Scroll suave activado
        "body": {"margin": "0", "padding": "0"}
    }
)
app.add_page(navbar_prueba)
