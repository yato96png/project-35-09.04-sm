class VotingSystem:
    def __init__(self):
        self.candidates = {}  
        self.voting_active = False

    def start_voting(self):
        if not self.candidates:
            print("Добавьте хотя бы одного кандидата перед началом голосования.")
            return
        self.voting_active = True
        print("Голосование началось!")

    def add_candidate(self, name):
        if self.voting_active:
            print("Нельзя добавлять кандидатов во время голосования.")
            return
        if name in self.candidates:
            print(f"Кандидат {name} уже существует.")
        else:
            self.candidates[name] = 0
            print(f"Кандидат {name} добавлен.")

    def vote(self, name):
        if not self.voting_active:
            print("Голосование еще не началось.")
            return
        if name in self.candidates:
            self.candidates[name] += 1
            print(f"Голос за {name} учтен.")
        else:
            print(f"Кандидат {name} не найден.")

    def show_results(self):
        print("\nТекущие результаты:")
        for name, votes in self.candidates.items():
            print(f"{name}: {votes} голосов")

    def end_voting(self):
        if not self.voting_active:
            print("Голосование не активно.")
            return
        self.voting_active = False
        print("\nГолосование завершено! Итоговые результаты:")
        self.show_results()
        winner = max(self.candidates, key=self.candidates.get)
        print(f"\nПобедитель: {winner}")

vs = VotingSystem()
vs.add_candidate("Алиса")
vs.add_candidate("Боб")
vs.start_voting()
vs.vote("Алиса")
vs.vote("Боб")
vs.vote("Алиса")
vs.show_results()
vs.end_voting()
