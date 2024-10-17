valid_data = """\
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
John Doe,5000
Jane Smith,4500
"""

invalid_data_value_error = """\
Alex Korp,3000
invalid_worker,not_a_number
John Doe,5000
"""

invalid_data_missing_salary = """\
Alex Korp,3000
Mark Invalid,
John Doe,5000
"""

invalid_data_no_comma = """\
Alex Korp,3000
Invalid No Comma 4500
John Doe,5000
"""

invalid_data_missing_name = """\
Alex Korp,3000
,3200
John Doe,5000
"""

empty_file = ""
