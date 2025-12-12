from django.core.mail import EmailMessage
from django.conf import settings
from .pdf_generator import generar_certificado_estudiante


def enviar_certificado_por_email(correo_destino, cedula, nombre, curso):
    # Genera el PDF solo con datos primitivos, sin tocar la BD
    pdf_buffer = generar_certificado_estudiante(
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
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[correo_destino],
    )

    email.attach(
        filename=f"certificado_{cedula}.pdf",
        content=pdf_bytes,
        mimetype="application/pdf",
    )

    try:
        resultado = email.send()
        print("CERTIFICADO ENVIADO A:", correo_destino, "RESULTADO:", resultado)
    except Exception as e:
        print("ERROR ENVIANDO CERTIFICADO:", repr(e))
