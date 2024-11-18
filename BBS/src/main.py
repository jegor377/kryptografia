import sympy
import random
import math

from gen_tests import *


# szukaj liczby relatywnie pierwszej tak długo aż się uda.
# ponieważ p * q daje ogromną liczbę przy założeniu, że p i q są liczbami 4-cyfrowymi
# to znalezienie takiej liczby powinno być bardzo łatwe i szybkie
def next_random_coprime_of(n):
    if n == 0 or n == 1:
        raise ValueError("Cannot find coprime of 0 or 1.")
    while True:
        random_coprime = random.randint(1, n - 1)
        while math.gcd(random_coprime, n) != 1 and random_coprime < n:
            random_coprime += 1
        if random_coprime != n:
            return random_coprime


def create_generator_seed() -> int:
    primes = sympy.primerange(1_000, 10_000)
    congruent_primes = [prime for prime in primes if prime % 4 == 3]
    p, q = random.sample(congruent_primes, 2)
    N = p * q
    x = next_random_coprime_of(N)
    x0 = pow(x, 2, N)
    return x0, N


def next_random(xi: int, N: int) -> int:
    return pow(xi, 2, N)


def calc_bits(count: int) -> list[int]:
    x0, N = create_generator_seed()
    bits = []
    xi = x0
    for _ in range(count):
        xi = next_random(xi, N)
        bits.append(xi & 1)
    return bits


if __name__ == '__main__':
    S = calc_bits(20_000)
    (
        seq_counts_zero,
        seq_counts_one,
        seq_counts_zero_capped,
        _
    ) = calc_sequences(S)
    
    test_result("Test pojedynczych bitów", single_bit_test(S))
    test_result("Test serii", sequence_test(seq_counts_zero_capped))
    test_result("Test długiej serii", long_sequence_test(
        seq_counts_zero, seq_counts_one))
    test_result("Test pokerowy", poker_test(S))