from dataclasses import dataclass
import pickledb
import json

@dataclass
class Service():
    json_path: str
    db: pickledb.PickleDB

    def __init__(self, json_path:str):
        self.json_path = json_path
        self.db = pickledb.load(json_path, False)

    def get(self, key: str):
        if key in self.db.getall():
            ret = self.db.get(key)
            if type(ret) == 'dict':
                obj = ret
            elif type(ret) == 'string':
                obj = json.loads(ret.replace("'",'"'))
            else:
                obj = ret
            #
            return obj
        else:
            return {"message": key + " not in json db"}

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
    media_root = 'media'
    json_path = Path(media_root,'json','pickle.json')
    service = Service(json_path)
    ## debug
    logger.debug(f'file="{json_path}"')
    logger.debug( f'ret={service.get("1")}' )
    logger.debug( f'ret={service.get("1234")}' )
    logger.debug( f'ret={service.get("Hello")}' )
    ##
    json_path2 = Path(media_root, 'json', 'tiny.json')
    service2 = Service(json_path2)
    logger.debug(f'ret={service2.get("users")}')
    logger.debug(f'ret["8"]={service2.get("users")["8"]}')
