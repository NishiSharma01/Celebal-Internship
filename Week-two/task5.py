def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    
    for i in range(0, n, k):
        substring = string[i:i+k]
        result = ""
        for char in substring:
            if char not in result:
                result += char
        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)