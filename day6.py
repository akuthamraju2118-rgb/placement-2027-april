print("--- Day 6: High-Speed System Token Router ---")

# 1. MATCH CASE: Route currency tokens instantly based on region
token = input("Enter asset token category (AED/INR/USD): ").strip().upper()

match token:
    case "AED":
        print("Routing Protocol: Direct transfer to Dubai DIFC Liquidity Pool.")
    case "INR":
        print("Routing Protocol: Processing via National Gateway settlement systems.")
    case "USD":
        print("Routing Protocol: Accessing Global Federal Reserve exchange desks.")
    case _:
        print("Routing Protocol: Unknown asset class. Transaction terminated.")

# 2. FOR LOOP: Simulate a 5-day continuous portfolio compilation sequence
print("\n--- Initiating 5-Day System Compilation Sequence ---")
for day in range(1, 6):
    print(f"Day {day}: Processing data array blocks at microsecond speeds...")
