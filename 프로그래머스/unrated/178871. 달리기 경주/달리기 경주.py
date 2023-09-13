def solution(players, callings):
    player_dict = {player: idx for idx, player in enumerate(players)}

    for i in callings:
        idx = player_dict[i]
        # 플레이어 위치를 바꿔야 할 때, 임시 변수를 사용하여 스왑합니다.
        temp = players[idx]
        players[idx] = players[idx - 1]
        players[idx - 1] = temp

        # 플레이어의 위치를 업데이트합니다.
        player_dict[players[idx]] = idx
        player_dict[players[idx - 1]] = idx - 1

    # 정렬된 플레이어 리스트를 반환합니다.
    return players