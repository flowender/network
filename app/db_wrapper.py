from db_create import *
from  sqlalchemy.sql.expression import func
class DataWrapper():
    def get_blogs_paginate(self, page, per_page):
        blog_paginate = Blog.query.order_by(Blog.created_time.desc()).\
                paginate(page, per_page)
        return blog_paginate
        
    def get_projects_all(self):
        projects = Project.query.all()
        return projects

    def get_project_by_id(self, proj_id):
        return Project.query.get(proj_id)

    def get_blog_by_title(self, blog_title):
        blog = Blog.query.filter(Blog.title == blog_title).first()
        blog.count += 1
        db.session.commit()
        return blog

    def get_category_all(self):
        return Category.query.all()

    def get_category_by_id(self, category_id):
        return Category.query.get(category_id)

    def get_a_random_motto(self):
        return  Motto.query.order_by(func.rand()).first().sentence

    def get_blogs_under_category(self, category_id, page, PER_PAGE):
        category = self.get_category_by_id(category_id)
        blog_paginate = category.blogs.order_by(Blog.created_time.\
                desc()).paginate(page, PER_PAGE)
        return blog_paginate
