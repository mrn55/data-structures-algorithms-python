class RateLimiter:
    def __init__(self, capacity: int, rate: int, interval: int):
        self.capacity = capacity
        self.rate = rate
        self.interval = interval
        self.tokens = capacity
        self.last_checked = 0

    def allow_request(self, timestamp: int) -> bool:
        # 1. Refill tokens based on time passed (before we process the request)
        elapsed = timestamp - self.last_checked
        if elapsed >= self.interval:
            intervals_passed = elapsed // self.interval
            self.tokens = min(
                self.capacity,
                self.tokens + intervals_passed * self.rate
            )

        # 2. Allow request if a token is available
        if self.tokens > 0:
            self.tokens -= 1
            self.last_checked = timestamp  # Update last checked time to current timestamp
            return True

        return False


rl = RateLimiter(capacity=5, rate=1, interval=10)
for t in [0, 1, 2, 3, 4, 5, 10, 20, 21, 22]:
    print(f"t={t}: {rl.allow_request(t)}")