def generate_sql_from_text(text):
    if not text:
        return None
    text = text.lower()
    if "all employees" in text:
        return "SELECT * FROM employees"
    elif "engineering" in text:
        return "SELECT * FROM employees WHERE department = 'Engineering'"
    elif "salary" in text:
        return "SELECT name, salary FROM employees ORDER BY salary DESC"
    else:
        return None
