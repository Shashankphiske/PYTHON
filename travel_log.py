country = input("Enter the visited country :")
city = []

a = int(input("enter the number of cities visited :"))
for i in range(0,a):
    city.append(input("Enter the city visited :"))

number = int(input("Enter the number of times you have travelled the country :"))
travelled  = []
def travel_log(country, number, city_list):
    sample = {"Country":country,
              "Times_visited":number,
              "Cities_visited":city_list}
    travelled.append(sample)
travel_log(country,number,city)

for i in travelled:
    print("Country visited :",i.get("Country"))
    print("Number of times visited :",i.get("Times_visited"))
    print("Cities visited :",i.get("Cities_visited"))
    