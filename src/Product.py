# 1行に複数の文字なので、split()関数でList化→map()関数で数値に変換。
a,b = map(int, input().split())
# 条件演算子でそのまま判定結果を返して出力。
print('Even' if (a * b) % 2 == 0  else 'Odd')