import inspect
import sys


def introspection_info(obj):
    obj_dir = dir(obj)
    obj_type = type(obj).__name__
    attributes = [attr for attr in obj_dir if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    methods = [method for method in obj_dir if callable(getattr(obj, method)) and not method.startswith("__")]
    module_info = inspect.getmodule(obj)
    module = module_info.__name__ if module_info else None
    size = sys.getsizeof(obj)
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
        'size': size
    }

    return info


string_info = introspection_info('test')
print(string_info)
