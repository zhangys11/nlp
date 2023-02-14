def get_stop_words():

    stpwrdlst1=open("stop_words.txt", "r", encoding='utf-8').read().splitlines()

    # SnowNLP has its own stopword list
    # https://github.com/isnowfy/snownlp/blob/master/snownlp/normal/stopwords.txt
    stpwrdlst2=open("stop_words_snownlp.txt", "r", encoding='utf-8').read().splitlines()

    # Join multiple lists
    stpwrdlst = list(set(stpwrdlst1).union(set(stpwrdlst2)))

    # special items
    stpwrdlst.append("中")
    stpwrdlst.append("前")
    stpwrdlst.append("\r\n")
    stpwrdlst.append(" ")
    stpwrdlst.append("\n")
    stpwrdlst.append('\xa0')
    stpwrdlst.append('\t')
    stpwrdlst.append('说')
    stpwrdlst.append('分')
    stpwrdlst.append('据了解')
    stpwrdlst.append('他说')
    stpwrdlst.append('她说')
    stpwrdlst.append('他认为')
    stpwrdlst.append('她认为')
    stpwrdlst.append('他指出')
    stpwrdlst.append('她指出')
    stpwrdlst.append('他相信')
    stpwrdlst.append('她相信')
    stpwrdlst.append('The')
    stpwrdlst.append('the')
    #stpwrdlst.append('昨天')
    #stpwrdlst.append('昨天上午')
    #stpwrdlst.append('昨天下午')
    stpwrdlst.append('不仅如此')

    # skip years
    for i in range(1900,2100):
        stpwrdlst.append(str(i))
        
    return stpwrdlst