from dataclasses import dataclass

from . import config

@dataclass
class Service():

    def get(self, key: str):
        if key == 'all':
            obj = config.settings
        elif key.upper() in config.settings.keys():
            obj = config.settings[key]
        else:
            obj = {"message": key + " not in json db"}
        #
        return obj

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
    logger.debug( f'ret={service.get("xxxx")}' )

