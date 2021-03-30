# from app.libs.enum import ClientTypeEnum
# from app.libs.error import Success, NotFound, AlreadyExsitError, DeleteSuccess, UpdateSuccess
# from app.libs.helper import verify_mongo_id
from app.libs.redprint import Redprint
from app.models.example import Example
# from app.models.admin import Admin
# from app.libs.token_auth import auth
# from app.models.doctor import Doctor
# from app.validator.forms import ClientForm, DoctorClientForm, DoctorForm

api = Redprint("example")

@api.route("/get_examples", methods=["GET", "POST"])
# @auth.login_required
def get_all_examples():
    examples = Example.query_all_example()
    return examples.to_json()


# @api.route("/add_doctor", methods=['PUT'])
# # @auth.login_required
# def register_doctor():
#     form = ClientForm().validate_for_api()
#
#     promise = {
#         ClientTypeEnum.DOCTOR_PHONE: __register_doctor_by_phone  # 301
#         #  302
#     }
#     promise[form.type.data]()  # 调用注册函数
#     return Success()
#
#
# @api.route("/del_doctor/<d_id>", methods=["DELETE"])
# # @auth.login_required
# def delete_doctor(d_id):
#     verify_mongo_id(d_id)
#     doctor = Doctor.query_doctor_by_id(d_id)
#     if doctor:
#         doctor.safe_delete()
#         return DeleteSuccess(code=204, msg="successfully delete")
#     else:
#         return NotFound("doctor not found")
#

