import os,json

danhsachkhachhang = []
quanly_ds_khachhang = []

def load_khachhang():
    for file_hoadon in os.listdir("../hoadon/"):
        with open("../hoadon/" + file_hoadon, "r") as f:
            data = json.load(f)
            if data['nguoimua'] not in danhsachkhachhang:
                danhsachkhachhang.append(data['nguoimua'])
                data_khachhang = {}
                data_khachhang['ten'] = data['nguoimua']
                data_khachhang['solan_gapmat'] = 1
                data_khachhang['sotien_damua'] = data['tongtien']
                data_khachhang['hanghoa_damua'] = []
                for hanghoa in data['danhsachhanghoa']:
                    data_hanghoa_damua = {}
                    data_hanghoa_damua[hanghoa['ten']] = hanghoa['soluong']
                    data_khachhang['hanghoa_damua'].append(data_hanghoa_damua)
                quanly_ds_khachhang.append(data_khachhang)
            else:
                for khachhang in quanly_ds_khachhang:
                    khachhang['solan_gapmat'] += 1
                    khachhang['sotien_damua'] += data['tongtien']
                    for hanghoa1 in data['danhsachhanghoa']:
                        for hanghoa_mua in khachhang['hanghoa_damua']:
                            ten_hh = hanghoa1['ten']
                            if ten_hh in hanghoa_mua:
                                hanghoa_mua[ten_hh] += hanghoa1['soluong']
                            else:
                                hanghoa_mua[ten_hh] = hanghoa1['soluong']                           
load_khachhang()
def xem_dskhachhang():
    print("+++++++++ DANH SACH KHACH HANG ++++++++")
    for khachhang in range(len(danhsachkhachhang)):
        print("[+] Khach hang {}: {}".format(khachhang+1, danhsachkhachhang[khachhang]))
def xem_thongtin_KH():
    count = 0
    nhap = input("Moi ban nhap ten khach hang can xem: ")
    print("+++++++++++ THONG TIN KHACH HANG ++++++++++++")
    for khachhang in quanly_ds_khachhang:
        if khachhang['ten'] == nhap:
            print("[+] Ten khach hang: ", khachhang['ten'])
            print("[+] So lan mua hang: ", khachhang['solan_gapmat'])
            print("[+] So tien da mua: ", khachhang['sotien_damua'])
            print("[+] Danh sach hang hoa da mua: ", end='')
            for hanghoa in khachhang['hanghoa_damua']:
                for data in hanghoa:
                    if count > 0:
                        print(32*" " + data + ": " + str(hanghoa[data]))
                    else:
                        print(" " + data + ": " + str(hanghoa[data]))
                        count += 1
# print(quanly_ds_khachhang)
def khachhang_thanmat():
    count = 1
    for khachhang in quanly_ds_khachhang:
        if khachhang['solan_gapmat'] > 1 and khachhang['sotien_damua'] > 100000:
            print("[+] Khach hang than mat thu {}: {}".format(count, khachhang['ten']))
            count += 1
# khachhang_thanmat()