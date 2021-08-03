import datetime
empno = [2822, 2823, 2824, 2825, 2826, 2827, 2828]
fname = ["Abel", "Ram", "Latha", "Neeti", "Kee", "Zee"]
lname = ["Fdo", "Nair","Iyer", "Rao", "Li", "Wink"]
x = str(datetime.datetime.now())
i= 2
attendancerecord = "\n"+str(empno[i])+" "+fname[i]+" "+ lname[i]+"  "+x
print(attendancerecord)
f = open("./DataFiles/Attendance.txt", "a")
f.write(attendancerecord)
f.close()    