from settings import  path

def total_salary(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        if not lines:
            return 'Empty file: no workers to process'

        total_salary = 0
        valid_workers = 0
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            if ',' not in line:
                return 'Invalid data in file'
            
            name, salary_str = line.split(',', 1)
            
            name = name.strip()
            salary_str = salary_str.strip()
            
            if not name:
                return 'No valid workers to calculate salary'
            
            if not salary_str:
                return 'Invalid data salary'

            try:
                salary = int(salary_str)
            except ValueError:
                return 'Invalid Data Value error' 
            
            total_salary += salary
            valid_workers += 1
        
        if valid_workers == 0:
            return 'No valid workers to calculate salary'
        
        average_salary = int(total_salary / valid_workers)
        return str(total_salary), str(average_salary)

    except OSError:
        return 'Error: File could not be read. It may be corrupted.'
    except UnicodeDecodeError:
        return 'Error: File encoding issue. The file might be corrupted or in the wrong format.'
    except Exception as e:
        return f'An unexpected error occurred: {str(e)}'


