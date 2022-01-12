from dataclasses import dataclass
from tinydb import TinyDB, Query
import uuid

@dataclass
class Service():
    data_path: str
    table_name: str
    db: TinyDB
    tbl: TinyDB.table
    query: Query = Query()

    def __init__(self, data_path, table_name):
        self.data_path = data_path
        self.table_name = table_name
        self.db = TinyDB(self.data_path)
        self.tbl = self.db.table(table_name)

    def list(self):
        return self.tbl.all()

    def get(self, id: str):
        lst = self.tbl.search(self.query.id == id)
        if lst :
            return lst[0]
        else:
            return {}

    def post(self, do):
        id = uuid.uuid4()
        do['id'] = str(id)
        self.tbl.insert(do)
        return do

    def put(self, do):
        id = do['id']
        self.tbl.update(do, self.query.id == id)
        return self.tbl.search(self.query.id == id)[0]

    def delete(self, id: str):
        self.tbl.remove(self.query.id == id)
        return id

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
    
    ## initialize
    data_path = Path('media', 'data','tiny.json')
    table_name = 'users'
    ## debug
    logger.debug(data_path)
    service = Service(data_path, table_name)
    ## list
    logger.debug(service.list())

    data_object = {
        'name': 'Yoko Ono',
        'age': 21,
        'city': 'Tokyo'
    }
    ## post
    data_entity = service.post(data_object)
    logger.debug(data_entity)
    id_yoko = data_entity['id']
    ## get
    obj_10002 = service.get('10002')
    logger.debug('get:')
    logger.debug(obj_10002)
    logger.debug(dir(obj_10002))
    logger.debug(type(obj_10002))
    ## delete
    logger.debug(service.delete(id_yoko))
    logger.debug(service.get(id_yoko))
    ## put (update)
    obj_10002['age'] = 44
    logger.debug(service.put(obj_10002))

