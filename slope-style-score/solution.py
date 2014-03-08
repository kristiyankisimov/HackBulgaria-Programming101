def slope_style_score(scores):
    sum_scores = sum(scores) - min(scores) - max(scores)
    score = int(sum_scores / (len(scores) - 2) * 100)
    return score / 100