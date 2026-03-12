import smtplib
from email.message import EmailMessage
import urllib.request

def descargar_gdoc_txt(url, nombre_archivo="documento.txt"):
    """
    Descarga un Google Doc en formato .txt y lo guarda localmente.
    """
    if "docs.google.com/document/d/" in url:
        doc_id = url.split("/d/")[1].split("/")[0]
        url = f"https://docs.google.com/document/d/{doc_id}/export?format=txt"
    
    with urllib.request.urlopen(url) as respuesta:
        contenido = respuesta.read().decode("utf-8")
    
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(contenido)
    
    return nombre_archivo

def enviar_email(destinatario, asunto, cuerpo, archivo_adjunto, remitente, password, smtp_server="smtp.gmail.com", smtp_port=587):
    """
    Envía un email con asunto, cuerpo y archivo adjunto.
    """
    mensaje = EmailMessage()
    mensaje["From"] = remitente
    mensaje["To"] = destinatario
    mensaje["Subject"] = asunto
    mensaje.set_content(cuerpo)

    # Adjuntar el archivo
    with open(archivo_adjunto, "rb") as f:
        datos = f.read()
        mensaje.add_attachment(datos, maintype="text", subtype="plain", filename=archivo_adjunto)

    # Conectar al servidor SMTP y enviar
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Iniciar TLS
        server.login(remitente, password)
        server.send_message(mensaje)
    
    print("Correo enviado correctamente a", destinatario)


# ----------------------------
# Uso del programa
# ----------------------------
url_gdoc = input("Introduce la URL del Google Doc: ")
archivo = descargar_gdoc_txt(url_gdoc)  # Descarga y guarda como .txt

destinatario = input("Introduce el correo del destinatario: ")
asunto = input("Introduce el asunto del email: ")
cuerpo = input("Introduce el cuerpo del email: ")

remitente = input("Introduce tu correo: ")
password = input("Introduce tu contraseña (o app password): ")

enviar_email(destinatario, asunto, cuerpo, archivo, remitente, password)
