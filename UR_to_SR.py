import sys

ILL     = input("What illocutionary force? (D/Q/I)")
if ILL == "D":
    print("\nOkay, so the UR for Declaratives must contain S/Verb so those are automatically included")
    print("What UR do you want to test?")
    print("To topicalize an item (S/Adv/O1/O2/PP) put a t after it: \'St\'")
    print("Provide an unordered list with the items separated by a slash: e.g. Adv/O1")
    UR      = input("Possible items to include: (Aux/O1/O2/PP/Adv/not/never)\n")
    UR     += "/S/Verb"
if ILL == "Q":
    pass
if ILL == "I":
    print("\nOkay, Imperatives cannot contain Aux or S, so those are not options for the UR")
    print("Also, imps must contain a Verb, so that is automatically included")
    print("What UR do you want to test?")
    print("Provide an unordered list with the items separated by a slash: e.g. Adv/O1") 
    UR      = input("Possible items to include: (O1/O2/PP/Adv/not/never)\n")
    UR     += "/Verb"

print("your UR is "+UR)
