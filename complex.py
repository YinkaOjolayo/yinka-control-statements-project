pass_input = input("Please enter a password: ")
special_chr_list = "!@#$%^&*()-_=+[];:'\",."
char_list = "abcdefghijklmnopqrstuvwxyz"

illegal_chr = "{}<>?/|`~"
def chr_check (password):
    sp_chr_check = 0
    low_chr_check = 0
    up_chr_check = 0
    num_check = 0
    for char in password:
        if char in char_list:
            low_chr_check = 1
        if char in char_list.upper():
            up_chr_check = 1
        if char in special_chr_list:
            sp_chr_check = 1
        if char.isdigit() == True:
            num_check = 1
        if char in illegal_chr:
            return False
    if low_chr_check == 1 and up_chr_check == 1 and sp_chr_check == 1 and num_check == 1:
            return True


count = 0
while (count != 1):
    if len(pass_input) >= 8:
        print("You password is of adequate length...")
        chr_check(pass_input)
        if chr_check(pass_input) == True:
            print("You have a strong password! Good Job!")
            count = 1
        else:
            print("Your password is still not very good")
            pass_input = input("Please enter a password: ")
    else:
        print("You need a longer password friend. Enter a longer one...")
        pass_input = input("Please enter a password: ")
