import reflex as rx


def Carrusel_fotos_grandes() -> rx.Component:
    
                return rx.box(
                                
                                rx.hstack(
            
                                        slide(  "bmw-publicidad.webp",
                                                "Cocina responsable",
                                                "Producto local y de temporada"),
            
                                        slide(  "Entrada_principal_Barron.jpg",
                                                "Compromiso sostenible",
                                                "Reducimos residuos y emisiones"),
            
                                        slide(  "giphy.gif",
                                                "Personas primero",
                                                "Respeto y condiciones justas"),
            
                                        slide(  "Pared_fondo_Barron.jpg",
                                                "Menos desperdicio",
                                                "Aprovechamos cada ingrediente"),
            
                                        slide(  "unnamed.jpg",
                                                "Cuidar el planeta",
                                                "También se sirve en la mesa"),
            
                                    
                                    width="100%",
                                    height="100%",
                                    animation="carousel 25s infinite"
        
                                            ),
        
                        overflow="hidden",
                        width="100%",
                        height="100vh",
                        position="relative",

                        # Keyframes CSS
                
                        sx={ "@keyframes carousel": 
                            
                                {   "0%": {"transform": "translateX(0vw)"}, 
                                    "16%": {"transform": "translateX(0vw)"}, 
                                    "20%": {"transform": "translateX(-99.5vw)"}, 
                                    "36%": {"transform": "translateX(-99.5vw)"},
                                    "40%": {"transform": "translateX(-199.5vw)"},
                                    "56%": {"transform": "translateX(-199.5vw)"},
                                    "60%": {"transform": "translateX(-298.5vw)"},
                                    "76%": {"transform": "translateX(-298.5vw)"},
                                    "80%": {"transform": "translateX(-399vw)"},
                                    "100%": {"transform": "translateX(-399vw)"},
                                }
                            }
    
                            )

def slide(image_url: str, title: str, subtitle: str) -> rx.Component:
    
                return rx.box(
                            
                                rx.image(   src=image_url,
                                            width="100%",
                                            height="100%",
                                            object_fit="cover",
                                            object_position="center",
                                        ),

                                rx.hstack(
                                        
                                            rx.vstack(
                                                        rx.heading(title, size="8", color="white"),
                                                        rx.text(subtitle, size="6", color="white"),

                                                    ),
                                
                                        
                                    align_items="center",
                                    justify="between",
                                    width="100%",
                                    height="100%",
                                    position="absolute",
                                    top="0",
                                    padding_left="6rem",
                                    
            
                            
                                        ),
                        # Overlay con contenido
        
                        width="100%",
                        height="100vh",
                        position="relative",
                        flex="0 0 100%",
                       
                            )

 

app = rx.App()
app.add_page(Carrusel_fotos_grandes)
