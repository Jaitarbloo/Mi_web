import reflex as rx

def navbar_desplegable() -> rx.Component:
    # Definimos los enlaces una sola vez para reutilizarlos
    nav_links = [
        ("Contáctame", "https://zabalgana.com"),
        ("jaitarbloo@yahoo.es", "https://zabalgana.com"),
        ("Frameworks modernos", "https://zabalgana.com"),
        ("Desarrollo y diseño", "https://zabalgana.com"),
    ]

    return rx.hstack(
        # Logo Izquierdo
        rx.image(src="/Logotipo Jb.jpg", height=["40px", "60px", "80px"]),

        # --- MENU ESCRITORIO (Se oculta en móvil 'none', se ve en laptop 'flex') ---
        rx.hstack(
            *[rx.link(rx.text(text, size="4"), href=url, color_scheme="gray") for text, url in nav_links],
            display=["none", "none", "flex"], # Breakpoints: [mobile, tablet, desktop]
            spacing="7",
        ),

        rx.spacer(),

        # --- MENU MÓVIL (Se ve en móvil 'flex', se oculta en escritorio 'none') ---
        rx.menu.root(
            rx.menu.trigger(
                rx.button(rx.icon("menu"), variant="soft", color_scheme="gray")
            ),
            rx.menu.content(
                *[rx.menu.item(text, on_click=rx.redirect(url)) for text, url in nav_links],
            ),
            display=["flex", "flex", "none"], # Solo visible en pantallas pequeñas
        ),

        # Logo Derecho (Opcional, podrías ocultarlo en móvil también)
        rx.image(src="/Logotipo Jb.jpg", height=["40px", "60px", "80px"], display=["none", "flex", "flex"]),

        width="100%",
        padding="1em",
        background="linear-gradient(45deg, #000033, #0000FF)",
        align="center",
        position="fixed",
        top="0",
        z_index="999",
    )

app = rx.App()
app.add_page(navbar_desplegable)
