from dataclasses import dataclass, asdict

import pandas as pd
import json
from pathlib import Path
import os
import shutil
import pendulum

# import config
from fixtures import config

@dataclass
class Batch():
    """ xlsx table service class """
    # class variables
    fixture_root: str
    xlsx_dir: str
    json_dir: str
    backup_dir: str
    #
    xlsx_file_path: Path
    json_file_path: Path
    table_name: str
    model_name: str
    id_field: str

    def __init__(self, fixture_root:str, xlsx_dir:str, json_dir:str, backup_dir:str, model_name:str, id_field:str):
        self.fixture_root = fixture_root
        self.xlsx_dir = xlsx_dir
        self.json_dir = json_dir
        self.backup_dir = backup_dir
        self.model_name = model_name
        self.id_field = id_field

    def convertto_json(self, file_root_name: str):
        """ get from xlsx data """
        # generate file names
        table_name = file_root_name
        dtm_str = pendulum.now().format('YYMMDD_HHmmss')
        xlsx_file_name = file_root_name + config.settings.XLSX_EXT
        json_file_name = file_root_name + config.settings.JSON_EXT
        xlsx_file_path = Path(self.fixture_root, self.xlsx_dir, xlsx_file_name)
        json_file_path = Path(self.fixture_root, self.json_dir, json_file_name)
        backup_dir = Path(self.fixture_root, self.backup_dir)
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
        # backup
        shutil.move(xlsx_file_path, xlsx_backup_path)
        # convert
        ary = []
        for k in obj:
            # print(k, obj[k])
            model_name = self.model_name  
            pk = obj[k][self.id_field]
            del obj[k][self.id_field]
            data = {
                "model": model_name,
                "pk": pk,
                "fields": obj[k],
            }
            ary.append(data)
            del(data)
        #   
        # write json data
        json_file_path.touch()
        with open(str(json_file_path), "w", encoding="utf-8") as fs:
            json.dump(ary, fs, ensure_ascii=False, indent=4)
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
    fixture_root = config.settings.FIXTURE_ROOT
    xlsx_dir = config.settings.XLSX_DIR
    json_dir = config.settings.JSON_DIR
    backup_dir = config.settings.BACKUP_DIR
    table_name = "actors".upper()
    model_name = config.settings[table_name + '.MODEL_NAME' ]
    id_field = config.settings[table_name + '.ID_FIELD' ]
    batch = Batch(fixture_root, xlsx_dir, json_dir, backup_dir, model_name, id_field)
    ret = batch.convertto_json(table_name)
    logger.debug(f'ret={ret}')
    #

