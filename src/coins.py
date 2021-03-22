a, b, c, x = map(int, open())
# リスト内包で回しつつ、合計値がXと同じになる回数をsum()関数で出力。
print(sum(500* i +100 *j +50 *k == x for i in range(a+ 1)for j in range(b+ 1)for k in range(c+ 1)))