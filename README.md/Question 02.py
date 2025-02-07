
# Question 02: File reading with Exception Handling

#Write a function that reads the contents of a file named 'data.txt'.Use try,except,and finally
#block to handle file not found reeors and ensures the file is properly closed.


def readData(fname):
    try:
        f = open(fname,'r')
        except FileNotFoundError:
            print("Please provide valid file name")
        else:
            data = f.read()
            print(data)
        finally:
            if f.closed() == false:
                f.close()
            else:
                print("File not even open")

fname = input("Enter File name to read:")

readData(fname)


