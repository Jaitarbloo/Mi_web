import reflex as rx
from rxconfig import config


from Componente_Ampliacion_fotos import Ampliacion_fotos
from Componente_Carrusel_fotos import Carrusel
from Componente_Favicon_rotando import Favicon_rotando
from Componente_Navbar import navbar
from Componente_Cambio_imagen import Cambio_imagen
from Componente_Zabalgana_Web import Zabalgana_web_Vercel
from Componente_Doble_fondo import Doble_fondo
from Componente_Contacto import Contacto
from Componente_Web_construccion import Web_en_construccion
from C_Desliza_fondo_fijo import Cabezera
from C_Cambio_fotos_texto_Dcha import Compromiso_naturaleza_icono
from C_Carrusel_foto_pequena import Carrusel_peque
from C_Ubicacion import UbicacionFooter
from C_Cuatro_fotos import El_Local
from C_Fondo_cambiante import Cambio_fondo1
from C_Foto_con_reborde import Reborde_llamativo1
from C_Ampliacion_dos_fotos import Ampliacion_fotos1


class State(rx.State):
    pass

def index():
    return rx.vstack(
                    
                    navbar(),

                    #Web_en_construccion(),
                  
                    Zabalgana_web_Vercel(),

                    Cabezera(),

                    Ampliacion_fotos(),

                    #Ampliacion_fotos1(),

                    Cambio_fondo1(), 

                    Doble_fondo(),

                    Compromiso_naturaleza_icono(),
        
                    Carrusel(),
        
                    Favicon_rotando(),

                    El_Local(),
        
                    Cambio_imagen(),

                    Carrusel_peque(),

                    Reborde_llamativo1(),

                    UbicacionFooter(),

                    Contacto(),
        
                            
                width="100%",
                min_height="100vh", 
                #background_color="blue"
                background_color="#1a1a2e",
                padding="0px",
                spacing="0"
                
                
                )



app = rx.App  ( stylesheets=["/animation.css"])

app.add_page(index, title="Jaitarbloo Full-stack developer")

