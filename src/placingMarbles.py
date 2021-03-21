# 文字として判定したいためinput()からjoin()でリスト化。
checkTarget = ''.join(str(input()))
# count()関数の結果を出力。
print(checkTarget.count('1'))