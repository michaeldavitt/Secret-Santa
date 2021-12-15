# A group is comprised of a number of participants. Can have multiple groups. Each group has a name, an associated budget, an exchange day
# A participant has a name, a date of birth, a gender, another participant they're matched with, a wishlist. They can buy gifts from the Market.
# A market has a name, a number of gifts on offer and a number of participants that interact with it
# A gift will have a name, a price, a seller (market), a description
# Some participants will be admins (is-a relationship). They are similar to normal group members, except they control who gets added and can remove people from the group


class Participant():
    """A class representing a member of a Secret Santa group"""
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.wishlist = []

    def set_match(self, match):
        """Method that sets the user's match"""
        pass

    def set_group(self, group):
        """Method that sets the user's group"""
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


class Admin(Participant):
    """A class representing an admin of the Secret Santa group"""
    def create_group(self, g_name, g_budget, g_exchange_day):
        """Method that allows an admin to create a secret santa group"""
        

    def add_member(self, member):
        """Method that allows an admin to add a member to the secret santa group"""
        pass

    def remove_member(self, member):
        """Method that allows an admin to remove a member from the secret santa group"""
        pass


class Group():
    """A class representing a group of Secret Santa participants created by an admin"""
    # Class variable that keeps track of group IDs
    current_id = 1

    def __init__(self, group_id, name, budget, exchange_day):
        self.group_id = group_id
        self.name = name
        self.budget = budget
        self.exchange_day = exchange_day
        self.members = []

    def assign_group_id(self):
        """Method that provides the group with the current group ID, then increments the variable storing group ID"""
        pass

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
        """Method that provides a string representation of the market
        
        Markets are represented by their name, a list of market participants and a list of items in stock
        """
        return self.name


class Gift():
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __repr__(self):
        """Method that provides a string representation of each gift
        
        Gifts are represented by their name, price and description
        """
        the_rep = "Name: " + self.name + "\nPrice: €" + self.price + "\nDescription: " + self.description
        return the_rep


# Testing the program

# Create some participants
michael = Participant("Michael", 23, "M")
alice = Participant("Alice", 22, "F")
joe = Participant("Joe", 23, "M")
lily = Participant("Lily", 23, "F")

# Create a group admin
james = Admin("James", 24, "M")