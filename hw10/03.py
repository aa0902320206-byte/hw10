

def cumulative_spend(daily_spend, n):
    """
    使用遞迴計算前 n 天的費用合計。
    n = 0 時回傳 0；n > 0 時，透過遞迴取得前 n-1 天的費用加上第 n 天的費用。
    """
    if n == 0:
        return 0
    return cumulative_spend(daily_spend, n - 1) + daily_spend[n - 1]

if __name__ == "__main__":
    # 一、共同設定：帶入自己的完整學號
    student_id = input("請輸入完整學號：").strip().upper()
    tail = student_id[-3:]
    a = int(student_id[-3])
    b = int(student_id[-2])
    c = int(student_id[-1])
    s = a + b + c

    # 題目資料設定
    daily_spend = [100 + 10 * a, 150 + 10 * b, 0,
                   200 + 10 * c, 50 + 10 * s]
    n = 3 + c % 3

    print(f"學號：{student_id}")
    print(f"每日費用：{daily_spend}")
    print(f"指定n：{n}")
    
    specified_total = cumulative_spend(daily_spend, n)
    print(f"指定前{n}天累計：{specified_total}元")

    # 依序印出前 0 至 5 天的累計費用
    for i in range(len(daily_spend) + 1):
        print(f"前{i}天：{cumulative_spend(daily_spend, i)}元")

    # 空資料測試
    empty_spend = cumulative_spend([], 0)
    print(f"空資料：{empty_spend}元")