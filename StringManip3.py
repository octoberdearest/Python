first_name = 'Mae Rose'
last_name = 'Bibit'

fname_fletter = first_name[1]
lname_fletter = last_name[1]

fname_length = len(first_name)
lname_length = len(last_name)
fname_lletter = first_name[fname_length-1]
lname_lletter = last_name[lname_length-1]

print(f"First name first letter is {fname_fletter} and last name first letter is {lname_fletter}")
print(f"First name last letter is {fname_lletter} and last name last letter is {lname_lletter}")

new_fname = first_name[1:fname_length]
print(f"{new_fname}")