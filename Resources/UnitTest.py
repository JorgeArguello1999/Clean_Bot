import Conector_Students as conector

main = conector.database()

def ConStudents():
    main = conector.database()
    print('-------View')
    for x in (main.view_students()):
        print(x)

    print('-------View Specific')
    _id = int(input('_id: '))
    for x in (main.view_student_specific(_id)):
        print(x)

    print('-------Insert')
    information = [
        input('id: '),
        input('name: '),
        input('user: '),
        input('claims: '),
        input('number of times clean curse: '),
    ]
    main.insert_student(information)

    print('-------Update')
    _id = int(input('_id: '))
    information = [
        input('id: '),
        input('name: '),
        input('user: '),
        input('claims: '),
        input('number of times clean curse: '),
    ]
    main.update_student(_id, information)

    print('-------Delete')
    _id = int(input('id: '))
    main.delete_student(_id)
