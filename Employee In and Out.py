class Employee:
    def __init__(self):
        print("Employee Created")
    def __del__(self):
        print("Destructor Called")
def Create_obj():
    obj = Employee()
    print("function end...")
    return obj
print("Calling Create_obj() function...")
obj = Create_obj()
print("Program End...")