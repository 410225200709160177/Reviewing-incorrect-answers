from storage import load_all_topics

def search_topics(keyword: str):
    data = load_all_topics()
    result = []
    keyword = keyword.lower()
    for t in data:
        if (keyword in t["题目"] or
            keyword in t["知识点"] or
            keyword in t["科目"]):
            result.append(t)
    return result
