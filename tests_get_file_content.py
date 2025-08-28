from functions.get_file_content import get_file_content

def tests():
    result = get_file_content("calculator", "lorem.txt")
    print("Result for lorem.txt:")
    print(result)
    print("")
    



if __name__ == "__main__":
    tests()