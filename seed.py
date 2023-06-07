import random
from faker import Faker
from models import Student, session

if __name__ == '__main__':

    fake = Faker()
    
    students = []
    for i in range(10):
        student = Student(
            Name = fake.unique.name(),
            Email = fake.unique.email(),
            Phone = random.randint(2547124532,2547980123),
            Address = fake.unique.address()
        )
        
        session.add(student)
        session.commit()
        students.append(student)