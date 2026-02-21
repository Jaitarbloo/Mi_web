import reflex as rx

def Presentacion_componentes():
    
    return rx.center(

                rx.vstack(
                
                        rx.heading("Componentes adaptables para tu negocio",
                    
                                size="8"),

                        rx.hstack(
                                
                                rx.text("A continuación, vas a poder observar una serie de componentes que son totalmente "
                                        " independientes y adaptables para poder diseñar una web a tu media.  "
                                        " De esa forma, conseguiremos trasmitir a tus clientes el potencial de tu negocio.",
                                        size="3",
                                        text_align="center",),

                               width= "75%",
                               justify="center"),

                    align="center",
                    spacing="4",
                    #width="80%",
                    padding="5em"),

                       
                align="center") 
        
      
