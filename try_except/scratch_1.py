def calculate_percent(value, total):
    try:
       percent = value * 100 / total
    except TypeError:
        print(f'Invalid values! "{value}" and "{total}" must be a valid number!')
    except ZeroDivisionError:
        print(f'Invalid values! "{value}" and "{total}" must be a valid number!')
    else:
        print(f'{value} from {total} is {percent} %')
    finally:
        print("I will always be displayed here!")


calculate_percent(1, 2)
calculate_percent('1', 2)
calculate_percent('a', None)
calculate_percent(28, 0)
calculate_percent(50, 99)