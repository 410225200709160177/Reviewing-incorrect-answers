def auto_classify(title: str, subject: str) -> str:
    """
    根据题目内容自动判断知识点
    """
    title = title.lower()

    # 数学
    if subject in ["数学", "math"]:
        if "函数" in title: return "函数"
        if "几何" in title or "三角形" in title: return "几何"
        if "方程" in title: return "方程"
        if "概率" in title: return "概率"
        return "数学其他"

    # 英语
    if subject in ["英语", "english"]:
        if "阅读" in title: return "阅读理解"
        if "完形" in title: return "完形填空"
        if "语法" in title: return "语法"
        return "英语其他"

    # 语文
    if subject in ["语文", "chinese"]:
        if "阅读" in title: return "现代文阅读"
        if "古诗" in title: return "古诗词"
        if "作文" in title: return "作文"
        return "语文其他"

    return "未分类"
