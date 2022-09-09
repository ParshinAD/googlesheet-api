def get_config():
    import os
    import importlib.util
    from importlib.machinery import SourceFileLoader

    c = os.getcwd()
    d = c.split('\\')[:] + ['config.py']
    d = '\\'.join(d)

    foo = SourceFileLoader("config.py", d).load_module()
    return foo
