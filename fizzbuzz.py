# input() -> n
# 1 to n,
# 3의 배수, "fizz"
# 5의 배수, "buzz"
# 15의 배수, "fizzbuzz"
# 나머지, 그 숫자를 출력하시오

#value = int(input("insert number:"))

#for i in range(1, value+1):

#    if i % 15 == 0:
#        print("fizzbuzz")
	
#    elif i % 3 == 0:
#        print("fizz")
	
#    elif i % 5 == 0:
#        print("buzz")
	
#    else:
#        print("i")

value = int(input("insert number:"))
result = [
    str(num) + ":fizzbuzz" if num % 15 == 0 else str(num) + ":i"
    for num in range(1, value+1)
]
print(result)
