def get_cats_info(path):
    cats_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                if not line.strip():
                    continue

                parts = line.strip().split(',')

                if len(parts) != 3:
                    print(f"Warning: line skipped due to incorrect format: {line.strip()}")
                    continue

                cat_id, name, age = parts

                cats_list.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })

    except FileNotFoundError:
        print(f"Error: File not found at path {path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return cats_list

path_to_file = '/Users/wital1y/Desktop/Projects/goit-pycore-hw-04.git/cats_info.txt'
cats_info = get_cats_info(path_to_file)
print(cats_info)

