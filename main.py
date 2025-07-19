import csv
import itertools


class SmallNumberCombination:
    def __init__(self, best_sum: int, best_combination: list, iterations_count: int):
        self.best_sum: int = best_sum
        self.best_combination: int = best_combination
        self.iterations_count: int = iterations_count


def get_small_number_in_row(input_row: list) -> list:
    temp_small_number = []

    for number in input_row:
        if not number:
            continue

        temp_small_number.append(int(number))

    return temp_small_number


def get_best_small_number_combinations(big_number: int, small_numbers: list) -> SmallNumberCombination:
    iterations_count: int = 0
    best_sum: int = 0
    best_combination: list = []

    for combination_count in range(1, len(small_numbers) + 1):
        for combination in itertools.combinations(small_numbers, combination_count):
            iterations_count = iterations_count + 1

            combination_sum = sum(combination)
            if big_number >= combination_sum > best_sum:
                best_sum = combination_sum
                best_combination = combination

    return SmallNumberCombination(best_sum=best_sum, best_combination=best_combination, iterations_count=iterations_count)


if __name__ == '__main__':
    with open('input.csv') as file:
        csv_file = csv.reader(file)

        for row in csv_file:
            big_number: int = int(row[0])
            small_numbers: list = get_small_number_in_row(row[1:])

            result = get_best_small_number_combinations(big_number=big_number, small_numbers=small_numbers)

            print(f"Big number is {big_number}")
            print(f"Closest sum is {result.best_sum}")
            print(f"The best combination is: {result.best_combination}")
            print(f"iterations_count: {result.iterations_count}")
            print()
