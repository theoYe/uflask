from flask import Flask

# 注册蓝图
from app.config.setting import envs
from app.models import init_db


def register_blueprints(app: Flask):
    from app.api.v1 import create_blueprint_v1
    # 注册蓝图层, 指定前缀 v1
    app.register_blueprint(blueprint=create_blueprint_v1(), url_prefix="/v1")


def create_app():
    app = Flask(__name__)

    # 初始化环境
    env = "production"     #app.env

    # 载入配置文件
    app.config.from_object(envs[env])

    # 加载安全配置
    # app.config.from_object("app.config.secure")

    # 加载数据库
    init_db(app)

    register_blueprints(app)
    return app



