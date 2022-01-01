import uuid

def get():
    uid = uuid.uuid4()    
    return str(uid)

print(get())
