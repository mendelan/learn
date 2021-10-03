from django.core.management.base import BaseCommand
from blog.forms import TagForm

class Command(BaseCommand):   
    def handle(self, *args, **options):
        print(123)
