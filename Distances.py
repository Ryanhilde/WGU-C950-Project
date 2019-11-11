import csv
import datetime

# Read in csv file that is the mapping of distances between locations
with open('WGUDistanceData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    readCSV = list(readCSV)

# Read in csv file that is the names of all possible delivery locations
with open('WGUDistanceNameData.csv') as csv_name_file:
    name_readCSV = csv.reader(csv_name_file, delimiter=',')
    name_readCSV = list(name_readCSV)

    # a list of row/column values are inserted into this function. This function then calculates the total distance
    # that distance is then returned and each iteration represents a distance between two locations
    # Space-time complexity is O(1)
    def check_distance(row_value, column_value, sum_of_distance):
        distance = readCSV[row_value][column_value]
        if distance is '':
            distance = readCSV[column_value][row_value]

        sum_of_distance += float(distance)
        return sum_of_distance

    # this function is very similar to the function above but returns a current distance
    # Space-time complexity is O(1)
    def check_current_distance(row_value, column_value):
        distance = readCSV[row_value][column_value]
        if distance is '':
            distance = readCSV[column_value][row_value]
        return float(distance)
    # this is the time that the first truck leaves the hub
    first_time_list = ['8:00:00']
    second_time_list = ['9:10:00']
    third_time_list = ['11:00:00']

    # this function takes a distance then divides it by 18. It then uses divmod to display a time and appends 00
    # this string that is a timestamp is then split and turned into a datetime timedelta object
    # that object is then added to sum which represents total distance for a particular truck
    # runtime of function is O(N)
    def check_time_first_truck(distance):
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        first_time_list.append(final_time)
        sum = datetime.timedelta()
        for i in first_time_list:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += d
        return sum
    # Repeated function for second truck
    def check_time_second_truck(distance):
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        second_time_list.append(final_time)
        sum = datetime.timedelta()
        for i in second_time_list:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += d
        return sum
    # Repeated function for the third truck
    def check_time_third_truck(distance):
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        third_time_list.append(final_time)
        sum = datetime.timedelta()
        for i in third_time_list:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += d
        return sum

    # this function returns the time objects to use in the Packages.py file
    # Space-time complexity is O(1)
    def check_address():
        return name_readCSV
    # these lists represent the sorted trucks that are put in order of efficiency in the function below
    first_optimized_truck = []
    first_optimized_truck_index_list = []
    second_optimized_truck = []
    second_optimized_truck_index_list = []
    third_optimized_truck = []
    third_optimized_truck_index_list = []

    # This is my sorting algorithm that uses a greedy approach to automate optimizing the delivery route for each truck.
    # the function takes 3 parameters (see section 1)
    # First parameter is the list of packages on a truck that has not been optimized yet
    # The second parameter represents the truck number
    # The third parameter represents the current location that is updated each time a truck moves

    # The base case of the algorithm is stated in the initial if statement (see section 2). This breaks the recursion
    # once the input list has a size of 0.
    # It starts by setting a "lowest value" of 50.0 and then uses the check current distance function to loop through
    # every possible point that is currently available to see if there is a lower value. If there is than the lowest
    # value is updated and the search continues (see section 3). Once it has searched through all possible routes
    # the truck can go given the available packages, it then adds that package object and associated index to
    # new lists (see section 4). To ensure that the right truck packages are being associated, the second parameter
    # is checked. If the truck truck is being sorted than the optimized delivery path will be associated to the lists
    # first_optimized_truck and first_optimized_truck_index. Each time these lists are updated, the lowest value is
    # removed from the argument list, truck_distance_list. This will allow us to update current location and recursively
    # call the function. Once the argument list is empty it will return the empty list and the function call will end.

    # The space-time complexity of this algorithm is O(N^2). This is due to the two for loops and the repeated lookup
    # functionality required to determine the lowest possible path then move the truck to that position.

    def calculate_shortest_distance(truck_distance_list, truck_number, current_location):  # section 1
        if len(truck_distance_list) == 0:  # section 2
            return truck_distance_list
        else:  #
            try:
                lowest_value = 50.0
                new_location = 0
                for index in truck_distance_list:
                    if check_current_distance(current_location, int(index[1])) <= lowest_value:
                        lowest_value = check_current_distance(current_location, int(index[1]))  # section 3
                        new_location = int(index[1])
                for index in truck_distance_list:  # section 4
                    if check_current_distance(current_location, int(index[1])) == lowest_value:
                        if truck_number == 1:
                            first_optimized_truck.append(index)
                            first_optimized_truck_index_list.append(index[1])
                            pop_value = truck_distance_list.index(index)
                            truck_distance_list.pop(pop_value)
                            current_location = new_location
                            calculate_shortest_distance(truck_distance_list, 1, current_location)
                        elif truck_number == 2:
                            second_optimized_truck.append(index)
                            second_optimized_truck_index_list.append(index[1])
                            pop_value = truck_distance_list.index(index)
                            truck_distance_list.pop(pop_value)
                            current_location = new_location
                            calculate_shortest_distance(truck_distance_list, 2, current_location)
                        elif truck_number == 3:
                            third_optimized_truck.append(index)
                            third_optimized_truck_index_list.append(index[1])
                            pop_value = truck_distance_list.index(index)
                            truck_distance_list.pop(pop_value)
                            current_location = new_location
                            calculate_shortest_distance(truck_distance_list, 3, current_location)
            except IndexError:
                pass

    first_optimized_truck_index_list.insert(0, '0')

    # Space-time complexity is O(1)
    def first_optimized_truck_index():
        return first_optimized_truck_index_list

    # Space-time complexity is O(1)
    def first_optimized_truck_list():
        return first_optimized_truck

    second_optimized_truck_index_list.insert(0, '0')

    # Space-time complexity is O(1)
    def second_optimized_truck_index():
        return second_optimized_truck_index_list

    # Space-time complexity is O(1)
    def second_optimized_truck_list():
        return second_optimized_truck

    third_optimized_truck_index_list.insert(0, '0')

    # Space-time complexity is O(1)
    def third_optimized_truck_index():
        return third_optimized_truck_index_list

    # Space-time complexity is O(1)
    def third_optimized_truck_list():
        return third_optimized_truck
