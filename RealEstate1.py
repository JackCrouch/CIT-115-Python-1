#get a valid sales value
def get_sales_value():
    while True:
        try:
            value = float(input("Enter property sales value: "))
            if value > 0:
                return value
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")
#calculate the median
def calculate_median(sales_list):
    sales_list.sort()
    n = len(sales_list)
    if n % 2 == 0:
        return (sales_list[n // 2 - 1] + sales_list[n // 2]) / 2
    else:
        return sales_list[n // 2]
#main program
def main():
    sales = []

    while True:
        sales.append(get_sales_value())
        another = input("Enter another value? (Y/N): ").strip().upper()
        if another == 'N':
            break

#sorting and calculating
    sales.sort()
    total = sum(sales)
    minimum = min(sales)
    maximum = max(sales)
    average = total / len(sales)
    median = calculate_median(sales)
    commission = total * 0.03

#results
    print("\nProperty Sales:")
    for i, sale in enumerate(sales, 1):
        print(f"Property {i}: ${sale:,.2f}")

    print(f"\nMinimum: ${minimum:,.2f}")
    print(f"Maximum: ${maximum:,.2f}")
    print(f"Total: ${total:,.2f}")
    print(f"Average: ${average:,.2f}")
    print(f"Median: ${median:,.2f}")
    print(f"Commission: ${commission:,.2f}")

#run
if __name__ == "__main__":
    main()
