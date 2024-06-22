student=[['anil',30,40,30],['hrutika',20,33,34],['cr',40,42,32]]
student.sort(key=lambda x:(x[1]+x[2]+x[3])/3)
print(student)

student.sort(key=lambda x:x[1])
print(student)

# student.sort(key=lambda x:)