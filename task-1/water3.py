def initial_state():
    return (8, 0, 0)

def is_goal(s):
    a, b, c = s
    if a==4 and b==4:
        return True

def successors(s):
    max_cap = [8,5,3]

    # i is parent and j is child
    for i in range(3):
        for j in range(3):
            # no tranfer if move x to x
            if i != j :
                part_cost = min(s[i],max_cap[j] - s[j])
                if part_cost != 0:
                    ans = list(s)
                    ans[i] -= part_cost
                    ans[j] += part_cost
                    yield (tuple([ans[k] for k in range(3)]),part_cost)

