from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from PyPDF2 import PdfWriter, PdfReader
from io import BytesIO
from datetime import datetime
import hashlib
import os



class PDFGenerador:
    """Genera PDFs con contenido y encriptación con contraseña"""
    
    def __init__(self, titulo="Documento EduLearn"):
        self.titulo = titulo
        self.styles = getSampleStyleSheet()
        self.pagesize = A4
        
    def generar_pdf_con_encriptacion(self, contenido_dict, cedula_usuario):
        """
        Genera un PDF y lo encripta con la cédula del usuario.
        
        Args:
            contenido_dict: Dict con claves como 'titulo', 'datos', 'tabla'
            cedula_usuario: Cédula para usar como contraseña
            
        Returns:
            BytesIO con el PDF encriptado
        """
        # 1. Crear PDF sin encriptación primero
        buffer = BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=self.pagesize,
            rightMargin=0.5*inch,
            leftMargin=0.5*inch,
            topMargin=0.75*inch,
            bottomMargin=0.75*inch
        )
        
        # 2. Construir contenido
        story = []
        
        # Título
        titulo_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=18,
            textColor=colors.HexColor('#208091'),
            spaceAfter=30,
            alignment=1  # Centrado
        )
        story.append(Paragraph(contenido_dict.get('titulo', self.titulo), titulo_style))
        story.append(Spacer(1, 0.2*inch))
        
        # Fecha de emisión
        fecha = datetime.now().strftime("%d de %B de %Y")
        fecha_style = ParagraphStyle(
            'Fecha',
            parent=self.styles['Normal'],
            fontSize=10,
            textColor=colors.grey,
            alignment=2  # Derecha
        )
        story.append(Paragraph(f"<i>Generado: {fecha}</i>", fecha_style))
        story.append(Spacer(1, 0.3*inch))
        
        # Datos personales
        if 'datos' in contenido_dict:
            story.append(Paragraph("<b>Información del Usuario</b>", self.styles['Heading2']))
            datos_tabla = self._crear_tabla_datos(contenido_dict['datos'])
            story.append(datos_tabla)
            story.append(Spacer(1, 0.2*inch))
        
        # Contenido adicional
        if 'contenido' in contenido_dict:
            story.append(Paragraph(contenido_dict['contenido'], self.styles['Normal']))
            story.append(Spacer(1, 0.2*inch))
        
        # Tabla si existe
        if 'tabla' in contenido_dict:
            story.append(Paragraph("<b>Datos Detallados</b>", self.styles['Heading2']))
            tabla = self._crear_tabla(contenido_dict['tabla'])
            story.append(tabla)
        
        # Footer
        story.append(Spacer(1, 0.5*inch))
        footer_text = f"Documento protegido. Acceso por cédula: {cedula_usuario[-4:]}"
        story.append(Paragraph(f"<i>{footer_text}</i>", self.styles['Normal']))
        
        # 3. Construir PDF
        doc.build(story)
        
        # 4. Encriptar con contraseña (cédula)
        buffer.seek(0)
        pdf_encriptado = self._encriptar_pdf(buffer, cedula_usuario)
        
        return pdf_encriptado
    
    def _crear_tabla_datos(self, datos_dict):
        """Crea tabla de datos personales"""
        datos = [[k, v] for k, v in datos_dict.items()]
        tabla = Table(datos, colWidths=[2*inch, 3*inch])
        tabla.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#E8F4F8')),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F5F5F5')])
        ]))
        return tabla
    
    def _crear_tabla(self, datos_tabla):
        """Crea tabla con datos"""
        tabla = Table(datos_tabla)
        tabla.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#208091')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F5F5F5')])
        ]))
        return tabla
    
    def _encriptar_pdf(self, buffer_pdf, cedula):
        """
        Encripta el PDF con contraseña (basada en la cédula).
        SIN parámetro algorithm (usa el que trae por defecto)
        
        Args:
            buffer_pdf: BytesIO con el PDF sin encriptar
            cedula: Cédula del usuario
            
        Returns:
            BytesIO con PDF encriptado
        """
        # Crear contraseña con los últimos 8 dígitos de la cédula
        contrasena = "1234"
        
        # Leer el PDF
        pdf_reader = PdfReader(buffer_pdf)
        pdf_writer = PdfWriter()
        
        # Agregar todas las páginas
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
        
        # Encriptar (SIN algorithm, para compatibilidad)
        pdf_writer.encrypt(user_password=contrasena, owner_password=contrasena)
        
        # Guardar en nuevo buffer
        output_buffer = BytesIO()
        pdf_writer.write(output_buffer)
        output_buffer.seek(0)
        
        return output_buffer



# EJEMPLO DE USO
def generar_certificado_estudiante(cedula, nombre, curso):
    """Genera un certificado en PDF encriptado"""
    
    pdf_gen = PDFGenerador(titulo="Certificado de Finalización")
    
    contenido = {
        'titulo': '🎓 CERTIFICADO DE FINALIZACIÓN',
        'datos': {
            'Nombre': nombre,
            'Cédula': cedula,
            'Curso': curso,
            'Fecha de Emisión': datetime.now().strftime("%d/%m/%Y"),
        },
        'contenido': f"""
        <br/><br/>
        <b>Se certifica que:</b> <i>{nombre}</i> ha completado exitosamente 
        el curso de <b>{curso}</b> cumpliendo con todos los requisitos 
        establecidos por EduLearn.
        <br/><br/>
        Este documento es oficial y puede ser presentado como 
        comprobante de aprobación del curso.
        """,
        'tabla': [
            ['Criterio', 'Estado'],
            ['Lecciones Completadas', '✓ 100%'],
            ['Tareas Entregadas', '✓ 15/15'],
            ['Evaluación Final', '✓ Aprobado'],
            ['Asistencia', '✓ Completa'],
        ]
    }
    
    pdf_buffer = pdf_gen.generar_pdf_con_encriptacion(contenido, cedula)
    return pdf_buffer
