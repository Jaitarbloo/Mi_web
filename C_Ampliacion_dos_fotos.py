import reflex as rx

class State(rx.State):
    
    expanded_coche: bool = False
    expanded_bici: bool = False

    
    def toggle_size_coche(self):
        self.expanded_coche = not self.expanded_coche

    
    def toggle_size_bici(self):
        self.expanded_bici = not self.expanded_bici


def Ampliacion_dos_fotos():
    
    return rx.vstack( 
                    
                    rx.text("Componente de ampliación de fotos al pasar el ratón por encima",
                            align="center",
                            width="100%",
                            size="8",
                            #padding="3em",
                            color="white"
                            ),

                    rx.flex(
                            
                            rx.box(
                                    rx.image(
                                            src="/Cueva.jpg",
                                            border_radius="7px",
                                            width=rx.cond(State.expanded_coche, "600px", "300px"),
                                            height=rx.cond(State.expanded_coche, "400px", "300px"),
                                            transition="all 0.5s ease-in-out",
                                            ),
                                on_mouse_enter=State.toggle_size_coche,
                                on_mouse_leave=State.toggle_size_coche,
                                align="center",
                                justify="center",
                                ),
                            
                            rx.box(
                                    rx.image(
                                            src="/Electrica.jpg",
                                            border_radius="7px",
                                            width=rx.cond(State.expanded_bici, "600px", "300px"),
                                            height=rx.cond(State.expanded_bici, "400px", "300px"),
                                            transition="all 0.5s ease-in-out",
                                            ),
                                on_mouse_enter=State.toggle_size_bici,
                                on_mouse_leave=State.toggle_size_bici,
                                align="center",
                                justify="center",
                                ), 
                        
                        margin_top="7em"
                        ), 
                
                justify="center",
                align="center",
                width="100%",
                min_height="100vh",
                    )

app = rx.App()
app.add_page(Ampliacion_dos_fotos, title="Ampliacion_fotos")
