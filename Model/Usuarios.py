from config.db import db,app,ma 

class Users(db.Model):
    __tablename__= "TblUsuarios"    
    
    
    id = db.Column(db.Integer,primary_key=True)
    full_name= db.Column(db.String(200))
    password= db.Column(db.String(200))
    Email= db.Column(db.String(200))
    telefono= db.Column(db.Integer)
    especialidad= db.Column(db.String(200))
    jornada= db.Column(db.String(200))
    direccion= db.Column(db.String(200))
    id_roles = db.Column(db.Integer, db.ForeignKey('tblrolesusuarios.id'))
    
    def __init__(self,full_name,password,Email,telefono,especialidad,jornada,direccion,id_roles):
       self.full_name= full_name
       self.password= password
       self.Email= Email
       self.telefono= telefono
       self.especialidad= especialidad
       self.jornada= jornada
       self.direccion= direccion
       self.id_roles = id_roles
       
       with app.app_context():
           db.create_all()

class UsuariosSchema(ma.Schema):
    class Meta:
        fields = ('id','full_name','password','Email','telefono','especialidad','jornada','direccion')
        
    
    
    
    
