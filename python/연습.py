# head = "Python"
# tail = " is fun!"
# head + tail
# print(head+tail)

# money = True
# if money:
#     print("택시를 타고 가라")
# else:
#     print("걸어 가라")

# money = 2000
# if money >= 3000:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")

# money = 2000
# card = True
# if money >= 3000 or card:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")
    
# test_list = ['one', 'two', 'three']
# for i in test_list:
#     print(i)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다" % number)
    
