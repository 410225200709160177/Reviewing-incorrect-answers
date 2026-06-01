from ai_classify import auto_classify
from storage import save_topic, load_all_topics
from search import search_topics

def show_menu():
    print("\n==== 错题记录与查找 AI ====")
    print("1. 添加错题")
    print("2. 查看所有错题")
    print("3. 查找错题")
    print("4. 退出")
    return input("请选择功能：")

def add_new_topic():
    print("\n--- 添加错题 ---")
    subject = input("科目：")
    title = input("题目：")
    your_ans = input("你的答案：")
    correct_ans = input("正确答案：")
    analysis = input("解析：")

    # AI 自动分类
    know_point = auto_classify(title, subject)
    
    topic = {
        "科目": subject,
        "题目": title,
        "你的答案": your_ans,
        "正确答案": correct_ans,
        "解析": analysis,
        "知识点": know_point
    }

    save_topic(topic)
    print(f"✅ 保存成功！自动归类为：{know_point}")

def show_all():
    data = load_all_topics()
    if not data:
        print("暂无错题")
        return
    print("\n--- 所有错题 ---")
    for i, t in enumerate(data, 1):
        print(f"\n【第{i}题】{t['科目']} - {t['知识点']}")
        print(f"题目：{t['题目']}")
        print(f"你的答案：{t['你的答案']}")
        print(f"正确答案：{t['正确答案']}")
        print(f"解析：{t['解析']}")

def search():
    keyword = input("\n输入关键词/知识点/科目：")
    results = search_topics(keyword)
    if not results:
        print("未找到相关错题")
        return
    print(f"\n找到 {len(results)} 条结果：")
    for t in results:
        print(f"\n【{t['科目']} - {t['知识点']}】")
        print(f"题目：{t['题目']}")

if __name__ == "__main__":
    while True:
        choice = show_menu()
        if choice == "1":
            add_new_topic()
        elif choice == "2":
            show_all()
        elif choice == "3":
            search()
        elif choice == "4":
            print("退出程序")
            break
        else:
            print("输入错误，请重试")
