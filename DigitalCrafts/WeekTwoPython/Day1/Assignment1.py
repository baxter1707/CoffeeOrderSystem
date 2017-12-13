###COME BACK AND DO BONUS MATERIAL###



class Person(object):
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0


    def greet(self, other_person):
        #print("Hello " + other_person.name + " I am " + self.name)
        print("Hello {0}, I am {1}.".format(other_person.name, self.name))
        self.greeting_count +=1

    def info(self):
        print(self.email + "-" + self.phone)

    def print_contact_info(self):
        print("{0}'s Email: {1}, {0}'s Phone: {2}".format(self.name,self.email,self.phone))

    def number_of_friends(self):
        print(len(self.friends))

    def add_friend(self, other_person):
        self.friends.append(other_person.name)

    def print_friends(self):
        print(len(self.friends))


#if self.greet():
#    self.greeting_count += 1


sonny = Person("Sonny", "sonny@hotmail.com","495-586-3456")
jordan = Person("Jordan", "jordan@aol.com","495-586-3456")

#print(sonny)
#print(person2)
sonny.greet(jordan)
jordan.greet(sonny)
sonny.info()
jordan.info()
sonny.print_contact_info()
jordan.print_contact_info()
#jordan.friends.append(sonny)
#sonny.friends.append(jordan)
#jordan.number_of_friends()
#sonny.number_of_friends()
jordan.add_friend(sonny)
sonny.add_friend(jordan)
jordan.print_friends()
sonny.print_friends()
sonny.greet(jordan)
print(sony.greeting_count)
