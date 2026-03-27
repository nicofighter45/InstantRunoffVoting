import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook

from data_extracting import get_datas
from votant import Votant



choices, votants, abstention = get_datas("Test.xlsx", "Test2.xlsx")


iter = 1
while True:
    if len(choices) == 1:
        print(f"The winner is {choices[0]} with {len(votants)} votes out of {len(votants)} voters.")
        break
    if len(choices) <= 0:
        print("No winner, all choices have been eliminated.")
        break

    votes = [0] * len(choices)
    for votant in votants:
        print(votant.get_vote())
        votes[votant.get_vote()] += 1

    # Plot the vote distribution for this round
    plt.figure(figsize=(10, 6))
    plt.pie(
        votes,
        labels=choices,
        autopct='%1.f%%',
        startangle=90,
        wedgeprops={'edgecolor': 'black'}
    )
    plt.title(f"Round {iter}: Vote Distribution")
    plt.axis('equal')  # Assure que le camembert est un cercle
    plt.tight_layout()
    plt.show()

    max_votes = max(votes)
    min_votes = min(votes)

    if max_votes > len(votants) / 2:
        max_index = votes.index(max_votes)
        print(f"The winner is {choices[max_index]} with {max_votes} votes out of {len(votants)} voters, and {abstention} abstentions.")
        break
    elif max_votes == min_votes:
        print(f"No winner. All remaining choices have the same number of votes ({max_votes} votes each).")
        break
    else:
        min_index_list = [i for i, v in enumerate(votes) if v == min_votes]
        print(f"No winner. Proceeding to round {iter}. The choice(s) with the fewest votes: {[choices[i] for i in min_index_list]} with {min_votes} votes each.")
        for votant in votants:
            votant.remove_choices(min_index_list)
        for min_index in sorted(min_index_list, reverse=True):
            choices.pop(min_index)
        iter += 1
