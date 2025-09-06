class FlightNotFoundError(Exception):
    pass

class SeatsUnavailableError(Exception):
    pass

with open("D:\\Linux-Dev\\PYHTON\\Python_Training\\ExceptionHandling\\flights.txt", 'r') as f:
    try:
        recordlist = []
        lines = f.readlines()
        for line in lines:
            templist = line.split()
            recordlist.append(templist)
        print(recordlist)
        
        try:
            flightnumber = input("Flight Number:")
            entryfoundIdx = -1
            for record in recordlist:
                if flightnumber == record[0]:
                    entryfoundIdx = recordlist.index(record)
                    break
            if entryfoundIdx == -1:
                raise FlightNotFoundError("Entered flight number does not exist")

            nooftickets = int(input("Numbers of tickets to book:"))
            if(nooftickets > int(recordlist[entryfoundIdx][1])):
                raise SeatsUnavailableError('Requested tickets exceed available seats')

            totalbookingcost = nooftickets * int(recordlist[entryfoundIdx][2])
            discountperticket = totalbookingcost / nooftickets

            print(f"Flight Number: {flightnumber}\nNo. of Tickets: {nooftickets}\nTotal booking cost: {totalbookingcost}\nDiscount per ticket: {discountperticket}")


        except FlightNotFoundError as e:
            print("Exception Occurred:", e)
        except SeatsUnavailableError as e:
            print("Exception Occurred: ", e)

    except ValueError as e:
        print("Invalid input (like string instead of integer): ", e)
    except ZeroDivisionError as e:
        print("User entered 0 tickets: ", e)
    except Exception as e:
        print("Generic Exception", e)
    finally:
        f.close()