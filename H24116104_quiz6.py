#隨機化正確字母
import random
alpha_list = ["a", "b", "c", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", 
"w", "x", "y", "z" ] 
true_alpha = random.choice(alpha_list)

#猜字母
guess_alpha = input("Guess the lowercase alphabet:")

#變量設定
tried_times = 1
Previous_guess = []
a_d = 0
e_h = 0
i_l = 0
m_p = 0
q_t = 0
u_x = 0
y_z = 0


#遊戲進行過程
while guess_alpha != true_alpha:
    #保留下猜過的字母
    Previous_guess += [guess_alpha]
    #判斷是否在範圍裏面
    if guess_alpha not in alpha_list:
        guess_num = input("Please enter a lowercase alphabet: ")
        tried_times += 1
    #判斷太高還太低
    if guess_alpha > true_alpha:
        guess_alpha = input("The alphabet you are looking for is alphabetically lower:")
        tried_times += 1
    if guess_alpha < true_alpha:
        guess_alpha = input("The alphabet you are looking for is alphabetically higher:")
        tried_times += 1
#最後的結果也要加進猜過的數字
Previous_guess += [guess_num]

#print
print("Congratualtions! You guessed the alphabet in", tried_times ,"tries")
print("Guess Histogram:")
print("a-d:", "*"*a_d)
print("e-h:", "*"*e_h) 
print("i-l:", "*"*i_l) 
print("m-p:", "*"*m_p) 
print("q-t:", "*"*q_t) 
print("u-x:", "*"*u_x)
print("y-z", "*"*y_z) 

