class MyCounter:
    count = 1

    @classmethod
    def increment_count(cls):
        cls.count += 1
        return cls.count