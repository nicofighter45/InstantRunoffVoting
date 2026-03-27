class Votant:
    def __init__(self, vote: list[str]):
        self.__vote = []
        for i in range(1, len(vote)+1):
            for j in range(len(vote)):
                if vote[j] == str(i):
                    self.__vote.append(j)

    def get_vote(self) -> int:
        return self.__vote[0]

    def remove_choice(self, choice: int):
        if choice in self.__vote:
            self.__vote.remove(choice)
