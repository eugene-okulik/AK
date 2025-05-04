def repeat_me(func, count):
    def wrapper(*args, count):
        func(*args, count)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
