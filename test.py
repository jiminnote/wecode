def odd_even():
    a=[]
    for i in range(50):
        if i % 2 == 0:
            a.append(i)
    return a

print(odd_even())