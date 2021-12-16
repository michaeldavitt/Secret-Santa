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
        """Method that allows the user to add items to their wishlist
        
        Gift added should be a member of the Gift class and should not be in the wishlist already
        """
        if isinstance(gift, Gift) and gift not in self.wishlist:
            self.wishlist.append(gift)

    def show_wishlist(self):
        """Method that shows all items in the wishlist"""
        for gift in self.wishlist:
            print(gift)

    def show_match_wishlist(self):
        """Method that shows all items in the wishlist of a participant's match"""
        self.match.show_wishlist()

    def buy_product(self, market, gift):
        """Method that allows a user to buy a gift on the market
        
        First verifies that the user provided a valid market
        Then verifies that the user provided a valid gift
        If the gift is invalid, displays a list of valid gifts
        """
        if isinstance(market, Market):
            if isinstance(gift, Gift) and gift in market.products:
                self.gift = gift

            else:
                print("Error: Invalid gift. Please select from the list of gifts below: ")
                market.show_products()

        else:
            print("Error: Invalid Market")

    def __repr__(self):
        """Method that provides a string representation for each user
        
        Each user will be represented as their name, age, gender and wishlist
        """
        return self.name


class Admin(Participant):
    """A class representing an admin of the Secret Santa group"""
    def create_group(self, g_name, g_budget, g_exchange_day):
        """Method that allows an admin to create a secret santa group
        
        Admin creates the group, assigns themselves to the group, then returns the group
        """
        new_group = Group(g_name, g_budget, g_exchange_day)
        self.set_group(new_group)
        new_group.members.append(self)
        return new_group
        

    def add_members(self, *args):
        """Method that allows an admin to add members to the secret santa group"""
        for member in args:
            if isinstance(member, Participant) and member not in self.members:
                self.members.append(member)
                member.set_group(self.group)

    def remove_member(self, member):
        """Method that allows an admin to remove a member from the secret santa group"""
        if isinstance(member, Participant) and member in self.members:
            self.members.remove(member)
            member.set_group(None)

    def match_members(self):
        """Method that allows the admin to match group participants to one another
        
        Deterministic, each person matches with the person immediately before them in the group members list
        The exception is the first group member, who is matched with the last member to join
        Assumes that the matching is done after all participants have joined the group
        """
        for i, member in enumerate(self.members):
            member.set_match(self.members[i - 1])

    def __getattr__(self, attr):
        """Method that attempts to find an attribute of interest in the group class if it cannot be found in the admin/participant class"""
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

    def save_member_info(self):
        """Store group member information in a csv file"""
        filename = str(self.group_id) + ".csv"
        with open(filename, "a+") as fh:
            fh.writelines("name,age,gender,wishlist,match")
            for member in g1.members:
                fh.writelines(f"\n{member.name},{member.age},{member.gender},{member.wishlist},{member.match}")

    def __repr__(self):
        return self.name


class Market():
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_gifts(self, *args):
        """Add a product to the market"""
        for gift in args:
            if isinstance(gift, Gift):
                self.products.append(gift)

    def remove_gift(self, gift):
        """Remove a gift from the market"""
        self.products.remove(gift)

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
        return self.name


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

# Now that all members are in the group, we can start matching them
james.match_members()

# View a match
print(michael.match)

# Create potential gifts
dairy_milk = Gift("Dairy Milk", 6, "Taste the deliciously creamy milk chocolate made with a glass and a half of fresh milk in every half pound bar of chocolate. This 850g extra-large bar is a birthday gift and it is ideal for sharing with friends and family. Every product in the Dairy Milk line is made with exclusively milk chocolate Suitable for vegetarians")
yankee_candle = Gift("Yankee Candle", 9, "A new Christmas tradition that is sure to charm: Perfectly pretty holiday cookies, deliciously decorated with sugary pink icing Authentic ingredients and premium wax deliver clean, consistent, room-filling aroma Scented candle burn time: Up to 30 hours; 8 cm height x 5.5 cm width (104 g) Housed in the classic glass jar with lid to preserve the fragrance; removable label for a custom look 100 percent natural fibre cotton wick straightened and centred for a clean, even burn")
fluffy_socks = Gift("Fluffy Socks", 15, "ONE SIZE FIT MOST - These women fluffy slipper socks fits for most size from UK size 4-9/ EU size 37-43. PREMIUM MATERIAL-Made of 98% polyester,2\% \spandex.These ladies fluffy thick socks with fashion design are suitable for womens and teen girls to wear. FLUFFY&SOFT - These bed fluffy socks for women have super soft coral velvet inner,It's very soft and warm, comfortable and breathable, no itching issue,taking good care of womens feet. ELASTICITY - The cuff,heel and toe of the fluffy slipper socks designing with High elastic microfiber,which improve the elasticity of socks and protect womens feet and leg effectively. GIFT IDEA - These winter women fluffy slipper socks are perfect presents for ladies /Teen girls,you can choose them as Christmas gift,Birthday gifts ,Halloween gift or other holiday gifts for mom,wife or girlfriend.")
vs_fragrance = Gift("Victoria Secret Bare Vanilla Fragrance", 14.25, "Notes: Cherry, Milk, Vanilla, Sandalwood, Amber Introduced: N/A")
wallet = Gift("Carbon Fiber Wallet", 17, "RFID Blocking Technology:secure wallet with protection to your identity; Block thieves' scanning devices; RFID technology keeps your private information and credit card safe; ensure your privacy and safety; US GOVT.FIPS 201 approved. Slim & Ultra Light:Securely carry cash (up to 9 folded bills) and 1-12 cards comfortably, such as your driver's license, passport, credit,insurance, debit, social security and business cards.Ultra light and thick body makes it comfortable for daily life or travel. Money Clip & Elastic Webbing: Made of 304 stainless steel and carbon fiber, it can be used to hold cash and bills handy. Humanized and easy-to-use design, flexible elastic webbing on three sides greatly improved the card holding capacity, your card will not slip out easily. High Quality and Good Appearance: 100 percent real carbon fiber Business Credit Card Holder which ensures long service life, 304 stainless steel money clip, slim yet expandable build, you can enjoy a durable wallet with good touch and stylish simplicity. Perfect Gift Idea:Fashionable design card clip wallet is decent gifts for friends, husband or business partners in Valentine's Day or birthday.")
jameson = Gift("Jameson Irish Whiskey", 18, "Blend of traditional Irish pot still and fine grain whiskeys, matured for at least four years Enjoy simply with ice, in a refreshing Jameson Ginger Ale & Lime, or in classic cocktails like the Whiskey Sour Perfect gift to offer for Christmas, dinners, birthdays, Father's & Mother's Day and other special occasions Winner of the 2018 The Irish Whiskey Masters (TIWM) Gold award")
toblerone = Gift("Toblerone", 8.75, "Smooth Swiss milk chocolate with delectable honey and almond nougat Unique triangles of delicious milk chocolate to give as a gift or share with family and friends Suitable for vegetarians Smooth Swiss milk chocolate with delectable honey and almond nougat Unique triangles of delicious milk chocolate to give as a gift or share with family and friends Suitable for vegetarians")
guinness = Gift("Guinness", 4.5, "The packaging of the item may differ from image as we may repackage to avoid damages Unmistakably Guinness Draught Stout Beer, from the first velvet sip to the last, lingering drop Every deep-dark satisfying mouthful in between, Brewed in Ireland Guinness Draught Stout Beer")

# Create a market
m1 = Market("Market 1")

# Add gifts to the market
m1.add_gifts(dairy_milk, yankee_candle, fluffy_socks, vs_fragrance, wallet, jameson, toblerone, guinness)

# Create some participant wishlists
michael.update_wishlist(dairy_milk)
amy.update_wishlist(yankee_candle)
alice.update_wishlist(fluffy_socks)
lily.update_wishlist(vs_fragrance)
kevin.update_wishlist(wallet)
james.update_wishlist(toblerone)
laura.update_wishlist(guinness)

# View all available products in the market
m1.show_products()

# View your matches wishlist
michael.show_match_wishlist()

# Purchase a gift for your match
michael.buy_product(m1, guinness)
print(michael.gift)

# Save member information in the group
g1.save_member_info()