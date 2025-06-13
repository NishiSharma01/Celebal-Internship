# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

x = int(input())
shoe_sizes = list(map(int, input().split()))

shoe_count = Counter(shoe_sizes)
n = int(input())

total_money = 0

for _ in range(n):
    size, price = map(int, input().split())
    if shoe_count[size] > 0:
        total_money += price
        shoe_count[size] -= 1  

print(total_money)
