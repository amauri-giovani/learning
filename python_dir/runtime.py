import threading
from time import perf_counter, sleep


class Runtime:
    lista = []
    def stopwatch_start(self):
        self.start_of_count = perf_counter()

    def stopwatch_end(self):
        self.end_of_count = perf_counter()

    def check_runtime(self):
        self.stopwatch = self.end_of_count - self.start_of_count
        while not self.stopwatch > 2:
            sleep(1)
        # else:

    def soma(self):
        thread_start = threading.Thread(target=self.stopwatch_start())
        # thread_end = threading.Thread(target=self.stopwatch_end())
        # thread_start.start()
        start_of_count = perf_counter()
        end_of_count = 0
        for num in range(10000):
            self.lista.append(num + 1)
            sleep(0.3)
            end_of_count = perf_counter()
            # self.stopwatch_end()
        runtime = end_of_count - start_of_count
        # return [(num + 1) for num in range(10000)]
        # return x + y
