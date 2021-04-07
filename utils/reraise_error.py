from typing import List, Type


def raise_exception_if_error_in(current_exception: Exception,
                                exceptions_to_check: List[Type[Exception]],
                                new_error: Type[Exception]):
    for exception_type in exceptions_to_check:
        if type(current_exception) == exception_type:
            raise new_error(str(current_exception))
    else:
        raise current_exception


def re_raise_error(old_errors: List[Type[Exception]], new_error: Type[Exception]):
    def decorator(function):
        def decorated_function(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except Exception as error:
                raise_exception_if_error_in(current_exception=error,
                                            exceptions_to_check=old_errors,
                                            new_error=new_error)
        return decorated_function

    return decorator


@re_raise_error(old_errors=[KeyError, IndexError], new_error=IndexError)
def test(a, b, c=6):
    print(a, b, c)
    raise KeyError('op')
