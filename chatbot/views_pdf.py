from django.http import HttpResponse
from .pdf_generator import generar_certificado_estudiante

def descargar_certificado(request, curso_id):
    # Datos de prueba (luego los cambias por los reales de tu BD)
    cedula = "1234567890"       # <- aquí pones una cédula cualquiera para probar
    nombre = "Usuario Prueba"
    curso = f"Curso {curso_id}"

    pdf_buffer = generar_certificado_estudiante(
        estudiante_id=1,
        cedula=cedula,
        nombre=nombre,
        curso=curso
    )

    response = HttpResponse(pdf_buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="certificado_{cedula}.pdf"'
    return response
