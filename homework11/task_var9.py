import requests
from tkinter import *


def click():
    print('Введите владельца репозитория(owner): ')
    owner = txt1.get()
    print('Введите название репозитория(repo): ')
    repo = txt2.get()
    r = requests.get(f'https://api.github.com/repos/{owner}/{repo}')

    with open('D:\\aza\\Jsonchik', 'w') as f:
        if 'company' in r.json():
            f.write(f"'company': '{r.json()['company']}'\n")
        else:
            f.write("'company':")
            f.write('None\n')
        f.write(f"'created_at': '{r.json()['created_at']}'\n")
        if 'email' in r.json():
            f.write(f"'email': '{r.json()['email']}'\n")
        else:
            f.write("'email':")
            f.write('None\n')
        f.write(f"'id': '{r.json()['id']}'\n")
        f.write(f"'name': '{r.json()['name']}'\n")
        f.write(f"'url': '{r.json()['url']}'\n")
        print('См. результат в файле')


window = Tk()
window.title('Ибрагимов Ильдар Равильевич')
window.geometry('550x150')
window.resizable(False, False)
lbl = Label(window, text='Введите владельца репозитория(owner):', font=('Times New Roman', 20))
lbl.grid(column=0, row=0)
lb2 = Label(window, text='Введите название репозитория(repo):', font=('Times New Roman', 20))
lb2.grid(column=0, row=2)

btn = Button(window, text='Получить данные в файл', command=click)
btn.grid(column=0, row=4)
txt1 = Entry(window, width=10)
txt1.grid(column=1, row=0)
txt2 = Entry(window, width=10)
txt2.grid(column=1, row=2)
window.mainloop()

