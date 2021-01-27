# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    user_dict = {}
    
    # user_dict 등록
    for row in record:
        action = row.split()[0].lower()
        uid = row.split()[1]
        
        if action != 'leave':
            name = row.split()[2]
            user_dict[uid] = name
        
    for row in record:
        action = row.split()[0].lower()
        uid = row.split()[1]
        if action == 'enter':
            answer.append(f"{user_dict[uid]}님이 들어왔습니다.")
        elif action == 'leave':
            answer.append(f"{user_dict[uid]}님이 나갔습니다.")
        
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))