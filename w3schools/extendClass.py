from dataclassfile import Person
from dataclasses import dataclass

@dataclass
class Student(Person):
    grade: int
    school: str

Anna = Student("Anna", "Steiger", 17, "Germany", True, 9, "UET")
Till = Student("Till", "Strebel", 17, "America", True, 9, "CPT")
Kevin = Person("Kevin", "Zingg", 18, "Sweden", False)
Janik = Person("Janik", "Bösch", 18, "Switzerland", False)
Tove = Person("Tove", "Näslund", 17, "Sweden", False)
Jürg = Student("Jürg", "Mausch", 38, "Switzerland", False, 0, "-")

print(Till)
print(Jürg)
print(Kevin.full_name())  # Output: Kevin Zingg
print(Till.is_this_person_minor())  # Output: True
print(Person.is_minor(25))  # Output: False
