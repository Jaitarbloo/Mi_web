import reflex as rx
from rxconfig import config


class State(rx.State):

    image_src: str = "/629083.jpg"
    
    def cambiar_imagen(self):
        self.image_src = "/3971879.webp"

    def restaurar_imagen(self):
        self.image_src = "/629083.jpg" 

    ...
def Cambio_imagen_con_cursor():
    
    return rx.vstack(
                    
                    rx.text("Componente cambio de imagen con cursor",
                            align="center",
                            width="100%",
                            size="8"
                            ), 
                    
                    rx.image(
                        src=State.image_src,
                        width="100%" ,#"["95vw", "550px"],  # Más grande y responsivo
                        max_width="550px",
                        height="auto",
                        margin_bottom="1.5em",
                        style={"boxShadow": "0 4px 32px rgba(0,0,0,0.5)"},
                        on_mouse_enter=State.cambiar_imagen,
                        on_mouse_leave=State.restaurar_imagen,
                        margin_top="7em",
                        border_radius="10px",
                            ),
                
                justify="center",
                align="center",
                width="100%",
                min_height="100vh"

                )

app = rx.App()
app.add_page(Cambio_imagen_con_cursor, title="Cambio de Imagen")
