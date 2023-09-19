import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee_salary = employee['salary'].drop_duplicates()
    second = employee_salary.nlargest(2).iloc[-1] if len(employee_salary) >= 2 else None
    if second is not None:
        return pd.DataFrame(data = {"SecondHighestSalary": [second]})
    else:
        return pd.DataFrame(data = {'SecondHighestSalary': [None]})