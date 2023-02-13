import pymongo

class database:
    def __init__(self):
        # In this URL you change de username:password
        # By default use admin and admin
        self.myclient = pymongo.MongoClient("mongodb://admin:admin@localhost:27017/?authMechanism=DEFAULT")
        self.db_students = self.myclient['students']
        self.col_students = self.db_students["students"]
        
        databases = self.myclient.list_database_names()
        print(databases)
        if "students" in databases:
            print('Database is exists')
        else:
            print('Creating a Database... students')

    def view_students(self):
        global data
        for data in self.col_students.find(): 
            print(data)
        return data

    def view_student_specific(self, student_id):
        global data
        for data in self.col_students.find({"_id": student_id}):
            print(data)
        return data

    def insert_student(self, information):
        try:
            self.col_students.insert_one({
                '_id': int(information[0]), # id: Int
                'name': information[1], # Complete name: String
                'user': information[2], # User fot Telegram: String
                'claims': int(information[3]), # claims: Int
                'times_clean': int(information[4]) # How many times clean a classrom: Int
            })
            self.view_students()
            return True
        except:
            print('Error as ocurred')
            return False

    def update_student(self, infromation):
        pass

    def delete_student(self, student_id):
        try:
            self.col_students.delete_one({'_id': student_id})
            return True
        except:
            print('Error as ocurred')
            return False

if __name__ == '__main__':
    main = database()

    print('-------View')
    main.view_students()

    print('-------View Specific')
    _id = int(input('_id: '))
    main.view_student_specific(_id)

    """
    print('-------Insert')
    information = [
        input('id: '),
        input('name: '),
        input('user: '),
        input('claims: '),
        input('number of times clean curse: '),
    ]
    main.insert_student(information)
    """

    print('-------Delete')
    _id = int(input('id: '))
    main.delete_student(_id)
