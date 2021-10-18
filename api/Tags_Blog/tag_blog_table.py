from api import db

tag_blog = db.Table('tag_blog',
                    db.Column('tag_id', db.Integer, db.ForiegnKey(
                        'tag_id'), primary_key=True),
                    db.Column('blog_id', db.Integer, db.ForiegnKey(
                        'blog_id'), primary_key=True)
                    )
