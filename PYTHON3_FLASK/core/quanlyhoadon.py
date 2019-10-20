import os,json

danhsachhanghoa = []
danhsachloaihanghoa = []
ds_hang_tonkho = []
danhsachhoadon = []

class lop_hanghoa:
  def load_loaihanghoa_luckhoidong():
    files = os.listdir("../danhmuc")
    if "loaihanghoa.csv" not in files:
      return
    
    with open('../danhmuc/loaihanghoa.csv', 'r') as f:
      line = f.readline()
      while line:
          str_to_reads = line.split("#")
          #print("str_to_reads:", str_to_reads)
          if len(str_to_reads) > 1:
              loaihanghoa = {}
              loaihanghoa["id"] = str_to_reads[0]
              tenloai = str_to_reads[1]
              if tenloai.endswith('\n'):
                  tenloai = tenloai[0:len(tenloai)-1]
              loaihanghoa["ten"] = tenloai
              danhsachloaihanghoa.append(loaihanghoa)
          line = f.readline()
  load_loaihanghoa_luckhoidong()

  def load_hanghoa_luckhoidong():
    files = os.listdir("../danhmuc")
    if "hanghoa.csv" not in files:
      return
    with open('../danhmuc/hanghoa.csv', 'r') as f:
      line = f.readline()
      while line:
          str_to_reads = line.split("#")
          #print("str_to_reads:", str_to_reads)
          if len(str_to_reads) > 1:
              hanghoa = {}
              hanghoa["id"] = str_to_reads[0]
              hanghoa["ten"] = str_to_reads[1]
              hanghoa["giaban"] = str_to_reads[2]
              hanghoa["loaihanghoa_id"] = str_to_reads[3]
              
              if hanghoa["loaihanghoa_id"].endswith('\n'):
                  hanghoa["loaihanghoa_id"] = hanghoa["loaihanghoa_id"][0:len(hanghoa["loaihanghoa_id"])-1]
              danhsachhanghoa.append(hanghoa)
          line = f.readline()
  load_hanghoa_luckhoidong()

  def xem_hanghoa(id=None):
    if id is None:
        id = input("xin moi nhap id hang hoa:")
    for hanghoa in danhsachhanghoa:
      if hanghoa["id"] == id:
        print(hanghoa)
        return hanghoa
  
    if id is None:
        id = input("xin moi nhap id hang hoa:")
    for loaihanghoa in danhsachloaihanghoa:
      if loaihanghoa["id"] == id:
        print(hanghoa)
        return hanghoa
  def xem_loaihanghoa(id=None):
    if id is None:
        id = input("xin moi nhap id loai hang hoa:")
    for loai in danhsachloaihanghoa:
      if loai["id"] == id:
        print("loai hang hoa: ", loai)
        return loai
  def tao_loaihanghoa():
    data = {}
    id = input("xin moi nhap id loai hang hoa:")
    tim_id_daco = xem_loaihanghoa(id)
    if tim_id_daco is not None:
      print("Da ton tai Ma loai hang hoa nay. Xin moi ban thu hien chu nang khac")
      return

    data["id"] = id
    data["ten"] = input("xin moi nhap ten loai hang hoa:")
    danhsachloaihanghoa.append(data)

    lop_hanghoa.append_loaihanghoa(data["id"], data["ten"])
  def tao_hanghoa():
    data = {}
    id = input("xin moi nhap id hang hoa: ")
    tim_id_daco = lop_hanghoa.xem_hanghoa(id)
    if tim_id_daco is not None:
      print("Da ton tai Ma loai hang hoa nay. Xin moi ban thu hien chu nang khac")
      return
    data["id"] = id
    data["ten"] = input("xin moi nhap ten hang hoa: ")
    data["giaban"] = input("xin moi nhap gia ban: ")
    loaihanghoa_id = input("xin moi nhap ma loai hang hoa: ")
    
    co_hienthi_danhsachloai = False
    tim_idloai_daco = lop_hanghoa.xem_loaihanghoa(loaihanghoa_id)
    
    while tim_idloai_daco is None:
      print("Danh sach loai hang hoa: ")
      for loaihanghoai in danhsachloaihanghoa:
          print(loaihanghoai["id"])
      loaihanghoa_id = input("xin moi nhap ma loai hang hoa: ")
      tim_idloai_daco = lop_hanghoa.xem_loaihanghoa(loaihanghoa_id)
    data["loaihanghoa_id"] = loaihanghoa_id
    danhsachhanghoa.append(data)

    lop_hanghoa.append_hanghoa(data['id'], data['ten'], data['giaban'], data["loaihanghoa_id"])
  def append_hanghoa(id, ten, giaban, loaihanghoa_id):
    str_to_save = id + "#" + ten + '#' + giaban + "#" + loaihanghoa_id + '\n'
    with open('../danhmuc/hanghoa.csv', 'a') as f:
        data = f.write(str_to_save)
  def append_loaihanghoa(id, ten):
    str_to_save = id + "#" + ten + '\n'
    with open('../danhmuc/loaihanghoa.csv', 'a') as f:
        data = f.write(str_to_save)
  def update_hanghoa(id, name):
    pass
  def update_loaihanghoa(id, name): 
    file_write = open("../danhmuc/loaihanghoa.csv", "w")
    for loai in danhsachloaihanghoa:
        if id == loai['id']:
            loai['ten'] = name
        str_to_save = loai['id'] + "#" + loai['ten'] + '\n'
        file_write.write(str_to_save)
  def mat_hang():
    danhsachban = {}
    loaihanghoaban = {}
    for hanghoa in danhsachhanghoa:
      danhsachban[hanghoa['ten']] = 0
    for loai in danhsachloaihanghoa:
      tenlhh = loai['id']
      loaihanghoaban[tenlhh] = {} 
      loaihanghoaban[tenlhh]['soluong'] = 0
      loaihanghoaban[tenlhh]['doanhthu'] = 0
    return danhsachban, loaihanghoaban
  mathang,loaihang = mat_hang()

  def hanghoatheothang(mathang=mathang):
    hanghoa_chaynhat = 0
    for file in os.listdir("../hoadon/"):
      with open("../hoadon/"+file, 'r') as f:
        data = json.load(f)
      for ten in data['danhsachhanghoa']:
        ten_hh = ten['ten']
        if ten_hh in mathang:
          mathang[ten_hh] += ten['soluong']

    hanghoa_chamnhat = mathang['coca']
    for hanghoa in mathang:
      if mathang[hanghoa] > hanghoa_chaynhat:
        hanghoa_chaynhat = mathang[hanghoa]
      if mathang[hanghoa] < hanghoa_chamnhat:
        hanghoa_chamnhat = mathang[hanghoa]
    for key in mathang:
      if mathang[key] == hanghoa_chaynhat:
        print("[+] Hang hoa ban chay nhat: ", key)
      elif mathang[key] == hanghoa_chamnhat:
        print("[+] Hang hoa ban cham nhat: ", key)
  def loaihh_chaynhat(loaihang=loaihang):
    soluong_chaynhat = doanhthu_chaynhat = 0
    for file in os.listdir("../hoadon/"):
      with open("../hoadon/"+file, 'r') as f:
        data = json.load(f)
      for ten in data['danhsachhanghoa']:
        ten_hh = ten['ten']
        for hh in danhsachhanghoa:
          if hh['ten'] == ten_hh:
            id_loaihh = hh['loaihanghoa_id']
            break
        if id_loaihh in loaihang:
          loaihang[id_loaihh]['soluong'] += ten['soluong']
          loaihang[id_loaihh]['doanhthu'] += ten['thanhtien']
    for loai in loaihang:
      if loaihang[loai]['soluong'] > soluong_chaynhat:
        soluong_chaynhat = loaihang[loai]['soluong']
      if loaihang[loai]['doanhthu'] > doanhthu_chaynhat:  
        doanhthu_chaynhat = loaihang[loai]['doanhthu']
    for loaihh in loaihang:
      if loaihang[loaihh]['soluong'] == soluong_chaynhat :
        print("[+] Loai hang hoa co so luong chay nhat la: ", loaihh)
      if loaihang[loaihh]['doanhthu'] == doanhthu_chaynhat:
        print("[+] Loai hang hoa co doanh thu chay nhat la: ", loaihh)
  def ktra_id_hanghoa():
    while True:
      id = input("Moi ban nhap ID hang hoa: ")
      for hanghoa in danhsachhanghoa:
        if id == hanghoa['id']:
          return hanghoa['ten'], hanghoa['giaban'], id

class lop_hoadon:
  def TaoFileHoaDon(thongtin_hoadon,tenhoadon):
      with open('../hoadon/'+str(tenhoadon)+'.json','w') as wfile:
          hoadon = json.dumps(thongtin_hoadon, indent=2)
          wfile.write(hoadon)
  def ktra_sohoadon():
      path = os.listdir("../hoadon/")
      while True:
        sohoadon = input('Moi ban nhap so hoa don: ')
        str_test = sohoadon + '.json'
        if path == []:
          return sohoadon
          break
        if str_test not in path:
          return sohoadon
          break
  def tao_hoadon():
      hoadon={}
      sohoadon = lop_hoadon.ktra_sohoadon()
      hoadon["sohoadon"] = sohoadon
      hoadon["ngayhoadon"]= input("nhap ngay hoa don :")
      hoadon["nguoimua"]= input("nhap nguoi mua hang :")
      hoadon["tongtientruocthue"] = 0
      hoadon["thue"] = 0.1
      hoadon["tongtien"] = 0
      hoadon["danhsachhanghoa"] = []

      nhaphanghoa = input("=> Ban co muon nhap hang hoa khong (y/n): ")
      while nhaphanghoa.upper() == 'Y':
          hanghoa = {}
          hanghoa["stt"] = input("nhap so thu tu: ")
          value_ten, value_gia, value_id = lop_hanghoa.ktra_id_hanghoa()
          print("Ten hang hoa: ", value_ten)
          print("Gia hang hoa: ", value_gia)
          hanghoa['ten'] = value_ten
          soluong = input("nhap so luong: ")
          hanghoa["soluong"] = int(soluong)
          hanghoa["dongia"] = int(value_gia)
          hanghoa["thanhtien"] = hanghoa["soluong"] * hanghoa["dongia"]
          
          # ham duoi la quan ly kho hang
          kiemtra_kho = lop_kho.kiemtra_kho(value_id, hanghoa['soluong'])
          if kiemtra_kho is not None:
            return

          hoadon["danhsachhanghoa"].append(hanghoa)
          hoadon["tongtientruocthue"] = hoadon["tongtientruocthue"] + hanghoa["thanhtien"]

          nhaphanghoa = input("=> Ban co muon nhap hang hoa khong (y/n): ")

      hoadon["tongtien"] = hoadon["tongtientruocthue"] + hoadon["tongtientruocthue"]*hoadon["thue"]
      lop_hoadon.TaoFileHoaDon(hoadon, sohoadon)
  def xem_hoadon():
    flag = 0
    nhap = input("Moi ban nhap so hoa don can xem: ")
    for file_hoadon in os.listdir("../hoadon/"):
      kiemtra_nhap = nhap + ".json"
      if kiemtra_nhap == file_hoadon:
        flag = 1 
        with open("../hoadon/"+ file_hoadon, "r") as f:     
          hoadon = json.load(f)
          sohoadon = hoadon['sohoadon']
          ngayhoadon = hoadon['ngayhoadon']
          nguoimua = hoadon['nguoimua']
          tongtien = str(hoadon['tongtien'])
          for data in hoadon['danhsachhanghoa']:
              stt = data['stt']
              hanghoa = data['ten']
              soluong = str(data['soluong'])
              dongia = str(data['dongia'])
              thanhtien = str(data['thanhtien'])
        print ('+++++++++++++++++THONG TIN HOA DON+++++++++++++++++++++ ')
        print ('So hoa don: ', sohoadon)
        print ('Ngay hoa don: ', ngayhoadon)
        print ('Nguoi mua: ', nguoimua)
        print ('+-------+----------+----------+----------+------------+')
        print ('|  STT  | hang hoa | so luong | don gia  | thanh tien |')
        print ('+-------+----------+----------+----------+------------+')
        print ('|'+stt+(7-len(stt))*' ', end='')
        print ('|'+hanghoa+(10-len(hanghoa))*' ', end='')
        print ('|'+soluong+(10-len(soluong))*' ', end='')
        print ('|'+dongia+(10-len(dongia))*' ', end='')
        print ('|'+thanhtien+(12-len(thanhtien))*' '+'|')
        print ('+-------+----------+----------+----------+------------+')
        print ('|'+' '*29+'|tong tien: '+tongtien+' '*(12-len(tongtien))+'|')
        print ('+-------+----------+----------+----------+------------+')
    if flag == 0:
      print("[!] So hoa don nay khong ton tai.")
  def xem_tongdoanhthu():
    tongdoanhthu = 0
    for file_hoadon in os.listdir("../hoadon/"):
      with open("../hoadon/"+ file_hoadon, "r") as f:     
        hoadon = json.load(f)
        tongdoanhthu = tongdoanhthu + hoadon["tongtien"]
    print("Tong doanh thu la: ", tongdoanhthu)
  def tonghanghoaban():
    tongsohanghoa = 0
    doanhsoban = 0
    tenhanghoa = input("nhap ten hang hoa can xem:")
    for file_hoadon in os.listdir("../hoadon/"):
      with open("../hoadon/"+ file_hoadon, "r") as f:     
        data = json.load(f)
        for hoadon in data['danhsachhanghoa']:
          if hoadon["ten"] == tenhanghoa:
            tongsohanghoa = tongsohanghoa + hoadon["soluong"]
            doanhsoban = doanhsoban + hoadon["thanhtien"]
            break
    print("Tong so hang hoa: ", tongsohanghoa)
    print("Doanh so ban: ", doanhsoban)

class lop_kho:
  def ghi_kho():
    file_w = open("../danhmuc/phieunhapkho.csv", "w")
    for hanghoakho in ds_hang_tonkho:
      for hanghoa in danhsachhanghoa:
        if hanghoa['id'] == hanghoakho['id']:
          str_save = hanghoakho['id'] + '#' + hanghoa['ten'] + '#' + str(hanghoakho['soluong']) + '\n'
          file_w.write(str_save)
          break
  def load_tonkho():
      with open("../danhmuc/phieunhapkho.csv", "r") as f:
          line = f.readline()
          while line:
              hang_tonkho = {}
              str_read = line.split("#")
              hang_tonkho['id'] = str_read[0]
              hang_tonkho['ten'] = str_read[1]
              if str_read[2].endswith('\n'):
                  hang_tonkho['soluong'] = str_read[2][:len(str_read[2])-1]
              else:
                  hang_tonkho['soluong'] = str_read[2]
              ds_hang_tonkho.append(hang_tonkho)
              line = f.readline()
  load_tonkho()
  def nhapkho():
      while True:
          nhap = input("Moi ban nhap id hang hoa: ")
          for hanghoa in ds_hang_tonkho:
              if nhap in hanghoa['id']:
                  soluong = int(input("Moi ban nhap so luong can nhap: "))
                  hanghoa['soluong'] = int(hanghoa['soluong'])
                  hanghoa['soluong'] += soluong
                  lop_kho.ghi_kho()
                  return 
  def kiemtra_kho(id, soluong): # khi tao hoa don hang hoa
      for hanghoa in ds_hang_tonkho:
          if id == hanghoa['id']:
              hanghoa['soluong'] = int(hanghoa['soluong'])
              if hanghoa['soluong'] < soluong:
                  print("[!] Khong du luu tru hang hoa trong kho")
                  return 1
              else:
                  hanghoa['soluong'] -= soluong
                  lop_kho.ghi_kho()
                  return
  def xuat_tonkho():
    for hanghoa in ds_hang_tonkho:
        print("[+] Ton kho {}: {}".format(hanghoa['ten'], hanghoa['soluong']))

