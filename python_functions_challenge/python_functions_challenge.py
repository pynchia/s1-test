import re


def list_of_integers():
  '''
  Returns a list of integers from 17 to 100 that are evenly divisible by 11.
  '''
  return [i for i in range(17, 101) if i%11==0]

# Unit tests
print(list_of_integers())


def dict_mapping():
  '''
  Returns a dictionary mapping integers to their 2.75th root for all integers
  from 2 up to 100 (including the 2.75th root of 100).
  '''
  power = 1/2.75
  return {i: pow(i,power) for i in range(2, 101)}

# Unit tests
print(dict_mapping())


def find_ips(inp):
  '''
  Returns a list of ip addresses of the form 'x.x.x.x' that are in the input
  string and are separated by at least some whitespace.
  >>> find_ips('this has one ip address 127.0.0.1')
  ['127.0.0.1']
  >>> find_ips('this has zero ip addresses 1.2.3.4.5')
  []
  '''
  ips = re.findall(r'(?:^|(?<!\.))\b(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})(?:$|(?<!\.)[^\w.])', inp)
  # Also check each ip element is below 256
  return [ip for ip in ips if all(int(el)<256 for el in ip.split("."))]
  # Note: In real life I would use python's standard library
  # e.g. socket.inet_aton(ip)


# Unit tests
print(find_ips("a.b.c.d 1.2.3.4  87.66.30.14"))
print(find_ips('this has zero ip addresses 1.2.3.4.5'))
print(find_ips("a.b.c.d 1.2.3.4  87.66.300.14"))


# Note: it is the same exercise I solved in the live session with Brandon
def check_type(type_):
  '''
  Write a function decorator that takes an argument and returns a decorator
  that can be used to check the type of the argument to a 1-argument function.
  Should raise a TypeError if the wrong argument type was passed.
  >>> @check_type(int)
  ... def test(arg):
  ... print arg
  ...
  >>> test(4)
  4
  >>> test(4.5) # raises TypeError because 4.5 isn't an int type
  '''
  def function_wrapper(fun):
    def helper(arg):
      if type(arg) == type_:
        return fun(arg)
      else:
        raise TypeError(f"Expects type {type_} but {type(arg)} passed")
    return helper
  return function_wrapper

@check_type(int)
def test(arg):
  print(arg)

# Unit tests
test(4)
test('4')
