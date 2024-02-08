"""
Write a class called Timer that calculates the execution time of a code block.
The class should have the following methods:

- __enter__(self): magic method that starts the timer;
- __exit__(self, exc_type, exc_val, exc_tb): magic method that stops the timer
and prints the execution time of the code block.
"""
from time import perf_counter


class Timer:
    def __enter__(self):
        """ Magic method that starts the timer.  """
        self.start_time = perf_counter()
        return self  # Returns self to allow use within 'with' statement

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Magic method that stops the timer and prints the execution time of the code block. """
        end_time = perf_counter()
        self.elapsed_time = end_time - self.start_time
        # Code for testing the class
        print(f"Execution time: {timer.elapsed_time:.4f} Seconds")  # printing 'time_elapesd' here for imediate answer


with Timer() as timer:
    for i in range(1000000):
        pass

# Code for testing the class
# print(f"Execution time: {timer.elapsed_time:.4f} Seconds")
