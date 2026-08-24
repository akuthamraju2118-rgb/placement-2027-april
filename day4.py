print("--- Day 4: core Data structures (Lists and Tuples) ---")

companies = ["Amazon", "Atlassian", "Microsoft"]
print("Initial companies lists:", companies)


companies.append("Google")
print("updated companies lists:", companies)

destinations = ("Japan", "Australia")
print("\nFixed Relocation Targets Tuple:", destinations)


try:
    destinations[0] = "dubai"
except TypeError as error:
    print(f"Tuple protected! Expected Error: {error}")
    