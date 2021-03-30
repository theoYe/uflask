"""
测试数据库连接
"""
from flask import Flask
from app.models import init_db
import  json
# 导入配置
from app.config.setting import DevelopConfig, StagingConfig
from bson import json_util
from app.models.example import Example

def test_development():
    app = Flask(__name__)

    app.config.from_object(DevelopConfig)

    init_db(app)

    print(Example.objects.to_json())



test_development()

