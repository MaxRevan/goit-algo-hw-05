import re
from typing import Callable

def generator_numbers(text: str):
    # Шаблон для пошуку дійсних чисел
    pattern = r'\b\d+\.\d+\b'  

    # Пошук у тексті за допомогою регулярних виразів   
    matches = re.findall(pattern, text)
    for match in matches:
        yield float(match)

def sum_profit(text: str, func: Callable):

    # Викликаємо генератор для отримання чисел
    numbers = func(text)
    
    # Сумуємо всі числа
    total = sum(numbers)
    
    return total


text = "Загальний дохід працівника складається з декількох частин: 2075.05 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
