def calculate_pf(basic_salary, wage_ceiling=15000, rate=0.12):
    """Employee PF: 12% of basic salary, capped at the wage ceiling."""
    pf_wage = min(basic_salary, wage_ceiling)
    return round(pf_wage * rate)