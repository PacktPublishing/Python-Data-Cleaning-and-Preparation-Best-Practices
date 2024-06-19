import random

# Simulated data usage metrics
def simulate_data_usage():
    # Simulate the number of users in the organization
    num_users = 500
    
    # Simulate data utilization rates for each user (percentage)
    data_utilization_rates = [random.uniform(20, 90) for _ in range(num_users)]
    
    # Simulate the number of data requests or queries made by each user
    data_requests = [random.randint(1, 100) for _ in range(num_users)]
    
    # Calculate the overall data utilization rate for the organization
    organization_data_utilization_rate = sum(data_utilization_rates) / num_users
    
    # Calculate the total number of data requests or queries
    total_data_requests = sum(data_requests)
    
    # Simulate user satisfaction surveys (on a scale of 1 to 5)
    user_satisfaction_scores = [random.randint(1, 5) for _ in range(num_users)]
    
    # Calculate average user satisfaction score
    avg_user_satisfaction_score = sum(user_satisfaction_scores) / num_users
    
    return {
        "data_utilization_rates": data_utilization_rates,
        "organization_data_utilization_rate": organization_data_utilization_rate,
        "data_requests": data_requests,
        "total_data_requests": total_data_requests,
        "user_satisfaction_scores": user_satisfaction_scores,
        "avg_user_satisfaction_score": avg_user_satisfaction_score,
    }

# Run the simulation
data_usage_metrics = simulate_data_usage()

# Display the results
print("\nOrganization Data Utilization Rate:")
print(f"{data_usage_metrics['organization_data_utilization_rate']:.2f}%")
print("\nTotal Number of Data Requests or Queries:")
print(data_usage_metrics["total_data_requests"])
print("\nAverage User Satisfaction Score:")
print(f"{data_usage_metrics['avg_user_satisfaction_score']:.2f}")
