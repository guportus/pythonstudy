# Netacad exercise 4.3.1.9
# Check if the number is a prime number or not

def is_prime(num):

    flag = True
    for i in range(2, num):
        if(num % i) == 0:
            flag = False
            break

    return flag

for i in range(1, 200):
	if is_prime(i + 1):
			print(i + 1, end=" ")


