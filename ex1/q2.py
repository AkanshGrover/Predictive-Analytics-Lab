int_num = 10
float_num = 5.6
string_ip1 = "Predictive Analytics Lab"
string_ip2 = "Experiment 1"
bool_1 = True
bool_2 = False
sum = int_num + float_num
diff = int_num - float_num
product = int_num * float_num
quotient = int_num / float_num
mod = int_num % float_num
string_concat = string_ip1 + " " + string_ip2
and_oper = bool_1 and bool_2
or_oper = bool_1 or bool_2
not_oper = not bool_2
print("Basic arithmetic operations:")
print(f"Sum of {int_num} and {float_num} is {sum}")
print(f"Difference of {int_num} and {float_num} is {diff}")
print(f"Product of {int_num} and {float_num} is {product}")
print(f"Quotient of {int_num} and {float_num} is {quotient}")
print(f"Modulus of {int_num} and {float_num} is {mod}")
print("\nConcatenating string using +: ")
print(f"Concatenation of \"{string_ip1}\" and \"{string_ip2}\" is \"{string_concat}\"")
print("\nUsing logical operators to evaluate boolean expressions:")
print(f"{bool_1} and {bool_2} is {and_oper}")
print(f"{bool_1} or {bool_2} is {or_oper}")
print(f"Not {bool_1} is {not_oper}")