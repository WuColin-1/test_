#d=1的等差数列求和
def countdown(n):
    if n==0:
        return 0
    else:
        print(n)
        countdown(n-1)
countdown(5)

#检查回文
def is_palindrome(s):
    if len(s)==0 or len(s)==1:
        return True
    elif s[0]!=s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])
s="abcba"
print(is_palindrome(s))

#阶乘
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

#逆转字符
def reverse(s):
    n=len(s)
    if n==0:
        return ""
    else:
        return str(s[-1])+str(reverse(s[0:n-1]))
print(reverse("hello"))

#斐波那契数列
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))


# 斐波那契数列（带缓存优化）
memo = {}
def fibonacci_memo(n):
    if n in memo:
        return memo[n]
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    memo[n] = result
    return result
print(fibonacci_memo(100))  # 输出 55，和 fibonacci(10) 一样，但更快

#arr求和
def sum_list(list):
    n=len(list)
    if n==0:
        return 0
    else:
        return list[-1]+sum_list(list[0:n-1])
arr=[1,2,3,4,5]
print(sum_list(arr))

#-------------------------------------------------#

#复合列表坍塌
def flatten(lst):
    arr=[]
    for i in lst:
        if isinstance(i,list):
            arr+=flatten(i)
        else:
            arr.append(i)
    return arr

arr=[[1, [2, [3, 4], 5], 6]]
print(flatten(arr))

#复合列表统计int
def count_integers(lst):
    count=0
    for i in lst:
        if isinstance(i,list):
            count+=count_integers(i)
        else:
            if type(i)==int:
                count+=1
    return count
arr=[1, [2, [3, "a"], 4], "b", [5]]
print(count_integers(arr))

#复合列表寻找最大值
def max_list(arr):
    num_max=float('-inf')
    for i in arr:
        if isinstance(i,list):
            num_max=max(num_max,max_list(i))
        elif isinstance(i,int):
            num_max=max(i,num_max)
    return num_max
arr=[1, [22, [3, 99], 4], "a", [10]]
print(max_list(arr))
#----------------------------------------------------------#

#二进制转换
def int_to_binary(n):
    if n==0:
        return "0"
    elif n==1:
        return "1"
    else:
        return int_to_binary(n//2)+str(n%2)
n=8
print(int_to_binary(n))

#digit sum
def sum_dig(n):
    if n<10:
        return n
    else:
        return sum_dig(n//10)+n%10
print(sum_dig(53546))

# 二元搜索
# import math
# def bi_search(arr,target):
#     arr_map={}
#     for i in range(len(arr)):
#         arr_map[arr[i]]=i
#     arr.sort()
#     up=len(arr)-1
#     down=0
#     if len(arr)==0:
#         return False
#     elif arr[math.ceil((up+down)/2)]==target:
#         return "你的目标在第",arr_map[math.ceil((up+down)/2)],"位"
#     elif arr[math.ceil((up+down)/2)]>target:
#         up=math.ceil((up+down)/2)
#         return bi_search(arr[down:up],target)
#     elif arr[math.ceil((up+down)/2)]<target:
#         down=math.ceil((up+down)/2)
#         return bi_search(arr[down:up],target)
# arr=[4,6,9,3,2,7]
# print(bi_search(arr,2))