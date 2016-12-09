def guest_greeting():
    print "Welcome Guest"


def ret_customer():
    print "Returning Customer"
    custid = raw_input("Enter your CustomerID: ")
    customer_data = find_ret_cust(custid)
    if customer_data == "False":
        print "Could not find your ID number: "+custid+"\nPlease Try Again"
        ret_customer()
    else:
        for word in customer_data:
            print word


def find_ret_cust(customer):
    try:
        with open("CustomerList.txt","r") as file:
            data = file.readlines()
            for line in data:
                words = line.split(',')
                if customer == words[0]:
                    return words
        return "False"
    except: print "Could not open CustomerList File"



choice = 0

while choice != -1:
    print "Hello..."
    print "1. Returning Customer"
    print "2. New Customer"
    print "3. Guest"

    choice = raw_input("Please enter a number: ")

    if choice == '1':
        ret_customer()
        choice = -1
    elif choice == '2':
        print "New Customer"
        choice = -1
    elif choice == '3':
        guest_greeting()
        choice = -1
    else:
        print "ERROR: Not Valid"
