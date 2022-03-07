class Worker:
    name = None
    age = 0
    gender = None
    count_person=0
    count_age=0
    man_count=0
    woman_count=0
    info = None
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender

        Worker.count_person += 1
        Worker.count_age += self.age
        print(Worker.count_person)
        if(gender=="남"): Worker.man_count +=1
        else : Worker.woman_count += 1

    def __str__(self) :

        return str(self.name)+","+str(self.age)+","+str(self.gender)


