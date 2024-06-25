import random

num = random.randrange(1000, 10000)

num_str = str(num)

n = int(input("Guess the 4 digit number: "))

if n == num:
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    ctr = 0

    while n != num:
        ctr += 1

        count = 0
        correct = ['X'] * 4

        n_str = str(n)

        for i in range(4):
            if n_str[i] == num_str[i]:
                count += 1
                correct[i] = n_str[i]

        print(f"Not quite the number. But you did get {count} digit(s) correct!")
        print("Correct digits so far: ", ''.join(correct))

        n = int(input("Enter your next choice of numbers: "))

    ctr += 1
    print("You've become a Mastermind!")
    print(f"It took you only {ctr} tries.")