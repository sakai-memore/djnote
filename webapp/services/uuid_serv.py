import uuid

def service():
    uid = uuid.uuid4()
    return str(uid)


## module debug -----------// entry point
## 
if __name__ == "__main__":
    print(service())

