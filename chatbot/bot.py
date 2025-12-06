from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.constants import ParseMode

# Tu token aquí
TOKEN = "7881485552:AAFG28vOWACkGHHJUSJhYpKjbb2sc0uiQhU"  # Cambia por tu token real

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start"""
    message = """
🎓 ¡Bienvenido a EduLearn! 
    
Este bot te ayudará a:
✅ Ver tus cursos
✅ Consultar tus tareas
✅ Verificar tu progreso
✅ Recibir notificaciones

Usa /help para más comandos.
    """
    await update.message.reply_text(message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /help"""
    help_text = """
📚 Comandos disponibles:

/start - Inicia el bot
/help - Muestra esta ayuda
/cursos - Ver mis cursos
/tareas - Ver mis tareas pendientes
/perfil - Ver mi perfil
/progreso - Ver mi progreso general
    """
    await update.message.reply_text(help_text)

async def ver_cursos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Ver cursos del usuario"""
    from cursos.models import Inscripcion
    
    try:
        # Obtener ID del usuario de Telegram (si está vinculado)
        user_id = update.effective_user.id
        
        # Aquí irían las consultas a tu BD
        message = "📚 Tus cursos:\n\n"
        message += "1. Python Básico - 50% completado\n"
        message += "2. Django Avanzado - 80% completado\n"
        message += "3. Bases de Datos - 20% completado\n"
        
        await update.message.reply_text(message)
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")

async def ver_tareas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Ver tareas pendientes"""
    message = "📋 Tareas pendientes:\n\n"
    message += "1. [Python Básico] - Ejercicios Tema 3 - Vence hoy\n"
    message += "2. [Django] - Proyecto API REST - Vence en 2 días\n"
    message += "3. [BD] - Diseño ER - Vence en 5 días\n"
    
    await update.message.reply_text(message)

async def ver_perfil(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Ver perfil del usuario"""
    message = """
👤 Mi Perfil:

Nombre: Johan Sebastian Castro Gonzalez
Email: johan@example.com
Rol: Estudiante
Cursos Inscritos: 3
Tareas Completadas: 15/28
    """
    await update.message.reply_text(message)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Manejar mensajes generales"""
    user_message = update.message.text.lower()
    
    if "hola" in user_message:
        await update.message.reply_text("¡Hola! 👋 ¿En qué puedo ayudarte?")
    elif "ayuda" in user_message:
        await update.message.reply_text("Usa /help para ver todos los comandos disponibles.")
    else:
        await update.message.reply_text("No entendí. Usa /help para ver los comandos.")

def main():
    """Inicia el bot"""
    # Crear aplicación
    application = Application.builder().token(TOKEN).build()
    
    # Handlers de comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("cursos", ver_cursos))
    application.add_handler(CommandHandler("tareas", ver_tareas))
    application.add_handler(CommandHandler("perfil", ver_perfil))
    
    # Handler para mensajes
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Inicia polling
    print("Bot iniciado... Esperando mensajes")
    application.run_polling()

if __name__ == '__main__':
    main()
