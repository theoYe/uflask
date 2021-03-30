# 1 数据模型的建立



## 1.1 hackolade 建立 mongodb 数据模型



![image-20210329235916975](https://raw.githubusercontent.com/theoYe/ImageRepo/master/image-20210329235916975.png)



![image-20210329235902325](https://raw.githubusercontent.com/theoYe/ImageRepo/master/image-20210329235902325.png)

> 如果过期了， 可以创建一个虚拟机 重新申请试用
>
> 1. 在虚拟机里申请14 天的Free trial
> 2. 填写一个邮箱获得 key
> 3. 将key填写给虚拟机外的主机即可
>
> 





## 1.2 建立mongo用户



1. use uflask_db;

2. 再该数据库下建立文件

```json
db.createUser(
  {
    user: "uflask",
    pwd: "uflask123",
    roles: [ {role:"root",db:"admin"} ]
  }
)
```

> roles 是必须填的字段

## 1.2 复制MongoDBScripts到mongodb中创建数据库







```python
use uflask_db;

db.createCollection( "example",{
    "storageEngine": {
        "wiredTiger": {}
    },
    "capped": false,
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "title": "example",
            "additionalProperties": false,
            "properties": {
                "_id": {
                    "bsonType": "objectId"
                },
                "Documen": {
                    "bsonType": "object",
                    "properties": {
                        "doc_id": {
                            "bsonType": "objectId"
                        },
                        "doc_name": {
                            "bsonType": "string"
                        },
                        "arr_name": {
                            "bsonType": "array",
                            "additionalItems": true,
                            "uniqueItems": false,
                            "items": {
                                "bsonType": "object",
                                "properties": {
                                    "sub_doc_name": {
                                        "bsonType": "string"
                                    },
                                    "sub_doc_num": {
                                        "bsonType": "number"
                                    }
                                },
                                "additionalProperties": false
                            }
                        }
                    },
                    "additionalProperties": false
                },
                "example_name": {
                    "bsonType": "string"
                }
            }
        }
    },
    "validationLevel": "off",
    "validationAction": "warn"
});
```







## 1.3 插入测试数据



1. 我们可以在 `hackolade` 中添加 `Sample`数据

![image-20210330000038008](https://raw.githubusercontent.com/theoYe/ImageRepo/master/image-20210330000038008.png)

2. 这样就有数据可以插入了 

并且还可以进行验证

![image-20210330000000868](https://raw.githubusercontent.com/theoYe/ImageRepo/master/image-20210330000000868.png)

3. 插入数据



```json
db.example.insert({
    "Documen": {
        "doc_id": ObjectId("507f1f77bcf86cd799439011"),
        "doc_name": "Lorem",
        "arr_name": [
            {
                "sub_doc_name": "sub_doc1",
                "sub_doc_num": 1234
            }
        ]
    },
    "example_name": "example1"
})
```

再插入一条



```
db.example.insert({
    "Documen": {
        "doc_id": ObjectId("507f1f77bcf86cd799439011"),
        "doc_name": "Lorem",
        "arr_name": [
            {
                "sub_doc_name": "sub_doc1",
                "sub_doc_num": 1234
            }
        ]
    },
    "example_name": "example1"
})
```

查看数据库



![image-20210329235840263](https://raw.githubusercontent.com/theoYe/ImageRepo/master/image-20210329235840263.png)



# 2 flask后端框架搭建



## 2.1 pipenv项目环境搭建

1. pipfile如下, 运行命令 `pipenv install Pipfile`

```python
[[source]]
url = "https://pypi.tuna.tsinghua.edu.cn/simple"
verify_ssl = true
name = "pypi"

[packages]
flask = "==1.0"
flask-sqlalchemy = "==2.3.2"
flask-wtf = "==0.14.2"
cymysql = "==0.9.1"
flask-cors = "==2.1.0"
flask-httpauth = "==2.7.0"
requests = "==2.18.4"
pipfile = "*"

[dev-packages]

[requires]
python_version = "3.6"

```



> 不要忘记关闭代理， 否则无法安装

目录结构图如下

![image-20210329225556947.png](https://raw.githubusercontent.com/theoYe/ImageRepo/master/image-20210329231532224.png)


## 2.2 数据库连接



1. 数据库连接工具使用 : `Robot 3T`
2. 数据库的连接逻辑在 ： `app\models\__init__.py`中





## 2.3 配置文件

1. 配置文件加载方式：

使用flask时， `app.config.from_object(class)` 会吧类 class的变量成员作为 config对象的键值对存在

```python
from flask import Flask
app = Flask()

app.config.from_objects(ConfigObject)
```

```python
class ConfigObject:
	USER = "username"
	PASS = "password"
```

> ConfigObject可以是任意对象！



2. 配置文件使用方式：

```python
app.config["USER"] # username
app.config["password"] #password
```







## 2.4 app启动流程



1. 载入配置文件
2. 加载数据库
3. 注册蓝图



```python
def create_app():
    app = Flask(__name__)

    # 初始化环境
    env = "production"     #app.env

    # 载入配置文件
    app.config.from_object(envs[env])

    # app.config.from_object("app.config.setting")
    app.config.from_object("app.config.secure")

    # 加载数据库
    init_db(app)

    register_blueprints(app)
    return app
```





# 3 编写





## 3.1 添加数据模型



```python
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


```



## 3.2 添加接口



## 3.3 添加错误error









# github图床token

```
8a97ea0b880c8b3b33ab7504acc312e5e9900e36
```



配置：

```
{
  "picBed": {
    "current": "github",
    "uploader": "github",
    "smms": {
      "token": "9x2JYkcDkIyGEYdq8Zvyv8kZsIR6px04"
    },
    "github": {
        "repo": "theoYe/ImageRepo", // 仓库名，格式是username/reponame
        "token": "8a97ea0b880c8b3b33ab7504acc312e5e9900e36", // github token
        "path": "", // 自定义存储路径，比如img/
        "customUrl": "", // 自定义域名，注意要加http://或者https://
        "branch": "master" // 分支名，默认是main
    },
  },
  "picgoPlugins": {}
}
```

