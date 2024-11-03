from collections import defaultdict

salaries_and_ternuries = [
    (5000.0, 3.5), 
    (7000.0, 5),
    (6500.0, 4.2),
    (8000.0, 6),
    (5500.0, 2.8),
    (9000.0, 9),
    (6000.0, 3),
    (7500.0, 5.5),
    (8500.0, 7),
    (3500.0, 1),
    (9500.0, 10),
]

salary_by_ternure = defaultdict(list)

for salary, ternure in salaries_and_ternuries:
    salary_by_ternure[ternure].append(salary)

average_salary_by_ternure = {
    ternure: sum(salaries) / len(salaries)     
    for ternure, salaries in salary_by_ternure.items()                        
}

print(average_salary_by_ternure)

salary_by_ternure_bucket = defaultdict(list)

def ternure_bucket(ternure):
    if ternure < 2:
        return "less than two years"
    elif ternure < 5:
        return "Between two and five years"
    else: 
        return "More them five years"



for salary, ternure in salaries_and_ternuries:
    print(salary, ternure)
    bucket = ternure_bucket(ternure)
    salary_by_ternure_bucket[bucket].append(salary)

print(salary_by_ternure_bucket)

average_salary_by_bucket = {
    ternure_bucket: sum(salaries) / len(salaries)
    for ternure_bucket ,salaries in salary_by_ternure_bucket.items()
}

print(average_salary_by_bucket)

def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "Paid"
    elif years_experience < 8.5:
        return "Unpaid"
    else: 
        return "Piad"
    
print(predict_paid_or_unpaid(salaries_and_ternuries[5][1]))
