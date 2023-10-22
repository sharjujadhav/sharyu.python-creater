26.Create a dictionary of student names and their scores, then find the average
score


def solve(scores):
    avg_scores = dict()
    for name in scores:
        avg_scores[name] = sum(scores[name])/len(scores[name])
        return list(avg_scores.values())
scores = {'soni' : [25,36,47,45], 'roshani' : [85,74,69,47], 'kranti' : [65,35,87,14], 'kanu' : [74,12,36,75]}
print(solve(scores))
    
