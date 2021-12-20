import time
from app.drop_create_insert_collection import drop_create_insert_collection

if __name__ == '__main__':
    start = time.perf_counter()
    drop_create_insert_collection()
    end = time.perf_counter()
    print(f"Success!!\n"
          f"The Starship collection has been created.\n"
          f"Elapsed time: {round(float(end - start)/60, 1)} minutes")
