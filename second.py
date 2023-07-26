# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.

def cash(names: list[str], salary: list[int], bonus: list[str]) -> dict | None:
    d = {}
    if len(names) == len(salary) == len(bonus):
        return {names[i]: salary[i] * (eval(bonus[i][:-2]) / 100 + 1) for i in range(len(names))}
    else:
        return None


if __name__ == "__main__":
    names = ["Bob", "Alice", "Mary"]
    salary = [5_000, 4_500, 9_999]
    bonus = ["5.5%", "3.5%", "6.9%"]
    for i,j in cash(names, salary, bonus).items():
        print(f"Name: {i}\nHoliday bonus: {j}")
