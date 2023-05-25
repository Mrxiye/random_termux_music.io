import requests
import os

print('the requirements of run the codes: pkg install wget , catimg , play-audio ')

while 1:
    print('\033[0;33m%s\033[0m' % '【随机听音乐 by 王熙业】终端应用')
    print('\033[0;36m%s\033[0m' % '所有资源来于网络api')
    print('\033[0;35m%s\033[0m' % '该文件用于liunix或termux终端，实现听音乐的小应用')
    os.system('date')
    want=input('选一种歌随机听?(1:热歌榜 2:新歌榜 3:电音榜 4:抖音榜 5:退出)')
    if want=='5':
        break
    
    if want=='1':
    	choose='热歌榜'
    if want=='2':
    	choose='新歌榜'
    if want=='3':
    	choose='电音榜'
    if want=='4':
    	choose='抖音榜'
    
    urls='https://api.uomg.com/api/rand.music?sort='+choose+'&format=json'
    res=requests.get(urls)
    print(res.text)
    #将文本格式转为字典
    rtt=eval(res.text)
    rt=rtt['data']
    
    #从网页获取数据的各个参数
    name=rt['name']
    url=rt['url']
    picurl=rt['picurl']
    artistsname=rt['artistsname']
    
    picname= name+'.jpg'
    wgetpic='wget -O ' +picname+' '+picurl
    os.system(wgetpic)
    
    #下载图和音乐文件到本地
    name=name+'.mp3'
    wget='wget -O ' +name+' '+url
    os.system(wget)
    play='play-audio '+name	
    #显示图片和参数信息
    pic='catimg '+picname
    os.system(pic)
    print('网址==> '+url)
    print('高清图片网址==> '+picurl)
    print(choose)
    print('歌手==> '+artistsname)
    print('歌名==> '+name)
    	
    print('playing......等待播完！')
    #终端播放音乐
    os.system(play)
    print('已经播完！')
    #是否保存文件
    save=input('Do you wanna save the song and the picture?(y or n)')
    if save=='y':
    	print('ok,it had been downloaded!')
    	os.system('ls')
    else:
    	dell='rm -r '+name
    	delpic='rm -r '+picname
    	os.system(dell)
    	os.system(delpic)
    		
print('thank you to use it!')
    