import reflex as rx

class State(rx.State):

    favicon_rotando: bool = False

    def girar_favicon(self):
        self.favicon_rotando = True

    def detener_favicon(self):
        self.favicon_rotando = False

def Foto_rotando():

    return rx.vstack(

                        rx.text("Componente con foto rotando al pasar el cursor por encima",
                                align="center",
                                width="100%",
                                size="8",
                                #padding="3em",
                                color="white"
                                ),
                        
                        rx.image( src="/hqdefault.jpg",
                                  width=["90vw", "400px"],  # Más grande y cuadrada
                                  height=["90vw", "400px"],
                                  max_width="400px",
                                  max_height="400px",
                                
                                  style={ "transition": "transform 0.5s",
                                          "transform": rx.cond(State.favicon_rotando, "rotate(360deg)", "rotate(0deg)"),
                                          "border_radius": "50%",
                                          "object_fit": "cover",
                                          "overflow": "hidden",
                                          "boxShadow": "0 4px 32px rgba(0,0,0,0.5)"
                                        },
                                
                                  on_mouse_enter=State.girar_favicon,
                                  on_mouse_leave=State.detener_favicon,
                                  margin_bottom="1.5em",
                                  margin_top="4em"
                                ),
                
                align="center",      
                justify="center",    
                height="100vh",
                width="100%", 
                background_color="blue",
                
                )

app = rx.App()
app.add_page(Foto_rotando, title="Foto Rotando")