def repeat_me(func):
    def wraper(*args, count):
        for i in range(count):
            results = func(*args)

        return results
    return wraper


@repeat_me
def example(text):
    print(text)


example('print me', count=5)
