def finish_me(func):
    def wraper(*args):
        results = func(*args)
        print('finished')
        return results

    return wraper


@finish_me
def example(text):
    print(text)


example('print me')
