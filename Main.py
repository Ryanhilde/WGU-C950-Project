# Ryan Hildebrant Student ID #: 000709587

from ReadCSV import get_hash_map
from Packages import total_distance
import datetime


class Main:
    # This is the display message that is shown when the user runs the program. The interface is accessible from here
    print('Welcome to the WGUPS package tracking system!')
    print('Current route was completed in', "{0:.2f}".format(total_distance(), 2), 'miles.')
    start = input("To begin, please type 'lookup' to search for an individual package or "
                  "type 'timestamp' to view delivery status at a give time: ")
    # Space-time complexity is O(N)
    while start is not 'exit':
        # if user types 'timestamp' then they are prompted for a time to display. Once a time is provided it will
        # display all packages at that timestamp. Runtime of this process is O(N)
        if start == 'timestamp':
            try:
                package_status_time = input('Please enter a time in the HH:MM:SS format: ')
                (h, m, s) = package_status_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                # Space-time complexity is O(N^2)
                for count in range(1,41):
                    try:
                        first_time = get_hash_map().get(str(count))[9]
                        second_time = get_hash_map().get(str(count))[10]
                        (h, m, s) = first_time.split(':')
                        convert_first_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        (h, m, s) = second_time.split(':')
                        convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    except ValueError:
                        pass
                    # First checks all packages against the given time determine if they have left the hub yet.
                    if convert_first_time >= convert_user_time:
                        get_hash_map().get(str(count))[10] = 'At Hub'
                        get_hash_map().get(str(count))[9] = 'Leaves at ' + first_time
                        print('Package ID:', get_hash_map().get(str(count))[0], '   Street address:',
                              get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                              get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                              '  Required delivery time:', get_hash_map().get(str(count))[6],
                              ' Package weight:', get_hash_map().get(str(count))[7], '  Truck status:',
                              get_hash_map().get(str(count))[9], '  Delivery status:',
                              get_hash_map().get(str(count))[10])
                    elif convert_first_time <= convert_user_time:
                        # Then checks to see which packages have left the hub but have not been delivered yet
                        if convert_user_time < convert_second_time:
                            get_hash_map().get(str(count))[10] = 'In transit'
                            get_hash_map().get(str(count))[9] = 'Left at ' + first_time
                            print('Package ID:', get_hash_map().get(str(count))[0], '   Street address:',
                                  get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                                  get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                                  '  Required delivery time:', get_hash_map().get(str(count))[6],
                                  ' Package weight:', get_hash_map().get(str(count))[7], '  Truck status:',
                                  get_hash_map().get(str(count))[9], '  Delivery status:',
                                  get_hash_map().get(str(count))[10])
                        # Finally checks all packages that have already been delivered and displays the delivered time
                        else:
                            get_hash_map().get(str(count))[10] = 'Delivered at ' + second_time
                            get_hash_map().get(str(count))[9] = 'Left at ' + first_time
                            print('Package ID:', get_hash_map().get(str(count))[0], '   Street address:',
                                  get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                                  get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                                  '  Required delivery time:', get_hash_map().get(str(count))[6],
                                  ' Package weight:', get_hash_map().get(str(count))[7],'  Truck status:',
                                  get_hash_map().get(str(count))[9],'  Delivery status:',
                                  get_hash_map().get(str(count))[10])
            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Invalid entry!')
                exit()
        # If 'lookup' is selected than the user is prompted for a package ID followed by a timestamp
        # Once that information is entered then the user will be shown a particular package at a given time
        elif start == 'lookup':
            try:
                count = input('Please enter a package ID to lookup: ')
                first_time = get_hash_map().get(str(count))[9]
                second_time = get_hash_map().get(str(count))[10]
                package_status_time = input('Please enter a time in the HH:MM:SS format: ')
                (h, m, s) = package_status_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = first_time.split(':')
                convert_first_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = second_time.split(':')
                convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                # First checks if the package has left the hub yet
                if convert_first_time >= convert_user_time:

                    get_hash_map().get(str(count))[10] = 'At Hub'
                    get_hash_map().get(str(count))[9] = 'Leaves at ' + first_time
                    print('Package ID:', get_hash_map().get(str(count))[0], '   Street address:',
                          get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                          get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                          '  Required delivery time:', get_hash_map().get(str(count))[6],
                          ' Package weight:', get_hash_map().get(str(count))[7], '  Truck status:',
                          get_hash_map().get(str(count))[9], '  Delivery status:',
                          get_hash_map().get(str(count))[10])
                elif convert_first_time <= convert_user_time:
                    # Then checks if the package has left the hub but has not been delivered yet
                    if convert_user_time < convert_second_time:
                        get_hash_map().get(str(count))[10] = 'In transit'
                        get_hash_map().get(str(count))[9] = 'Left at ' + first_time
                        print('Package ID:', get_hash_map().get(str(count))[0], '   Street address:',
                              get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                              get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                              '  Required delivery time:', get_hash_map().get(str(count))[6],
                              ' Package weight:', get_hash_map().get(str(count))[7], '  Truck status:',
                              get_hash_map().get(str(count))[9], '  Delivery status:',
                              get_hash_map().get(str(count))[10])
                    # If the package has already been delivered than it displays the time
                    else:
                        get_hash_map().get(str(count))[10] = 'Delivered at ' + second_time
                        get_hash_map().get(str(count))[9] = 'Left at ' + first_time
                        print('Package ID:', get_hash_map().get(str(count))[0], '   Street address:',
                              get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                              get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                              '  Required delivery time:', get_hash_map().get(str(count))[6],
                              ' Package weight:', get_hash_map().get(str(count))[7], '  Truck status:',
                              get_hash_map().get(str(count))[9], '  Delivery status:',
                              get_hash_map().get(str(count))[10])
            except ValueError:
                print('Invalid entry')
                exit()
        elif start == 'exit':
            exit()
        else:
            print('Invalid entry!')
            exit()