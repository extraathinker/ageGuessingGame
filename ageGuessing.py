# get the age
inputAge = int(input('Enter your age or enter your year of birth :'))

# check if age is out of range
if inputAge < 0:
    print('Are you kidding me ? ')
elif inputAge > 110 and inputAge < 1900:
    print('Not funny!')
elif inputAge > 1900:
    if inputAge > 2021:
        print('You are not born yet.')
    else:
        # display when the person will be hundred years
        presentAge = 2021 - inputAge
        remainingAge = 100 - presentAge
        hundredthYear = 2021 + remainingAge
        print('You will be 100 years old on', hundredthYear)

        # get the year
        inputYear = int(input('Enter the year you want to know your age :'))

        # tell the age of the person on that year
        if inputYear < 2021:
            requiredAge = inputYear - inputAge
            if requiredAge < 0:
                print('You were not born yet.')
            else:
                print('You were',requiredAge,'years old.')
        else:
            requiredAge = inputYear - 2021 + presentAge
            print('You will be',requiredAge,'years old on',inputYear)
else:
    remainingAge = 100 - inputAge
    hundredthYear = 2021 + remainingAge
    print('You will be 100 years old on', hundredthYear)

    # get the year
    inputYear = int(input('Enter the year you want to know your age :'))

    # tell the age of the person on that year
    if inputYear < 2021:
        requiredAgeZero = 2021 - inputAge
        requiredAge = inputYear - requiredAgeZero
        if requiredAge < 0:
            print('You were not born yet.')
        else:
            print('You were',requiredAge,'years old.')
    else:
        requiredAge = inputYear - 2021 + inputAge
        print('Your age will be',requiredAge,'on',inputYear)





