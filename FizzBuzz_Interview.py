#no. is divisible by 3 fizz
#no. is divisible by 5 buzz
#no. is divisible by 15 fizzbuzz

def fizzbuzz():
    for i in range(0,101):
        if i%3==0 and i%5==0:
            print("fizzbuzz")
        elif i%3==0:
            print("buzz")
        elif i%5==0:
            print("fizz")
        else:
            print(i)

fizzbuzz()

