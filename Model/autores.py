from config.db import db, app, ma 

class autores(db.Model):
    __tablename__ = "tblautores"
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    nacionalidad= db.Column(db.String(200))
    
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad =  nacionalidad
        

with app.app_context():
    db.create_all()
    
class AutoresSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre', 'nacionalidad')