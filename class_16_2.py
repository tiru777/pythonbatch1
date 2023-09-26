# file handling:
"""
we can handle files using multiple modes or methods

modes:
----------
r --> to read the file
w --> to write the file(it will override existing file data with new data),
      - it will create & override a file if not exist
a --> to add the data to existing file
r+ --> read and write
w+ --> write and read
a+ --> append and read
x --> exclusive creation(if file not there it will create, if file is there it will raise error"

variable = open("file_name",mode)
"""


# Example 1: file creation and checking
def file_handling():
    try:
        x = open("vinod.txt", "w")
        print("file_name:", x.name)
        print("mode:", x.mode)
        print("file closed or not:", x.closed)
        x.close()
        print("file closed or not:", x.closed)

    except Exception as error:
        print("error is:", error)

    finally:
        x.close()


# file_handling()

"""
# read =>r
    - read()# it will read entire data present in file
    - read(number) # it will read specfic number of charectors
    - readline()# it will read one line
    - readlines()# it will read all lines in the form list
"""


# read example and methods


def read_function(file):
    """

    :param file: text file
    :return: file data
    """
    try:
        file_data = open(file, 'r')
        # read_data = file_data.read() # it will entire file data
        # read_data = file_data.read(5)
        # read_data = file_data.readline()
        read_data = file_data.readlines()
        # for i in read_data:
        #     print(i)
        return read_data

    except FileNotFoundError:
        print(f"file not there {file}")
    except Exception as error:
        print("error is:", error)


# print(read_function('vinod.txt'))

# write
"""
write:
    - w
    - it will create file if not present and it will override
    - write("content") # 
    - writeclines() # it will add multiple lines
"""


def write_function(file):
    try:
        file_write = open(file, "w")
        file_write.write("hey i am vinod reddy")
        file_write.writelines("thirumala reddy \n hellow world \n hwllo govindha \n python course")
        print("data inserted")
    except FileNotFoundError:
        print(f"file not there {file}")


# write_function("bhargav")

# append
def append_function(file):
    try:
        file_write = open(file, "a")
        file_write.write("hey i am chanikya")
    except FileNotFoundError:
        print(f"file not there {file}")


# append_function("chanikya.txt")

# read & append
def append_read_function(file):
    try:
        with open(file, 'r') as fp:  # w+,a+
            data = fp.read()
            fp.write("\n hey i am chanikya")
            return data
    except FileNotFoundError:
        print(f"file not there {file}")


# print(append_read_function("chanikya.txt"))

# exclusive creation
# var = open("file2.txt","x")
# var.write("hellow")

# with
"""
# no need to close explicitly  by using with
with open("file_name",mode) as fp:
    fp.read()
"""
with open("chanikya.txt", 'r') as fp:
    data = fp.read()
    print(data)
