def prime_check(number):
  is_prime=True
  for i in range(2,number-1):
    if number%i==0:
      is_prime=False
  if is_prime:
    print(f" {number} Is Prime Number")
  else:
    print("Not a Prime  Number")
n=int(input("Enter the Number="))
prime_check(number=n)