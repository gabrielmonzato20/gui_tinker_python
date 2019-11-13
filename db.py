import sqlite3
class Db:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS parts(id INTEGER PRIMARY KEY,part text,cliente text,aluguel text, preco text)')
        self.conn.commit()
    def index(self):
        self.cur.execute("SELECT * FROM PARTS")
        rows = self.cur.fetchall()
        return rows
    def inserir(self,preco,aluguel,cliente,part):
        self.cur.execute("INSERT INTO PARTS VALUES(NULL,?,?,?,?)",(part,cliente,aluguel,preco))
        self.conn.commit()
    def destroy(self,id):
        self.cur.execute("DELETE FROM parts Where id=?",(id,))
        self.conn.commit()
    def update(self,id,cliente,aluguel,part,preco):
        self.cur.execute("UPDATE PARTS SET part =?, cliente =?,aluguel=?,preco=? where id =?",(part,cliente,aluguel,preco,id))
        self.conn.commit()
    def __del__(self):
        self.conn.close()

# db = Db('location.db')
# for c in range(80,85,1):
#     db.destroy(c)
# db.inserir("4GB DDR4 Ram", "John Doe", "Microcenter", "160")
# db.inserir("Asus Mobo", "Mike Henry", "Microcenter", "360")
# db.inserir("500w PSU", "Karen Johnson", "Newegg", "80")
# db.inserir("2GB DDR4 Ram", "Karen Johnson", "Newegg", "70")
# db.inserir("24 inch Samsung Monitor", "Sam Smith", "Best Buy", "180")
# db.inserir("NVIDIA RTX 2080", "Albert Kingston", "Newegg", "679")
# db.inserir("600w Corsair PSU", "Karen Johnson", "Newegg", "130")



