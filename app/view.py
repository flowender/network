#coding=UTF-8
import os
from StringIO import StringIO
import random
from . import app
from flask import render_template, g, session,\
        request, make_response, redirect, url_for
from db_wrapper import DataWrapper
from html2text import  html2text_file
from introduction import INTRO
from resume import RESUME, EDUCATION
dw = DataWrapper()

PER_PAGE = 6
MOTTO = "My life is much more interesting inside my head"

img = "../static/img"
#index
topic = u"与花有关的一切"
intro = "Flowender Studio"
intro_2 = u"我们为您的生活，派对，婚礼，商务空间提供花艺设计及周边服务"

#About studio
about_studio = u"致力于用花艺美化生我们是来的花艺师我们是来的花艺师我们是来的花艺师我们是来的花艺师活"
about_us = u"我我们是来的花艺师我们是来的花艺师我们是来的花艺师我们是来的花艺师我们是来的花艺师我们是来的花艺师们是来的花艺师"

#Our service
our_service = u"提供专业展会，派对，礼仪的花艺设计"
service_items = ((u"花礼",u"富有设计感的花艺礼品"),(2,3),(3,4))

#gallery
gallery_intro = u"与众不同的创意体验"

#contact
hot_line = u"18621555270"

def _html2text(html):
    sio = StringIO()
    html2text_file(html, sio.write)
    text = sio.getvalue()
    sio.close()
    return text.replace(" ", "")

app.jinja_env.filters['_html2text'] = _html2text

#@app.before_request
#def before_request():
    #g.Category = dw.get_category_all()
    #g.Projects = dw.get_projects_all()
    #g.Contact={
    #    "email": "wenbin.rc AT gmail.com",
    #    "intro": INTRO,
    #    }
    #g.MOTTO = u"\" 怕只怕认真二字 \""
    #u"我们在燃烧的忍耐中武装，随着拂晓进入光辉的城镇"#dw.get_a_random_motto()

def date_format(date):
    return u"%d年%d月%d日"%(date.year, date.month, date.day)
app.jinja_env.filters['dateformat'] = date_format

@app.route('/images')
def view_images():
    motto = dw.get_a_random_motto()
    if session.has_key('img_num'):
        if  session['img_num'] < 9:
            session['img_num'] += 1
        else:
            session['img_num'] = 1
    else:
        session['img_num'] = 1
    print session['img_num']
    return render_template('images.html',
                motto = motto,
                RANDOM_PIC = session['img_num'],
            )

@app.route('/blog/<int:page>')
@app.route('/blog')
def index(page=1):
    motto = dw.get_a_random_motto()
    blog_paginate = dw.get_blogs_paginate(page, PER_PAGE)
    session['nav'] = "index"
    RANDOM_PIC = 9#random.randrange(1, 10)
    if blog_paginate.total == 0:
        pagination = 0
    if blog_paginate.total % PER_PAGE:
        pagination = blog_paginate.total / PER_PAGE + 2
    else:
        pagination = blog_paginate.total / PER_PAGE + 1
    response = make_response(render_template('index.html',
            blogs = blog_paginate.items,
            page = page,
            pagination = pagination,
            motto = motto,
            RANDOM_PIC = RANDOM_PIC,
            ))
    print request.cookies
#    if not request.cookies.get('popped'):
#        print "POPED"
#   #     print " not popped",request.cookies.get('popped')
#        response.set_cookie("popped","hello", max_age = 5 )
    return response

@app.route('/blogs_under_category/<int:category_id>-<int:page>')
@app.route('/blogs_under_category/<int:category_id>')
def blogs_under_category(category_id, page=1):
    blog_paginate = dw.get_blogs_under_category(category_id,\
                     page, PER_PAGE)
    if blog_paginate.total == 0:
        pagination = 0
    elif blog_paginate.total % PER_PAGE:
        pagination = blog_paginate.total / PER_PAGE + 2
    else:
        pagination = blog_paginate.total / PER_PAGE + 1
    session['nav'] = "index"
    return render_template('blog_by_category.html',
            blogs = blog_paginate.items,
            pagination = pagination,
            page = page,
            category_id = category_id,
            )

@app.route('/project')
def project():
    return "I'M OK"
#    projects = dw.get_projects_all()
#    session['nav'] = 'project'
#    return render_template('project.html',
#                projects = projects,
#                )
@app.route('/project_details/<project_id>')
def project_details(project_id):
    project = dw.get_project_by_id(project_id)
    return render_template('project-single.html',
                project = project,
                )
@app.route('/blog/<blog_title>')
def blog(blog_title):
    blog = dw.get_blog_by_title(blog_title)
    return render_template('blog.html',
                blog = blog,
                )

@app.route('/test/<test_id>')
def test(test_id):
    #project_id = 1
    project = dw.get_project_by_id(test_id)
    return render_template('test.html',
                project=project,
                )

@app.route('/contact')
def contact():
    session['nav'] = "contact"
    return render_template('contact_me.html',
                        )
@app.route('/message',methods=['post'])
def message():
    if request.method == "POST":
        sender_name = request.form.get('name','')
        sender_email = request.form.get('email','')
        message =request.form.get('message','')
        #print sender_name,sender_email,message
        if 'SERVER_SOFTWARE' in os.environ:
            import sae.mail
            sae.mail.send_mail("wenbin.rc@gmail.com",
                            "You've recieved a new letter from you blog",
                            "%s/%s send you a message:\n%s"%(sender_name,sender_email, message),
                            ('smtp.gmail.com', 587, "winoiv@gmail.com", "jimshu1989", True)
                            )
        return "You message has already send to me. Thanks for your attention!"

@app.route('/')
@app.route('/resume')
def show_resume():
    return render_template('index.html',
            topic = topic,
            intro = intro,
            intro_2 = intro_2,

            about_studio = about_studio,
            about_us = about_us,

            our_service = our_service,
            service_items = service_items,
            gallery_intro = gallery_intro,

            hot_line = hot_line,
  	    img = img,

           #resume = RESUME,
           #education = EDUCATION,
           )
