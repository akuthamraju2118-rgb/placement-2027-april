print("--- Day 5: Dubai Enterprise API Simulation ---")

api_payload = {
    "candidate": "Akshith",
    "target_ctc_aed": 240000,
    "skills": ["DSA", "AIML", "FastAPI"]
}
print("Incoming API Payload Data:", api_payload)

api_payload.update({"visa_status": "Golden Visa Track"})
print("Updated Database State   :", api_payload)

print("\n--- JSON Field Extraction ---")
print(f"Verified Name   : {api_payload.get('candidate')}")
print(f"Verified Stack  : {api_payload.get('skills')}")
print(f"Visa Allocation : {api_payload.get('visa_status')}")
