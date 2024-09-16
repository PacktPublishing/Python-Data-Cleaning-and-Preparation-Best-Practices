import random

# Simulate a dataset with compliance checks
def simulate_data_compliance(num_records):
    data_records = []
    compliant_count = 0  # Counter for compliant records

    for _ in range(num_records):
        # Generate a random record (e.g., containing age and consent fields)
        age = random.randint(18, 100)
        consent_given = random.choice([True, False])

        # Define compliance rules
        age_rule = age >= 18
        consent_rule = age >= 18 and consent_given

        # Check compliance with specific regulations
        age_compliant = "Age Compliant" if age_rule else "Age Non-Compliant"
        consent_compliant = "Consent Compliant" if consent_rule else "Consent Non-Compliant"

        # Define overall compliance status
        compliance_status = "Compliant" if age_rule and consent_rule else "Non-Compliant"

        # Count compliant records
        if compliance_status == "Compliant":
            compliant_count += 1

        data_records.append({
            "Age": age,
            "Consent Given": consent_given,
            "Age Compliance": age_compliant,
            "Consent Compliance": consent_compliant,
            "Overall Compliance Status": compliance_status
        })

    # Calculate the percentage of compliant records
    percentage_compliant = (compliant_count / num_records) * 100

    return data_records, percentage_compliant

# Define the number of data records to simulate
num_records = 100

# Simulate data compliance checks
data_records, percentage_compliant = simulate_data_compliance(num_records)

# Display the results for a sample of data records and the percentage of compliance
sample_size = 10
for record in data_records[:sample_size]:
    print(record)

print(f"\nPercentage of Compliant Records: {percentage_compliant:.2f}%")
