# chatbot/views_pdf.py
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from chatbot.email_utils import enviar_certificado_por_email
from .pdf_generator import generar_certificado_estudiante


def descargar_certificado(request, curso_id):
    cedula = "1234567890"
    nombre = request.user.get_full_name() or request.user.username
    curso = f"Curso {curso_id}"

    pdf_buffer = generar_certificado_estudiante(
        cedula=cedula,
        nombre=nombre,
        curso=curso,
    )

    response = HttpResponse(pdf_buffer, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="certificado_{cedula}.pdf"'
    return response


def enviar_certificado_view(request, curso_id):
    # 1. Leer el correo que viene del formulario
    if request.method == "POST":
        correo = request.POST.get("email_destino")
    else:
        correo = request.user.email  # opcional, por si alguien entra por GET

    cedula = "1234567890"  # luego lo puedes sacar de la BD
    nombre = request.user.get_full_name() or request.user.username
    curso = f"Curso {curso_id}"

    enviar_certificado_por_email(
        correo_destino=correo,
        cedula=cedula,
        nombre=nombre,
        curso=curso,
    )

    return HttpResponseRedirect(reverse("detalle_curso", args=[curso_id]))
