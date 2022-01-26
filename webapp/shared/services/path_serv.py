from dataclasses import dataclass

from pathlib import Path
import string
import random
## 
if __name__ == "__main__":
    from config import settings
else:
    from django.conf import settings

@dataclass
class Service():
    media_dir: str
    target_dir: str
    parent_path: Path

    def __init__(self, target_dir:str):
        self.media_dir = settings.MEDIA_DIR
        self.target_dir = target_dir
        self.parent_path = Path(self.media_dir, self.target_dir)

    def exist(self, file_name: str):
        target_path = Path(self.parent_path, file_name)
        return target_path.is_file()

    def get_filename(self, file_name: str):
        target_path = Path(self.parent_path, file_name)
        if not target_path.is_file():
            return {"file_name" : str(target_path)}
        else:
            file_name_new = ''
            while True:
                random_str = generate_randomstr(6)
                file_name_new = target_path.stem + '_' + random_str + target_path.suffix
                if self.exist(file_name_new):
                    pass
                else:
                    break
            #
            file_path_new = Path(self.parent_path, file_name_new)
            return {'file_name': str(file_path_new)}


## common function
def generate_randomstr(length):
    all_char = string.ascii_letters + string.digits + '-_+~#$%^&!?'
    ret = ''
    for i in range(length):
        char = random.choice(all_char)
        ret = ret + char
    return ret


## module debug -----------// entry point
## 
if __name__ == "__main__":
    from pathlib import Path
    import logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] - %(message)s'
    )
    logger = logging.getLogger(__name__)
    ##
    ## initialize
    target_dir = settings.XML_DIR
    logger.debug(f'target_dir={target_dir}')
    service = Service(target_dir)
    file_name = "django-app-framework.bpmn"
    ## debug
    logger.debug( service.get_filename(file_name))
    ##
    file_name = "no_file"
    logger.debug( service.get_filename(file_name))

    logger.debug(generate_randomstr(5))


