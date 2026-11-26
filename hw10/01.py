

def ad_report(impressions, clicks, target=3.0):
    """
    計算廣告 CTR 與達標狀態。
    當 impressions 為 0 時，回傳 (None, False)。
    當 impressions > 0 但 clicks 為 0 時，CTR 為 0.0。
    """
    if impressions == 0:
        return (None, False)
    
    ctr = (clicks / impressions) * 100
    passed = ctr >= target
    return (ctr, passed)

if __name__ == "__main__":
    # 一、共同設定：帶入自己的完整學號
    student_id = input("請輸入完整學號：").strip().upper()
    tail = student_id[-3:]
    a = int(student_id[-3])
    b = int(student_id[-2])
    c = int(student_id[-1])
    s = a + b + c

    # 題目資料設定
    ads = [
        ("搜尋廣告", 1000 + 100 * a, 30 + 5 * b),
        ("社群廣告", 1200 + 100 * b, 24 + 4 * c),
        ("影音廣告", 0, 0),
    ]
    target = 2.5 + 0.1 * c

    print(f"學號：{student_id}")
    print(f"CTR門檻：{target:.2f}%")

    passed_count = 0
    for name, imp, clk in ads:
        ctr, passed = ad_report(imp, clk, target=target)
        if passed:
            passed_count += 1
            
        if ctr is None:
            ctr_str = "無曝光資料"
        else:
            ctr_str = f"{ctr:.2f}%"
            
        print(f"{name}：曝光={imp}，點擊={clk}，CTR={ctr_str}，達標={passed}")

    print(f"達標廣告數：{passed_count}")

    # 驗證預設門檻與零點擊
    default_test = ad_report(1000, 30)
    zero_click_test = ad_report(1000, 0)
    print(f"預設門檻測試：{default_test}")
    print(f"零點擊測試：{zero_click_test}")