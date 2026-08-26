print("--- Day 8: Automated System Compensation Calculator ---")

# Defining a reusable mathematical processing engine
def calculate_tax_free_package(base_aed, performance_bonus):
    total_monthly = base_aed + performance_bonus
    total_annual_inr = (total_monthly * 12) * 22.7
    return total_annual_inr

# Calling the custom calculation engine with specific inputs
anish_package = calculate_tax_free_package(20000, 4000)
print(f"Calculated Annual Profile Value: ₹{anish_package:,.2f} INR per year")
