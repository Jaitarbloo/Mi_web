import reflex as rx

def Reborde_llamativo():
    return rx.center(
                    
                    rx.vstack(
                                rx.text( "Detalles luminosos que refuerzan el diseño sin saturar",
                                        align="center",
                                        width="100%",
                                        size="8",
                                        color="white"
                                        ),
            
                                rx.image( src="/wallpapersden.com_galaxy-stars-over-mountain_1280x720.jpg",
                                        alt="Mi foto bonita",
                                        width=["300px", "350px", "400px"],
                                        height=["200px", "250px", "300px"],
                                        border_radius="50%",
                                        box_shadow="0 0 30px 0 #6cf",
                                        transition="all 0.3s ease",
                                        _hover={"transform": "scale(1.5)",
                                                "box_shadow": "0 0 400px 0 #6cf",
                                                "cursor": "pointer"
                                                },
                                        object_fit="cover",
                                        margin="auto",
                                        margin_top="4em"
                                        ),

                        align="center",
                        spacing="4",
                        width="100%",
                        padding=["1em", "2em", "3em"]
                            ),
        
                min_height="100vh",
                background_color="blue",
                width="100%"
                        )

app = rx.App()
app.add_page(Reborde_llamativo, title="Reborde Llamativo")