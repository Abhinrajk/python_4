
#6. Online Learning Platform (Abstraction + Inheritance)

from abc import ABC, abstractmethod

class Course(ABC):
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    @abstractmethod
    def course_details(self):
        pass


class ProgrammingCourse(Course):
    def __init__(self, course_name, duration, language):
        super().__init__(course_name, duration)
        self.language = language

    def course_details(self):
        print("Programming Course")
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)
        print("Language:", self.language)


class DesignCourse(Course):
    def __init__(self, course_name, duration, software):
        super().__init__(course_name, duration)
        self.software = software

    def course_details(self):
        print("Design Course")
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)
        print("Software Used:", self.software)


class MarketingCourse(Course):
    def __init__(self, course_name, duration, platform):
        super().__init__(course_name, duration)
        self.platform = platform

    def course_details(self):
        print("Marketing Course")
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)
        print("Marketing Platform:", self.platform)


# Creating objects
course1 = ProgrammingCourse("Python Basics", "3 Months", "Python")
course2 = DesignCourse("Graphic Design", "2 Months", "Photoshop")
course3 = MarketingCourse("Digital Marketing", "4 Months", "Google Ads")

courses = [course1, course2, course3]

for course in courses:
    course.course_details()
    print()