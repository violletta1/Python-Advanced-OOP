def repeat_n_times(n):
    def decorator(func):
        def wrapper(*args):
            for _ in range(n):
                func(*args)

        return wrapper

    return decorator


a = 5

@repeat_n_times(2)
@repeat_n_times(5)
def hello(name):
    print(f"Hello, {name}")


hello("Alice")