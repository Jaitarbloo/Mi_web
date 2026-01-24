import reflex as rx
from Estilos import hero_bg_style, hero_text_style



def Cambio_fondo():
    
    return rx.box(
        
                    rx.text("El fondo también comunica Hagámoslo dinámico", style= hero_text_style ),
                        
            style=hero_bg_style ,
            margin_top="20em", 
                    )
    
    
    
                
app = rx.App ()  
app.add_page(Cambio_fondo, title="Cambio de Fondo")