while True:
    try:
        s = raw_input()
        terms = s.split()
        n = int(terms[0])
         
        word_list = list()
         
        i = 1
        while i < n + 1:
            word_list.append(terms[i])
            i = i + 1
             
        query_word = terms[i]
        query_index = int(terms[-1])
         
        sort_list = list()
         
        for word in word_list:
            if word == query_word:
                continue
             
            if len(word) != len(query_word):
                continue
             
            l = list(word)
             
            for each in query_word:
                if each in l:
                    l.remove(each)
                     
            if len(l) == 0:
                sort_list.append(word)
                 
                 
        sort_list.sort()
         
        print len(sort_list)
         
         
        if query_index <= len(sort_list):
            print sort_list[query_index - 1]
                     
         
    except:
        break