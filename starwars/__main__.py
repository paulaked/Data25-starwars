import time
from app.drop_create_insert_collection import drop_create_insert_collection

if __name__ == '__main__':
    start = time.time()
    drop_create_insert_collection()
    end = time.time()
    print(f"Success!!\nThe Starship collection has been created.\nElapsed time: {end - start}")
