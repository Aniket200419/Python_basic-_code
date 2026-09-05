print("..........MOVIE TICKET SYSTEM..........")

print("pushpa")
print("KGF")
print("Saman teri kasam")
print("Maharshi")
choice=int(input("choice the movie(1-4) :"))

if choice==1:
    movie_name="pushpa"
    price_per_ticket=200
elif choice==2:
    movie_name="KGF"
    price_per_ticket=250
elif choice==3:
    movie_name="Sanam teri kasam"
    price_per_ticket=300
elif choice==4:
    movie_name="Maharshi"
    price_per_ticket=150
else:
     print("invalid choice")

print("Show Time")
print("Morning Show(15.00AM)Discount:10%")
print("Night Show(7.30 PM) Discount:NO Discount")

Show_choice=int(input("Enter show choice(1-2)"))
if Show_choice==1:
    discount_percent=5
elif Show_choice==2:
    discount_percent=0
else:
    print("invalid show choice")

tickets=int(input("Enter number of tickets :——"))
Gross_amount=price_per_ticket*tickets
discount_amount=(Gross_amount*discount_percent)/100
net_amount=Gross_amount-discount_amount
print("========TICKET BILL========")
print("Movie_name:",movie_name)
print("Ticket_price:",price_per_ticket)
print("Show_discount",str(discount_percent)+ "%")
print("Gross_amount",Gross_amount)
print("Discount amount:",discount_amount)
print("Total_payable:",net_amount)
print("=========================")
print("Thank you for booking")