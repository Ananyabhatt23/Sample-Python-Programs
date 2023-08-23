from sample1pgms import *
from sample2pgms import *
from sample3 import *

assert(swap(10,20) == (20,10))

assert(checkIsPositive(2))

assert divisibilityCheck(20,4) == [4,8,12,16,20]

assert(remAndquo(10,2) == (0,5))

assert odd_num(10) == [1,3,5,7,9]

assert(sum_of_digits(123) == 6)

assert smallest_divisor(12) == 2

assert pow_of_num(2) == 6

assert avg_of_list() == 3

assert number_of_digits(123) == 3

assert palindrome_of_num(1221) == 1221

assert char_of_string_is_true("Ananya") == 1

assert occurance_of_a("ananya") == "$n$ny$"

assert vowels_inString("ananya") == 3

assert blank_spaceInString("Ana is a bee") == "Ana-is-a-bee"

assert length_of_String("Ana is a bee") == 12

assert larger_strings("Ana is a bee","Ana is a Qbee") == "Ana is a Qbee"

assert upper_lowerCase("AnAnYa") == (3,3)

assert numberLettersInString("Ana123") == (3,3)

assert lareNumInList() == 67

assert secondLargestElemInList() == 4

assert oddEvenList() == ([2,4,6],[1,3,5])

assert sameListorNot() == 1

assert UnionOfList() == ([1,2,3,4,5,6])

assert interscOfList() == ([3])

assert count_substring_occurrences("ananya","an") == 2

assert lowest_index_of_substring("ananya","an") == 0

assert uniqueList() == [2]

assert dups() == [2,3]

assert splitList([1,2,3,4,5],2) == ([[1,2],[3,4],[5]])