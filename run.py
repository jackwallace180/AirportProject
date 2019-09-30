from Flight_Class import *
from Passenger import *

flight1 = Flight(1, 'Bali')
flight2 = Flight(2, 'Sydney')
flight3 = Flight(3, 'Manchester')

passengerid = 1
passengerlist = []
flightlist1 = []
flightlist2 = []
flightlist3 = []

print (' # list all flights')
print (' # add a passenger')
print (' # list all passengers')
print (' # add a passenger to a flight')
print (' # list all passengers on a flight')
print (' # exit')
to_do = input('what do you want to ?').lower().strip()


while True:

    if to_do == 'list all flights':
        print(flight1.flight_ID, flight1.destination)
        print(flight2.flight_ID, flight2.destination)
        print(flight3.flight_ID, flight3.destination)
        to_do = input('do you want to do something else?').lower().strip()

    elif to_do == 'add a passenger':
        passname = input ('what is the passenger name?')
        passpassport = input ('what is the passenger passport number?')
        passemail = input ('what is the passengers email?')
        passenger = Passenger(passname, passemail, passengerid, passpassport)
        print(f'your passenger id is {passengerid}' )
        passengerlist.append(passenger.passid)
        passengerlist.append(passenger.name)
        passengerlist.append('////')
        passengerid = passengerid + 1

        to_do = input('do you want to do something else?').lower().strip()

    elif to_do == 'list all passengers':
        print(passengerlist)
        to_do = input('do you want to do something else?').lower().strip()

    elif to_do == 'add a passenger to a flight':
        passid = int(input ('what is the ID number of the passenger')) # use my new add to passenger list method
        destination = int(input('where does he want to go? (1,2,3)'))
        if destination == 1:
            print(f'{passid} is going to {flight1.destination}')
            flightlist1.append(passid)
        elif destination == 2:
            print(f'{passid} is going to {flight2.destination}')
            flightlist2.append(passid)
        elif destination == 3:
            print(f'{passid} is going to {flight2.destination}')
            flightlist3.append(passid)
        else:
            print('this is not a valid customer')

        to_do = input('do you want to do something else?').lower().strip()

    elif to_do == 'list all passengers on a flight':
        flightid = int(input('which flight ID do you want to view?'))
        if flightid == 1:
            print (flightlist1)
        elif flightid == 2:
            print (flightlist2)
        elif flightid == 3:
            print (flightlist3)
        else:
            print('this is not a valid flight ID')

        to_do = input('do you want to do something else?').lower().strip()




    else:
        print ('goodbye')
        break


