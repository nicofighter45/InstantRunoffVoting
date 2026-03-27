class Votant:
    def __init__(self, vote: list[str]):
        self.__vote = []
        for i in range(1, len(vote)+1):
            for j in range(len(vote)):
                if vote[j] == str(i):
                    self.__vote.append(j)

    def get_vote(self) -> int:
        return self.__vote[0]

    def remove_choices(self, choices: list[int]):
        print(self.__vote)
        for choice in choices:
            self.__vote.remove(choice)
        for i in range(len(self.__vote)):
            minus = 0
            for choice in choices:
                if self.__vote[i] > choice:
                    minus += 1
            self.__vote[i] -= minus
        print(self.__vote)
