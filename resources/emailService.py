from datetime import date
from flask import Flask, app, render_template
from google.google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__,template_folder='../templates')
CLIENTE= "google.json"
API_NAME="gmail"
API_VERSION="v1"
SCOPES=["https://mail.google.com/"]

service = Create_Service(CLIENTE,API_NAME, API_VERSION, SCOPES)


def enviarEmailPedidoRecibido(mailCliente,nombreUsuario, listaProductos, subTotal, descuento, total):
   fechaHoy=date.today()
   fechaModificada=fechaHoy.strftime('%d/%m/%Y')
   with app.app_context():
      html=render_template("mailPedido.html", nombreUsuario=nombreUsuario, listaProductos=listaProductos, subTotal=subTotal, descuento=descuento, total=total, fecha=fechaModificada)
   mimeMessage = MIMEMultipart()
   mimeMessage["subject"]="Detalle de pedido Alba Deco"
   mimeMessage["to"]=mailCliente
   mimeMessage.attach(MIMEText(html, "html"))
   raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
   message=service.users().messages().send(userId="me", body={"raw":raw_string}).execute()
   print(message)

def enviarEmailPedidoSeñado(mailCliente,nombreUsuario,numeroPedido):
   with app.app_context():
      html=render_template("mailPedidoSeñado.html", nombreUsuario=nombreUsuario,numeroPedido=numeroPedido )
   mimeMessage = MIMEMultipart()
   mimeMessage["subject"]="Seña del pedido Alba Deco"
   mimeMessage["to"]=mailCliente
   mimeMessage.attach(MIMEText(html, "html"))
   raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
   message=service.users().messages().send(userId="me", body={"raw":raw_string}).execute()
   print(message)

def enviarEmailPedidoEnviado(mailCliente,nombreUsuario,numeroPedido, transporte, nroRemito):
   with app.app_context():
      html=render_template("mailPedidoEnviado.html", nombreUsuario=nombreUsuario,numeroPedido=numeroPedido, transporte=transporte, nroRemito=nroRemito )
   mimeMessage = MIMEMultipart()
   mimeMessage["subject"]="Pedido Alba Deco Enviado"
   mimeMessage["to"]=mailCliente
   mimeMessage.attach(MIMEText(html, "html"))
   raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
   message=service.users().messages().send(userId="me", body={"raw":raw_string}).execute()
   print(message)
