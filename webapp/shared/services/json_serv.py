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
            ret_str = self.db.get(key)
            obj = json.loads(ret_str.replace("'",'"'))
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
    json_path = Path(media_root,'data','pickle.json')
    service = Service(json_path)
    ## debug
    logger.debug(f'file="{json_path}"')
    logger.debug( f'ret={service.get("1")}' )
    logger.debug( f'ret={service.get("1234")}' )
    logger.debug( f'ret={service.get("Hello")}' )

