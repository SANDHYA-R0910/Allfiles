#method overridding

class ineuron:
    def student(self):
        print("print the details of students")
    def achivers(self):
        print("print list of all achivers")
    def hall_of_fame(self):
        print("print everyone from hall of fame")

class ineuron_vision(ineuron):

    def student(self):
        print("these are the filter students")

s = ineuron_vision()
s.student()
s.achivers()
s.hall_of_fame()