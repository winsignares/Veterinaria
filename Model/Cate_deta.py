from config.db import db, app, ma 

class cate_deta(db.Model):
    __tablename__ = "tblcatedeta"

    
    id  = db.Column(db.Integer, primary_key=True)
    id_cate = db.Column(db.Integer, db.ForeignKey('tblcategorias.id'))
    id_li = db.Column(db.Integer, db.ForeignKey('tbllibros.id'))
    

    def __init__(self, id_cate, id_li):
        self.id_cate = id_cate
        self.id_li = id_li


with app.app_context():
    db.create_all()

class cate_detaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_cate', 'id_li')