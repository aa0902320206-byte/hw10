

def collect_codes(raw_codes, saved=None):
    """
    收集並整理優惠碼：
    1. 去頭尾空白、轉大寫，略過空字串。
    2. 結果串列先保留 saved，再加入新碼，保持不重複、首次出現順序。
    3. 不得修改原 saved 或 raw_codes。
    """
    # 建立結果串列副本（若 saved 為 None 則從空串列開始）
    if saved is None:
        result = []
    else:
        result = list(saved)
        
    for code in raw_codes:
        cleaned = code.strip().upper()
        if cleaned != "" and cleaned not in result:
            result.append(cleaned)
            
    return result

if __name__ == "__main__":
    # 一、共同設定：帶入自己的完整學號
    student_id = input("請輸入完整學號：").strip().upper()
    tail = student_id[-3:]
    a = int(student_id[-3])
    b = int(student_id[-2])
    c = int(student_id[-1])
    s = a + b + c

    # 題目資料設定
    saved = ["BASE"]
    raw_a = [" welcome" + tail + " ", "vip" + tail, "",
             "WELCOME" + tail, "   "]
    raw_b = [" new" + tail + " ", " welcome" + tail + " "]

    print(f"學號：{student_id}")

    # 執行活動 A 與活動 B
    activity_a = collect_codes(raw_a, saved=saved)
    activity_b = collect_codes(raw_b)

    print(f"活動A：{activity_a}")
    print(f"活動B：{activity_b}")
    print(f"原始saved：{saved}")
    print(f"原始raw_a：{raw_a}")

    # 空資料測試
    empty_result = collect_codes([])
    print(f"空資料：{empty_result}")