def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    try:
        for number in numbers:
            try:
                result += number
            except TypeError:
                incorrect_data += 1
                print(f"Некорректный тип данных для подсчета суммы - {number}")
    except TypeError:
        return None
    return result, incorrect_data


def calculate_average(numbers):
    result = personal_sum(numbers)
    try:
        return result[0] / (len(numbers) - result[1])
    except (ZeroDivisionError, TypeError) as err:
        return 0 if err.__class__.__name__ == 'ZeroDivisionError' else None



