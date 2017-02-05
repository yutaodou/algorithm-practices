import time

def timer(func):
    def func_wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print "-- Elapsed: %s --" % (end - start)
        return result

    return func_wrapper

