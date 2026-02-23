import reflex as rx
from rxconfig import config

from C_Ampliacion_dos_fotos import Ampliacion_dos_fotos
from C_Cabezera_fotos_textos_abajo import cabezera_fotos_textos_abajo
from C_Cambio_fotos_automatico import Cambio_fotos_automatico
from C_Cambio_fotos_texto_Dcha import Cambio_fotos_texto_Dcha
from C_Cambio_imagen_con_cursor import Cambio_imagen_con_cursor
from C_Carrusel_fotos_grandes import Carrusel_fotos_grandes
from C_Carrusel_fotos_pequenas import Carrusel_fotos_pequenas
from C_Contacto import Contacto
from C_Cuatro_fotos import Cuatro_fotos
from C_Desliza_fondo_fijo import Desliza_fondo_fijo
from C_Doble_fondo import Doble_fondo


#from C_en_proceso import


from C_Fondo_cambiante import Fondo_cambiante
from C_Foto_con_reborde import Foto_con_reborde
from C_Foto_rotando import Foto_rotando
from C_Fotos_textos_abajo_dos_botones import Fotos_textos_abajo_dos_botones
from C_Navbar_trasparente import Navbar_trasparente
from C_Navbar import navbar
from C_One_Page import One_Page
from C_Presentacion_componentes import Presentacion_componentes
from C_Ubicacion import UbicacionFooter
from C_Web_construccion import Web_en_construccion



class State(rx.State):
    pass

def index():
    
    return rx.vstack(
                    
                    #navbar(),

                    Navbar_trasparente(),

                    #Web_en_construccion(),
                  
                    rx.box(cabezera_fotos_textos_abajo(),
                            id="inicio",
                         ),

                    rx.box(One_Page(),
                            id="one_page",
                            scroll_margin_top="120px"
                          ),

                    rx.box(Presentacion_componentes(),
                            id="componentes",
                            scroll_margin_top="120px"
                          ),

                    Desliza_fondo_fijo(),

                    Ampliacion_dos_fotos(),

                    Fondo_cambiante(),

                    Doble_fondo(),

                    Carrusel_fotos_grandes(),

                    Cambio_fotos_texto_Dcha(),

                    Cambio_fotos_automatico(),

                    Fotos_textos_abajo_dos_botones(),
        
                    Foto_rotando(),

                    Cuatro_fotos(),
        
                    Cambio_imagen_con_cursor(),

                    Carrusel_fotos_pequenas(),

                    Foto_con_reborde(),

                    UbicacionFooter(),
                    
                    rx.box(Contacto(),
                            id="contacto",
                            scroll_margin_top="120px"
                          ),

                   
        
                            
                width="100%",
                min_height="100vh", 
                background_color="#1a1a2e",
                spacing="0",
                align="center"
                
                
                
                )



app = rx.App (html_lang="es", stylesheets=["Estilos.css"])

app.add_page(index, title="Jaitarbloo Full-stack developer")

