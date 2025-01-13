class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def get_info(self):
        return f'Employee ID: {self.id}, Name: {self.name}'
class Manager(Employee):
    def __init__(self,name,id,department):
        Employee.__init__(self,name,id)
        self.department=department
    def manage_project(self,project_name):
        return f'Manager {self.name} is controling project: {project_name} in the {self.department} department.'
    def get_info(self):
        return f'{super().get_info()}, Department: {self.department}'
class Technician(Employee):
    def __init__(self,name,id,specialization):
        super().__init__(name,id)
        self.specialization=specialization
    def perform_maintenance(self):
        return f'{self.name} is performing maintenance in the field of {self.specialization}.'
    def get_info(self):
        return f'{super().get_info()}, Specialization: {self.specialization}.'
class TechManager(Manager,Technician):
    def __init__(self,name,id,department,specialization):
        super().__init__(name,id,department)
        self.specialization=specialization
        self.team=[]
    def add_employee(self,employee):
        self.team.append(employee)
        return f'{employee.name} was added to the team.'
    def get_team_info(self):
        team_info='Team Members:\n'
        for member in self.team:
            team_info+=member.get_info()+"\n"
        return team_info

employee_1=Employee('Ivan',1)
employee_2=Technician('Anna',2,'cleaner')
manager_1=Manager('Maksim',3,'IT')
tech_manager=TechManager('Nikita',4,'Development','Software development')
tech_manager.add_employee(employee_1)
tech_manager.add_employee(employee_2)
tech_manager.add_employee(manager_1)
print(tech_manager.get_team_info())
