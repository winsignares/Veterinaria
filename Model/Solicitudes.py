from config.db import db, app, ma 

class Solicitudes(db.Model):
    __tablename__ = "tblSolicitudes"

    id = db.Column (db.Integer, primary_key = True)
    fecha_solicitud = db.Column(db.DateTime)
    cantidad = db.Column(db.Integer)
    Id_usu = db.Column(db.Integer, db.ForeignKey('TblUsuarios.id'))

  #  id_usu = db.Columm (db.integer) 
    

    def __init__(self, fecha_solicitud, cantidad, Id_usu ):
        self.fecha_solicitud = fecha_solicitud
        self.cantidad = cantidad
        self.Id_usu = Id_usu


with app.app_context():
    db.create_all()

class SolicitudesSchema(ma.Schema):
    class meta:
        fields = ('id', 'fecha_solicitud','cantidad', 'Id_usu' )
#a
#e