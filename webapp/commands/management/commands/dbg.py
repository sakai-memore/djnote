from django.core.management.base import BaseCommand
import django

import logging
import sys
import importlib
sys.path.append(str(django.conf.settings.BASE_DIR) + '\services')
## print(sys.path)

logger = logging.getLogger(__name__)

## fromによりpathを指定。__init__.pyでpackagingされていること
## from services import uuid_serv as serv

class Command(BaseCommand):
    help = 'Get started on manage.py command'

    def add_arguments(self, parser):
        parser.add_argument(
            '--f',
            ## action='debug_service',
            type=str,
            help='target py file',
        )

    def handle(self, *args, **options):
        if options['f']:
            module_name = options["f"]
            serv = importlib.import_module(module_name)
            print_debug(f'serv: {module_name}')
            ##
            ret = serv.service()
            logger.debug(ret)
            ##
            print_debug('End')

def print_debug(name):
    logger.info(f'// --------------// {name}..')

