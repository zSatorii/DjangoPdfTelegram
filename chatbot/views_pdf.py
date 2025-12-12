# chatbot/views_pdf.py
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from chatbot.email_utils import enviar_certificado_por_email
from .pdf_generator import generar_certificado_estudiante


def descargar_certificado(request, curso_id):
    # Datos de prueba; luego los sacas de la BD / usuario
    cedula = "1234567890"
    nombre = request.user.get_full_name() or request.user.username
    curso = f"Curso {curso_id}"

    pdf_buffer = generar_certificado_estudiante(
        estudiante_id=request.user.id,
        cedula=cedula,
        nombre=nombre,
        curso=curso,
    )

    response = HttpResponse(pdf_buffer, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="certificado_{cedula}.pdf"'
    return response


def enviar_certificado_view(request, curso_id):
    correo = request.user.email
    cedula = "1234567890"  # luego lo sacas de la BD
    nombre = request.user.get_full_name() or request.user.username
    curso = f"Curso {curso_id}"

    enviar_certificado_por_email(
        correo_destino=correo,
        estudiante_id=request.user.id,
        cedula=cedula,
        nombre=nombre,
        curso=curso,
    )

    return HttpResponseRedirect(reverse("detalle_curso", args=[curso_id]))
