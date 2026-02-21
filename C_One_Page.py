import reflex as rx

def One_Page():
    
    return rx.center(
        
                    rx.vstack(
                            
                                rx.heading("Especialista en webs One Page", size="8"),
            
                                
                                rx.center("Me especializo en crear webs One Page que van directo al grano: diseño un sitio profesional," 
                                        " claro y visual donde tus clientes encuentran todo lo que necesitan en un solo lugar. " 
                                        "En solo un mes, tendrás una página optimizada que guía a tus visitas de forma natural para " 
                                        "convertirlas en clientes potenciales, sin complicaciones ni esperas eternas.",
                                        width="75%",
                                        ),

                                rx.vstack(
                                            rx.text("• Comunicación clara y directa"),
                                            rx.text("• Navegación sencilla (todo en un solo lugar)"),
                                            rx.text("• Experiencia optimizada para móviles"),
                                            rx.text("• Desarrollo más rápido y controlado"),
                                            rx.text("• Ideal para captar clientes y presentar servicios"),
                                            
                             
                                    align="start"),
            
                        
                            align="center"),
    
                align="center",
                width="100%",
                padding="3em",)

