# import permutations
from itertools import permutations

towers = [
    { (10, 1, False) },
    { (41, 1, True), (8, 1, True), (19, 1, True), (17, 1, True) },
    { (0, 1.0/3.0, False), (85, 1, True), (121, 1, True), (98, 1, True) },
    { (886, 1, True), (197, 1, True), (0, 2, False), (273, 1, True) }
]

# in score_path, path is a list of tuples. The score adds the left value and multiplies by the right 
# value, as an integer. If the score is even zero or negative, return. If the score is not 777, return.
# otherwise, print the score and the path.
def score_path(path):
    score = 0
    for v_add, v_mult, is_goblin in path:
        if is_goblin and score <= v_add:
            return
        score = int((score + v_add) * v_mult)
        if score <= 0:
            return
    if score != 2222:
        return
    print (score, path)

def follow_path(tower, path = []):
    if not tower:
        score_path(path)
    else:
        current_tower = tower[0]
        for subpath in permutations(current_tower):
            follow_path(tower[1:], path + list(subpath))

follow_path(towers)
