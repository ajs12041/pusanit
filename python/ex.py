jumsu = [80, 75, 55]
total = 0
for i in jumsu:
    total = total + i
avg = total / len(jumsu)
print(f"평균은 {avg}점 입니다")


print((80+75+55)/3)

pin = "881120-1068234"
if pin[7] == "1":
    print("남자")
else:
    print("여자")


## 5
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

## 6
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

a = ['life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

a = (1, 2, 3)
a
(1, 2, 3)
a = a +(4,)
print(a)


a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

