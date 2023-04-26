from config.db import db, app, ma 

class DetallesAutores(db.Model):
    __tablename__ = "tbldeta_autores"
    
    id = db.Column(db.Integer, primary_key=True)
    id_libros = db.Column(db.Integer, db.ForeignKey('tbllibros.id'))
    id_autores= db.Column(db.Integer, db.ForeignKey('tblautores.id'))
    
    def __init__(self, id_libros, id_autores):
        self.id_libros = id_libros
        self.id_autores =  id_autores
        

with app.app_context():
    db.create_all()
    
class detallesAutoresSchema(ma.Schema):
    class Meta:
        fields = ('id','id_libros', 'id_autores')