import os

from flask import Flask, render_template

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass    # a simple page that says hello


    @app.route('/')
    def index():
        return render_template('index.html', home=True)
    
    @app.route('/about')
    def about():
        return render_template('about.html')
    
    @app.route('/blog')
    def blog():
        return render_template('blog.html')

    @app.route('/letter')
    def letter():
        return render_template('letter.html', letter=True)
    
    @app.route('/contact')
    def contact():
        return render_template('contact.html')


    return app