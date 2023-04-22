from config.db import db, app, ma 

class Editoriales(db.Model):
    __tablename__ = "tbEditoriales"

    
    id  = db.Column(db.Integer, primary_key=True)
    N_Edi = db.Column(db.String(50))
    id_Prov = db.Column(db.Integer,db.ForeignKey("tblproveedores.id"))
    

    def __init__(self, N_Edi, id_Prov):
        self.N_Edi = N_Edi
        self.id_Prov = id_Prov
       
        
    
with app.app_context():
    db.create_all()

class EditorialesSchema(ma.Schema):
    class Meta:
        fields = ('id','N_Edi','id_Prov')