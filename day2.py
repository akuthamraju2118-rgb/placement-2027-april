print("--- Day 2: Dynamic Placement Profile Tracker ---")

student_name = input("Enter your name: ")
target_ctc = input("Enter your target package (in LPA): ")

numeric_package = int(target_ctc)
shortfall_calculation = 16 - numeric_package

print("\n--- Student Tech Profile Created ---")
print(f"Candidate Name : {student_name}")
print(f"Current Target : {numeric_package} LPA")
print(f"Gap to Minimum Target: {shortfall_calculation} LPA")
