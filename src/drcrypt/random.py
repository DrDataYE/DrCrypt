import time

class Random:
    def __init__(self, seed=None):
        if seed is None:
            seed = int(time.time() * 1000)

        self.seed = seed
        self.state = seed

    def random(self):
        self.state = (self.state * 1103515245 + 12345) & 0xFFFFFFFF
        return self.state

    def randint(self, start, end):
        return start + self.random() % (end - start + 1)

    def randstr(self, length, characters):
        result = []
    
        for _ in range(length):
            result.append(characters[self.randint(0, len(characters) - 1)])
        
        return ''.join(result)
