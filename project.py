class StakeholderCommunicationTool:
    def _init_(self):  
        self.stakeholders = []
        self.communication_logs = []
        self.meetings = []
        self.outcomes = []

    def create_stakeholder(self, name):
        stakeholder = {"id": len(self.stakeholders) + 1, "name": name}
        self.stakeholders.append(stakeholder)
        return stakeholder

    def create_communication_log(self, stakeholder_id, method, summary, date_time):
        log = {
            "id": len(self.communication_logs) + 1,
            "stakeholder_id": stakeholder_id,
            "method": method,
            "summary": summary,
            "date_time": date_time,
        }
        self.communication_logs.append(log)
        return log

    def schedule_meeting(self, stakeholder_id, date_time, agenda):
        meeting = {
            "id": len(self.meetings) + 1,
            "stakeholder_id": stakeholder_id,
            "date_time": date_time,
            "agenda": agenda,
        }
        self.meetings.append(meeting)
        return meeting

    def log_outcome(self, communication_log_id, description):
        outcome = {
            "id": len(self.outcomes) + 1,
            "communication_log_id": communication_log_id,
            "description": description,
        }
        self.outcomes.append(outcome)
        return outcome

    def get_stakeholder(self, stakeholder_id):
        for stakeholder in self.stakeholders:
            if stakeholder["id"] == stakeholder_id:
                return stakeholder
        return None

    def get_communication_log(self, log_id):
        for log in self.communication_logs:
            if log["id"] == log_id:
                return log
        return None

    def get_meeting(self, meeting_id):
        for meeting in self.meetings:
            if meeting["id"] == meeting_id:
                return meeting
        return None

    def get_outcome(self, outcome_id):
        for outcome in self.outcomes:
            if outcome["id"] == outcome_id:
                return outcome
        return None

    def display_menu(self):
        print("\n--- Stakeholder Communication Tool Menu ---")
        print("1. Create Stakeholder")
        print("2. Create Communication Log")
        print("3. Schedule Meeting")
        print("4. Log Outcome")
        print("5. Retrieve Stakeholder")
        print("6. Retrieve Communication Log")
        print("7. Retrieve Meeting")
        print("8. Retrieve Outcome")
        print("9. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Select an option (1-9): ")

            if choice == '1':
                name = input("Enter stakeholder name: ")
                stakeholder = self.create_stakeholder(name)
                print("Stakeholder created:", stakeholder)

            elif choice == '2':
                try:
                    stakeholder_id = int(input("Enter stakeholder ID: "))
                    method = input("Enter communication method (e.g., email, phone): ")
                    summary = input("Enter communication summary: ")
                    date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
                    log = self.create_communication_log(stakeholder_id, method, summary, date_time)
                    print("Communication Log created:", log)
                except ValueError:
                    print("Invalid input. Please enter a valid stakeholder ID.")

            elif choice == '3':
                try:
                    stakeholder_id = int(input("Enter stakeholder ID: "))
                    date_time = input("Enter meeting date and time (YYYY-MM-DD HH:MM:SS): ")
                    agenda = input("Enter meeting agenda: ")
                    meeting = self.schedule_meeting(stakeholder_id, date_time, agenda)
                    print("Meeting scheduled:", meeting)
                except ValueError:
                    print("Invalid input. Please enter a valid stakeholder ID.")

            elif choice == '4':
                try:
                    communication_log_id = int(input("Enter communication log ID: "))
                    description = input("Enter outcome description: ")
                    outcome = self.log_outcome(communication_log_id, description)
                    print("Outcome logged:", outcome)
                except ValueError:
                    print("Invalid input. Please enter a valid communication log ID.")

            elif choice == '5':
                try:
                    stakeholder_id = int(input("Enter stakeholder ID: "))
                    retrieved_stakeholder = self.get_stakeholder(stakeholder_id)
                    print("Retrieved Stakeholder:", retrieved_stakeholder)
                except ValueError:
                    print("Invalid input. Please enter a valid stakeholder ID.")

            elif choice == '6':
                try:
                    log_id = int(input("Enter communication log ID: "))
                    retrieved_log = self.get_communication_log(log_id)
                    print("Retrieved Communication Log:", retrieved_log)
                except ValueError:
                    print("Invalid input. Please enter a valid communication log ID.")

            elif choice == '7':
                try:
                    meeting_id = int(input("Enter meeting ID: "))
                    retrieved_meeting = self.get_meeting(meeting_id)
                    print("Retrieved Meeting:", retrieved_meeting)
                except ValueError:
                    print("Invalid input. Please enter a valid meeting ID.")

            elif choice == '8':
                try:
                    outcome_id = int(input("Enter outcome ID: "))
                    retrieved_outcome = self.get_outcome(outcome_id)
                    print("Retrieved Outcome:", retrieved_outcome)
                except ValueError:
                    print("Invalid input. Please enter a valid outcome ID.")

            elif choice == '9':
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please select a valid option.")

tool = StakeholderCommunicationTool()
tool.run()
