from app import db


class BlogPost(db.Model):
    __tablename__ = "blog_post"

    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    title = db.Column(db.String(100), unique=True, index=True)
    text = db.Column(db.String(100))

    def __repr__(self):
        return f"<BlogPost title={self.title} text={self.text}>"

    @classmethod
    def by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    @classmethod
    def by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def as_dict(self):
        return {"id": self.id, "title": self.title, "text": self.text}
