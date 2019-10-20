import quanlyhoadon,quanlykhachang,quanlyuser
import os
import json

def user():
  print("+--------------MENU_USER-------------------------------+")
  print("|Chon CUSER de tao user                                |")
  print("|Chon DUSER de xoa user                                |")
  print("|Chon RUSER de xem danh sach user                      |")
  print("|Chon LOGIN de login                                   |")
  print("|Chon E de thoat                                       |")
  print("+------------------------------------------------------+")
  while True:
    x = input("=> chon chuc nang USER: ")
    print("=> ban da chon chuc nang: ",x)
    if x.upper() == 'CUSER':
      quanlyuser.tao_user()
    if x.upper() == 'DUSER':
      quanlyuser.xoa_user()
    if x.upper() == 'RUSER':
      quanlyuser.xem_user()
    if x.upper() == 'LOGIN':
      quanlyuser.login()
    if x.upper() == 'E':
      return

def hoadon():
  print("+--------------MENU_HOA_DON----------------------------+")
  print("|Chon C de tao hoa don                                 |")
  print("|Chon R de xem thong tin hoa don                       |")
  print("|Chon T de tinh tong doanh thu                         |")
  print("|Chon A de tinh tong hang hoa ban ra                   |")
  print("|Chon E de thoat                                       |")
  print("+------------------------------------------------------+")
  while True:
    x = input("=> chon chuc nang HOADON: ")
    print("=> ban da chon chuc nang: ",x)
    if x.upper() == 'C':
      quanlyhoadon.lop_hoadon.tao_hoadon()
    if x.upper() == 'R':
      quanlyhoadon.lop_hoadon.xem_hoadon()
    if x.upper() == 'T':
      quanlyhoadon.lop_hoadon.xem_tongdoanhthu()
    if x.upper() == 'A':
      quanlyhoadon.lop_hoadon.tonghanghoaban()
    if x.upper() == 'E':
      return
def hanghoa():
  print("+--------------MENU_HANG_HOA---------------------------+")
  print("|Chon HH de xem hang theo thang                        |")
  print("|Chon LHH de xem loai hang hoa chay nhat               |")
  print("|Chon THH de tao hang hoa                              |")
  print("|Chon XHH de xem hang hoa                              |")
  print("|Chon TLH de tao loai hang hoa                         |")
  print("|Chon XTK de xem ton kho hang hoa                      |")
  print("|Chon NK de nhap kho hang hoa                          |")
  print("|Chon E de thoat                                       |")
  print("+------------------------------------------------------+")
  while True:
    x = input("=> chon chuc nang HANGHOA: ")
    print("=> ban da chon chuc nang: ",x)
    if x.upper() == 'HH':
      quanlyhoadon.lop_hanghoa.hanghoatheothang()
    if x.upper() == 'LHH':
      quanlyhoadon.lop_hanghoa.loaihh_chaynhat()
    if x.upper() == 'TLH':
      quanlyhoadon.lop_hanghoa.tao_loaihanghoa()
    if x.upper() == 'XLH':
      quanlyhoadon.lop_hanghoa.xem_loaihanghoa()
    if x.upper() == 'THH':
      quanlyhoadon.lop_hanghoa.tao_hanghoa()
    if x.upper() == 'XHH':
      quanlyhoadon.lop_hanghoa.xem_hanghoa()
    if x.upper() == 'NK':
      quanlyhoadon.lop_kho.nhapkho()
    if x.upper() == 'XTK':
      quanlyhoadon.lop_kho.xuat_tonkho()
    if x.upper() == 'E':
      return

def khachhang():
  print("+--------------MENU_KHACH_HANG-------------------------+")
  print("|Chon XDSKH de xem danh sach khach hang                |")
  print("|Chon XTTKH de xem thong tin khach hang                |")
  print("|Chon XKHTM de xem khach hang than mat                 |")
  print("|Chon E de thoat                                       |")
  print("+------------------------------------------------------+")
  while True:
    x = input("=> chon chuc nang KHACHHANG: ")
    print("=> ban da chon chuc nang: ",x)
    if x.upper() == 'XDSKH':
      quanlykhachang.xem_dskhachhang()
    if x.upper() == 'XTTKH':
      quanlykhachang.xem_thongtin_KH()
    if x.upper() == 'XKHTM':
      quanlykhachang.khachhang_thanmat()
    if x.upper() == 'E':
      return
while True:
  print("+------------------------------+")
  print("|[1]  Thao tac voi user        |")
  print("|[2]  Thao tac voi hang hoa    |")
  print("|[3]  Thao tac voi hoa don     |")
  print("|[4]  Thao tac voi khach hang  |")
  print("|[5]  Thoat                    |")
  print("+------------------------------+")
  nhap = input("[+]  Chon chuc nang: ")
  if nhap == '1':
    user()
  if nhap == '2':
    hanghoa()
  if nhap == '3':
    hoadon()
  if nhap == '4':
    khachhang()
  if nhap == '5':
    print("Cam on! Hen gap lai...")
    break
