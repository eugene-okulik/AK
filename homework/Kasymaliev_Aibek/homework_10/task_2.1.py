def repeat_me(count):
    def decorator_func(func):
        def wraper(*args):
            for i in range(count):
                func(*args)

        return wraper

    return decorator_func


@repeat_me(count=5)
def example(text):
    print(text)


example('print me')
