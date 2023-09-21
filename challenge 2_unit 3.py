class student:
  def __init__(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa
def sort_students(student_list):
#sort the list of students in descending order of cgpa
  sorted_sudents = sorted(student_list, key=lambda student:student.cgpa,reverse=True)
#syntax-lambda arg:exp
  return sorted_sudents 
#example usage:
students=[student("sathiya","A04",9.3),student("abi","A29",9.5),student("nithya","A17",9.7),student("Deepasri","A21",9.9)]
sorted_students=sort_students(students)
#print the sorted list of students 
for students in sorted_students:
  print("name:{},roll_number:{},cgpa:{}".format(students.name,students.roll_number,students.cgpa))
