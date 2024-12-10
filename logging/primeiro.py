import logging


logging.basicConfig(
    filename='myapp.log',
    # filemode='w',
    format='%(asctime)s %(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.DEBUG
)

logging.warning('is when this event was logged.')
