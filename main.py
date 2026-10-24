from fastapi import FastAPI,Form
from Class.User import User
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/login")
def login(idnum:str,=Form(...) pw:str=Form(...)):
    u=User()
    res=u.login(idnum,pw)
    return res