# Boolean Type has two values
True # T is capital, uncapitalized true will return errors
False # F is capital, uncapitalized false will return errors

type(True) # <class 'bool'>
type(False) # <class 'bool'>

bool(28) # True
bool(2.34) # True
bool(-3) # True

bool(0) # False
bool("") # False
bool(" ") # True

# trivial values are converted to False
# non-trivial values are converted to True

int(True) # 1
int(False) # 0

sum = 5 + True # sume = 6
multiplication = 10 * False  # multiplication  = 0

# Python trats 1 as True and 0 as False and vice-versa