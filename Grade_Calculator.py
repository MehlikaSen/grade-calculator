def get_categories():
    categories = []
    num = int(input("Enter the number of categories that make up your grade: "))
    for i in range(num):
        name = input(f"Enter name of category {i+1}: ")
        weight = float(input(f"Enter weight for {name} as a %: "))
        categories.append({"name": name , "weight" : weight, "assignments": []})
    return categories

def get_assignments(category_name):
    assignments = []
    num = int(input(f"Enter the number of assignments in {category_name}: "))
    for i in range(num):
        possible_pts = float(input(f"Enter points possible for assignment {i+1}: "))
        earned_pts = float(input(f"Enter points earned for assignment {i+1}: "))
        assignments.append(( earned_pts, possible_pts))
    return assignments

def calc_category_percent(assignments):
    total_earned = 0
    total_possible = 0
    for earned, possible in assignments:
        total_earned += earned
        total_possible += possible
    if total_possible == 0:
        return 0
    return (total_earned/total_possible) * 100

def calc_weighted_total(categories):
    final = 0
    for category in categories:
        final += category["percent"] * (category["weight"] / 100)
    return final

def show_grades(categories, final_grade):
    print("Grade Calculation Totals\n")
    for cat in categories:
        print(f"{cat['name']}: {cat['percent']:.2f}% (Weight: {cat['weight']}%)")
    print(f"Weighted total grade: {final_grade:.2f}%")
        
def save_results(categories, final_grade):
    choice = input("Do you want to save the results to a file? (yes/no): ").strip().lower()
    if choice == "yes":
        filename = input("Enter file name ")
        with open(filename, "w") as file:
            file.write("Grade Calculation Totals\n")
            for category in categories:
                file.write(f"{category['name']}: {category['percent']:.2f}% (Weight: {category['weight']}%)\n")
            file.write(f"Weighted total grade: {final_grade:.2f}%\n")
        print(f"Grades saved to {filename}.")
    else:
        print(f"No file saved.")
#MAIN
categories = get_categories()
for category in categories:
    category["assignments"] = get_assignments(category["name"])
    category["percent"] = calc_category_percent(category["assignments"])
final_grade = calc_weighted_total(categories)
show_grades(categories, final_grade)
save_results(categories, final_grade)
    