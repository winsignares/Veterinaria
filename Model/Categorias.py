from config.db import db, app, ma 

class Categorias(db.Model):
    __tablename__ = "tblcategorias"

    
    id  = db.Column(db.Integer, primary_key=True)
    N_cat = db.Column(db.String(50))
    Descripcion = db.Column(db.String(50))

    def __init__(self, N_cat,Descripcion):
        self.N_cat = N_cat
        self.Descripcion = Descripcion
    
with app.app_context():
    db.create_all()

class CategoriasSchema(ma.Schema):
    class Meta:
        fields = ('id','N_Cat','Descripción')
        