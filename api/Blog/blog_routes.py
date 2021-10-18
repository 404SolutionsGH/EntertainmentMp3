from api.Tag.tag_model import Tag
from api.Blog.blog_model import Blog
from types import MethodDescriptorType
from flask import Blueprint, jsonify
from flask.wrappers import Request

from api import db

blogs = Blueprint('blogs', __name__)


@blogs.route('/add_blog', methods=['POST'])
def create_blog():
    data = Request.get_json()
    new_blog = Blog(title=data['title'], content=data['content'],
                    feature_image=data['feature_image'])

    for tag in data['tags']:
        present_tag = Tag.query.filter_by(name=tag).first()
        if(present_tag):
            present_tag.blogs_associated.append(new_blog)
        else:
            new_tag = Tag(name=tag)
            new_tag.blogs_associated.append(new_blog)
            db.session.add(new_tag)

    db.session.add(new_blog)
    db.session.commit()

    blog_id = getattr(new_blog, 'id')
    return jsonify({'id': blog_id})
