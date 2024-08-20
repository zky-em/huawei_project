import sys

def add_numbers(numbers):
    total = sum(numbers)
    return total

def minus_numbers(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply_numbers(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result *= num
    return result

def divide_numbers(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result /= num
    return result

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = [float(line.strip()) for line in file]
    return numbers

def main():
    if len(sys.argv) != 3:
        print("使用示例：cal -add/-minus/-multiply/-divide filename")
        return

    command = sys.argv[1]
    filename = sys.argv[2]

    if command == "-add":
        numbers = read_numbers_from_file(filename)
        result = add_numbers(numbers)
        print("加法计算结果：", result)
    elif command == "-minus":
        numbers = read_numbers_from_file(filename)
        result = minus_numbers(numbers)
        print("减法计算结果：", result)
    elif command == "-multiply":
        numbers = read_numbers_from_file(filename)
        result = multiply_numbers(numbers)
        print("减法计算结果：", result)
    elif command == "-divide":
        numbers = read_numbers_from_file(filename)
        result = divide_numbers(numbers)
        print("减法计算结果：", result)
    else:
        print("无效的命令")

if __name__ == "__main__":
    main()
