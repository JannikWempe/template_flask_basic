from sqlalchemy.exc import IntegrityError

from .routes import blog_bp


@blog_bp.cli.command("init_db")
def create():
    from .models import BlogPost
    from app import db

    db.create_all()
    print(f"Database table [{BlogPost.__tablename__}] successfully created.")


@blog_bp.cli.command("populate_tables")
def populate():
    from .models import BlogPost
    from app import db

    post = BlogPost(title="my title", text="Lorem ipsum.")
    try:
        db.session.add(post)
        db.session.commit()
    except IntegrityError:
        print(f"Data in [{BlogPost.__tablename__}] already has been populated.")
    else:
        print(f"Data in [{BlogPost.__tablename__}] has successfully been populated.")
