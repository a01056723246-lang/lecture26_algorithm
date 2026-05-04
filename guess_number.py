# 1. 컴퓨터가 숫자를 생각한다
# 2. 사용자가 숫자를 말한다
# 3. 숫자가 맞으면 사용자 win
# 4. 틀리면 컴퓨터가 up, down을 알려준다
# 5. 2~4번까지 7번 반복
# 6. 7번 내에 맞추지 못하면 컴퓨터 win
import random

# 1. 컴퓨터가 숫자를 생각한다 (1~100 사이의 임의의 숫자)
computer_number = random.randint(1, 100)
attempts = 7  # 제한 횟수
win = False

print("--- 숫자 맞추기 게임 (Up & Down) ---")
print(f"1부터 100 사이의 숫자를 맞춰보세요. 기회는 {attempts}번입니다.")

# 5. 2~4번까지 7번 반복
for i in range(1, attempts + 1):
    # 2. 사용자가 숫자를 말한다
    try:
        user_guess = int(input(f"[{i}회차] 숫자를 입력하세요: "))
    except ValueError:
        print("숫자만 입력 가능합니다. 기회를 1번 잃었습니다.")
        continue

    # 3. 숫자가 맞으면 사용자 win
    if user_guess == computer_number:
        print(f"축하합니다! {i}번 만에 정답을 맞췄습니다. 당신의 승리입니다!")
        win = True
        break
    
    # 4. 틀리면 컴퓨터가 up, down을 알려준다
    elif user_guess < computer_number:
        print("UP! 더 큰 숫자입니다.")
    else:
        print("DOWN! 더 작은 숫자입니다.")

# 6. 7번 내에 맞추지 못하면 컴퓨터 win
if not win:
    print("-" * 30)
    print("컴퓨터의 승리입니다!")
    print(f"정답은 {computer_number}였습니다.")