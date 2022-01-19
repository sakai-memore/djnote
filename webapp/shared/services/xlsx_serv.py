from dataclasses import dataclass

import pandas as pd
import json
from pathlib import Path
import os
import shutil
import pendulum

import config
import tinydb_serv as service;

@dataclass
class Service():
    """ xlsx table service class """
    # class variables
    media_root: str
    xlsx_dir: str
    json_dir: str
    xlsx_file_path: Path
    json_file_path: Path
    table_name: str
    serv: service.Service

    def __init__(self, media_root:str, xlsx_dir:str, json_dir:str):
        self.media_root = media_root
        self.xlsx_dir = xlsx_dir
        self.json_dir = json_dir

    def initialize_table(self, file_root_name: str):
        """ get from xlsx data """
        is_exists_xlsx = True
        # generate file names
        table_name = file_root_name
        dtm_str = pendulum.now().format('YYMMDD_HHmmss')
        xlsx_file_name = file_root_name + config.settings.XLSX_EXT
        json_file_name = file_root_name + config.settings.JSON_EXT
        xlsx_file_path = Path(self.media_root, self.xlsx_dir, xlsx_file_name)
        json_file_path = Path(self.media_root, self.json_dir, json_file_name)
        backup_dir = Path(self.media_root, self.xlsx_dir, config.settings.backup_DIR)
        backup_file_path = Path(backup_dir, xlsx_file_name + '.' + dtm_str)
        # file exists
        if not xlsx_file_path.exists():
            msg = {'message': f'file is not found: {xlsx_file_path}'}
            print(msg)
            # return msg 
            is_exists_xlsx = False
        # file exists
        if json_file_path.exists() :
            if is_exists_xlsx:
                if json_file_path.is_file():
                    # os.remove(str(json_file_path))
                    shutil.move(json_file_path, backup_file_path)
                    json_file_path.unlink()
                else:
                    return {'message': f'directory exists: {json_file_path}'}
            else:
                if json_file_path.is_file():
                    pass
                else:
                    return {'message': f'directory exists: {json_file_path}'}
        # 
        # read xlsx
        if is_exists_xlsx:
            df = pd.read_excel(str(xlsx_file_path), header=1)
            json_str = df.T.to_json()
            obj = json.loads(json_str)
            obj_table = {file_root_name: obj}
        #
        # write json data
        if not json_file_path.exists():
            json_file_path.touch()
            with open(json_file_path, "w", encoding="utf-8"):
                json.dump(obj_table, json_file_path, ensure_ascii=False, indent=4)
        #
        # set class variables
        self.json_file_path = json_file_path
        self.xlsx_file_path = xlsx_file_path
        self.table_name = table_name
        self.service = service.Service(self.json_file_name, self.table_name)

    def list(self):
        return self.serv.list()

    def get(self, id: str):
        return self.serv.get(id)

    def post(self, do: dict):
        return self.serv.post(do)

    def put(self, do: dict):
        return self.serv.put(do)

    def delete(self, id: str):
        return self.serv.delete(id)


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
    table_name = "actors"
    service = Service(media_root, xlsx_dir, json_dir)
    service.initialize_table(table_name)
    #
    logger.debug(dir(service))
