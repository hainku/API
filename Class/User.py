from .Database import Database
class User(Database):
    def __init__(self):
        super().__init__()
    
    def login(self,idnum:str ,pw:str):
        sql="select * from user where IdNumber=%s and Password=%s"
        cursor=self.conn.cursor(dictionary=True)
        cursor.execute(sql,(idnum,pw))
        res=cursor.fetchone()
        cursor.close()
        if res:
            return{
                "success" :True,
                "IdNumber": res['IdNumber'],
                "Role" : res['Role']
            }
        else:
            return{
                "success" : False,
                "message" : "Invalid Id Number or Password"
            }