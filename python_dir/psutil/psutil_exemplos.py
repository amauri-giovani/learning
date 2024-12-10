from pprint import pprint

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


memory_used_before = psutil.virtual_memory().used
memory_percent_before = psutil.virtual_memory().percent
memory_before = {"Total": convert_value(memory_used_before), "Percent": f"{memory_percent_before} %"}

execution = list(range(10_000_000))

memory_used_after = psutil.virtual_memory().used
memory_percent_after = psutil.virtual_memory().percent
memory_after = {"Total": convert_value(memory_used_after), "Percent": f"{memory_percent_after} %"}

memory_used = convert_value(memory_used_after - memory_used_before)
memory_percent = f"{round(memory_percent_after) - round(memory_percent_before): .2f} %"
memory_total = {
    "Memory Before": memory_before,
    "Memory After": memory_after,
    "Memory used in execution": {
        "Total": memory_used,
        "Percent": memory_percent
    }
}
pprint(memory_total)
