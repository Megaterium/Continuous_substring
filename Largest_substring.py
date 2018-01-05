s = 'azcbokczakl'

#### My best in 8 lines ###


x,start,str_,list_,new = [[ord(_) for _ in s],0,'',[],0]
for i,_ in enumerate(x):
    if _ >= start: str_,start = [str_+s[i],_]
    else:
        str_ , start ,none_= [s[i] , _,list_.append(str_)]
list_.append(str_)
for _ in list_:
    if len(_) >= new: final,new = [_,len(_)]
    
    

#### My best in 8 lines ###

print(final)
