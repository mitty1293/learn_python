import csv

def main():
    csvpath: str = input("CSV Path ->")
    score_dict: dict = set_score_dict(csvpath)
    mean_dict: dict = set_mean_dict(score_dict)
    print_ranking(mean_dict)

def set_score_dict(csvpath: str) -> dict:
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

def set_mean_dict(score_dict: dict) -> dict:
    mean_dict: dict = {}
    for player_id in score_dict.keys():
        mean_score = score_dict[player_id]['sum_score'] / score_dict[player_id]['count']
        mean_dict[player_id] = mean_score
    return mean_dict

def print_ranking(mean_dict: dict) -> None:
    rank_list: list = sorted(mean_dict.items(), key=lambda i: i[1], reverse=True)
    print("rank, player_id, mean_score")
    rank: int = 1
    for player_id, mean_score in rank_list:
        print(f'{rank}, {player_id}, {mean_score}')
        rank += 1

if __name__ == '__main__':
    main()