class Passenger:
    def __init__(self, passenger_name, place, no_of_days, no_of_tickets):
        self.__passenger_name = passenger_name
        self.__place = place
        self.__no_of_days = no_of_days
        self.__no_of_tickets = no_of_tickets
        self.__bill_amount = 0.0

    def get_passenger_name(self):
        return self.__passenger_name

    def set_passenger_name(self, passenger_name):
        self.__passenger_name = passenger_name

    def get_place(self):
        return self.__place

    def set_place(self, place):
        self.__place = place

    def get_no_of_days(self):
        return self.__no_of_days

    def set_no_of_days(self, no_of_days):
        self.__no_of_days = no_of_days

    def get_no_of_tickets(self):
        return self.__no_of_tickets

    def set_no_of_tickets(self, no_of_tickets):
        self.__no_of_tickets = no_of_tickets

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill_amount(self, place):
        place_prices = {
            "Beach": 270,
            "Pilgrimage": 350,
            "Heritage": 430,
            "Hill Station": 780,
            "Water Falls": 1200,
            "Adventures": 4500
        }
        if place in place_prices:
            self.__bill_amount = self.__no_of_days * self.__no_of_tickets * place_prices[place]
        return self.__bill_amount
