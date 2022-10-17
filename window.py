import tkinter

file = open('words.txt', 'r')
word_q, word_a = file.readline().split()
file.close()





def test():
    user_answer = entry_word.get()
    if user_answer == word_a:
        label_test["text"] = "верно"
    else:
        label_test["text"] = "неверно"

window = tkinter.Tk()
window.geometry('300x200')
window.title("тренажёр по русскому языку")

label_question = tkinter.Label()
label_question['text'] = word_q
label_question.pack()

label_test = tkinter.Label()
label_test.pack()
entry_word = tkinter.Entry()
entry_word.pack()

button_test = tkinter.Button()
button_test['text'] = "проверить"
button_test["command"] = test
button_test.pack()



window.mainloop()