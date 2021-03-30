from flask import Blueprint
# from app.api.v1 import example,admin, patient,token, doctor, treatment, motion, motion_record
from app.api.v1 import example

__author__ = "yejuzhang"

def create_blueprint_v1():
    bp_v1 = Blueprint("v1", __name__)

    # 红图绑定到蓝图层
    example.api.register(bp_v1)


    # admin.api.register(bp_v1)
    # patient.api.register(bp_v1)
    # token.api.register(bp_v1)
    # doctor.api.register(bp_v1)
    # treatment.api.register(bp_v1)
    # motion.api.register(bp_v1)
    # motion_record.api.register(bp_v1)
    # 返回蓝图层, 在 App.py中注册
    return bp_v1





