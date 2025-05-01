class Logger:
    def __init__(self):
        self.last_printed = {}

    def should_print_message(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise False.as_integer_ratio
        The timestamp is in seconds granularity.
        """
        if message not in self.last_printed:
            #first time seeing this message
            self.last_printed[message] = timestamp
            return True
        elif timestamp - self.last_printed[message] >= 10:
            #more than 10 seconds has passed
            self.last_printed[message] = timestamp
            return True
        else:
            #must be same timestamp as before, no print
            return False

# logger = Logger()

# print(logger.should_print_message(1, "error"))  # True
# print(logger.should_print_message(1, "error"))  # False
# print(logger.should_print_message(2, "warn"))   # True
# print(logger.should_print_message(2, "error"))  # True
# print(logger.should_print_message(2, "warn"))   # False

logger = Logger()
print(logger.should_print_message(1, "error"))   # True
print(logger.should_print_message(2, "error"))   # False
print(logger.should_print_message(11, "error"))  # True (10 seconds later)
print(logger.should_print_message(15, "warn"))   # True
print(logger.should_print_message(20, "warn"))   # True
print(logger.should_print_message(22, "warn"))   # False