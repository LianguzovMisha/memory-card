#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint

#создание приложения и главного окна
#создание приложения
app = QApplication([])
#создание окна
window = QWidget()
#размер окна
window.resize(750, 450)
#создание виджетов главного окна
window.setWindowTitle('Memory Card')
lb_Question = QLabel('Какой национальности не существует?')
#создание кнопок
answer = QPushButton('Ответить')

#создание группы и 4 ёх вхоящих в неё флажков
RadioGruopBox = QGroupBox('Варианты ответов')
RadioGruopBox1 = QGroupBox('Результат теста')
RadioGruopBox1.hide()
lb_Result = QLabel('Правильно/Неправильно')
lb_Correct = QLabel('Правильный/неправильный ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft|Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
RadioGruopBox1.setLayout(layout_res)

rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

#линии и привязки к линиям
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGruopBox.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=Qt.AlignHCenter)
layout_line2.addWidget(RadioGruopBox)
layout_line2.addWidget(RadioGruopBox1)

layout_line3.addStretch(1)

layout_line3.addWidget(answer, stretch=2)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
layout_card.addWidget(answer, alignment=Qt.AlignCenter)

window.setLayout(layout_card)


#функциии и классы, списки и тд

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []

question_list.append(Question('Какой национальности не существует?', 'Энцы', 'Смурфы', 'Чулымцы', 'Алеуты'))
question_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Синий', 'Белый'))
question_list.append(Question('Государственный язык Португалии?', 'Португальский', 'Испанский', 'Бразильский', 'Английский'))
question_list.append(Question('В каком году началась вторая мировая война?', '1939', '1942', '1941', '1938'))
question_list.append(Question('Когда была выпущена коммерческая версия Android 1.0?', '2008', '2000', '2010', '2007'))
question_list.append(Question('В каком году закончилась Великая Отечественная война?', '1945', '1943', '1944', '1946'))
question_list.append(Question('В каком году сформировался СССР?', '1923', '1918', '1927', '1922'))
question_list.append(Question('В каком году компания Apple выпустила свой первый смартфон?', '2007', '2008', '2012', '2005'))
question_list.append(Question('Какой самый простой язык программирования?', 'Python', 'Java', 'C#', 'C++'))
question_list.append(Question('В каком году распался СССР?', '1991', '1990', '1998', '1986'))
question_list.append(Question('В какой день началась Великая Отечественная война?', '22 июня', '1 сентября', '1 июля', '23 августа'))

def next_question():
    window.total += 1
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)

def click_ok():
    if answer.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def show_result():
    RadioGruopBox.hide()
    RadioGruopBox1.show()
    answer.setText('Следующий вопрос')
    lb_Question.setText('Самый сложный вопрос в мире!')

def show_question():
    RadioGruopBox.show()
    RadioGruopBox1.hide()
    answer.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика:\n-Всего вопросов:', window.score, '\n-Правильных ответов:', window.total)
        print('-Рейтинг:', window.score/window.total * 100)
    else:
        window.score -= 1
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('-Рейтинг:', window.score/window.total * 100)
q = Question('Какой национальности не существует?', 'Энцы', 'Смурфы', 'Чулымцы', 'Алеуты')

window.cur_question = -1

ask(q)

window.total = 0

window.score = 0

next_question()
#обработка нажатий
answer.clicked.connect(click_ok)

#видимое окно
window.show()
#открытое до нажатия на крестик
app.exec_()