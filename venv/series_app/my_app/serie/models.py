from my_app import db

class Serie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    genero = db.Column(db.String(50))
    temporadas = db.Column(db.Integer)
    mediaIMDB = db.Column(db.Float(asdecimal=True))
    ativa = db.Column(db.Boolean)

    def __init__(self, titulo, genero, temporadas, mediaIMDB, ativa):
        self.titulo = titulo
        self.genero = genero
        self.temporadas = temporadas
        self.mediaIMDB = mediaIMDB
        self.ativa = ativa

    def __repr__(self):
        return'Serie: {0}'.format(self.id)
