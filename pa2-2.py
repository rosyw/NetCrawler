import requests,csv,time
lst = []
# 设置start，每隔2s访问一下
for n in range(0,250,20):
    api = 'https://api.douban.com/v2/movie/top250?start=%d&apikey=0df993c66c0c636e29ecbb5344252a4a'% n
    time.sleep(2)
    r = requests.get(api,headers={'user-agent':'chrome'})
    top_dict = r.json()
    # print(top_dict)
    # 最后一次只返回10部电影
    sub = top_dict.get('subjects')
    for i in range(len(sub)):
        movie = sub[i]
        score = movie.get('rating')['average']
        title = movie.get('title')
        # 电影《二十二》无演员，排除这种异常
        try:
            name = ''
            for j in range(3):
                cast = movie.get('casts')[j]
                name += cast.get('name')+'，'
        except:
            name = '无'
        du = movie.get('durations')[0]
        poster = movie.get('images')['small']
        tuple = (i+n+1,title,score,name,du,poster)
        lst.append(tuple)

# print(lst)
headers = ['排名','电影名','评分','主演','片长','海报']
with open('top250.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(lst)