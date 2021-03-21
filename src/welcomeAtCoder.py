# 入力1行目。普通に受け取る。
a = int(input())

# 入力2行目。２種文字列があるので、split()でList化しmap()でint型に変換。
b,c = map(int, input().split())

# 入力3行目。普通に受け取る。
str = str(input())

# 結果の出力。プレースホルダとformat()関数を利用する。
print('{} {}'.format(a+ b+ c, str))