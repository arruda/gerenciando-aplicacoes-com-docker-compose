from app import db


class Pessoa(db.Model):
    __tablename__ = 'pessoas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String())

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return '<id {}>'.format(self.id)
