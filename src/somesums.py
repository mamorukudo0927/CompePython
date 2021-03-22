# 1行に半角スペース区切りで複数の文字なので、Split,Mapを利用して取得
N,A,B=map(int,input().split())
# 数値*boolはTrue=1,False=0となることを利用してNの数値に到達するまでループ
print(sum(i*(A<=sum(map(int,str(i)))<=B)for i in range(N+1)))
