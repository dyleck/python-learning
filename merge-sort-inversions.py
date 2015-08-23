def sort(seq):
    seq = list(seq)
    if len(seq) <= 1: return (seq, 0)
    left, inv1 = sort(seq[:len(seq)//2])
    right, inv2 = sort(seq[len(seq)//2:])
    inv = inv1 + inv2
    res = []
    while left and right:
        if left[0] > right[0]:
            res.append(right.pop(0))
            inv += len(left)
        else:
            res.append(left.pop(0))
    res.extend(left)
    res.extend(right)
    return res, inv
    
def count_inversion(seq):
    """
        Count inversions in a sequence of numbers
    """
    inv = 0
    seq, inv = sort(list(seq))
    return inv

if __name__ == '__main__':
    print count_inversion((1,2,5,3,4,7,6))
    print count_inversion((0,1,2,3))