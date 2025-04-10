# lambda practice
x = lambda x : x * 2

print(x(23))

hi = lambda name : "Hello there " + name
print(hi("Alex"))

evenOrOdd = lambda y : "even" if y % 2 == 0 else "odd"
print(evenOrOdd(37))

# List Comprehensions
test = ["hello" for i in range(10)]
print(test)

listA = [1,2,3,4,5]
test = [listA[i] for i in range(len(listA))]
print(test)

listB = [[1,2,3],[4,5,6]]
test = [listB[i][j] for i in range(len(listB)) for j in range(len(listB[0]))]
print(test)

test = [("X", i) if i % 2 == 0 else ("Y", i) for i in range(10)]
print(test)

test = [("X", i) for i in range(10) if i % 2 == 0]
print(test)

test = "X" if True else "Y"
print(test)

grade = 80
reportcard = "doing well" if grade >= 70 else "not good"
print(reportcard)

# test = [("X", i) if i > 18 ("Y", i) elif i == 18 ("Z", i) if i < 18 for i in range(20)]
result = [i for i in range(20) if i % 3 == 0 and i % 5 == 0]
print(result)

result = [i for i in range(20) if i % 3 == 0 or i % 5 == 0]
print(result)  
