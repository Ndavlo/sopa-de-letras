from flask import Flask

def create_app():
    app= Flask(__name__)
    app.config['SECRET_KEY'] = 'jh3g4123ouh4gk123jhg4762134tb1i23ute78ibtqi7r6587612543b34i152whedgfvuyed'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app