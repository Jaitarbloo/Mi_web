import reflex as rx

def Doble_fondo():
            
                return rx.vstack(

                                rx.text("Componente de doble fondo",
                                        align="center",
                                        width="100%",
                                        size="8",
                                        padding="1.5em",
                                        color="white"
                                        ),

                                
                                rx.image(
                                            src="/1871835.jpg",
                                             width="300px",
                                             height="300px",
                                        background="linear-gradient(#e66465, #9198e5)",
                                        box_shadow="10px 5px 5px red",
                                        border_radius="20px",
                                        padding="1em",
                                        color="white",
                                        font_size="0.2em",
                                        text_align="center",
                                        margin_top="10em",
                                        
                                        ),
                        align="center",      
                        justify="center",              
                        min_height="100vh",
                        background_color="blue",
                        width="100%",
                        padding="2em"
                            )
                            
                            

app = rx.App()
app.add_page(Doble_fondo, title="Doble Fondo")