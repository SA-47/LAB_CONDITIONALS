movietitle = "Black list"

movierating = int(input("Enter movie rating (out of 5): "))
popularityscore = float(input("Enter popularity score: "))

if movierating >= 4 and popularityscore > 80:
   print("Highly recommended")
elif movierating >= 3 and popularityscore > 70:
   print("I recommended it. It is good")
elif movierating <= 2 and popularityscore > 60:
   print("You should check it out!")
elif movierating <= 2 and popularityscore < 50:
   print("Don't watch it. It is a waste of time")