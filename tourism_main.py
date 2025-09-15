from tourism import Tourism
from invalid_place_exception import InvalidPlaceException

def main():
    tourism = Tourism()

    num_registrations = int(input("Enter the number of registrations:\n"))

    for i in range(num_registrations):
        registration_details = input(f"Enter the registration details {i + 1}:\n")
        passenger_name, place, no_of_days, no_of_tickets = registration_details.split(":")
        no_of_days = int(no_of_days)
        no_of_tickets = int(no_of_tickets)

        try:
            if tourism.validate_place_name(place):
                tourism.add_passenger_details(passenger_name, place, no_of_days, no_of_tickets)
        except InvalidPlaceException as e:
            print(e)

    search_place = input("Enter the Place that needs to be searched:\n")
    passengers = tourism.view_passenger_details(search_place)

    if not passengers:
        print("No Passengers found")
    else:
        for passenger in passengers:
            print(f"Passenger Name {passenger.get_passenger_name()}")
            print(f"Number Of Days {passenger.get_no_of_days()}")
            print(f"Number Of Tickets {passenger.get_no_of_tickets()}")
            print(f"Bill Amount {passenger.get_bill_amount()}")

if __name__ == "__main__":
    main()
