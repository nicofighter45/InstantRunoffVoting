import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook

from data_extracting import get_datas
from votant import Votant



choices, votants, abstention = get_datas("test_results.xlsx")


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
        votes[votant.get_vote()] += 1

    # Plot the vote distribution for this round
    plt.figure(figsize=(10, 6))
    plt.bar(choices, votes, color='skyblue')
    plt.title(f"Round {iter}: Vote Distribution")
    plt.xlabel("Choices")
    plt.ylabel("Number of Votes")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    max_votes = max(votes)
    min_votes = min(votes)

    if max_votes > len(votants) / 2:
        max_index = votes.index(max_votes)
        print(f"The winner is {choices[max_index]} with {max_votes} votes out of {len(votants)} voters, and {abstention} abstentions.")
        break
    else:
        min_index = votes.index(min_votes)
        print(f"No winner. Proceeding to round {iter}. The choice with the fewest votes is {choices[min_index]} with {min_votes} votes out of {len(votants)} voters.")
        for votant in votants:
            votant.remove_choice(min_index)
        choices.pop(min_index)
        iter += 1
