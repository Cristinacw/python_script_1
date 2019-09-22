import random
import linecache
#生成fastq文件
for i in range(10):
    seq=""
    string=""
    #描述行的生成
    description_name=random.choice(["@SEQ_ID","@HWUSI-EAS100R"])
    lane=random.randint(1,10)
    tile=random.randint(1,100)
    x=random.randint(1,1000)
    y=random.randint(1,2000)
    description=""
    signal_flag=random.randint(1,2)
    description='%s:%d:%d:%d:%d#0/%dlength=150'%(description_name,lane,tile,x,y,signal_flag)
    #碱基序列的生成
    for j in range(150):
        seq+=random.choice('ATCG')
    #生成间隔行
    s="+"+description+'\n'
    #生成质量控制行
    for j in range(150):
        q=random.randint(0,60)+33
        string+=chr(q)
    all_string=description+'\n'+seq+'\n'+s+string+'\n'
    #写入fastq文件中
    with open('ten_examples.fastq', 'a') as fp:
        fp.write(all_string)

#fastq到fasta文件的转换
for i in range(10):
    #描述行的生成
    description=random.choice([">chr1",">chr2",">chr3"])
    #按照行号提取fastq文件并存入临时变量并写入fasta文件中
    linenumber=2+4*i
    line=""
    line=linecache.getline('ten_examples.fastq',linenumber)
    line=line.strip()
    line_first=line[0:80]
    line_last=line[80:]
    line_final=description+'\n'+line_first+'\n'+line_last+'\n'
    with open('ten_examples.fasta', 'a') as fp:
        fp.write(line_final)
#    print(line_first)
#    print(line_last)
#    print(len(line_first))
#    print(len(line_last))