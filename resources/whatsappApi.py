


from flask import redirect


def enviarWhatsapp(telefono, mensaje):


    ruta="https://graph.facebook.com/v13.0/116541164391542/messages"
    mensaje={
    "messaging_product": "whatsapp", 
    "to": "543541694534",
    "type": "template",
    "template": 
        { "name": "hello_world",
        "language": 
            { 
                "code": "en_US" 
            } 
        } 
    }
    return mensaje