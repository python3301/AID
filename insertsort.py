#插入排序
#原始数据 value
#[91,60,20,120,149,48,100,50,75,70]

def insert(value):
    #外层循环：对应遍历所有无序数据，找出插入位置
    for i in range(1,len(value)):
        #备份取出数据
        temp = value[i]
        #记录取出时的下标
        pos = i

        #内层循环：对应从后向左扫描所有有序数据
        #1->
        #2->
        #3->
        for j in range(i-1,-1,-1):
            #若有序数据大于取出数据
            if value[i] > temp:
                #有序数据后移
                value[j+1] = value[i]
                #更新数据的插入位置
                pos = j# 对应所有有序数据
            #若有序数据小于等于取出数据
            else:
                #更新数据的插入位置
                pos = j + 1
                break
        #在指定位置插入数据
        value[pos] = temp





if __name__ == "__main__":
    #原始数据
    value = [91,60,20,120,149,48,100,50,75,70]
    #插入排序
    print("排序前：",value)
    insert(value)
    print("排序后:",value)