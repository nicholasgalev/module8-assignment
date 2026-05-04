# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
# Store in variable: services
# Example: services = {"Web Development": 150, "Data Analysis": 175, ...}
# Include at least 5 different services
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cybersecurity": 220,
    "Cloud Solutions": 200,
    "IT Support": 95
}

# TODO 2: Create customer dictionaries
# Each customer should have: company_name, contact_person, email, phone
# Create at least 4 customer dictionaries
# Example: customer1 = {"company_name": "ABC Corp", "contact_person": "John Smith", ...}
customer1 = {
    "company_name": "Sunrise Retail",
    "contact_person": "Emily Carter",
    "email": "emily@sunriseretail.com",
    "phone": "555-1001"
}

customer2 = {
    "company_name": "Peak Financial",
    "contact_person": "Michael Lee",
    "email": "michael@peakfinancial.com",
    "phone": "555-1002"
}

customer3 = {
    "company_name": "GreenTech Manufacturing",
    "contact_person": "Sophia Martinez",
    "email": "sophia@greentechmfg.com",
    "phone": "555-1003"
}

customer4 = {
    "company_name": "BlueWave Media",
    "contact_person": "Daniel Brooks",
    "email": "daniel@bluewavemedia.com",
    "phone": "555-1004"
}

# TODO 3: Create a master customers dictionary
# Store in variable: customers
# Use customer IDs as keys and customer dictionaries as values
# Example: customers = {"C001": customer1, "C002": customer2, ...}
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
# Add your code here to display all customer information
for customer_id, customer_info in customers.items():
    print(customer_id)
    for key, value in customer_info.items():
        print(f"  {key}: {value}")
    print()

# TODO 5: Look up specific customers
# Use dictionary access to:
# - Get and display customer C002's information (store in c002_info)
# - Get and display customer C003's contact person (store in c003_contact)
# - Try to get customer C999 (doesn't exist) using .get() with a default message (store in c999_info)

print("\n\nCustomer Lookups:")
print("-" * 60)
# Add your code here
c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer C999 not found")

print("C002 Information:", c002_info)
print("C003 Contact Person:", c003_contact)
print("C999 Information:", c999_info)

# TODO 6: Update customer information
# - Change customer C001's phone number
# - Add a new field "industry" to customer C002
# - Display the updated customer information

print("\n\nUpdating Customer Information:")
print("-" * 60)
# Add your code here
customers["C001"]["phone"] = "555-7777"
customers["C002"]["industry"] = "Finance"

print("Updated C001:", customers["C001"])
print("Updated C002:", customers["C002"])

# TODO 7: Create project dictionaries for each customer
# Each project: {"name": "Project Name", "service": "Service Type", "hours": X, "budget": Y}
# Create a projects dictionary where customer IDs map to lists of projects
# Store in variable: projects
# Example: projects = {"C001": [project1, project2], "C002": [project3], ...}

print("\n\nProject Information:")
print("-" * 60)
# Add your code here
project1 = {"name": "Retail Website Redesign", "service": "Web Development", "hours": 120, "budget": 18000}
project2 = {"name": "Help Desk Setup", "service": "IT Support", "hours": 40, "budget": 3800}
project3 = {"name": "Financial Dashboard", "service": "Data Analysis", "hours": 90, "budget": 16000}
project4 = {"name": "Network Security Upgrade", "service": "Cybersecurity", "hours": 75, "budget": 20000}
project5 = {"name": "Cloud Migration", "service": "Cloud Solutions", "hours": 100, "budget": 21000}
project6 = {"name": "Media Analytics Report", "service": "Data Analysis", "hours": 60, "budget": 11000}

projects = {
    "C001": [project1, project2],
    "C002": [project3],
    "C003": [project4, project5],
    "C004": [project6]
}

for customer_id, project_list in projects.items():
    print(customer_id)
    for project in project_list:
        print(f"  {project}")
    print()

# TODO 8: Calculate project costs
# For each project, calculate: cost = hourly_rate * hours
# Display each project with its calculated cost

print("\n\nProject Cost Calculations:")
print("-" * 60)
# Add your code here
for customer_id, project_list in projects.items():
    for project in project_list:
        cost = services[project["service"]] * project["hours"]
        print(f"{customer_id} - {project['name']}: ${cost:.2f}")

# TODO 9: Customer statistics using dictionary methods
# Display:
# - All customer IDs using .keys()
# - All customer companies using .values() and extracting company names
# - Count of total customers using len()

print("\n\nCustomer Statistics:")
print("-" * 60)
# Add your code here
print("Customer IDs:", list(customers.keys()))
print("Customer Companies:", [customer["company_name"] for customer in customers.values()])
print("Count of Total Customers:", len(customers))

# TODO 10: Service usage analysis
# Create a dictionary that counts how many projects use each service
# Store in variable: service_counts
# Display the service usage counts

print("\n\nService Usage Analysis:")
print("-" * 60)
# Add your code here
service_counts = {}

for project_list in projects.values():
    for project in project_list:
        service = project["service"]
        service_counts[service] = service_counts.get(service, 0) + 1

for service, count in service_counts.items():
    print(f"{service}: {count}")

# TODO 11: Financial aggregations
# Calculate and display:
# - Total hours across all projects (store in total_hours)
# - Total budget across all projects (store in total_budget)
# - Average project budget (store in avg_budget)
# - Most expensive and least expensive projects (store in max_budget, min_budget)

print("\n\nFinancial Summary:")
print("-" * 60)
# Add your code here
all_projects = []
for project_list in projects.values():
    for project in project_list:
        all_projects.append(project)

total_hours = sum(project["hours"] for project in all_projects)
total_budget = sum(project["budget"] for project in all_projects)
avg_budget = total_budget / len(all_projects)
max_budget = max(project["budget"] for project in all_projects)
min_budget = min(project["budget"] for project in all_projects)

most_expensive_project = max(all_projects, key=lambda project: project["budget"])
least_expensive_project = min(all_projects, key=lambda project: project["budget"])

print("Total Hours:", total_hours)
print("Total Budget:", total_budget)
print(f"Average Project Budget: ${avg_budget:.2f}")
print("Most Expensive Project:", most_expensive_project["name"], "-", f"${max_budget}")
print("Least Expensive Project:", least_expensive_project["name"], "-", f"${min_budget}")

# TODO 12: Customer summary report
# For each customer, show:
# - Customer details
# - Number of projects
# - Total hours
# - Total budget

print("\n\nCustomer Summary Report:")
print("-" * 60)
# Add your code here
for customer_id, customer_info in customers.items():
    customer_projects = projects.get(customer_id, [])
    num_projects = len(customer_projects)
    customer_hours = sum(project["hours"] for project in customer_projects)
    customer_budget = sum(project["budget"] for project in customer_projects)

    print(f"{customer_id} - {customer_info['company_name']}")
    print(f"  Contact Person: {customer_info['contact_person']}")
    print(f"  Email: {customer_info['email']}")
    print(f"  Phone: {customer_info['phone']}")
    print(f"  Number of Projects: {num_projects}")
    print(f"  Total Hours: {customer_hours}")
    print(f"  Total Budget: ${customer_budget:.2f}")
    print()

# TODO 13: Create rate adjustments using dictionary comprehension
# Create a new dictionary with all service rates increased by 10%
# Store in variable: adjusted_rates
# Use dictionary comprehension: adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
# Add your code here
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

for service, rate in adjusted_rates.items():
    print(f"{service}: ${rate:.2f}")

# TODO 14: Filter customers using dictionary comprehension
# Create a dictionary of only customers who have projects
# Store in variable: active_customers
# Hint: Use the projects dictionary to check which customers have projects

print("\n\nActive Customers (with projects):")
print("-" * 60)
# Add your code here
active_customers = {customer_id: customer_info for customer_id, customer_info in customers.items() if customer_id in projects and len(projects[customer_id]) > 0}

for customer_id, customer_info in active_customers.items():
    print(f"{customer_id}: {customer_info['company_name']}")

# TODO 15: Create project summaries using dictionary comprehension
# Create a dictionary mapping customer IDs to their total project budgets
# Store in variable: customer_budgets
# Example result: {"C001": 25000, "C002": 15000, ...}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
# Add your code here
customer_budgets = {customer_id: sum(project["budget"] for project in project_list) for customer_id, project_list in projects.items()}

for customer_id, budget in customer_budgets.items():
    print(f"{customer_id}: ${budget:.2f}")

# TODO 16: Service pricing tiers using dictionary comprehension
# Create a dictionary categorizing services as "Premium" (>= 200), "Standard" (100-199), or "Basic" (< 100)
# Store in variable: service_tiers
# Use conditional expressions in the comprehension

print("\n\nService Pricing Tiers:")
print("-" * 60)
# Add your code here
service_tiers = {
    service: "Premium" if rate >= 200 else "Standard" if rate >= 100 else "Basic"
    for service, rate in services.items()
}

for service, tier in service_tiers.items():
    print(f"{service}: {tier}")

# TODO 17: Customer validation function
# Create a function validate_customer(customer_dict) that:
# - Checks if all required fields are present (company_name, contact_person, email, phone)
# - Returns True if valid, False otherwise
# - Use conditional logic to verify each field
# Test it on all customers and report results

print("\n\nCustomer Validation:")
print("-" * 60)
# Add your code here
def validate_customer(customer_dict):
    required_fields = ["company_name", "contact_person", "email", "phone"]
    for field in required_fields:
        if field not in customer_dict or customer_dict[field] == "":
            return False
    return True

for customer_id, customer_info in customers.items():
    print(f"{customer_id}: {validate_customer(customer_info)}")

# TODO 18: Project status tracking with loops and conditionals
# Add a "status" field to each project ("active", "completed", "pending")
# Use a loop to count projects by status
# Store counts in status_counts dictionary
# Display a summary of project statuses

print("\n\nProject Status Summary:")
print("-" * 60)
# Add your code here
status_counts = {"active": 0, "completed": 0, "pending": 0}
statuses = ["active", "completed", "pending"]
index = 0

for project_list in projects.values():
    for project in project_list:
        project["status"] = statuses[index % len(statuses)]
        status_counts[project["status"]] += 1
        index += 1

for status, count in status_counts.items():
    print(f"{status}: {count}")

# TODO 19: Budget analysis function with aggregation
# Create a function analyze_customer_budgets(projects_dict) that:
# - Takes the projects dictionary as input
# - Uses loops to calculate total and average budget per customer
# - Returns a dictionary with customer IDs as keys and budget stats as values
# - Each value should be a dict with 'total', 'average', and 'count' keys

print("\n\nDetailed Budget Analysis:")
print("-" * 60)
# Add your code here
def analyze_customer_budgets(projects_dict):
    results = {}

    for customer_id, project_list in projects_dict.items():
        total = 0
        count = len(project_list)

        for project in project_list:
            total += project["budget"]

        average = total / count if count > 0 else 0

        results[customer_id] = {
            "total": total,
            "average": average,
            "count": count
        }

    return results

budget_analysis = analyze_customer_budgets(projects)
for customer_id, stats in budget_analysis.items():
    print(f"{customer_id}: {stats}")

# TODO 20: Service recommendation system
# Create a function recommend_services(customer_id, customers, projects, services) that:
# - Analyzes the customer's past projects
# - Identifies services they haven't used yet
# - Returns a list of recommended services based on their budget range
# - Use loops, conditionals, and dictionary operations

print("\n\nService Recommendations:")
print("-" * 60)
# Add your code here
def recommend_services(customer_id, customers, projects, services):
    if customer_id not in customers:
        return ["Customer not found"]

    customer_projects = projects.get(customer_id, [])
    used_services = []

    for project in customer_projects:
        if project["service"] not in used_services:
            used_services.append(project["service"])

    unused_services = []
    for service in services:
        if service not in used_services:
            unused_services.append(service)

    if len(customer_projects) == 0:
        return unused_services

    average_budget = sum(project["budget"] for project in customer_projects) / len(customer_projects)

    recommendations = []
    for service in unused_services:
        estimated_cost = services[service] * 80
        if estimated_cost <= average_budget * 1.2:
            recommendations.append(service)

    return recommendations

for customer_id in customers:
    print(f"{customer_id}: {recommend_services(customer_id, customers, projects, services)}")