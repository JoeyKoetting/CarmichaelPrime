import random
import math

################################################################################
# prime_test
# Returns one of three values: 'prime', 'composite', or 'carmichael'
def prime_test (N, k):

    # Gets a collection of random numbers from range 1 <= a < N
    random_sample = random.sample(range(1, N - 1), k)

    # Tests each Random number based on algorithm in book
    # If fails, then number is composite
    for random_number in random_sample:
        if mod_exp(random_number, N - 1, N) != 1:
            return 'composite'

    # A carmichael number may fool the fermat test
    # If it is a carmichael number this will check
    if is_carmichael(N, N - 1, random.randint(1, N - 2)):
        return 'carmichael'

    # Fits definition of a prime number.
    return 'prime'

################################################################################
# mod_exp
# Performs high number exponential modding
# TIME COMPLEXITY TOTAL: ((n + 2 ^ m) * k where k is the number why which y / 2^k
# # in which k makes y zero)
# y / 2 : Right Shifts, O(n)
# z ** 2 : Exponent, O(2 ^ m)
# SPACE COMPLEXITY
# y / 2 : Right Shifts, Uses one less bit
# z ** 2 : Left Shifts, Uses one more bit
def mod_exp (x, y, N):
    if y == 0:
        return 1

    z = mod_exp(x, math.floor(y / 2), N)

    # y is even
    if y % 2 == 0:
        return (z ** 2) % N
    # y is odd
    else:
        return (x * (z ** 2)) % N

################################################################################
# probability
# Returns the possibility of a number being prime after 'k' checks
# TIME COMPLEXITY TOTAL : O(n + 2 ^ m)
# 2 ** k : Exponent, O(2 ^ m)
# 1 / (.....) : 1 / a number, Division, O(n)
# SPACE COMPLEXITY
# 2 ** k : Adds one bit to number by k times
# 1 / (.....) : Right Shifts, Uses one less bit
# DESCRIPTION:
# A prime diagnosis using Fermats theorem guarantees a 50% chance of being actually true.
# Therefore if we perform the Algorithim additional times we can decrease the chance by
# an additional 50% of the previous prime validity percentage.
# for example 1/2 -> 1/4 -> 1/8, Decreases 50% of the previous value
def probability (k):
    return 1 / (2 ** k)

################################################################################
# is_carmichael
# Determines whether a number is a carmichael or not
# TIME COMPLEXITY TOTAL: O((n + 1) * k, where k is the number why which N / 2^k
# in which k makes N zero or odd)
# tempN % 2 : Checks last bit, O(1)
# tempN / 2 : Right Shifts, O(n)
# SPACE COMPLEXITY
# tempN / 2 : Right Shifts, Uses one less bit

def is_carmichael (N, tempN, a):

    # This will hold for a prime number but not for a carmichael number
    x = mod_exp(a, tempN, N)
    if x != 1 and x != N - 1:
        return True

    # if tempN is divisible by two continue checking the square roots
    # of the the exponent to further check
    if tempN % 2 == 0:
        return is_carmichael(N, tempN / 2, a)

    return False
