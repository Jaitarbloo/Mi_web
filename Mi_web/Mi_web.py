import reflex as rx
from rxconfig import config


from Componente_Ampliacion_fotos import Ampliacion_fotos
from Componente_Carrusel_fotos import Carrusel
from Componente_Favicon_rotando import Favicon_rotando
from Componente_Navbar import navbar
from Componente_Cambio_imagen import Cambio_imagen
from Componente_Zabalgana_Web import Zabalgana_web_Vercel
from Componente_Cambio_fondo import Cambio_fondo
from Componente_Reborde_llamativo import Reborde_llamativo
from Componente_Doble_fondo import Doble_fondo
from Componente_Contacto import Contacto
from Componente_Web_construccion import Web_en_construccion

class State(rx.State):
    pass

def index():
    return rx.vstack(
                    
                    navbar(),

                    #Web_en_construccion(),
                  
                    Zabalgana_web_Vercel(),

                    Ampliacion_fotos(),
        
                    Cambio_fondo(), 

                    Doble_fondo(),
        
                    Carrusel(),
        
                    Favicon_rotando(),
        
                    Cambio_imagen(),
        
                    Reborde_llamativo(),

                    Contacto(),
        
                            
                width="100%",
                min_height="100vh", 
                #background_color="blue"
                background_color="#1a1a2e",
                padding="0px",
                
                
                )



app = rx.App  ( stylesheets=["/animation.css"])

app.add_page(index, title="Jaitarbloo Full-stack developer")

