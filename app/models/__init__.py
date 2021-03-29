from mongoengine import connect



def init_db(app):
    dbname = app.config["DATABASE"]
    engine = app.config["ENGINE"]
    host = app.config["HOST"]
    port = app.config["PORT"]
    password = app.config["PASSWORD"]
    username = app.config["USER"]
    authentication_source = app.config["AUTHENTICATION_SOURCE"]
    connect(f'{dbname}',
            username=f"{username}",
            password=f"{password}",
            host=f'{engine}://{host}/{dbname}',
            port=port,
            authentication_source=f'{authentication_source}'
            )

