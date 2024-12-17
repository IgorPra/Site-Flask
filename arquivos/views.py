from db import db

class Contato(db.Model):
    __tablename__ = 'contatos'

    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(50),nullable=False)
    telefone = db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f"<{self.nome}>"
