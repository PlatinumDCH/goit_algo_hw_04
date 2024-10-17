from pathlib import Path

path = Path() / "data.txt"


def get_cats_info(path):
    cats_list = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if not lines:
                return "Empty file: no data to process"
            for line in lines:
                if not line:
                    continue
                parts = line.strip().split(",")
                if len(parts) != 3:
                    return f"Invalid data format"

                id_obj, name_obj, age_obj = parts
               
                try:
                    age = int(age_obj)
                except ValueError:
                    return f"Invalid age value"
                
                cats_list.append({
                    "id": id_obj,
                    "name": name_obj,
                    "age": age
                    })
            

    except OSError:
        return "Error: File could not be read. It may be corrupted."
    except UnicodeDecodeError:
        return "Error: File encoding issue. The file might be corrupted or in\
        the wrong format."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
    
    return cats_list


print(get_cats_info(path))
