from datetime import datetime, timedelta

def calc_fee(one_call):

    call_time, duration = one_call
    call_h, call_m = map(int, call_time.split(':'))

    if 6 < call_h < 18:
        fee = 10 * duration
    elif call_h > 18 or call_h < 6:
        fee = 5 * duration
    elif call_h == 6:
        if call_m + duration > 60:
            exceed_time = call_m+duration - 60
            base_time = duration - exceed_time
            fee = 5 * base_time + 10 *exceed_time
        else:
            fee = 5*duration
    elif call_h==18:
        if call_m + duration > 60:
            exceed_time = call_m+duration - 60
            base_time = duration - exceed_time
            fee = 10 * base_time + 5 *exceed_time
        else:
            fee = 10*duration
    return fee

def calc_fee_timedelta(one_call):
    fee_info = {i:10 if 7<=i<=18 else 5 for i in range(24)}

    call_time, duration = one_call
    call_time = datetime.strptime(call_time, "%H:%M")
    end_time = call_time + timedelta(minutes=duration)
    print(f"{call_time} (+{duration}) => {end_time}")
    call_h, call_m = call_time.hour, call_time.minute
    end_h, end_m = end_time.hour, end_time.minute

    if call_h != end_h:
        duration_forward = duration-end_m
        duration_backward = end_m
        fee = duration_forward*fee_info[call_h] + duration_backward*fee_info[end_h]

    else:
        fee = duration*fee_info[call_h]
    return fee
    


            
if __name__=="__main__":
    n = int(input()) # 전화 건 횟수(1~100)
    calls = []
    for _ in range(n):
        call_time, duration = input().split()
        duration = int(duration) # 최대 60분
        calls.append([call_time, duration])
        
    total_fee = 0
    for call in calls:
        fee = calc_fee_timedelta(call)
        total_fee += fee
    print(total_fee)