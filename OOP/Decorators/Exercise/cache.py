# def cache(func):
#
#     def wrapper(num):
#         if num not in wrapper.log:
#             wrapper.log[num] = func(num)
#
#         return wrapper.log[num]
#
#     wrapper.log = {}
#
#     return wrapper
#
#
# @cache
# def fibonacci(n):
#     if n < 2:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# fibonacci()
# print(fibonacci.log)

def cache(func):
    def wrapper(n):
        cache_key = n
        if cache_key not in wrapper.log:
            wrapper.log[cache_key] = func(n)
        return wrapper.log[cache_key]

    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):

    if n < 2:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


