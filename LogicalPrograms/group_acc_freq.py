
import re
def count_character(str1):
    dict1={}
    pattern =r"\w"
    
    for i in str1:
        
        if re.match(pattern,i):
            
            dict1[i]=dict1.get(i,0)+1
    return dict1

def group_acc_freq(dict2):
    
    dict4 ={}
    print(dict2)
    for key,value in dict2.items():
        if value in dict4:
            dict4[value].append(key)
        else:
            dict4[value]=[key]
    return dict4

def main():
    
   dict2 =count_character("dileep4444wwwrrr@gmail.com")
   print(dict2)
   print(group_acc_freq(dict2))  
main()