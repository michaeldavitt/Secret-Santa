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
        self.match = match

    def set_group(self, group):
        """Method that sets the user's group"""
        self.group = group

    def update_wishlist(self, gift):
        """Method that allows the user to add items to their wishlist"""
        self.wishlist.append(gift)

    def buy_product(self, market, gift):
        """Method that allows a user to buy a gift on the market"""
        if gift in market.products:
            self.gift = gift

    def __repr__(self):
        """Method that provides a string representation for each user
        
        Each user will be represented as their name, age, gender and wishlist
        """
        the_rep = "Name: " + self.name + "\nAge: " + str(self.age) + "\nGender: " + self.gender + "\nWishlist:"
        for item in self.wishlist:
            the_rep += ", " + item

        return the_rep


class Admin(Participant):
    """A class representing an admin of the Secret Santa group"""
    def create_group(self, g_name, g_budget, g_exchange_day):
        """Method that allows an admin to create a secret santa group
        
        Admin creates the group, assigns themselves to the group, then returns the group
        """
        new_group = Group(g_name, g_budget, g_exchange_day)
        self.set_group(new_group)
        return new_group
        

    def add_members(self, *args):
        """Method that allows an admin to add members to the secret santa group"""
        for member in args:
            self.members.append(member)
            member.set_group(self.group)

    def remove_member(self, member):
        """Method that allows an admin to remove a member from the secret santa group"""
        self.members.remove(member)
        member.set_group(None)

    def match_members(self):
        """Method that allows the admin to match group participants to one another
        
        Deterministic, each person matches with the person immediately before them in the group members list
        The exception is the first group member, who is matched with the last member to join
        Assumes that the matching is done after all participants have joined the group
        """
        mem_list = self.members.copy()
        for i, member in enumerate(mem_list):
            member.set_match(mem_list[i - 1])

    def __getattr__(self, attr):
        return getattr(self.group, attr)


class Group():
    """A class representing a group of Secret Santa participants created by an admin"""
    # Class variable that keeps track of group IDs
    current_id = 1

    def __init__(self, name, budget, exchange_day):
        self._assign_group_id()
        self.name = name
        self.budget = budget
        self.exchange_day = exchange_day
        self.members = []

    def _assign_group_id(self):
        """Method that provides the group with the current group ID, then increments the variable storing group ID"""
        self.group_id = Group.current_id
        Group.current_id += 1

    def __repr__(self):
        return "Group ID: " + str(self.group_id) + "\nGroup Name: " + self.name

class Market():
    def __init__(self, name):
        self.name = name
        self.participants = []
        self.products = []

    def add_gift(self, gift):
        """Add a product to the market"""
        self.products.append(gift)

    def remove_gift(self, gift):
        """Remove a gift from the market"""
        self.products.remove(gift)

    def add_market_participant(self, participant):
        """Add a participant to the market"""
        self.participants.append(participant)

    def show_products(self):
        """Show a list of all available products for sale in the market"""
        for product in self.products:
            print(product)

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

# Group admin creates a group
g1 = james.create_group("Group 1", 15, "17/12/2021")

# Group admin adds participants to the group
james.add_members(michael, alice, joe, lily)

# View group members
print(g1.members)

# Remove a member
james.remove_member(joe)

# View group members
print(g1.members)

# Create new participants
kevin = Participant("Kevin", 21, "M")
amy = Participant("Amy", 19, "F")
jessica = Participant("Jessica", 25, "F")
laura = Participant("Laura", 23, "F")

# Add new participants to the group
james.add_members(kevin, amy, jessica, laura)

# View group members
print(g1.members)
