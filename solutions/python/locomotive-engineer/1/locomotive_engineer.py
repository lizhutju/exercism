"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    return list(args)
    


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    first,second,*rest = each_wagons_id
    each_wagons_id = [*rest,first,second]
    index = each_wagons_id.index(1)
    left = each_wagons_id[:index+1]
    right = each_wagons_id[index+1:]
    each_wagons_id = [*left,*missing_wagons,*right]
    return each_wagons_id

def add_missing_stops(route,**kwarg):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """

    stops=[]
    for key,value in kwarg.items():
        stops.append(value)
    route["stops"]= stops
    return route

def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    route.update(more_route_information)

    return route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    result = []

    for i in range(3):
        row = []

        for j in range(3):
            row.append(wagons_rows[j][i])

        result.append(row)

    return result
