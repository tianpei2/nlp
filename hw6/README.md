Assignment 6  

The feature set I tried is like below:  
is_start: whether the token is "start" (the first token in the sentence)  
is_end: whether the token is "end" (the last token in the sentence)  
is_alpha  
is_ascii  
is_digit  
is_punct  
is_alnum  
like_num: whether the token is a number  
is_title  
is_lower  
is_upper  
is_date  
w_self: return the token itself  
p_self: return pos itself  
c_self: return the chunk itself  
t_self: return the tag itself  
pre_w: return the previous token  
pre_p: return the previous pos  
pre_c: return the previous chunk  
pre_t: return the previous tag  
post_w: return the next token  
post_p: return the next pos  
post_c: return the next chunk  
prepre_w: return the previous two token  

Run the program:  
javac -cp maxent-3.0.0.jar:trove.jar MEtrain.java  
javac -cp maxent-3.0.0.jar:trove.jar MEtag.java  
python3 assignment6.py CONLL_NAME_CORPUS_FOR_STUDENTS/CONLL_train.pos-chunk-name  
java -cp .:maxent-3.0.0.jar:trove.jar MEtrain output model  
python3 assignment6.py CONLL_NAME_CORPUS_FOR_STUDENTS/CONLL_dev.pos-chunk  
java -cp .:maxent-3.0.0.jar:trove.jar MEtag output model response.name  
python score.py  

score on the development corpus:  
accuracy: 96.17  
5917 groups in key  
5454 groups in response  
4552 correct groups  
precision: 83.46  
recall:    76.93  
F1:        80.06  
