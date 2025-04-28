class Task:
    groups = [
        {
            "Ungrouped": [
                # 1st Task
                {
                    "Task Description": "",
                    "Due Date": "",
                    "Priority": "",
                    "Sub Tasks": 
                    [
                        {
                            "Task Description": "",
                            "Due Date": ""
                        }
                    ]
                }
            ]
        },
    ]

    

    def display_groups(self):
        print("****************************")
        print("********** GROUPS **********")
        print("****************************")
        print()

        # group_names = 
        # for i in range(len(self.groups)):
        #     print(f"{self.groups[i].keys()[0]}:-")
        #     print()
        #     print("\t Tasks")
        #     if self.groups[i].keys()[0].get("Task Description") == "":
        #         print("Working")
        #         continue
        #     else:
        #         print("Not Working")

            
                # if self.groups[i].keys[0][0].get("Task Description") == "":
                #     print()
                #     continue
                # else:
                #     for j in range(len(self.groups[i].keys[0])):
                #         print(f"\t\t {j+1}. {self.groups[i].keys[0][j].get("Task Description")}")
                #         print(f"\t\t Due Date: {self.groups[i].keys[0][j].get("Due Date")}") if self.groups[i].keys[0][j].get("Due Date") != "" else print(f"\t\t Due Date: None")
                #         print(f"\t\t Priority: {self.groups[i].keys[0][j].get("Priority")}") if self.groups[i].keys[0][j].get("Priority") != "" else print(f"\t\t Priority: None")

                #         if self.groups[i].keys[0][j].get("Sub Tasks")[0].get("Task Description") == "":
                #             print()
                #             continue
                #         else:
                #             for k in range(len(self.groups[i].keys[0][j].get("Sub Tasks"))):
                #                 print(f"\t\t\t {k+1}. {self.groups[i].keys[0][j].get("Sub Tasks")[k].get("Task Description")}")
                #                 print(f"\t\t\t {k+1}. {self.groups[i].keys[0][j].get("Sub Tasks")[k].get("Due Date")}") if self.groups[i].keys[0][j].get("Sub Tasks")[k].get("Due Date") != "" else print(f"\t\t Due Date: None")
                #             print()
    
    def add_groups(self):
        new_group = input("Enter the group name: ")
        try:
            self.groups.append(
                {
                new_group: [
                    # 1st Task
                    {
                        "Task Description": "",
                        "Due Date": "",
                        "Priority": "",
                        "Sub Tasks": 
                        [
                            {
                                "Task Description": "",
                                "Due Date": ""
                            }
                        ]
                    }
                ]
            }
            )
        except:
            print("Please enter a valid group name!")
            



    def display_tasks_menu(self):
        self.display_groups()
        print()
        print("1. Add Group")
        print("2. Add Task/SubTasks")
        print("3. Modify Task/SubTasks")
        print("4. Delete Task/SubTasks")
        print("5. Add/Modify Due Date")
        print("6. Add/Modify Priority")
        print("7. Change Display Order")
        print("8. Exit Task Menu")
        print()
        task_menu_response = input("What do you want to do? (1-8): ")

        """
        match(task_menu_response):
            case 
        """


if __name__ == "__main__":
    app = Task()
    app.display_tasks_menu()