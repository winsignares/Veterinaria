from config.db import db, app, ma 

class Servicios(db.Model):
    __tablename__ = "tblservicios"

    
    id  = db.Column(db.Integer, primary_key=True)
    Nombre_servicio = db.Column(db.String(50))
    tipo_servicios = db.Column(db.Integer, db.ForeignKey('tbltipo_servicio.id'))
    productos = db.Column(db.Integer, db.ForeignKey)

    def __init__(self, Nombre_servicio, tipo_servicios, productos):
        
        self.Nombre_servicio = Nombre_servicio
        self.tipo_servicios = tipo_servicios
        self.productos = productos
       
    
with app.app_context():
    db.create_all()

class ServiciosSchema(ma.Schema):
    class Meta:
        fields = ('id','Nombre_servicio', 'tipo_servicios', 'productos')