from project import Project

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


def display_projects(projects):

    for project in projects:



main()
