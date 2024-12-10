import logging


class ConfigLog:
    def __init__(self, filename):
        self.filename = filename

    def config(self):
        logging.basicConfig(
            filename=self.filename,
            format='%(asctime)s  %(message)s',
            datefmt='%m/%d/%Y %H:%M:%S',
            level=logging.DEBUG
        )
