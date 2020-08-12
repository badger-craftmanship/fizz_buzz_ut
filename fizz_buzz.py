def is_fizz(number):
  return number % 3 == 0

def is_buzz(number):
  return  number % 5 == 0

def fizzBuzzString(x):
  fizz = is_fizz(x)
  buzz = is_buzz(x)
  if fizz and buzz:
    return "FizzBuzz"
  elif fizz and not buzz:
    return "Fizz"
  elif not fizz and buzz:
    return "Buzz"
  else:
    return x

if __name__ == "__main__":
  for x in range(101):
    print(fizzBuzzString(x))
