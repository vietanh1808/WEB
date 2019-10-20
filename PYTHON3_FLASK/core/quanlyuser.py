import os
danhsachuser = []

def load_user_luckhoidong():
    with open("../user_and_customer/danhsachuser.csv", "r") as f:
        line = f.readline()
        while line:
            user = {}
            str_cut = line.split("#") 
            user['id'] = str_cut[0]
            user['name'] = str_cut[1]
            user['pass'] = str_cut[2][0:len(str_cut[2]) - 1]
            danhsachuser.append(user)
            line = f.readline()
load_user_luckhoidong()
def kiemtra_id_user():
    while True:
        flag = 0
        nhap = input("Moi ban nhap ID user: ")
        for user in danhsachuser:
            if nhap == user['id']:
                flag = 1
        if flag == 0:
            return nhap
            break
        else:
            print("ID user nay da ton tai!")
def tao_user():
    id_user = kiemtra_id_user()
    user = {}
    user['id'] = id_user
    user['name'] = input("Moi ban nhap USERNAME cua user: ")
    user['pass'] = input("Moi ban nhap PASSWORD cua user: ")
    danhsachuser.append(user)
    with open("../user_and_customer/danhsachuser.csv", "a") as f:
        str_save = user['id'] + '#' + user['name'] + '#' + user['pass'] + '\n' 
        f.write(str_save)
        return
def update_user():
    with open("../user_and_customer/danhsachuser.csv", "w") as f:
        for user in danhsachuser:
            str_save = user['id'] + '#' + user['name'] + '#' + user['pass'] + '\n' 
            f.write(str_save)
def xoa_user():
    nhap = input("Moi ban nhap ID user can xoa: ")
    for i in range(len(danhsachuser)):
        if nhap == danhsachuser[i]['id']:
            del danhsachuser[i]
            print("Done!")
            update_user()
            return
    print("[!] Khong co ID nay trong danh sach")
def login_user():
    #input()
    flag = 0
    while True:
        print("+++++++++++++ LOGIN +++++++++++++")
        id = input("ID: ")
        username = input("username: ")
        password = input("password: ")
        for user in danhsachuser:
            if username in user['name'] and id in user['id'] and password in user['pass']:
                print("Done!")
                flag = 1
        if flag == 0:
            print("Ten tai khoan hoac mat khau hoac id bi sai. Moi ban nhap lai!")
        else:
            break
def xem_user():
    count = 0
    print("++++++++++++ DANH SACH USER ++++++++++++")
    for user in danhsachuser:
        count += 1
        print("[+] USER{}: id = {}, username = {}".format(count, user['id'], user['name']))
# print(danhsachuser)
# login_user()
# xoa_user()
# tao_user()