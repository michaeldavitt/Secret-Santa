# A group is comprised of a number of participants. Can have multiple groups. Each group has a name, an associated budget, an exchange day
# A participant has a name, a date of birth, a gender, another participant they're matched with, a wishlist. They can buy gifts from the Market.
# A market has a name, a number of gifts on offer and a number of participants that interact with it
# A gift will have a name, a price, a seller (market), a description


class Participant():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.wishlist = []

    def match(self, match):
        """Method that sets the user's match"""
        pass

    def update_wishlist(self):
        """Method that allows the user to add items to their wishlist"""
        pass

    def buy_product(self, market, gift):
        """Method that allows a user to buy a gift on the market"""
        pass

    def __repr__(self):
        """Method that provides a string representation for each user
        
        Each user will be represented as their name, age, gender and wishlist
        """
        the_rep = "Name: " + self.name + "\nAge: " + self.age + "\nGender: " + self.gender + "\nWishlist:"
        for item in self.wishlist:
            the_rep += ", " + item

        return the_rep

class Group():
    def __init__(self, name, budget, exchange_day):
        self.name = name
        self.budget = budget
        self.exchange_day = exchange_day
        self.members = []

    def match_members(self):
        """Method that allows the group to match group participants to one another"""
        pass

    def __repr__(self):
        return self.name

class Market():
    def __init__(self, name):
        self.name = name
        self.participants = []
        self.products = []

    def add_gift(self, gift):
        self.products.append(gift)

    def remove_gift(self, gift):
        self.products.remove(gift)

    def add_participants(self, participant):
        self.participants.append(participant)

    def __repr__(self):
        return self.name


class Gift():
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description