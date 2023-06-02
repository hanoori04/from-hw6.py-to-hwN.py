import os
import pickle

def input_scores():
    scores = []

    i = 1
    while True:
        score = float(input(f"#{i}? "))
        i += 1
        if score < 0:
            break
        scores.append(score)
    return scores


def get_average(scores):
    if len(scores) == 0:
        return 0
    average = sum(scores) / len(scores)
    return average


def show_scores(scores, average):
    print("개인점수:", end=' ')
    for score in scores:
        print(score, end=' ')
    print()

    if average != 0:
        print("평균:", format(average, ".1f"))


def save_scores(scores, file_path):
    with open(file_path, "wb") as file:
        pickle.dump(scores, file)


def load_scores(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            scores = pickle.load(file)
        return scores
    return []


file_path = "score.bin"


loaded_scores = load_scores(file_path)
show_scores(loaded_scores, get_average(loaded_scores))


if not os.path.exists(file_path):
    scores_list = input_scores()
    save_scores(scores_list, file_path)

    
    average_score = get_average(scores_list)
    show_scores(scores_list, average_score)