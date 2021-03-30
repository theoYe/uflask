from flask import request, json
from werkzeug.exceptions import HTTPException



class APIException(HTTPException):
    code = 500  # 未知错误
    msg = "sorry , something unpredictable happend "
    error_code = 999  # 未知错误

    def __init__(self, msg=None, code=None, error_code=None, headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        response_body = dict(
            msg=self.msg,
            error_code=self.error_code,
            request=request.method + ' ' + self.get_url_no_param()
        )
        text = json.dumps(response_body)
        return text

    # 指定返回头为  application/json
    def get_headers(self, environ=None):
        """指定返回头"""
        return [("Content-type", "application/json")]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]


"""未知错误"""
class ServerError(APIException):
    code = 500
    msg = "unknown error"
    error_code = 999

class UltraAuthError(APIException):
    code = 403
    msg = "permission denied"
    error_code = 1005





class Success(APIException):
    """成功的状态返回"""
    code = 201  # 新增成功
    msg = "success"
    error_code = 0  # 代表正常

class DeleteSuccess(APIException):
    code = 204
    msg = "succesfully delete"
    error_code = 0

class UpdateSuccess(APIException):
    code = 201
    msg = "update Success"
    error_code = 0

class NotFound(APIException):
    code = 404
    msg = "resource not found"
    error_code = 1002

class AuthFailed(APIException):
    code = 401
    error_code = 1003
    msg = "authorization failed"



class IdError(APIException):
    code = 400
    error_code = 1000
    msg = "Id incorrect, check your id format"

class AlreadyExsitError(APIException):
    code = 400
    error_code = 1006
    msg = "resources already exsits"


#class ClientTypeError(APIException):
#    code = 400  # 请求参数错误
#    msg = "Client type is invalid"
#    error_code = 1006
#
#
#class PatientExistsError(APIException):
#    code = 400
#    msg = "The patient already exsits"
#    error_code = 1007
