from dataclasses import dataclass

@dataclass
class Person:
    fname: str
    lname: str
    age: int
    heritage: str
    isGymi: bool

    def full_name(self) -> str:
        return f"{self.fname} {self.lname}"

    @staticmethod
    def is_minor(age: int) -> bool:
        return age < 18

    def is_this_person_minor(self) -> bool:
        return self.is_minor(self.age)
