import csv

def import_csv(csvpath: str):
    score_dict: dict = {}
    with open(csvpath, 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for line in csv_reader:
            create_timestamp, player_id, score = line
            if player_id not in score_dict:
                sum_score = score
                count = 1
            else:
                sum_score = score_dict[player_id][0] + score
                count = score_dict[player_id][1] + 1
            score_dict[player_id] = [sum_score, count]
    return score_dict
# 次はplayer_id毎の平均点を出す⇒ソートしてランキングにする

