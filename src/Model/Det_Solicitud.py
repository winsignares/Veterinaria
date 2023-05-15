from config.db import db, app, ma 

class Det_Solicitud(db.Model):
    __tablename__ = "tbldet_solicitud"
    
    id = db.Column(db.Integer, primary_key=True)
    idLibros = db.Column(db.Integer, db.ForeignKey('tblServicios.id'))
    idSolicitudes = db.Column(db.Integer, db.ForeignKey('tblSolicitudes.id'))
    
    def __init__(self, idServicios, idSolicitudes):
        self.idLibros = idServicios
        self.idSolicitudes = idSolicitudes
        
        
    
with app.app_context():
    db.create_all()

class Det_SolicitudesSchema(ma.Schema):
    class Meta:
        fields = ('id','idServicios','idSolicitudes')
    