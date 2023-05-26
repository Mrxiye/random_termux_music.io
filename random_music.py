import requests
import os
# 调用inputimeout，超时代码
from inputimeout import inputimeout, TimeoutOccurred

while 1:
	print('\033[0;32m%s\033[0m' % '=========================================')
		  
	print('\033[0;33m%s\033[0m' % '【随机听音乐 by 王熙业】终端应用')
	print('\033[0;36m%s\033[0m' % '所有资源来于网络api')
	print('\033[0;35m%s\033[0m' % '该文件用于liunix或termux终端，实现听音乐的小应用')
	print('the requirements of run the codes: pip3 install requests , pkg install wget , catimg ,  mpv ')
	print('\033[0;32m%s\033[0m' % '=========================================')
	os.system('date')
	
	want=input('选一种歌随机听?默认1(1:热歌榜 2:新歌榜 3:电音榜 4:抖音榜 5:退出) ')
	if want=='5':
		break
	save=input('是否save？默认否( y or n )')
	circle=input('是否一直播放?默认否( y or n) ')
	choose='0'
	
	if want=='2':
	    choose='新歌榜'
	elif want=='3':
	    choose='电音榜'
	elif want=='4':
		choose='抖音榜'
	else:
	    choose='热歌榜'
		
	off=0
	while off==0:
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
	    #显示图片和参数信息
	    pic='catimg '+picname
	    os.system(pic)
	    print('网址==> '+url)
	    print('高清图片网址==> '+picurl)
	    print(choose)
	    print('歌手==> '+artistsname)
	    print('歌名==> '+name)
	    print('\033[0;33m%s\033[0m' % 'playing......等待播完！ctrl+c to stop. p:暂停和继续 L:循环播放 左箭头:快退5秒 右箭头:快进5秒 上箭头:快进1分钟 下箭头:快退1分钟')
	    mpv= 'mpv '+name
	    os.system(mpv)
	    #终端播放音乐
	    print('已经播完！')
	    
	    #是否保存文件
	    if save=='y':
	    	print('ok,it had been downloaded!')
	    	os.system('ls')
	    else:
	    	dell='rm -r '+name
	    	delpic='rm -r '+picname
	    	os.system(dell)
	    	os.system(delpic)
	    			
	    if circle=='y':
	    	print('准备加载下一首。。。。。。。')	
	    else:
	    	off=1
	    
	    try:
	    	# 数秒内未完成输入，则超时
	        bback = inputimeout(prompt='你有5秒时间考虑是否回到首页(y or n)', timeout=5)
	        if bback=='y':
	        	bback='n'
	        	off=1
	        	save='n'
	        	circle='n'
	    except TimeoutOccurred:
	   		print('超时。开始加载下一首。。。。。。。')
	    # 继续执行后续代码

print('thank you to use it!')
    