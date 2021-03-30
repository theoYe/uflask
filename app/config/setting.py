






class Config():
    DEBUG = True
    TESTING = False
    """token超时时间2小时"""
    TOKEN_EXPIRATION = 7200
    ENGINE = "mongodb"
    DRIVER = "mongoengine"


class DevelopConfig(Config):
    """
    开发环境的配置
    """
    # DEBUG = True
    # COLLECTION = "paths"
    # USER = "wheel"
    # PASSWORD = "wheel123"
    # HOST = "192.168.163.129"
    # PORT = 27017
    # DESCRIPTION = "DevelopConfig"
    # AUTHENTICATION_SOURCE = "wheel_db"

    DEBUG = True
    DATABASE = "uflask_db"
    USER = "uflask"
    PASSWORD = "uflask123"
    HOST = "192.168.163.137"
    PORT = 27017
    DESCRIPTION = "DevelopConfig"
    AUTHENTICATION_SOURCE = "uflask_db"



class StagingConfig(Config):
    """
    部署环境的配置
    """
    DEBUG = False

    DATABASE = "carer_db"
    USER = "carer"
    PASSWORD = "carernb123"
    HOST = "134.175.100.199"
    PORT = 27017
    DESCRIPTION = "StagingConfig"
    AUTHENTICATION_SOURCE = "carer_1db"



class TestingConfig(Config):
    """
    测试环境的配置
    """
    DEBUG = False

    DATABASE = "carer_db"
    USER = "carer"
    PASSWORD = "carernb123"
    HOST = "134.175.100.199"
    PORT = 27017
    DESCRIPTION = "TestingConfig"


class ProductionConfig(Config):
    """
    生产环境的配置
    """
    DEBUG = False
    COLLECTION = "carer_db"
    USER = "carer"
    PASSWORD = "carernb123"
    HOST = "134.175.100.199"
    PORT = 27017
    DESCRIPTION = "ProductionConfig"






envs = {
    "development": DevelopConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig
}
