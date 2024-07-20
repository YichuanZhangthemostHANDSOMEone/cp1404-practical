from project import Project
import datetime

MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n"
        "- (U)pdate project\n- (Q)uit")
FILE_NAME = "projects.txt"


def main():
    projects = load_file()


def load_file(input_name):
    file_name = input(input_name)
    try:
        in_file = open(file_name, 'r')
    except FileNotFoundError:
        print(f"File not found, open default file--{FILE_NAME}")
        file_name = FILE_NAME
        in_file = open(file_name, 'r')
    projects = []
    for line in in_file:
        parts = line.strip().split("\t")
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)
    in_file.close()
    return projects


def get_file_name(projects):
    user_input_name = input("Input name:")
    if not user_input_name.endswith(".txt"):
        user_input_name += ".txt"
    save_projects(projects, user_input_name)


def save_projects(projects, file_name):
    with open(file_name, 'w') as new_file:
        print("Name	Start Date	Priority	Cost Estimate	Completion Percentage")
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.percentage}", file = new_file)


def display_projects(projects):
    incomplete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]

    if incomplete:
        print("Incomplete projects:")
        for project in sorted(incomplete):
            print(project)
    else:
        print("No incomplete projects.")

    if complete:
        print("Completed projects:")
        for project in sorted(complete):
            print(project)
    else:
        print("No completed projects.")


def filter_projects(projects):
    projects_to_filter = [projects]
    input_date = input("Show projects that start after date (dd/mm/yy):")
    date = datetime.datetime.strptime(input_date, "%d/%m/%Y").date()
    projects_to_filter.sort()
    for project in projects_to_filter:
        date1 = datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
        if date1 > date:
            print(project)


def add_project(projects):
    name = input("Name:")
    start_date = input("Start date (dd/mm/yy):")
    priority = int(input("Priority:"))
    cost_estimate = float(input("Cost estimate:"))
    percentage = int(input("Percent complete:"))
    project = Project(name, start_date, priority, cost_estimate, percentage)
    projects.append(project)


def update_project(projects):
    for index, project in enumerate(projects):
        print(index, project)

    choice = int(input("Project choice:"))
    print(projects[choice])

    new_percentage = int(input("New Percentage:"))
    new_priority = int(input("New Priority:"))
    projects[choice].percentage = new_percentage
    projects[choice].priority = new_priority


def get_valid_input(user_input):
    is_valid = False
    while not is_valid:
        try:
            user_input_to_validate = float(input(user_input))
            if user_input_to_validate < 0:
                print("Number must be > 0")
            else:



main()
