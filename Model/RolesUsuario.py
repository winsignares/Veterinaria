from config.db import db , app, ma

class RolesUsuario(db.model):
    tablename = "roles"
    id = db.Column(db.identity, primary_key=True)
    roles = db.column(db.String(255))
    
    def __init__(self, roles):
        self.roles = roles
        
        
with app.app_context():
   db.create_all()
   
   class RolesSchema(ma.schema()):
       class meta:
           fields =('id', 'roles')
       
       
       

        
        
    
        
