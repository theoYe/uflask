"""
RedPrint Util class
created by TheoYe on 2020-4-17
"""



class Redprint():
    def __init__(self, name):
        self.name = name
        self.mount = []

    # 路由定义
    def route(self, rule, **options):
        def decorator(f):
            self.mount.append((f, rule, options))   # 将路由加入到 mount 列表当中
            return f
        return decorator
    # 绑定蓝图

    def register(self, bp, url_prefix=None):
        if url_prefix is None:  # 如果为空, 则默认指定name 为路由前缀
            url_prefix = '/'+self.name
        for f, rule, options, in self.mount:
            endpoint = options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix+rule, endpoint, f, **options)





