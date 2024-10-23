def total_salary(path):
    try:
        total = 0
        count = 0
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1
        average = total / count if count > 0 else 0
        return total, average
    except FileNotFoundError:
        return "Error: File not found."
    except ValueError:
        return "Error: Incorrect file format."

data = """Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000"""

file_path = '/Users/wital1y/Desktop/Projects/goit-pycore-hw-04.git//salary_data.txt'

with open(file_path, 'w', encoding='utf-8') as file:
    file.write(data)


result = total_salary(file_path)
print(f"Загальна сума заробітної плати: {6000}, Середня заробітна плата: {2000}")

