import re
import sys

def parse_log_line(line):
    # Регулярний вираз для розбору рядка логу
    match = re.match(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.*)$', line)
    if match:
        return {'timestamp': match.group(1), 'level': match.group(2), 'message': match.group(3)}
    return None

def load_logs(file_path):
    # Завантажує лог-файл і повертає список записів
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log_entry = parse_log_line(line.strip())
                if log_entry:
                    logs.append(log_entry)
    except IOError as e:
        print(f"Помилка при читанні файлу логів: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs, level):
    # Фільтрує логи за рівнем логування
    return [log for log in logs if log['level'] == level]

def count_logs_by_level(logs):
    # Підраховує кількість записів за рівнем логування
    log_counts = {'INFO': 0, 'DEBUG': 0, 'ERROR': 0, 'WARNING': 0}
    for log in logs:
        if log['level'] in log_counts:
            log_counts[log['level']] += 1
    return log_counts

def display_log_counts(counts):
    # Виводить результати підрахунку в читабельній формі
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17} | {count:<8}")

def main():
    if len(sys.argv) < 2:
        print("Використання: <шлях_до_лог_файлу> [рівень_логування]")
        sys.exit(1)

    file_path = sys.argv[1]
    log_level = sys.argv[2].upper() if len(sys.argv) > 2 else None

    logs = load_logs(file_path)

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        print(f"\nДеталі логів для рівня '{log_level}':")
        for log in filtered_logs:
            print(f"{log['timestamp']} - {log['message']}")
        print()

    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)

if __name__ == "__main__":
    main()
