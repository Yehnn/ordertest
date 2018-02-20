from flask import Flask,render_template
from order.config import configs
from order.models import db, Product,User

#app=Flask(__name__)

'''
app.config.update(dict(
    SECRET_KEY='very secret key',
    SQLALCHEMY_DATABASE_URI='mysql+mysqldb://root@localhost:3306/locktest3?charset=utf8'
    ))
'''
def register_blueprints(app):
    from .handlers import front,product,user
    app.register_blueprint(front)
    app.register_blueprint(product)
    app.register_blueprint(user)

def create_app(config):
    app=Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    register_blueprints(app)
    return app

    



'''
if __name__=='__main__':
    app.run()
'''
