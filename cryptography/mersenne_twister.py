# https://en.wikipedia.org/wiki/Mersenne_Twister

class MersenneTwister:
    def __init__(self, seed):
        self.seed = seed
        self.w = 32
        self.f = 1812433253
        self.m = 397
        self.n = 624
        self.state = [0] * self.n
        self.upper_mask = 0x80000000 # 2**31
        self.lower_mask = 0x7fffffff # 2**31 - 1
        self.index = self.n
        self.matrix_a = 0x9908b0df
        self.int_32 = lambda number: int(number & 0xFFFFFFFF)
        self.set_state()

    def set_state(self):
        self.state[0] = self.seed
        f = self.f
        w = self.w

        for i in range(1, self.n):
            self.state[i] = self.int_32(f * (self.state[i-1] ^ (self.state[i-1] >> (w - 2))) + i)

    def generate_rand_int(self):
        N = self.n
        M = self.m
        mag01 = [0x0, self.matrix_a]
        y = 0

        if self.index >= N:
            # generate N words at one time
            k = 0
            for i in range(N-M):
                y = (self.state[i] & self.upper_mask) | (self.state[i + 1] & self.lower_mask)
                self.state[i] = self.state[i + M] ^ (y >> 1) ^ mag01[y & 0x1]
                k = i

            for j in range(k, N - 1, 1):
                y = (self.state[j] & self.upper_mask) | (self.state[j + 1] & self.lower_mask)
                self.state[j] = self.state[j + (M - N)] ^ (y >> 1) ^ mag01[y & 0x1]

            y = (self.state[N - 1] & self.upper_mask) | (self.state[0] & self.lower_mask)
            self.state[N - 1] = self.state[M - 1] ^ (y >> 1) ^ mag01[y & 0x1]
            self.index = 0

        y = self.state[self.index]
        y ^= (y >> 11)
        y ^= (y << 7) & 0x9d2c5680
        y ^= (y << 15) & 0xefc60000
        y ^= (y >> 18)
        self.index += 1
        return self.int_32(y)
