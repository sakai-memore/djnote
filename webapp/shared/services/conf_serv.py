from dataclasses import dataclass

from config.services import config
# import config

@dataclass
class Service():

    def get(self, key: str):
        key = key.upper()
        if key == 'ALL':
            return config.settings
        elif key in config.settings.keys():
            return config.settings[key]
        else:
            return {"message": f'no key found: {key}'}


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
    service = Service()
    ## debug
    logger.debug( f'ret={service.get("all")["XML_DIR"]}' )
    logger.debug( service.get("XML_DIR") )
    logger.debug( service.get("XML_DER") )

