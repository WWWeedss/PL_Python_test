# my_functions.py

def add(a, b):
    """可调试的加法函数"""
    print(f"Debug: add({a}, {b}) called")  # 调试信息
    return a + b

def multiply(a, b):
    """可调试的乘法函数"""
    print(f"Debug: multiply({a}, {b}) called")
    return a * b

print(add(3, 5))
print(multiply(4, 6))
