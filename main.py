# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



            #module 3_5
            # "Рекурсия"

def get_multiplied_digits(number):
      str_number = str(number)
      first = int(str_number[0])
      if len(str_number) > 1:
          return first * get_multiplied_digits(int(str_number[1:]))
      else:
          return first

result = get_multiplied_digits(40203)
print(result)
result = get_multiplied_digits(85)
print(result)