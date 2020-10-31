# use list
# find all positive divisors of a positive integer from its prime
# factorization

def Main():
    # prime_fact = [2, 2, 5]
    prime_fact = [2, 2, 2, 3]

    answer = []

    num = 1

    length = len(prime_fact)
    divisor = 0

    for i in range(length):
        num = num * prime_fact[i]

    count = 0
    for j in range(length):
        temp = num
        for k in range(count, length):
            divisor = int(temp / prime_fact[k])
            if divisor not in answer:
                answer.append(divisor)
            temp = divisor
        count = count + 1

    answer.append(num)

    answer.sort()
    print(answer)


Main()
