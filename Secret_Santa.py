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

    def __repr__(self):
        return self.name

class Group():
    def __init__(self, name, budget, exchange_day):
        self.name = name
        self.budget = budget
        self.exchange_day = exchange_day
        self.members = []

    def __repr__(self):
        return self.name

class Market():
    def __init__(self, name):
        self.name = name
        self.participants = []
        self.products = []

    def add_gift(self, gift):
        self.products.append(gift)

    def add_participants(self, participant):
        self.participants.append(participant)

    def __repr__(self):
        return self.name


class Gift():
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description