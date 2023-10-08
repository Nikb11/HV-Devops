##parkinglot

car_rate=20
bike_rate=10

hours_open=6

num_of_cars=int(input("enter no of cars: "))
num_of_bikes=int(input("enter no of bikes: "))

collection_of_cars=car_rate*num_of_cars*hours_open
collection_of_bikes=bike_rate*num_of_bikes*hours_open
amt_collected=collection_of_cars+collection_of_bikes

if(amt_collected>10000):
    print("good day")
else:
    print("not a good day")    
  