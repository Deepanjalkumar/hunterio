from typing import Optional
import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/email/{domain}")
def read_root(domain:str):
    file=[]
    try:
        cwd=os.getcwd()
        path=os.path.join(cwd, "data", "email")
        with open(f"{path}/{domain}.txt", "r") as file:
            file=file.readlines()
    except Exception as e:
        print("\n Not found in database")
        print(e)
        file="Not found"

    return {domain: file}
