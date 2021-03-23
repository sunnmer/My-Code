import os

filename = 'student.txt'


def main():
    while True:
        menu()
        choice = int(input('Select:'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('Are you sure you want to log out?')
                if answer == 'y' or answer == 'Y':
                    print('Thank You for Using ')
                    break
                else:
                    continue
            elif choice == 1:
                insert()  # Input Student Information
            elif choice == 2:
                search()  # Search Student Information
            elif choice == 3:
                delete()  # Delete Student Informtaion
            elif choice == 4:
                modify()  # Modify Student Informtaion
            elif choice == 5:
                sort()  # Sort Student Informtaion
            elif choice == 6:
                total()  # Count the Total Number of Students
            elif choice == 7:
                show()  # Show All students Informatio
        else:
            print('Wrong Number')


def menu():
    print('============================= Student Information Management System =============================')
    print('======================================== Function Menu ==========================================')
    print('\t\t\t\t\t\t1. Input Student Information')
    print('\t\t\t\t\t\t2. Search Student Information')
    print('\t\t\t\t\t\t3. Delete Student Informtaion')
    print('\t\t\t\t\t\t4. Modify Student Informtaion')
    print('\t\t\t\t\t\t5. Sort Student Informtaion')
    print('\t\t\t\t\t\t6. Count the Total Number of Students')
    print('\t\t\t\t\t\t7. Show All students Information')
    print('\t\t\t\t\t\t0. Quit')
    print('================================================================================================')


def insert():
    student_list = []
    while True:
        id = input('ID:')
        if not id:
            break
        name = input('Name:')
        if not name:
            break

        try:
            english = int(input('English Grades:'))
            python = int(input('Python Grades:'))
            java = int(input('Java Grades:'))

        except:
            print('Is Not An Integer Type, Please Input again')
            continue

        # Save the input student information to the dictionary.
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}

        # Add student information to the list
        student_list.append(student)
        answer = input('Continue to Add Student Information? y/n:')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break

    # save in file
    save(student_list)
    print('Student Information Input Finished')


def save(lst):
    try:
        student_txt = open(filename, 'a')
    except:
        student_txt = open(filename, 'w')

    for item in lst:
        student_txt.write(str(item) + '\n')
    student_txt.close()


def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('1.ID or 2.Name:')
            if mode == '1':
                id = input('ID:')
            elif mode == '2':
                name = input('Name:')
            else:
                print('Wrong number')
                search()
            with open(filename, 'r') as rflie:
                student = rflie.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)

                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
                show_student(student_query)
                student_query.clear()
                answer = input('Continue to Serach Student Information? y/n:')
                if answer == 'y' or answer == 'Y':
                    search()
                else:
                    main()


        else:
            print('NO the Student information')
            return


def show_student(lst):
    if len(lst) == 0:
        print('No the student Information')
        return
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^14}'
    print(format_title.format('ID', 'Name', 'English Grades', 'Python Grades', 'Java Grades', 'Total Grades'))
    format_data = '{:^6}\t{:^12}\t{:^15}\t{:^15}\t{:^10}\t{:^10}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english')) + int(item.get('python')) + int(item.get('java'))
                                 ))


def delete():
    while True:
        student_id = input('Please Enter the ID of The Student to Delete:')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r') as rfile:
                    student_old = rfile.readlines()

            else:
                student_old = []
            flag = False
            if student_old:
                with open(filename, 'w') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'The Information of the Student with ID {student_id} Has Been Deleted')
                    else:
                        print(f'The Information of the Student with ID {student_id} Was Not Found')
            else:
                print('No Student Information')
                break
            show()
            answer = input('Continue to Delete Student Information? y/n:')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break



def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input('Enter the Student ID to be Modified:')
    with open(filename, 'w') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('Student Information can be Modified.')
                try:
                    d['name'] = input('Name:')
                    d['english'] = input('English Grades:')
                    d['python'] = input('Python Grades:')
                    d['java'] = input('Java Grades:')
                except:
                    print('Enter Error')
            wfile.write(str(d) + '\n')
        answer = input('Continue to Modify Student Information? y/n:')
        rfile.close()
        wfile.close()
        if answer == 'y' or answer == 'Y':
            modify()


def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
            student_list = rfile.readlines()
        student_new = []
        for item in student_list:
            d = dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc = input('Select(0.Ascrnding, 1.Descending)')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('Wrong Number')
        sort()
    mode = input('1.English Grades, 2.Python Grades, 3.Java Grades, 0.Total Grades')
    if mode == '1':
        student_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc_bool)
    elif mode == '2':
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif mode == '3':
        student_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)
    elif mode == '0':
        student_new.sort(key=lambda x: int(x['english']) + int(x['python']) + int(x['java']), reverse=asc_or_desc_bool)
    else:
        print('Wrong Number')
        sort()
    show_student(student_new)


def total():
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
            students = rfile.readlines()
            if students:
                print(f'There are {len(students)} students in all')
            else:
                print('No student information')
    else:
        print('No Student Information')


def show():
    student_lst = []
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
            students = rfile.readlines()
            for item in students:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
                student_lst.clear()
    else:
        print('No Student Information')


if __name__ == '__main__':
    main()
