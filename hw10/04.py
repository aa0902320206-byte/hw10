

def select_clicks(raw_clicks, min_clicks=10):
    """
    清理素材點擊紀錄並篩選合格項目：
    1. map() 搭配 lambda 去除頭尾空白。
    2. filter(None, ...) 刪除空字串。
    3. map(int, ...) 轉整數並存成 list。
    4. 篩選出大於或等於 min_clicks 的項目。
    """
    # 清理流程：去除空白 -> 過濾空字串 -> 轉整數
    stripped = map(lambda x: x.strip(), raw_clicks)
    non_empty = filter(None, stripped)
    numbers = list(map(int, non_empty))

    # 篩選合格項目
    qualified = list(filter(lambda x: x >= min_clicks, numbers))

    return numbers, qualified

if __name__ == "__main__":
    # 一、共同設定：帶入自己的完整學號
    student_id = input("請輸入完整學號：").strip().upper()
    tail = student_id[-3:]
    a = int(student_id[-3])
    b = int(student_id[-2])
    c = int(student_id[-1])
    s = a + b + c

    # 題目資料設定
    raw_clicks = [str(10 + a), "0", "", " " + str(5 + b) + " ",
                  "   ", str(15 + c), str(5 + b)]
    min_clicks = 5 + b

    print(f"學號：{student_id}")
    print(f"點擊門檻：{min_clicks}")

    numbers, qualified = select_clicks(raw_clicks, min_clicks=min_clicks)
    print(f"清理結果：{numbers}")
    print(f"合格結果：{qualified}")
    print(f"合格筆數：{len(qualified)}")
    print(f"合格合計：{sum(qualified)}")

    # 排序與排名輸出
    sorted_qualified = sorted(qualified, reverse=True)
    for rank, val in enumerate(sorted_qualified, start=1):
        print(f"第{rank}名：{val}次")

    # 門檻 100 測試
    _, qualified_100 = select_clicks(raw_clicks, min_clicks=100)
    print(f"門檻100合格結果：{qualified_100}")
    print(f"門檻100合格筆數：{len(qualified_100)}")
    print(f"門檻100合格合計：{sum(qualified_100)}")
    if len(qualified_100) == 0:
        print("無符合門檻的素材")