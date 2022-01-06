import uuid

def service():
    uid = uuid.uuid4()
    return str(uid)


## module debug -----------// entry point
## 
if __name__ == "__main__":
    import logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] - %(message)s'
    )
    logger = logging.getLogger(__name__)
    
    ## debug
    logger.debug(f'ret="{service()}"')

