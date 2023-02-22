import pymongo
# import Resources.UnitTest as UnitTest 

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
        return self.col_students.find()
        

    def view_student_specific(self, student_id):
        return self.col_students.find({"_id": student_id})

    def insert_student(self, information):
        try:
            self.col_students.insert_one({
                '_id': int(information[0]), # id: Int
                'name': information[1], # Complete name: String
                'user': information[2], # User fot Telegram: String
                'claims': int(information[3]), # claims: Int
                'times_clean': int(information[4]) # How many times clean a classrom: Int
            })
            return True
        except:
            print('Error as ocurred')
            return False

    def update_student(self, student_id, information):
        for i in information:
            print(i)

        try: 
            self.col_students.update_one(
                {'_id': student_id},
                {'$set':
                    {
                        'name': information[1],
                        'user': information[2],
                        'claims': int(information[3]),
                        'times_clean': int(information[4])
                    }
                }
            )
            return True
        except:
            print('Error as ocurred')
            return False

    def delete_student(self, student_id):
        try:
            self.col_students.delete_one({'_id': student_id})
            return True
        except:
            print('Error as ocurred')
            return False

if __name__ == '__main__':
    #UnitTest.ConStudents()
    print(0)
