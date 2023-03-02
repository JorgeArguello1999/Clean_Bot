import pymongo
from pymongo import errors
# import Resources.UnitTest as UnitTest 

class database:
    def __init__(self, mongo):
        # In this URL you change de username:password
        # By default use admin and admi
        self.myclient = pymongo.MongoClient(mongo)
        self.db_school= self.myclient['school']
        self.col_students = self.db_school["students"]
        
        databases = self.myclient.list_database_names()
        print(databases)
        if "school" in databases:
            print('Database is exists')
        else:
            print('Creating a Database... school')

    def view_students(self):
        return self.col_students.find()
        

    def view_student_specific(self, student_id):
        return self.col_students.find({"_id": student_id})

    def insert_student(self, information):
        try:
            self.col_students.insert_one({
                '_id': int(information[0]), # id: Int
                'name': information[1], # Complete name: String
                'claims': int(information[2]), # claims: Int
                'times_clean': int(information[3]), # How many times clean a classrom: Int
                'last_time': information[4] # Date
            })
            return True
        except errors.PyMongoError as e:
            print('Error as ocurred', e)
            return False

    def update_student(self, information):
        for i in information:
            print(i)
        try: 
            self.col_students.update_one(
                {'_id': information[0]},
                {'$set':
                    {
                        'name': information[1],
                        'claims': int(information[2]),
                        'times_clean': int(information[3]),
                        'last_time': information[4]
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

    def confirm(self, information):
        try:
            self.col_students.update_one(
                {'_id': information[0]},
                {'$set':
                 {
                     'times_clean' : information[1],
                     'last_time':  information[2]
                 }
                }
            )
            return True
        except:
            print('Error as ocurred')
            return False

if __name__ == '__main__':
    #UnitTest.ConStudents()
    print(0)
