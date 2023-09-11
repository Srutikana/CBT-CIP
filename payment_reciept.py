p1_name,p1_price="Apples",10.00
p2_name,p2_price="Mango",15.90
p3_name,p3_price="Lichi",5.50
p4_name,p4_price="Banana",5.00
p5_name,p5_price="Guava",7.80
p6_name,p6_price="Chilli",16.00
p7_name,p7_price="Tomato",22.99
p8_name,p8_price="Grapes",18.00
company_name="ALFANSO"
company_address="Beadon Street"
company_city="Kolkata"
Message="Thank You for shopping with us!!"
print("\t\t RECEIPT")

print("*"*50)
print(f"\t{company_name}")
print(f"{company_address},{company_city}")
print("*"*50)
print("\t Product name \t Product Price")
print("\t{}\t{}".format(p1_name.title(), p1_price))
print("\t{}\t{}".format(p2_name.title(), p2_price))
print("\t{}\t{}".format(p3_name.title(), p3_price))
print("\t{}\t{}".format(p4_name.title(), p4_price))
print("\t{}\t{}".format(p5_name.title(), p5_price))
print("\t{}\t{}".format(p6_name.title(), p6_price))
print("\t{}\t{}".format(p7_name.title(), p7_price))
print("\t{}\t{}".format(p8_name.title(), p8_price))
print("*"*50)
print("\t\t\t TOTAL")
total=p1_price+p2_price+p3_price+p4_price+p5_price+p6_price+p7_price+p8_price
print("\t\t\t Rs{}".format(total))
print("*"*50)
print('\t{}'.format(Message))

