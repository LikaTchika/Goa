def check_license_eligibility():
        
        age = int(input("enter your nage: "))
        driving_experience = int(input("how many year driver expiriance you have:"))

        if age < 0 or driving_experience < 3:
            print("you can have lices")

        if age < 18:
            print("you cant take driver lices your under 18")
        elif age >= 18 and driving_experience < 1:
            print("you can't take friver lices becouse you dont have enough experionce")
        else:
            print("you can't take driver lices")

check_license_eligibility()