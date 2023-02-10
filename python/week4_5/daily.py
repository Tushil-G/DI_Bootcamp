
get_user_input=input("Enter words seperated by commas(,): ")
x= [word for word in get_user_input.split(",")]
print(",".join(sorted(list(set(x)))))

