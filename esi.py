
"""ESI (Employees' State Insurance) contribution rules for the demo HRMS.

The rates and wage ceiling here are sample values. Please check them with
the latest ESIC notifications before this is used in real payroll.
"""
import math

ESI_WAGE_CEILING = 21000   # maximum monthly gross wage covered by ESI
EMPLOYEE_RATE = 0.0075     # employee pays 0.75% of gross wages
EMPLOYER_RATE = 0.0325     # employer pays 3.25% of gross wages


def is_esi_applicable(gross_wage, ceiling=ESI_WAGE_CEILING):
    """Return True when monthly gross wages are within the ESI ceiling."""
    return gross_wage <= ceiling


def esi_employee_share(gross_wage):
    """Employee ESI contribution, rounded up to the next full rupee."""
    if not is_esi_applicable(gross_wage):
        return 0
    return math.ceil(gross_wage * EMPLOYEE_RATE)


def esi_employer_share(gross_wage):
    """Employer ESI contribution, rounded up to the next full rupee."""
    if not is_esi_applicable(gross_wage):
        return 0
    return math.ceil(gross_wage * EMPLOYER_RATE)


def esi_summary(gross_wage):
    """Return all ESI figures for one employee as a dictionary."""
    employee = esi_employee_share(gross_wage)
    employer = esi_employer_share(gross_wage)
    return {
        "gross_salary": gross_wage,
        "applicable": is_esi_applicable(gross_wage),
        "employee_share": employee,
        "employer_share": employer,
        "total": employee + employer,
    }


if __name__ == "__main__":
    for salary in (15000, 21000, 30000):
        print(esi_summary(salary))
