userReply = input("would you like to buy stamps, buy an enevlope, or make a copy? (Enter stamps, envelope, or copy)")
if userReply == "stamps":
    print("we have many stamps design to choose from.")
elif userReply == "enevlope":
    print("we have many enevlope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number)")
    print("Here are {} copies.".format(copies))
    
else:
    print("Thank you, please come again.")
    