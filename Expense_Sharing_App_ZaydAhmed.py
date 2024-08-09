class ExpenseManager:
    def __init__(self):
        self.participants = []
        self.paid_status = []

    def collect_participants(self):
        try:
            number = int(input("How many roommates are there? "))
            if number <= 0:
                raise ValueError("The number must be positive.")
            for i in range(number):
                participant = input(f"Enter roommate {i + 1} name: ").strip().capitalize()
                self.participants.append(participant)
        except ValueError as e:
            print(f"Invalid input: {e}")

    def calculate_and_display_shares(self, total_amount):
        if not self.participants:
            print("No roommates to split the bill.")
            return
        share_per_person = round(total_amount / len(self.participants), 2)
        name_length = max(len(name) for name in self.participants)
        
        print("\n=== Bill Split ===")
        print(f"{'roommate':<{name_length}} {'Share':>10}")
        print("-" * (name_length + 12))
        for participant in self.participants:
            print(f"{participant:<{name_length}} Rs. {share_per_person:>10.2f}")

    def record_payment_info(self):
        while True:
            payer = input("Enter the name of the person who paid (type 'done' to finish): ").strip().capitalize()
            if payer.lower() == 'done':
                break
            if payer in self.participants:
                if payer not in self.paid_status:
                    self.paid_status.append(payer)
            else:
                print("Name not found in the list of roommates.")

    def display_payment_status(self):
        name_length = max(len(name) for name in self.participants)
        print("\n=== Payment Status ===")
        print(f"{'roommate':<{name_length}} {'Payment Status':>15}")
        print("-" * (name_length + 18))
        for participant in self.participants:
            status = "Paid" if participant in self.paid_status else "Not Paid"
            print(f"{participant:<{name_length}} {status:>15}")

def main():
    app = ExpenseManager()

    print("--------------Welcome to the Expense Sharing Application--------------")

    app.collect_participants()

    try:
        total_bill = float(input("Enter the total amount of the bill: Rs. "))
        if total_bill <= 0:
            raise ValueError("The amount must be a positive number.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    app.calculate_and_display_shares(total_bill)
    app.record_payment_info()
    app.display_payment_status()

if __name__ == "__main__":
    main()
