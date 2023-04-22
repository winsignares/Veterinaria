from config.db import db, app, ma 
class estadosolicitud(db.Model):
    __tablename__ = "tblestadosolicitud"

    
    id  = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    id_solicitud =db.Column(db.Integer ,db.ForeignKey('tblSolicitudes.id'))  
    fecha_devolucion = db.Column(db.Date)
    dias_atraso = db.Column(db.Integer)
    estsado = db.Column(db.Integer)
    

    def __init__(self, fecha,id_solicitud , fecha_devolucion,dias_atraso,estado):
        self.fecha = fecha
        self.id_solicitud = id_solicitud
        self.fecha_devolucion = fecha_devolucion
        self.dias_atraso = dias_atraso
        self.estado = estado
with app.app_context():
    db.create_all()

class estadoSchema(ma.Schema):
    class Meta:
        fields = ('id','fecha' ,'id_solicitud' ,'fecha_devolucion','dias_atraso' ,'estado')

