from esi import (
    esi_summary,
    esi_employee_share,
    esi_employer_share,
    is_esi_applicable,
)

# Eligibility: ESI applies up to and including the 21,000 ceiling
assert is_esi_applicable(15000) is True
assert is_esi_applicable(21000) is True
assert is_esi_applicable(21001) is False
assert is_esi_applicable(30000) is False

# Contributions are zero when the employee is above the ceiling
assert esi_employee_share(30000) == 0
assert esi_employer_share(30000) == 0

# Example contributions for a 15,000 salary
assert esi_employee_share(15000) == 113   # 112.5 rounded up
assert esi_employer_share(15000) == 488   # 487.5 rounded up

# The summary combines everything
summary = esi_summary(15000)
assert summary["total"] == 113 + 488
assert esi_summary(30000)["applicable"] is False

print("All ESI tests passed")
