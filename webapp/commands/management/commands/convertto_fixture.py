from django.core.management.base import BaseCommand
import django

from fixtures import convert_xlsx as converter
from fixtures import config

import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] - %(message)s'
)
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Get started on manage.py command'

    def add_arguments(self, parser):
       parser.add_argument(
           'files',
           nargs='+',
           type=str,
           help='set target xlsx file stem',
       )

    def handle(self, *args, **options):
        logger.info('// -----------------------// start')
        for file in options['files']:
            ret = process(file)
            logger.info(f'processing {file}, .. ret:{ret}')
        #
        logger.info('// -----------------------// end..')

def process(file):
    ##
    ## debug
    fixture_root = config.settings.FIXTURE_ROOT
    xlsx_dir = config.settings.XLSX_DIR
    json_dir = config.settings.JSON_DIR
    backup_dir = config.settings.BACKUP_DIR
    table_name = file.upper()
    model_name = config.settings[table_name + '.MODEL_NAME' ]
    id_field = config.settings[table_name + '.ID_FIELD' ]
    batch = converter.Batch(fixture_root, xlsx_dir, json_dir, backup_dir, model_name, id_field)
    ret = batch.convertto_json(table_name)
    return ret


