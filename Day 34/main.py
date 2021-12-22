# type hints
# specify the data type to be fixed (avoid dynamic typing)
age: int
name: str
height: float
is_human: bool

# : fixed the input data type
# -> fixed the output data type
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False

    return can_drive


# the : helps to find out, before execute pgm, if input has type error with parm, the input will blink to notify
# police_check("twelve")

print(police_check(12))
