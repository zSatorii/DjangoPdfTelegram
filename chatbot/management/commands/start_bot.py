from django.core.management.base import BaseCommand
from chatbot.bot import main

class Command(BaseCommand):
    help = 'Inicia el bot de Telegram'
    
    def handle(self, *args, **options):
        self.stdout.write('Iniciando bot de Telegram...')
        main()
