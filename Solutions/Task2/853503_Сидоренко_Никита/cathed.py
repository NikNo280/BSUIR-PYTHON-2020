def cached(func):
    old_args = {}
    def wrapper(*args, **kwargs):
        if old_args.get(args):
            return old_args[args]
        else:
            old_args.update({args : func(*args, **kwargs)})
            return old_args[args]

    return wrapper


@cached
def add(a, b):
    return a + b
