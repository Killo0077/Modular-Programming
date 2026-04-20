# Week 7 - Exam Workshop 2026 (practice)

## Customer Loyalty Report Program


# two list / append a new customer to the list / allow the user to update a customer's spending / Determinate loyalty tiers/ 
# Display the number  and name so those receiving cinema tickets subject to a minimun spend.




# Creating a Loyalty Tier Function
def loyalty_tiers(amount):
    if amount < 200:
        return "Bronze"
    elif amount <800:
        return "Silver"
    else:
        return "Gold"

def table(names_list,money):
     for i in range (len(names_list)):
        tier = loyalty_tiers(money[i])
        print(f"{names_list[i]:20} {money[i]:10} {tier }")
# creating lints.

def main():

    names = ['Olivia Smith', 'Daniel Wu', 'Grace Pate', 'Marcus Lee']
    spent = [120.78, 540.34, 980.27, 250.00]

    # add new customer and amount
    name = input("Add a new customer: ")
    amount = float(input(f"Enter amount {name} has: "))

    names.append(name)
    spent.append(amount)

    # print list
    print("===========================================")
    print("customer Name ---- Total Spent ($)-----Tier")
    print("===========================================")

    table(names,spent)
   # Determining the tier using a function
    for i in range (len(names)):
        tier = loyalty_tiers(spent[i])
        print(f"{names[i]:20} {spent[i]:10} {tier }")

    
    # Finding the highest spending customer
    max_spend = max(spent)
    index = spent.index(max_spend)

    print("\nThe highest spending customer is: \n",names[index])


# Update a Customer's Spending

    search = input("Enter customer name to update spending: ")

    if search in names:
        index = names.index(search)
        extra = float(input("Enter additional spending: "))
        spent[index] += extra
        tier = loyalty_tiers(spent[index])
        print(f"{search} , new total is {spent[index]} and is a  {tier} customer")
    else:
        print("Customer not found.")

# # Display a table function

# print("********************************")
# print("Customer Name -------------- Tier")
# print("********************************")

# for i in range(len(names)):
#     tier = loyalty_tiers(spent[i])
#     print(f"{names[i]:20} {tier}")
    
    


    






if __name__  == "__main__":
    main()