from flask_script import Manager
from werkzeug.exceptions import HTTPException

from app.initapp import create_app
from app.libs.error import APIException, ServerError

app = create_app()


# 捕获全局所有异常
@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1001
        return APIException(msg, code, error_code)
    else:
        #  非调试模式返回json结果
        if not app.config["DEBUG"]:
            return ServerError()
        else:
            raise e
        return ServerError()


manager = Manager(app=app)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
