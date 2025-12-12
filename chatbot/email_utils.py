# chatbot/email_utils.py
from django.core.mail import EmailMessage
from .pdf_generator import generar_certificado_estudiante

def enviar_certificado_por_email(correo_destino, estudiante_id, cedula, nombre, curso):
    pdf_buffer = generar_certificado_estudiante(
        estudiante_id=estudiante_id,
        cedula=cedula,
        nombre=nombre,
        curso=curso,
    )

    pdf_buffer.seek(0)
    pdf_bytes = pdf_buffer.read()

    asunto = f"Certificado del curso {curso}"
    cuerpo = (
        f"Hola {nombre},\n\n"
        f"Adjuntamos tu certificado en PDF para el curso: {curso}.\n\n"
        "Saludos."
    )

    email = EmailMessage(
        subject=asunto,
        body=cuerpo,
        from_email=None,
        to=[correo_destino],
    )

    email.attach(
        filename=f"certificado_{cedula}.pdf",
        content=pdf_bytes,
        mimetype="application/pdf",
    )

    email.send()
