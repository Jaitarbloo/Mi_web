import reflex as rx
from Estilos import hero_bg_style, hero_text_style



def Fondo_cambiante ():
    
    return rx.box(

                        rx.box( rx.text("Componente de fondo cambiante", style=hero_text_style ),
                                style=hero_bg_style ,
                                margin_top="25em", 
                                width="80%",
                                  ),
                
                background_color="#d38832",
                width="100%"
                    )
    
    
    
                
app = rx.App ()  
app.add_page(Fondo_cambiante, title="Fondo cambiante")