import inspect
from functools import wraps


def strict(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_data = inspect.signature(func)
        params_data = func_data.parameters
        arg_value_map = func_data.bind(*args, **kwargs).arguments
        return_annotation = func_data.return_annotation
        if isinstance(return_annotation, func_data.empty):
            raise TypeError('Strict decorator requires return annotation.')

        for name, value in arg_value_map.items():
            param_data = params_data.get(name)

            if isinstance(value, param_data.empty):
                raise TypeError('Strict decorator requires annotations.')
            if not isinstance(value, param_data.annotation):
                raise TypeError('Argument type must match annotation.')

        result = func(*args, **kwargs)

        if not isinstance(result, return_annotation):
            raise TypeError('Return type must match annotation.')

        return result

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def sum_str(s1: str, s2: str, s3: str) -> str:
    return s1 + s2 + s3


@strict
def no_return_annotation(a: str):
    return a


@strict
def no_params_annotation(a, b) -> str:
    return a + b


@strict
def bad_return_annotation(a: int, b: int) -> str:
    return a + b
