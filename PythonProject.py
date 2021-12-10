import csv


def insert_Student():

    with open('studentdatabase.csv', 'w', newline='') as outcsv:
        writer = csv.DictWriter(outcsv,
                                fieldnames=['STUDENT ID', 'FIRST NAME', 'LAST NAME', 'MAJOR', 'PHONE', 'GPA',
                                            'Date_of_birth'])
        writer.writeheader()


    with open('studentdatabase.csv', 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
#promt the user for input
        n = int(input("Enter the number of students needs to be entered"))
        for x in range(n):
            print("Enter the student " + str(x + 1) + "'s details")
            studentidinput = input("student_ID:\t")
            firstnameinput = input("First Name:\t")
            lastnameinput = input("Last Name:\t")
            majorinput = input("Major:\t")
            phoneinput = int(input("Phone:\t"))
            gpainput = float(input("GPA:\t"))
            dobinput = input("DATE OF BIRTH:\t")

            student = {'studentid': studentidinput, 'firstname': firstnameinput, 'lastname': lastnameinput,
                       'major': majorinput, 'phone': phoneinput, 'gpa': gpainput, 'Date_of_birth': dobinput}
            writer.writerow(student.values())
    return

#displays the records in format
def displayRecord(stdlist):
    print('Student ID       : ', stdlist[0])
    print('First Name       : ', stdlist[1])
    print('Last Name        : ', stdlist[2])
    print('Major            : ', stdlist[3])
    print('Phone            : ', stdlist[4])
    print('GPA              : ', stdlist[5])
    print('Date of Birth    : ', stdlist[6])
    print('---------------------------------')
    return

#displays the student details from studentdatabase file
def displayStudent():
    file1 = open("studentdatabase.csv", "r")

    for line in file1:
        if line != '':
            data = line.split(',')
            displayRecord(data)
    file1.close()
    return

#method used to sort
def sortStudent():
    with open('studentdatabase.csv', 'r') as file:
        csv_reader = csv.reader(file)

        que = int(input("Sorting options: " + \
                        "\n1. Sort by First Name\n2. Sort by Last Name\n3. Sort by Major :"))
        if que == 1:
            for line in csv_reader:
                n = list(csv_reader)
                for i in n:
                    sortstudents = sorted(n, key=lambda x: x[1])
                print(sortstudents)
                print()
        elif que == 2:
            for line in csv_reader:
                n = list(csv_reader)
                for i in n:
                    sortstudents = sorted(n, key=lambda x: x[2])
                print(sortstudents)
                print()
        elif que == 3:
            for line in csv_reader:
                n = list(csv_reader)
                for i in n:
                    sortstudents = sorted(n, key=lambda x: x[3])
                print(sortstudents)
                print()
        else:
            print("Invalid entry! Try again")

    return


#search the file using student details
def searchStudent():
    print('inside search statement')
    csv_file = csv.reader(open('studentdatabase.csv', "r"), delimiter=",")
    search = int(input("Select the Search Options\n " + \
                   "1.Search using Student ID\n " + \
                   "2.Search using Last Name\n " + \
                   "3.Search using Major:\n\nOption: "))

    flag = 0

    if search == 1:
        option = input('Enter Student ID: \n')

        for row in csv_file:
            if option == row[0]:
                flag = 1
                displayRecord(row)

    elif search == 2:
        option = input('Enter Last Name :  \n')

        for row in csv_file:
            if option == row[2]:
                flag = 1
                displayRecord(row)

    elif search == 3:
        option = input('Enter the Major:  \n')
        for row in csv_file:
            if option == row[3]:
                flag = 1
                displayRecord(row)
    else:
        print('Invalid input! Try Again')
    if flag == 0:
        print("Value not found!")
    return


def display_data(stdlist):
    print('---------------------------------')
    print('Student ID       : ', stdlist[0])
    print('First Name       : ', stdlist[1])
    print('Last Name        : ', stdlist[2])
    print('Major            : ', stdlist[3])
    print('Phone            : ', stdlist[4])
    print('GPA              : ', stdlist[5])
    print('Date of Birth    : ', stdlist[6])
    print('---------------------------------')


def updateStudent():
    print("\n Updating the student info")
    studentId = input('Enter the student ID  you want to update \n')
    file = open('studentdatabase.csv', 'r')
    line = file.readline()
    while line != '':
        data = line.split(',')
        if studentId == data[0]:
            first_name = data[1]
            last_name = data[2]
            major = data[3]
            phone = data[4]
            gpa = data[5]
            dob = data[6]
            display_data(data)
        line = file.readline()
    up = input('\nDo yo want to update the details of this student ?(Y/N) \n')

    if up == 'y' or up == 'Y':
        print('Enter the options for updating \n')

        updateChoice = int(input('1. First Name\n2. Last Name\n3. Major\n4. Phone\n5. GPA\n6. Date Of Birth\n'))

        # Modify First Name
        if updateChoice == 1:
            first_name = input('Enter the First Name : \n')
            while not (first_name.isalpha()):
                first_name = input('Name contains invalid characters! Enter a valid name : \n')

        # Modify Last Name
        if updateChoice == 2:
            last_name = input('Enter the Last Name : ')
            while not (last_name.isalpha()):
                last_name = input('Name contains invalid characters! Enter a valid name : \n')

        # Modify Major
        if updateChoice == 3:
            major = input('Enter the Major : \n')

        # modify phone
        if updateChoice == 4:
            phone = input('Enter the phone number\n')
            while not (phone.isdigit()):
                last_name = input('Please enter only numeric character \n')

        # Modify GPA
        if updateChoice == 5:
            gpa = input('Enter the GPA : \n')
            while float(gpa) > 4:
                gpa = input('GPA cannot exceed 4!! Enter a valid GPA : \n')

        # Modify Date of Birth
        if updateChoice == 6:
            dob = input('Enter the Date of Birth : \n')

        #append the string into one
        stddetails = studentId + ',' + first_name.upper() + ',' + last_name.upper() + ',' + major.upper() + ',' + phone + ',' + gpa + ',' + dob

        file_r = open('studentdatabase.csv', 'r')
        r_line = file_r.readline()
        file_w = open('temp.csv', 'w')
        while r_line != '':
            data = r_line.split(',')
            if studentId == data[0]:
                file_w.write(stddetails)
            else:
                file_w.write(r_line)
            r_line = file_r.readline()
        file_w.close()
        file_r.close()
        #transferring the content using a temporary file
        file_r = open('temp.csv', 'r')
        file_w = open('studentdatabase.csv', 'w')
        r_line = file_r.readline()
        while r_line != '':
            file_w.write(r_line)
            r_line = file_r.readline()
        file_w.close()
        file_r.close()
    return


def main():
    userInput = 1
    print('******************MENU**************************')

    print("1. Insert Student details" + \
          "\n2. Display the students list" + \
          "\n3. Sorting " + \
          "\n4. Search" + \
          "\n5. Modify" + \
          "\n6. Exit\n")
    userInput = input()
    while userInput != 6:
        if int(userInput) == 1:
            insert_Student()
        elif int(userInput) == 2:
            displayStudent()
        elif int(userInput) == 3:
            sortStudent()
        elif int(userInput) == 4:
            searchStudent()
        elif int(userInput) == 5:
            updateStudent()
        elif int(userInput) == 6:
            print('BYE!')
            break
        print('******************MENU**************************')
        print("1. Insert Student details" + \
              "\n2. Display the students list" + \
              "\n3. Sorting " + \
              "\n4. Search" + \
              "\n5. Modify" + \
              "\n6. Exit\n\noption: ")
        userInput = input()


main()
