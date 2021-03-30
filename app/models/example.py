from mongoengine import Document, EmbeddedDocument, StringField, FloatField, DateTimeField, ObjectIdField, ListField, EmbeddedDocumentField
from datetime import datetime


from werkzeug.security import check_password_hash

# from app.libs.error import NotFound, AuthFailed


class SubDoc(EmbeddedDocument):
    sub_doc_name = StringField()
    sub_doc_num = FloatField()

class Documen(EmbeddedDocument):
    doc_id = ObjectIdField()
    doc_name = StringField()
    arr_name = ListField(EmbeddedDocumentField(SubDoc))


class Example(Document):
    _id = ObjectIdField()
    Documen = EmbeddedDocumentField(Documen)
    example_name = StringField()

    @staticmethod
    def query_all_example():
        return Example.objects
    # @staticmethod
    # def verify(username, password):
    #     admin = Admin.objects(admin_username=username).first()
    #     if not admin:
    #         raise NotFound(msg="user not found")
    #     if not admin.check_password(raw=password):
    #         raise AuthFailed(msg="AuthFailed!Please check your password")
    #     return admin
    #
    #
    # def check_password(self, raw):
    #     if not self.password:
    #         return False
    #     # return check_password_hash(self.password, raw)
    #     return self.password == raw