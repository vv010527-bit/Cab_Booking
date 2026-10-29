def Total_Fare_Amount(dist, fare):
    return dist * fare

# Initialize ride history list outside the main execution loop
if 'Ride_History' not in locals():
    Ride_History = []

while True:
    print("\n================ MENU ================")
    print("1. Book a Ride\n2. Calculate Fare\n3. Customer Details (Last Booking)\n4. Show All Riders Details (History)\n5. Exit")
    try:
        Function = int(input("Select an option (1-5): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if Function == 1:
        print("\n======== BOOK A RIDE ========")
        try:
            name = input("Enter YOUR Name : ")
            pickup = input("Enter YOUR Pick-UP Location : ")
            dropoff = input("Enter YOUR Drop-Off Location : ")
            distance = float(input("Enter YOUR Distance (km) : "))
            date = input("Enter YOUR Date : ")

            customer = {
                "Name": name,
                "Pick_UP_Location": pickup,
                "Drop_Off_Location": dropoff,
                "Distance": distance,
                "Date": date
            }

            Ride_History.append(customer)
            print("Ride Booked Successfully!")
        except ValueError:
            print("Invalid input for distance. Booking failed.")

    elif Function == 2:
        print("\n======== CALCULATE FARE ========")
        try:
            Distance = float(input("Enter Ride Distance to calculate fare: "))
            if Distance < 0:
                print("Distance cannot be negative.")
            elif Distance <= 10:
                Fare_Amount = 12
            elif Distance <= 15:
                Fare_Amount = 11
            else:
                Fare_Amount = 10

            total = Total_Fare_Amount(Distance, Fare_Amount)
            print(f"Total Fare: ${total:.2f}")
        except ValueError:
            print("Please enter a valid numeric distance.")

    elif Function == 3:
        print("\n---------------- Last Customer Details --------------------")
        if Ride_History:
            last_customer = Ride_History[-1]
            print(f"Name : {last_customer['Name']}")
            print(f"Pick_UP_Location : {last_customer['Pick_UP_Location']}")
            print(f"Drop_Off_Location : {last_customer['Drop_Off_Location']}")
            print(f"Distance : {last_customer['Distance']} km")
            print(f"Date : {last_customer['Date']}")
        else:
            print("No bookings found yet. Please book a ride first.")

    elif Function == 4:
        print("\n===== All Riders Details (History) =====")
        if not Ride_History:
            print("No ride history available.")
        else:
            for i, ride in enumerate(Ride_History, 1):
                print(f"\nRide #{i}:")
                print(f"  Name: {ride['Name']}")
                print(f"  Route: {ride['Pick_UP_Location']} -> {ride['Drop_Off_Location']}")
                print(f"  Distance: {ride['Distance']} km")
                print(f"  Date: {ride['Date']}")

    elif Function == 5:
        print("Thank you for using the ride system. Goodbye!")
        break
    else:
        print("Invalid selection. Please choose a number between 1 and 5.")