from dataclasses import dataclass, asdict
from tinydb import TinyDB, Query
import uuid

@dataclass
class Service():
    data_path: str
    table_name: str
    id_field: str
    db: TinyDB
    tbl: TinyDB.table
    query: Query = Query()

    def __init__(self, data_path, table_name, id_field):
        self.data_path = data_path
        self.table_name = table_name
        self.id_field = id_field
        self.db = TinyDB(self.data_path)
        self.tbl = self.db.table(table_name)

    def list(self):
        return self.tbl.all()

    def get(self, key: str):
        lst = self.tbl.search(self.query[self.id_field] == key)
        if lst :
            return lst[0]
        else:
            return {}

    def post(self, do):
        uid = uuid.uuid4()
        do[self.id_field] = str(uid)
        self.tbl.insert(do)
        return do

    def put(self, do):
        key = do[self.id_field]
        self.tbl.update(do, self.query[self.id_field] == key)
        return self.tbl.search(self.query[self.id_field] == key)[0]

    def delete(self, key: str):
        self.tbl.remove(self.query[self.id_field] == key)
        return key

    def filter(self, query):
        lst = self.tbl.search(self.query.fragment(query))
        return lst

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
    #
    ## initialize
    data_path = Path('media', 'json','tiny.json')
    table_name = 'users'
    key_field = 'id'
    ## debug
    logger.debug(data_path)
    service = Service(data_path, table_name, key_field)
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
    #
    l = service.filter({'age': 21, 'city': 'Tokyo'})
    logger.debug('list:')
    logger.debug(l)
    # 
    logger.debug('------------')
    ## initialize
    data_path2 = Path('media', 'json','actors.json')
    table_name2 = 'actors'
    key_field2 = 'actor_id'
    service2 = Service(data_path2, table_name2, key_field2)
    obj_4 = service2.get(4)
    logger.debug(dir(service2))
    logger.debug(service2.id_field)
    logger.debug(obj_4)

