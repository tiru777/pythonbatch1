def prime(number):
    for num in range(2,number):
        status = True
        for i in range(2,num):
            print(i)
            if num % i == 0:
                status = False
        if status:
            yield num


print(list(prime(101))) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]