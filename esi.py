"""ESI (Employees' State Insurance) calculations for the demo HRMS.

Rates and the wage ceiling below are example values. Verify them against
the current ESIC notifications before using this in real payroll.
"""
import math

ESI_WAGE_CEILING = 21000   # monthly gross wage limit for ESI coverage
EMPLOYEE_RATE = 0.0075     # employee share: 0.75% of gross wages
EMPLOYER_RATE = 0.0325     # employer share: 3.25% of gross wages


def is_esi_applicable(gross_salary, ceiling=ESI_WAGE_CEILING):
    """ESI applies only when monthly gross wages are within the ceiling."""
    return gross_salary <= ceiling


def esi_employee_share(gross_salary):
    """Employee contribution, rounded up to the next rupee (verify rule)."""
    if not is_esi_applicable(gross_salary):
        return 0
    return math.ceil(gross_salary * EMPLOYEE_RATE)


def esi_employer_share(gross_salary):
    """Employer contribution, rounded up to the next rupee (verify rule)."""
    if not is_esi_applicable(gross_salary):
        return 0
    return math.ceil(gross_salary * EMPLOYER_RATE)


def esi_summary(gross_salary):
    """Return all ESI figures for one employee as a dictionary."""
    employee = esi_employee_share(gross_salary)
    employer = esi_employer_share(gross_salary)
    return {
        "gross_salary": gross_salary,
        "applicable": is_esi_applicable(gross_salary),
        "employee_share": employee,
        "employer_share": employer,
        "total": employee + employer,
    }


if __name__ == "__main__":
    for salary in (15000, 21000, 30000):
        print(esi_summary(salary))
