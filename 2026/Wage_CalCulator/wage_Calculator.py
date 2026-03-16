

def wage_Calculator(successful_Deliveries):

    successful_Deliveries = int(input("Enter number of successful deliveries: "))
    base_Salary = 5000;
    total_Package = 100

    collection_Rate = (successful_Deliveries / total_Package) * 100

    if collection_Rate < 50:
        amount_Per_Parcel = 160

    elif collection_Rate <= 59:
        amount_Per_Parcel = 200

    elif collection_Rate <= 69:
        amount_Per_Parcel = 250

    else:
        amount_Per_Parcel = 500

    total_Wage = (successful_Deliveries * amount_Per_Parcel) + base_Salary
    return total_Wage


print(wage_Calculator(1))
