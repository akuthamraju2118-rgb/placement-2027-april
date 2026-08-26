print("--- Day 7: Live HFT Data Stream Simulation ---")
price = 10.0

while True:
    price += 1.5
    print(f"Current live ticker price: {price} AED")
    
    if price < 14.0:
        continue  # Skips execution lines below and goes to next loop cycle
        
    if price >= 16.0:
        print("Target threshold breached! Executing trade allocation.")
        break  # Halts the infinite loop instantly
