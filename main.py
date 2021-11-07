import csv

def set_score_dict(csvpath: str):
    score_dict: dict = {}
    with open(csvpath, 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f, delimiter=',')
        header = next(csv_reader)
        for create_timestamp, player_id, score in csv_reader:
            if player_id not in score_dict:
                sum_score = int(score)
                count = 1
            else:
                sum_score = score_dict[player_id]['sum_score'] + int(score)
                count = score_dict[player_id]['count'] + 1
            score_dict[player_id] = {'sum_score': sum_score, 'count': count}
    return score_dict

def set_mean_dict(score_dict: dict):
    mean_dict: dict = {}
    for player_id in score_dict.keys():
        mean_score = score_dict[player_id]['sum_score'] / score_dict[player_id]['count']
        mean_dict[player_id] = mean_score
    return mean_dict

