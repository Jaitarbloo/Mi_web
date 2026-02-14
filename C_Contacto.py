import reflex as rx
import smtplib
from email.mime.text import MIMEText

class State(rx.State):
    
    def enviar_email(self, form_data: dict):
        
        try:
            smtp_server = "smtp.gmail.com"
            port = 587
            sender_email = "tu_email@gmail.com"
            password = "tu_contraseña_de_app"
            
            msg = MIMEText( f"Nombre: {form_data['nombre']}\nEmail: {form_data['email']}\nMensaje: {form_data['mensaje']}")
            msg['Subject'] = 'Nuevo mensaje de contacto'
            msg['From'] = sender_email
            msg['To'] = sender_email
            
            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls()
                server.login(sender_email, password)
                server.send_message(msg)
            return rx.window_alert("Mensaje enviado con éxito!")
        
        except Exception as e:
            return rx.window_alert(f"Error al enviar el mensaje: {str(e)}")


def Contacto():
    
    return rx.center(
        
                    rx.vstack(
                            
                                rx.divider(),
        
                                rx.heading("Contáctame", size="6"),
        
                                rx.form(
                
                                        rx.vstack(
                                                rx.input(placeholder="Tu nombre", name="nombre", required=True),
                                                rx.input(placeholder="Tu email", name="email", required=True, type="email"),
                                                rx.text_area(placeholder="¿En qué te puedo ayudar?", name="mensaje", required=True, rows="4"),
                                                rx.button("Enviar", type="submit", color_scheme="indigo"),
                                                 ),
                        
                                    width="100%",
                                    max_width="400px",
                                    align="center",
                                    on_submit=State.enviar_email,
                                    reset_on_submit=True,
                                     ),
        
                        spacing="4",
                        padding="6em",
                        align="center",
                         
                            ),
                
                spacing="4",
                justify="center",
                align="center",
                width="100%",
                height="60vh",
                #margin_top="21em",
                bg="#1a1a2e"
                    )
    
                

app = rx.App()
app.add_page(Contacto, title="Contacto")