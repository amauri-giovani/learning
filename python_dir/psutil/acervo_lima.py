# importing libraries
import os
import psutil


def convert_value(value):
    # measurement_units = ['bytes', 'kilobytes', 'megabytes', 'gigabytes', 'terabytes', 'petabytes']
    # measurement_units = ['B (bytes)', 'KB (kilobytes)', 'MB (megabytes)', 'GB (gigabytes)', 'TB (terabytes)', 'PB (petabytes)']
    measurement_units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']

    base_size = 1024  # Base for unit conversion

    for unit in measurement_units:
        if value < base_size or unit == measurement_units[-1]:
            return f"{value: .2f} {unit}"
        value /= base_size


# inner psutil function
def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss


# decorator function
def profile(func):
    def wrapper(*args, **kwargs):
        mem_before = process_memory()
        result = func(*args, **kwargs)
        mem_after = process_memory()
        print("mem_before =", convert_value(mem_before))
        print("mem_after =", convert_value(mem_after))
        print("mem_after - mem_before =", convert_value(mem_after - mem_before))
        print("{}:consumed memory: {:,}".format(
            func.__name__,
            mem_before, mem_after, mem_after - mem_before))
        # print("{}:consumed memory: {:,}".format(
        #     func.__name__,
        #     convert_value(mem_before), convert_value(mem_after), convert_value(mem_after - mem_before)))

        return result

    return wrapper


# instantiation of decorator function
@profile
# main code for which
# memory has to be monitored
def func():
    x = [1] * (10 ** 7)
    y = [2] * (4 * 10 ** 8)
    del x
    return y


func()