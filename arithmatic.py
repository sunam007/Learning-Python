# python-v3 , three number types: int , floats , complex
# python uses "j" as the sqr root of -1
# Four types of arithmetic operations + - * /

# to convert an int to float just add a .0 or use  constructor float(int_num)
int_num = 230
print("type of" , int_num , "is" , type(int_num))

float_num = float(int_num)
print("type of" , float_num , "is" , type(float_num))

# integer number can be converted to float type
# if we convert float number to integer it only gives the rounded integer

# ints are narrower than floats
# floats are wider than ints

PI = 3.14
converted_num = int(PI)
print("after converting from float to integers ", converted_num)

# to cnvert a float to complex number add + 0j or use constructor complex()
# can not convert a complex number into a float
converted_complex = complex(PI)
print("converted from float to complex" , converted_complex)

# floats are narrower than complex
# complex are wider than floats

# Rule of thumb: when combining numbers of different types , python will converts the narrower type to the wider types and then perform arithmatic operations

num_a = 1 # int
num_b = 2.5 # float
num_c = 2 + 3j # complex

# Addition
add = num_a + num_b # int + float ; int is the narrower type; int will first converts to float
print("addition int+float:" , add)

add2 = num_b + num_c # float + complex ; float is the narrower type; float will first converts to float
print("addition float+complex:" , add2)

# Division
# In python v3 Division always returns float even if there is no remainder, division by zero will return
# the % operator returns the remainder value; to get the quotient use double forward slash //

division = 12/5 # 1.5
remainder = 12%5 # 2
quotient = 12//5 # 2

print ("division >>" , division)
print ("remainder >>" , remainder)
print ("quotient >>" , quotient)