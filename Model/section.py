from config.db import db, app, ma 

class Section(db.Model):
    __tablename__ = "tblsection"

    
    id  = db.Column(db.Integer, primary_key=True)
    year  = db.Column(db.Integer)
    especialidad = db.Column(db.String(200))
    seccion = db.Column(db.String(1))
    

    def __init__(self, year, especialidad, seccion):
        self.year = year
        self.especialidad = especialidad
        self.seccion = seccion


with app.app_context():
    db.create_all()

class sectionSchema(ma.Schema):
    class Meta:
        fields = ('id','year', 'especialidad', 'seccion')