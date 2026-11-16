import random
def danh_gia_mat_khau(mk: str) -> tuple:
  do_dai_thuc = min(len(mk), 12)
  diem_do_dai = (do_dai_thuc / 12) * 50
  co_thuong = any(c.islower() for c in mk)
  co_hoa = any(c.isupper() for c in mk)
  co_so = any(c.isdigit() for c in mk)
  co_dac_biet = any(not c.isalnum() for c in mk)
  so_nhom = sum((co_thuong, co_hoa, co_so, co_dac_biet))
  diem_nhom = 12.5 * so_nhom
  tong_diem = diem_do_dai + diem_nhom
  diem_hien_thi = round(tong_diem)
  if tong_diem < 50:
    nhan = "YẾU"
  elif tong_diem < 80:
    nhan = "TRUNG BÌNH"
  else:
    nhan = "RẤT MẠNH"
  so_o_day = round(diem_hien_thi / 10)
  so_o_day = max(0, min(10, so_o_day))
  thanh_do = "█" * so_o_day + "░" * (10 - so_o_day)
  return thanh_do, diem_hien_thi, nhan
print("========================================")
print("   TRÌNH TẠO MẬT KHẨU NGẪU NHIÊN")
print("========================================")
TOI_THIEU = 6
TOI_DA = 15
while True:
  try:
    dodai = int(input("Nhập độ dài mật khẩu (min = 6, max = 15): "))
    if dodai < TOI_THIEU:
      print(f"Độ dài quá ngắn! Mật khẩu phải có tối thiểu {TOI_THIEU} ký tự. Vui"" lòng nhập lại.")
    elif dodai > TOI_DA:
      print(f"Độ dài quá dài! Mật khẩu chỉ được tối đa {TOI_DA} ký tự. Vui lòng"" nhập lại.")
    else:
      break
  except ValueError:
    print("Lỗi: Vui lòng chỉ nhập số nguyên!")
chonhoa = input("Bao gồm chữ HOA? (y/n): ").strip().lower()
chonso = input("Bao gồm chữ SỐ? (y/n): ").strip().lower()
chondacbiet = input("Bao gồm KÝ TỰ ĐẶC BIỆT? (y/n): ").strip().lower()
while True:
  try:
    soluong = int(input("Số lượng mật khẩu muốn tạo: "))
    if soluong < 1:
      print("Số lượng phải từ 1 trở lên! Vui lòng nhập lại.")
    else:
      break
  except ValueError:
    print("Lỗi: Vui lòng chỉ nhập số nguyên!")
chuthuong = "abcdefghijklmnopqrstuvwxyz"
chuhoa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chuso = "0123456789"
dacbiet = "!@#$%^&*()_+"
ds_matkhau = []
for _ in range(soluong):
  kho = chuthuong
  matkhau = [random.choice(chuthuong)]

  if chonhoa == "y":
    kho += chuhoa
    matkhau.append(random.choice(chuhoa))

  if chonso == "y":
    kho += chuso
    matkhau.append(random.choice(chuso))

  if chondacbiet == "y":
    kho += dacbiet
    matkhau.append(random.choice(dacbiet))

  so_con_lai = dodai - len(matkhau)
  for i in range(so_con_lai):
    matkhau.append(random.choice(kho))

  random.shuffle(matkhau)
  matkhau = "".join(matkhau)
  ds_matkhau.append(matkhau)

for stt, mk in enumerate(ds_matkhau, 1):
  thanh, diem, nhan = danh_gia_mat_khau(mk)
  print(f"[{stt}] {mk}")
  print(f"    Đánh giá độ mạnh: [{thanh}] {diem}% - {nhan}")
luu_file = (input("Bạn có muốn xuất ra file passwords.txt không (y/n)? ").strip().lower())
if luu_file == "y":
  with open("passwords.txt", "w", encoding="utf-8") as f:
    for mk in ds_matkhau:
      f.write(mk + "\n")
  print(f"✔ Đã lưu thành công {len(ds_matkhau)} mật khẩu vào file passwords.txt!")
