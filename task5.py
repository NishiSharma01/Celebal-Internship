from math import comb

# Read inputs
n = int(input())
letters = input().split()
k = int(input())

count_a = letters.count('a')
count_non_a = n - count_a


total_combinations = comb(n, k)

non_a_combinations = comb(count_non_a, k) if count_non_a >= k else 0


prob_no_a = non_a_combinations / total_combinations


prob_at_least_one_a = 1 - prob_no_a

print(f"{prob_at_least_one_a:.3f}")