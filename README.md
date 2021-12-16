# Secret Santa Program

## Description
This is a Secret Santa program written in Python using OOP concepts. There are many users of this Secret Santa program, and certain users are admins who can create groups and have control over who is in the group. Admins match members in a group with other members. Members can create a wishlist and buy gifts for their matches on a market.

## Participants
The Participant class represents a generic member of the secret santa group. Each participant has a name, age, gender, wishlist, another participant they are matched with and a gift for their match. They are able to add items to their wishlist, view their match's wishlist, and buy their match a gift on the market

## Admins
An admin is a specialised version of a participant, and as a result, admins inherit all attributes and methods from the participant class. Admins can also create groups, add and remove members from groups, and match the members in the group to one another. 

## Group
A group is a collection of secret santa members. Each group has an ID, a name, a budget, a date of exchange, and a list of group participants, which includes the group admins. 

## Gift
A gift is an item of value that group members buy for one another on a market. Each gift has a name, price and description. 

## Market
A market is a place where members can buy gifts for other members. A market has a name and a list of gifts that it sells. The market can add gifts, remove gifts, and show all available gifts. 