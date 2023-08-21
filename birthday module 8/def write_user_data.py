def write_user_data(name, date_str):
    with open(r'E:\PYTHON\REPOSITORY PYTHON\First_repo\birthday module 8\users.txt', 'a') as file:
        file.write(f"name: {name}, birthday: {date_str},\n")

# Input new user data
new_name = input("Enter the user's name: ")
new_date_str = input("Enter the user's birthday (YYYY. M. D): ")
write_user_data(new_name, new_date_str)

# Print the contents of the file
with open(r'E:\PYTHON\REPOSITORY PYTHON\First_repo\birthday module 8\users.txt', 'r') as file:
    contents = file.read()
    print(contents)
