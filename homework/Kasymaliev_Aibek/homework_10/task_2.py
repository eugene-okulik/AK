# У меня сработало, хотя везде пишут, что не должен работатать

def repeat_me(func):
    def wrapper(*args, count):
        for _ in range(count):
            results = func(*args)

        return results
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=1)


# исправленный вариант


def repeat_me(func):
    def wrapper(*args, **kwargs):
        count = kwargs.pop('count', 1)
        for _ in range(count):
            results = func(*args)

        return results
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
