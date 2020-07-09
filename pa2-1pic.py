import requests
from PIL import Image
api = 'https://api.douban.com/v2/movie/1292052?apikey=0df993c66c0c636e29ecbb5344252a4a'
r = requests.get(api,headers={'user-agent':'chrome'})
# r.text
# r.encoding
dict = r.json()

# 获取海报的url
pic_link = dict.get('image')
# print(pic_link)
p = requests.get(pic_link,headers={'user-agent':'chrome'})

# 将海报写入本地图片
with open('xiao.jpg','wb') as f:
    f.write(p.content)

# 打开图片
img = Image.open('xiao.jpg')
img.show()
