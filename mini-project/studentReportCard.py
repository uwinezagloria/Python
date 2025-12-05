"""
Input student info, compute averages, grade 
students, and store results in a text file.
    """
class Student:
      def __init__(self,name,age,level,subjects=dict()):
          self.name=name
          self.age=age
          self.level=level
          self.subjects=subjects
      def subject_marks_dict(self,course,marks): 
            self.subjects[course]=marks
            return self.subjects
      def studentfile(self)  :
          file=open("students.txt","w")
          lines=[self.name,"\n" ,self.age,"\n" ,self.level,]
student1=Student("uwineza",21,2)
student1.subject_marks_dict("biology",50)
student1.subject_marks_dict("math",40)    
print(student1.subjects)   
      
