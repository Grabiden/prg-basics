cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]
print(cinema_seats[0])
def seats_total(seats):
   seats = len(cinema_seats) * len(cinema_seats[0])
   return seats


def seats_available(seats):  
   return sum(seat == 'A' for row in seats for seat in row)

   

def seats_booked(seats):
   return sum(seat == 'B' for row in seats for seat in row)
   
   

def seat_status(seats, row, place):
   if cinema_seats[row-1][place-1] == 'A':
      status = "available"
   else:
      status = "unavailable"   
   return status



print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:',seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))