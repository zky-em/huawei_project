import sys

def add_numbers(numbers):
    return sum(numbers)

def minus_numbers(numbers):
    return numbers[0] - sum(numbers[1:])

def multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide_numbers(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result /= num
    return result

def read_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            numbers = [float(line.strip()) for line in file]
        return numbers
    except FileNotFoundError:
        print(f"文件 '{filename}' 不存在")
    except ValueError:
        print(f"文件 '{filename}' 的格式不正确")

def calculate(command, filename):
    numbers = read_numbers_from_file(filename)
    if numbers:
        if command == "-add":
            result = add_numbers(numbers)
            print("加法计算结果：", result)
        elif command == "-minus":
            result = minus_numbers(numbers)
            print("减法计算结果：", result)
        elif command == "-multiply":
            result = multiply_numbers(numbers)
            print("乘法计算结果：", result)
        elif command == "-divide":
            result = divide_numbers(numbers)
            print("除法计算结果：", result)
        else:
            print("无效的命令")

def main():
    if len(sys.argv) != 3:
        print("使用示例：cal -add/-minus/-multiply/-divide filename")
        return

    command = sys.argv[1]
    filename = sys.argv[2]
    calculate(command, filename)

if __name__ == "__main__":
    main()

