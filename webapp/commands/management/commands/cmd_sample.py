from django.core.management.base import BaseCommand
import django

class Command(BaseCommand):
    help = 'Get started on manage.py command'

    ## def add_arguments(self, parser):
    ##    parser.add_argument('id', nargs='+', type=int)

    def handle(self, *args, **options):
        print(django.conf.settings.DEBUG)
        print_hello('Django Admin command')

def print_hello(name):
    print(f'Hello, {name}!')

