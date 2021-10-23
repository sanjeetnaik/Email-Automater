import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Sanjeet1402",
  database = 'orders_clients'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM clients_info")

myresult = mycursor.fetchall()

ls_of_clients = []

for i in myresult:
    ls_of_clients.append(i[1])


def see_clients():

    mycursor.execute("SELECT * FROM clients_info")

    myresult = mycursor.fetchall()

    clients = []

    for i in myresult:
        clients.append(i)

    print()

    for i in range(0,len(clients),1):
        print('client name : ', clients[i][4])
        print('client country : ', clients[i][5])
        print('client company : ', clients[i][3])
        print('client address : ', clients[i][2])
        print()





def add_client(tclient_email = 'pain@somaiya.edu',tclient_phone = '9870011094',tclient_address = '177A Bleecker Street'
,tclient_company =  'gain', tclient_name = "pain", tclient_country = "akatsuki"):
   
    tclient_email = tclient_email
    tclient_phone = tclient_phone
    tclient_address = tclient_address
    tclient_company =  tclient_company
    tclient_name = tclient_name
    tclient_country = tclient_country

    if(tclient_email in ls_of_clients):
        print("Client Already Exists !!!!")
    
    else:
        sql = "INSERT INTO clients_info (client_email, client_phone, client_address, client_company, client_name, client_country) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (tclient_email, tclient_phone, tclient_address, tclient_company, tclient_name, tclient_country)
        mycursor.execute(sql, val)

        print(mycursor.rowcount, "was inserted.")

        mydb.commit()

def clients_by_country():
    mycursor.execute("CALL country_procedure()")
    mycursor.execute("SELECT * FROM country_clients")
    data = mycursor.fetchall()
    for i in data:
        print(i)

# def see_clients():
#     count =1
#     for i in myresult:
#         print("Client "+str(count), end = " : ")
#         print(i)
#         count+=1

while(True):

    print()
    print("1. Add new client ")
    print("2. See existing clients ")
    print("3. Check client by counrty ")
    print("4. Exit")
    print()
    choice  = int(input("Enter your choice : "))

    if(choice ==1):
        name = input("Input name : ")
        email = input("Input email : ")
        phone = input("Input phone : ")
        country = input("Input country : ")
        company = input("Input company : ")
        address = input("Input address : ")

        add_client(tclient_email=email, tclient_address=address, tclient_company=company, tclient_country=country, tclient_name=name, tclient_phone=phone)

    elif(choice == 2):
        see_clients()

    elif (choice == 3):
        clients_by_country()
    
    elif(choice == 4):
        break



