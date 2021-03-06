__author__ = 'Aseem'
__name__ = '0001-0050'

#Most of these are in functions directory
import calendar
import combinatorics
import common
import files
import lcm
import math
import primes
import series
import sys
import utils_ab
from numbers_ab import *

from fractions import Fraction
from itertools import count, islice, permutations, product


RESOURCES = 'Resources'


def prob_001():
    return series.sum_multiples_upto((3, 5), 1000)


def prob_002():
    return sum(b for b in series.fibonacci(1, 2, 4000000)
               if b % 2 == 0)


def prob_003():
    return primes.largest_prime_factor(600851475143)


def prob_004():
    largest = 0
    for i in range(100, 1000):
        for j in range(i + 1, 1000):
            num = i * j
            if num > largest and is_palindrome(num):
                largest = num
    return largest


def prob_005():
    return lcm.lcm_of_range(1, 21)


def prob_006():
    return series.sum_numbers(100) ** 2 - series.sum_squares(100)


def prob_007():
    return primes.nth_prime(10001)


def prob_008():
    number_str = ''.join(files.get_lines(RESOURCES, '008.txt'))

    consecutive = 5
    return max(product_digits(number_str[i: i + consecutive])
               for i in range(len(number_str) - consecutive))


def prob_009():
    for c in range(1, 997):
        c_square = c * c
        for b in range(1, c):
            a = 1000 - b - c
            if a * a + b * b == c_square and b > a > 0:
                return a * b * c


def prob_010():
    return sum(primes.primes_list(2000000))


def prob_012():
    for num in count(1):
        cur_tri_num = triangle_num(num)
        div = num_of_divisors(cur_tri_num)
        if div > 500:
            return cur_tri_num


def prob_013():
    total = sum(int(line)
                for line in files.get_lines(RESOURCES, '013.txt'))
    return str(total)[:10]


def prob_014():
    recursion_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(recursion_limit * 10)
    longest = 1
    longest_num = 1
    for i in range(1, 1000000):
        current = series.len_collatz(i)
        if current > longest:
            longest = current
            longest_num = i
    sys.setrecursionlimit(recursion_limit)
    return longest_num


def prob_015():
    return combinatorics.combinations(40, 20)


def prob_016():
    num = str(2 ** 1000)
    return sum(int(i) for i in num)


def prob_018():
    return common.max_path_sum_tri_file(RESOURCES, "018.txt")


def prob_019():
    ans = 0
    for month in range(1, 13):
        for year in range(1901, 2001):
            if calendar.monthrange(year, month)[0] == 6:
                ans += 1
    return ans


def prob_020():
    return sum(int(i) for i in str(math.factorial(100)))


def prob_021():
    #TODO Refactor Maybe
    sums = [sum_proper_divisors(i) for i in range(10000)]

    total = 0
    for i in range(10000):
        b = sums[i]

        if b >= 10000 or b == i:
            continue
        if sums[b] == i:
            total += i
    return total


def prob_022():
    names = files.get_line(RESOURCES, '022.txt', split_option=',')
    names.sort()

    scores = 0
    for i in range(len(names)):
        score = 0
        for c in names[i][1:-1]:
            score += ord(c) - ord('A') + 1
        scores += (score * (i + 1))
    return scores


def prob_023():
    listt = []
    total = 0
    for i in range(1, 28124):
        listt.append(i < sum_proper_divisors(i))

        for j in range(1, i):
            if listt[j - 1] and listt[i - j - 1]:
                break
        else:
            total += i
    return total


def prob_024():
    for cur_per in islice(permutations("0123456789"), 999999, 999999 + 1):
        return utils_ab.iterable_to_int(cur_per)


def prob_025():
    for b, i in zip(series.fibonacci(1, 1), count(2)):
        if len(str(b)) > 999:
            return i


def prob_028():
    #To do this I derived the formula for sum of corners in n x n spiral
    #It's easy to find the pattern if you consider the outer ring only in spiral
    def sum_of_outer_ring(n):
        return 4*(n*n) - 6 * (n - 1)
    return 1 + sum(sum_of_outer_ring(i) for i in range(3, 1002, 2))


def prob_029():
    return len({pow(a, b)
                for a in range(2, 101)
                for b in range(2, 101)}
               )


def prob_033():
    ans = Fraction(1, 1)
    for num, den in product(range(10, 100), repeat=2):
        if num >= den:
            continue

        num_list = [i for i in str(num)]
        den_list = [i for i in str(den)]
        temp_list = [i for i in num_list if i in den_list]

        if len(temp_list) != 1 or '0' in temp_list:
            continue

        num_list.remove(temp_list[0])
        den_list.remove(temp_list[0])

        num2 = int(num_list[0])
        den2 = int(den_list[0])

        if not(num2 and den2):
            continue

        if Fraction(num, den) == Fraction(num2, den2):
            ans *= Fraction(num, den)

    return ans.denominator


def prob_035():
    return(4 + sum(primes.is_circular_prime(i, len(str(i)))
                   for i in range(11, 1000000, 2)))


def prob_036():
    return sum(i for i in range(1, 1000000)
               if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]))


def prob_039():
    maximum = 0
    maximum_p = 3
    for param in range(3, 1001):
        cur = 0
        for a in range(1, param-1):
            #This equation can be obtained by solving the two given equations
            b = (param * (param - 2 * a))/(2.0 * (param - a))
            if b != int(b):
                continue
            c = param - a - b
            if c <= 0:
                break
            if a*a + b*b == c*c:
                cur += 1
        else:
            if cur > maximum:
                maximum = cur
                maximum_p = param
    return maximum_p


def prob_040():
    s = ''
    for i in count(1):
        s += str(i)
        if len(s) >= 1000000:
            break

    total = 1
    for i in range(7):
        total *= int(s[10 ** i - 1])

    return total


def prob_041():
    largest = 0
    for i in range(1, 9):
        for j in permutations(range(1, i + 1)):
            temp = utils_ab.iterable_to_int(j)
            if temp > largest and primes.is_prime(temp):
                largest = temp

    return largest


def prob_042():
    words = files.get_line(RESOURCES, "042.txt", split_option=',')
    triangles = 0
    for word in words:
        value = sum((ord(c) - ord('A') + 1)
                    for c in word[1:-1])
        if is_triangle_num(value):
            triangles += 1
    return triangles


def prob_043():
    from utils_ab import iterable_to_int as converter
    total = 0
    divisors = [2, 3, 5, 7, 11, 13, 17]
    for cur_per in permutations(range(10)):
        if cur_per[0] == 0:
            continue

        for j in range(7, 0, -1):
            if converter(cur_per[j:j + 3]) % divisors[j - 1] != 0:
                break
        else:
            total += converter(cur_per)
    return total


def prob_045():
    for i in count(286):
        tri_num = triangle_num(i)
        if is_pentagonal_num(tri_num) and is_hexagonal_num(tri_num):
            return tri_num


def prob_046():
    #TODO Refactor
    for i in count(9, 2):
        if primes.is_prime(i):
            continue
        for j in count(1):
            temp = i - 2 * j ** 2
            if temp < 0:
                return i
            if primes.is_prime(temp):
                break


def prob_047():
    nums = 0
    for i in count(1):
        if primes.num_distinct_prime_factors(i) == 4:
            nums += 1
            if nums == 4:
                return i - 3
        else:
            nums = 0


def prob_048():
    return str(sum(i ** i for i in range(1, 1001)))[-10:]

if __name__ == "0001-0050":
    common.run_all(__name__)