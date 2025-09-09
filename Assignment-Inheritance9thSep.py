class Flight:
    def __init__(self, flightnumber, airline):
        self.flightnumber = flightnumber
        self.airline = airline

    
    def printflightdetails(self):
        print(f"Number: {self.flightnumber}   Airline: {self.airline}")



class ScheduledFlight(Flight):
    def __init__(self, number, airline, depttime, arrvtime):
        super().__init__(number, airline)
        self.depttime = depttime
        self.arrvtime = arrvtime
    
    def printflightschedule(self):
        super().printflightdetails()
        print(f"Dept Time: {self.depttime}    Arrival Time: {self.arrvtime}")


schfligth = ScheduledFlight("Indigo", "AI7370", "16:10:00",  "20:30:00")
schfligth.printflightschedule()

 # =============================================
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def printpersondetails(self):
        print(f"Name: {self.name}   ID: {self.id}")



class CrewMember(Person):
    def __init__(self, name, id, role):
        super().__init__(name, id)
        self.role = role
    
    def printcrewdetails(self):
        super().printpersondetails()
        print(f"Role: {self.role}")



class Pilot(CrewMember):
    def __init__(self, name, id, role, licensenumber, rank):
        super().__init__(name, id, role)
        self.licensenumber = licensenumber
        self.rank = rank
    
    def printpilotdetails(self):
        super().printcrewdetails()
        print(f"Licensenumber: {self.licensenumber}    Rank: {self.rank}")

pilot = Pilot("A Das", 3322, "Cabin Crew", 102341, "Captain")
pilot.printpilotdetails()

#=========================================================================

class PassengerDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printpassengerdetails(self):
        print(f"Name: {self.name}   Age: {self.age}")



class TicketDetails:
    def __init__(self, ticketnumber, seatnumber):
        self.ticketnumber = ticketnumber
        self.seatnumber = seatnumber
    
    def printticketdetails(self):
        print(f"Ticketnumber: {self.ticketnumber} Seatnumber: {self.seatnumber}")



class Booking(PassengerDetails, TicketDetails):
    def __init__(self, name, age, ticketnumber, seatnumber):
        PassengerDetails.__init__(self, name, age)
        TicketDetails.__init__(self, ticketnumber, seatnumber)
    
    def printbookingdetails(self):
        self.printpassengerdetails()
        self.printticketdetails()


booking = Booking("A Chatterjee", 45, "AI65621-W", "W32")
booking.printbookingdetails()




