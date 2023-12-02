import math
tokens = [str(i) for i in range(10)] + ["zero","one", "two","three","four","five","six","seven","eight","nine"]
english2int = {v:str(k) for k,v in enumerate(["zero","one", "two","three","four","five","six","seven","eight","nine"])}
def solution(input_str):
    return int(min([(tok if tok.isdigit() else english2int[tok],x) for tok in tokens if (x:=input_str.find(tok)) != -1], key=lambda x: x[1])[0]+max([(tok if tok.isdigit() else english2int[tok],x) for tok in tokens if (x:=input_str.rfind(tok)) != -1], key=lambda x: x[1])[0])
with open('input.txt') as f:
    input_text = [x for x in f.read().split('\n') if x]
    ret = [solution(x) for x in input_text]
    print(sum(ret))
