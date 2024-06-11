class Country:
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.silver = 0
        self.bronze = 0


class ClassCategory:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class CompetingClass:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category
        self.contestants = []


class Contestant:
    def __init__(self, id, name, age, height, country, competing_class):
        self.id = id
        self.name = name
        self.age = age
        self.height = height
        self.country = country
        self.competing_class = competing_class


class Bout:
    def __init__(self, contestant1, contestant2, winner=None, score=None):
        self.contestant1 = contestant1
        self.contestant2 = contestant2
        self.winner = winner
        self.score = score


class Championship:
    def __init__(self):
        self.countries = {}
        self.class_categories = {}
        self.competing_classes = {}
        self.contestants = {}
        self.bouts = {}

    def add_country(self, name):
        self.countries[name] = Country(name)

    def add_class_category(self, id, name):
        self.class_categories[id] = ClassCategory(id, name)

    def add_competing_class(self, id, name, category_id):
        if category_id in self.class_categories:
            self.competing_classes[id] = CompetingClass(
                id, name, self.class_categories[category_id]
            )
        else:
            print("Category not found")

    def add_contestant(self, id, name, age, height, country_name, competing_class_id):
        if (
            country_name in self.countries
            and competing_class_id in self.competing_classes
        ):
            self.contestants[id] = Contestant(
                id,
                name,
                age,
                height,
                self.countries[country_name],
                self.competing_classes[competing_class_id],
            )
            self.competing_classes[competing_class_id].contestants.append(
                self.contestants[id]
            )
        else:
            print("Country or competing class not found")

    def generate_bouts(self):
        for competing_class in self.competing_classes.values():
            contestants = competing_class.contestants
            # Using a simple round-robin scheduling algorithm for bout generation
            for i in range(len(contestants)):
                for j in range(i + 1, len(contestants)):
                    bout = Bout(contestants[i], contestants[j])
                    self.bouts[
                        f"{competing_class.id}_{contestants[i].id}_{contestants[j].id}"
                    ] = bout

    def input_score(
        self, competing_class_id, contestant1_id, contestant2_id, winner_id, score
    ):
        bout_id = f"{competing_class_id}_{contestant1_id}_{contestant2_id}"
        if bout_id in self.bouts:
            self.bouts[bout_id].winner = self.contestants[winner_id]
            self.bouts[bout_id].score = score
        else:
            print("Bout not found")

    def complete_championship(self):
        for bout in self.bouts.values():
            if bout.winner is None or bout.score is None:
                print("All bouts must have a winner and score")
                return False
        return True

    def get_winners(self, competing_class_id):
        winners = []
        class_bouts = [
            bout
            for bout in self.bouts.values()
            if bout.contestant1.competing_class.id == competing_class_id
        ]
        # Simple sorting by score to determine winners
        sorted_bouts = sorted(class_bouts, key=lambda x: x.score, reverse=True)
        for i in range(min(4, len(sorted_bouts))):
            winners.append(sorted_bouts[i].winner)
        return winners

    def get_medal_count(self):
        medal_count = {}
        for country in self.countries.values():
            medal_count[country.name] = {
                "Gold": country.gold,
                "Silver": country.silver,
                "Bronze": country.bronze,
            }
        return medal_count


def main():
    championship = Championship()

    while True:
        print("\nChampionship Management System\n")
        print("1. Add country")
        print("2. Add class category")
        print("3. Add competing class")
        print("4. Add contestant")
        print("5. Generate bouts")
        print("6. Input score")
        print("7. Complete championship")
        print("8. Get winners")
        print("9. Get medal count")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter country name: ")
            championship.add_country(name)
        elif choice == "2":
            id = input("Enter category id: ")
            name = input("Enter category name: ")
            championship.add_class_category(id, name)
        elif choice == "3":
            id = input("Enter competing class id: ")
            name = input("Enter competing class name: ")
            category_id = input("Enter category id: ")
            championship.add_competing_class(id, name, category_id)
        elif choice == "4":
            id = input("Enter contestant id: ")
            name = input("Enter contestant name: ")
            age = input("Enter contestant age: ")
            height = input("Enter contestant height: ")
            country_name = input("Enter country name: ")
            competing_class_id = input("Enter competing class id: ")
            championship.add_contestant(
                id, name, age, height, country_name, competing_class_id
            )
        elif choice == "5":
            championship.generate_bouts()
            print("Bouts generated successfully")
        elif choice == "6":
            competing_class_id = input("Enter competing class id: ")
            contestant1_id = input("Enter contestant1 id: ")
            contestant2_id = input("Enter contestant2 id: ")
            winner_id = input("Enter winner id: ")
            score = input("Enter score: ")
            championship.input_score(
                competing_class_id, contestant1_id, contestant2_id, winner_id, score
            )
        elif choice == "7":
            if championship.complete_championship():
                print("Championship completed successfully")
            else:
                print("Please input scores for all bouts")
        elif choice == "8":
            competing_class_id = input("Enter competing class id: ")
            winners = championship.get_winners(competing_class_id)
            for i, winner in enumerate(winners):
                print(f"Rank {i+1}: {winner.name}")
        elif choice == "9":
            medal_count = championship.get_medal_count()
            for country, medals in medal_count.items():
                print(
                    f"{country}: {medals['Gold']} Gold, {medals['Silver']} Silver, {medals['Bronze']} Bronze"
                )
        elif choice == "10":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
