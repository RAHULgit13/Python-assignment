class MyMath:
    def calculate(self, op_name, n):

        if op_name == "sum":
            result = n * (n + 1) // 2
            print("Sum of first", n, "natural numbers:", result)

        elif op_name == "prime":
            num = 2         
            count = 0         

            print("First", n, "prime numbers:", end=" ")
            while count < n:
                is_prime = True
                for i in range(2, num):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    print(num, end=" ")  
                    count += 1
                num += 1
            print() 

        elif op_name == "fibonacci":
            a, b = 0, 1
            print("Fibonacci series:")
            for i in range(n):
                print(a, end=" ")
                a, b = b, a + b
            print()

        elif op_name == "factorial":
            fact = 1
            for i in range(1, n + 1):
                fact *= i
            print("Factorial of", n, "is:", fact)

        else:
            print("Invalid operation")

math_obj = MyMath()

print("Operations: sum, prime, fibonacci, factorial")
user_op = input("Enter operation name: ")
user_n = int(input("Enter value of n: "))
math_obj.calculate(user_op, user_n)
