import random

random_list: list[bool] = [random.choice([True, False]) for _ in range(3)]
print(random_list)
print("all true?", all(random_list))
print("any true?", any(random_list))
print("all false?", not any(random_list))
print("at least one false?", not all(random_list))
random_5: list[int] = [random.randint(-2, 2) for _ in range(5)]
print(random_5)
print("no zeroes at all?", all(random_5))
print("at least one number that is not zero?", any(random_5))
print("all zeroes", not any(random_5))
print("at least one zero?", not all(random_5))
