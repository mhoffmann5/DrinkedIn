from flask import Blueprint, render_template

home_page = Blueprint('home_page', __name__,
                      template_folder ='templates')
@home_page.route('/')
@home_page.route('/Home')
def landingPage():
    return render_template('homepage.html');
