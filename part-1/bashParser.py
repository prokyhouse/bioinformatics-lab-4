import sys

target_line = 4
val_pos = 4


def parser(file):
  lines = f.readlines()
  splitted = lines[target_line].split(" ")
  val = splitted[val_pos]
  result = val[1:-1]
  if float(result) > 90.0:
    print("GOOD")
  else:
    print("FAIL")


if __name__ == '__main__':
    name = sys.argv[1]
    f = open(name, 'r')
    parser(f)

