from dataclasses import dataclass, asdict

import pandas as pd
import json
from pathlib import Path
import os
import shutil
import pendulum

import config

@dataclass
class Batch():
    """ xlsx table service class """
    # class variables
    media_root: str
    xlsx_dir: str
    json_dir: str
    backup_dir: str
    xlsx_file_path: Path
    json_file_path: Path
    table_name: str

    def __init__(self, media_root:str, xlsx_dir:str, json_dir:str, backup_dir:str):
        self.media_root = media_root
        self.xlsx_dir = xlsx_dir
        self.json_dir = json_dir
        self.backup_dir = backup_dir

    def initialize_table(self, file_root_name: str):
        """ get from xlsx data """
        # generate file names
        table_name = file_root_name
        dtm_str = pendulum.now().format('YYMMDD_HHmmss')
        xlsx_file_name = file_root_name + config.settings.XLSX_EXT
        json_file_name = file_root_name + config.settings.JSON_EXT
        xlsx_file_path = Path(self.media_root, self.xlsx_dir, xlsx_file_name)
        json_file_path = Path(self.media_root, self.json_dir, json_file_name)
        backup_dir = Path(self.media_root, self.backup_dir)
        xlsx_backup_path = Path(backup_dir, xlsx_file_name + '.' + dtm_str)
        #
        # set class variables
        self.json_file_path = json_file_path
        self.xlsx_file_path = xlsx_file_path
        self.table_name = table_name
        # file exists
        if not xlsx_file_path.exists():
            msg = {'message': f'file is not found: {xlsx_file_path}'}
            return msg
        #
        # file exists
        if json_file_path.exists() :
            if json_file_path.is_file():
                json_file_path.unlink()
            else:
                return {'message': f'directory exists: {json_file_path}'}
        else:
            pass
        # 
        # read xlsx
        df = pd.read_excel(str(xlsx_file_path), header=1)
        json_str = df.T.to_json()
        obj = json.loads(json_str)
        obj_table = {file_root_name: obj}
        shutil.move(xlsx_file_path, xlsx_backup_path)
        #
        # write json data
        json_file_path.touch()
        with open(str(json_file_path), "w", encoding="utf-8") as fs:
            json.dump(obj_table, fs, ensure_ascii=False, indent=4)
        #
        return 0

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
    ## debug
    media_root = config.settings.MEDIA_ROOT
    xlsx_dir = config.settings.XLSX_DIR
    json_dir = config.settings.JSON_DIR
    backup_dir = config.settings.BACKUP_DIR
    table_name = "actors"
    batch = Batch(media_root, xlsx_dir, json_dir, backup_dir)
    ret = batch.initialize_table(table_name)
    logger.debug(f'ret={ret}')
    #
    logger.debug(dir(batch))
    logger.debug(asdict(batch))

