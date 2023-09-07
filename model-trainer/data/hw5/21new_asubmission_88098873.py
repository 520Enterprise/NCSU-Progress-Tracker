def hailstone(start):
  integer = start
  num_int = 1
  print(integer, end = ',')
  while integer > 1:
    if integer % 2 == 1:
      integer = int(integer*3 + 1)
      print(integer, end = ',')
      num_int = num_int + 1
    if integer % 2 == 0:
      integer = int(integer / 2)
      if integer != 1:
        print(integer, end = ',')
      if integer == 1:
        print(integer)
      num_int = num_int + 1
  return num_int
def main():
    hailstone(18)
if __name__ == '__main__':
    main()
#@#