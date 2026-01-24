import reflex as rx

class State(rx.State):
    pass

def Web_en_construccion():
    
                return rx.center(
                                
                                rx.heading( "WEB en construcción....disculpen las molestias",
                                            align="center",
                                            width="100%",
                                            size="9",
                                            #margin_top="3em",
                                            color="red"
                                            ),
                        
                            #spacing="4",
                            justify="center",
                            align="center",
                            width="100%",
                            height="30vh",
                            margin_top="2em",
                            background_color="blue",

                                  )

app = rx.App()
app.add_page( Web_en_construccion, title="web_en_costrucción" )