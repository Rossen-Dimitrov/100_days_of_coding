def format_name(first: str, last: str):

    return f"{first.title()} {last.title()}"


f_name = input("Enter your first name\n")
l_name = input("Enter your last name\n")

print(format_name(f_name, l_name))
