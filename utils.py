def print_time(f):
    import time

    def inner(*args, **kwargs):
        start = time.time()
        val = f(*args, **kwargs)
        print(f"{f.__name__} --Took {time.time() - start} secs--")
        return val

    return inner