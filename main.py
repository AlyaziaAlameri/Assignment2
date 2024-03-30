from datetime import datetime
from enum import Enum


class ExhibitionLocation(Enum):
    PERMANENT_GALLERY = "Permanent Gallery"
    EXHIBITION_HALL = "Exhibition Hall"
    OUTDOOR_SPACE = "Outdoor Space"


class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_significance, location):
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance
        self.location = location

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_artist(self):
        return self.artist

    def set_artist(self, artist):
        self.artist = artist

    def get_date_of_creation(self):
        return self.date_of_creation

    def set_date_of_creation(self, date_of_creation):
        self.date_of_creation = date_of_creation

    def get_historical_significance(self):
        return self.historical_significance

    def set_historical_significance(self, historical_significance):
        self.historical_significance = historical_significance

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def display_artwork_info(self):
        print("Title:", self.title)
        print("Artist:", self.artist)
        print("Date of Creation:", self.date_of_creation)
        print("Historical Significance:", self.historical_significance)
        print("Location:", self.location.value)


class Exhibition:
    def __init__(self, name, start_date, end_date, description, location):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.location = location

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_start_date(self):
        return self.start_date

    def set_start_date(self, start_date):
        self.start_date = start_date

    def get_end_date(self):
        return self.end_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def display_exhibition_info(self):
        print("Exhibition Name:", self.name)
        print("Start Date:", self.start_date)
        print("End Date:", self.end_date)
        print("Description:", self.description)
        print("Location:", self.location)


class Visitor:
    def __init__(self, name, age, ticket):
        self.name = name
        self.age = age
        self.ticket = ticket

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_ticket(self):
        return self.ticket

    def set_ticket(self, ticket):
        self.ticket = ticket

    def display_visitor_info(self):
        print("Visitor Name:", self.name)
        print("Age:", self.age)
        print("Ticket Information:")
        self.ticket.display_ticket_info()


class Ticket:
    def __init__(self, ticket_type, price, is_free, event_name, event_date):
        self.ticket_type = ticket_type
        self.price = price
        self.is_free = is_free
        self.event_name = event_name
        self.event_date = event_date

    def get_ticket_type(self):
        return self.ticket_type

    def get_price(self):
        return self.price

    def get_is_free(self):
        return self.is_free

    def get_event_name(self):
        return self.event_name

    def get_event_date(self):
        return self.event_date

    def set_ticket_type(self, ticket_type):
        self.ticket_type = ticket_type

    def set_price(self, price):
        self.price = price

    def set_is_free(self, is_free):
        self.is_free = is_free

    def set_event_name(self, event_name):
        self.event_name = event_name

    def set_event_date(self, event_date):
        self.event_date = event_date

    def is_expired(self):
        current_date = datetime.now().date()
        event_date = self.event_date.date()
        return current_date > event_date

    def display_ticket_info(self):
        print("Ticket Type:", self.ticket_type)
        print("Price:", self.price)
        print("Is Free:", self.is_free)
        print("Event Name:", self.event_name)
        print("Event Date:", self.event_date)


class TicketingSystem:
    def __init__(self):
        self.tickets_sold = 0
        self.ticket_prices = {}
        self.vat_rate = 0.05

    def purchase_ticket(self, visitor, ticket):
        self.tickets_sold += 1
        print(f"{visitor} has purchased a ticket for {ticket.get_event_name()}.")

    def generate_receipt(self, ticket):
        print("Generating receipt for ticket:")
        ticket.display_ticket_info()
        print()

    def calculate_price(self, ticket):
        price = ticket.get_price()
        vat_amount = price * self.vat_rate
        total_price = price + vat_amount
        return total_price


class LouvreAbuDhabi:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def display_opening_hours(self):
        print("Opening Hours:")
        print("Monday: Closed")
        print("Tuesday - Thursday: 10:00 AM - 6:30 PM")
        print("Friday - Sunday: 10:00 AM - 8:30 PM")
        print("Museum Café:", "Weekdays: Closes at 8:00 PM", "Weekends (Friday - Sunday): Closes at 10:00 PM")
        print("Aptitude Café:", "Closes at 10:00 PM daily")
        print("Dome:", "Open until midnight, last entry at 11:00 PM")


# Example usage
if __name__ == "__main__":
    # Creating Artwork instances
    artworks = [
        Artwork("The Bezique Game", "Gustave Caillebotte", datetime(1880, 1, 1),
                "Iconic portrait", ExhibitionLocation.PERMANENT_GALLERY),
        Artwork("Children Wrestling", "Paul Gauguin", datetime(1888, 1, 1),
                "Breton wrestling match", ExhibitionLocation.PERMANENT_GALLERY),
        Artwork("Composition with Blue, Red, Yellow and Black", "Piet Mondrian", datetime(1922, 1, 1),
                "Abstract composition", ExhibitionLocation.EXHIBITION_HALL),
        Artwork("Esther Fainting Before Ahasuerus", "Jean-François De Troy", datetime(1730, 1, 1),
                "Biblical story depiction", ExhibitionLocation.OUTDOOR_SPACE),
        Artwork("In Fontainebleau Forest: Pines and Birch Trees in the Rocks", "Camille Corot",
                datetime(1845, 1, 1), "Forest landscape", ExhibitionLocation.PERMANENT_GALLERY),
        Artwork("Oriental Bliss", "Paul Klee", datetime(1938, 1, 1),
                "Abstract painting", ExhibitionLocation.EXHIBITION_HALL)
    ]

    # Display information for each artwork
    for artwork in artworks:
        artwork.display_artwork_info()
        print()

    # Creating Exhibition instance
    exhibition = Exhibition("From Kalila wa Dimna to La Fontaine: Travelling through Fables",
                            datetime(2024, 3, 26),
                            datetime(2024, 7, 21),
                            "This timeless literary genre transcends across cultures and centuries, "
                            "imparting life lessons and values to both adults and children",
                            "Exhibition Hall")

    # Display exhibition information
    exhibition.display_exhibition_info()

    # Creating Visitor instance
    ticket = Ticket("Adult", 60.0, False, "Museum Visit", datetime(2024, 3, 24))
    visitor = Visitor("Alyazia", 18, ticket)

    # Display visitor information
    visitor.display_visitor_info()

    # Creating TicketingSystem instance
    ticketing_system = TicketingSystem()

    # Create tickets based on admission information
    tickets = [
        Ticket("Adult", 60.00, False, "Museum Visit", datetime(2024, 3, 24)),
        Ticket("Workshop Ticket Holder", 30.00, False, "Workshop", datetime(2024, 3, 25)),
        Ticket("UAE Teachers", 30.00, False, "Exhibition: From Kalila wa Dimna to La Fontaine", datetime(2024, 3, 26)),
        Ticket("UAE Military", 30.00, False, "The Jungle Book", datetime(2024, 3, 27)),
        Ticket("Fazaa Card Holder", 42.00, False, "MASQUERAVE", datetime(2024, 3, 28)),
        Ticket("Under 18", 0.00, True, "Tour", datetime(2024, 3, 29)),
        Ticket("Homat Al Watan", 30.00, False, "Film Screening", datetime(2024, 3, 30)),
        Ticket("People of Determination", 0.00, True, "Museum Visit", datetime(2024, 3, 31)),
        Ticket("ICOM/ICOMOS Member", 0.00, True, "Performance", datetime(2024, 4, 1)),
        Ticket("Senior Citizens", 0.00, True, "Exhibition: Transparencies", datetime(2024, 4, 2)),
    ]

    # Display information for each ticket
    for ticket in tickets:
        ticket.display_ticket_info()
        print("Is ticket expired?", ticket.is_expired())
        print()

    # Example usage of TicketingSystem methods
    print("Total tickets sold:", len(tickets))  # Calculate total tickets sold using the length of the tickets list
    ticketing_system.purchase_ticket("Alyazia", tickets[4])

    ticketing_system.generate_receipt(tickets[4])
    print("Total price with VAT:", ticketing_system.calculate_price(tickets[4]))

    # Creating LouvreAbuDhabi instance
    louvre_abu_dhabi = LouvreAbuDhabi("Louvre Abu Dhabi", "Abu Dhabi, UAE")

    # Display museum information
    louvre_abu_dhabi.display_opening_hours()
