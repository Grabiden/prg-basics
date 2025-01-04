class Statistics:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def display_numbers(self):
        print("Numbers:", " ".join(map(str, self.numbers)))

    def greatest_number(self):
        return max(self.numbers) if self.numbers else None

    def smallest_number(self):
        return min(self.numbers) if self.numbers else None

    def arithmetic_mean(self):
        if not self.numbers:
            return None
        return sum(self.numbers) / len(self.numbers)

    def median(self):
        if not self.numbers:
            return None
        n = len(self.numbers)
        mid = n // 2
        if n % 2 == 0:
            return (self.numbers[mid - 1] + self.numbers[mid]) / 2
        else:
            return self.numbers[mid]

    def print_statistics(self):
        print("Minimum:", self.smallest_number())
        print("Maximum:", self.greatest_number())
        print("Arithmetic Mean:", self.arithmetic_mean())
        print("Median:", self.median())


# Example usage
if __name__ == "__main__":
    stats = Statistics()

    # Adding numbers from the keyboard
    print("Enter numbers (type 'done' to finish):")
    while True:
        user_input = input("Enter a number: ")
        if user_input.lower() == 'done':
            break
        try:
            number = float(user_input)
            stats.add_number(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Displaying numbers
    stats.display_numbers()

    # Printing statistics
    stats.print_statistics()
        