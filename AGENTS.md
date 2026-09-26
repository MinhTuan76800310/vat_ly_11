# Agents Guide — vatly_11 (Vật Lí 11 Chuyên Sâu)

Tài liệu hướng dẫn quy chuẩn biên soạn và nghiên cứu khoa học cho bộ sách: **"Vật Lí 11 Chuyên Sâu: Bản Chất Vật Lí & Nền Tảng Toán Học"**.

---

## 1. Tôn Chỉ Sư Phạm & Đối Tượng Độc Giả

### Đối tượng độc giả mục tiêu & Bộ sách quy chiếu
* **Chuẩn quy chiếu trực tiếp**: **SGK Vật lí 11 — Bộ sách "Kết nối tri thức với cuộc sống"** (NXB Giáo dục Việt Nam - Chương trình GDPT 2018).
* **Độc giả**: Học sinh lớp 11 tại Việt Nam, học sinh chuyên Vật lý, học sinh khá giỏi muốn hiểu cặn kẽ bản chất vật lý đằng sau các bài học trong SGK Kết nối tri thức mà không sa vào học vẹt hay mẹo giải số học.

### Chuẩn hóa Ký hiệu & Thuật ngữ theo SGK Kết Nối Tri Thức
* **Động năng**: Bắt buộc dùng ký hiệu **$W_đ$** (không dùng $E_đ$, không dùng $W_d$).
* **Thế năng**: Bắt buộc dùng ký hiệu **$W_t$** (không dùng $E_t$).
* **Cơ năng**: Bắt buộc dùng ký hiệu **$W$** (không dùng $E$).
* **Các đại lượng động học**: Li độ $x$, biên độ $A$, chu kì $T$, tần số $f$, tần số góc $\omega$, pha ban đầu $\varphi$, pha dao động $(\omega t + \varphi)$, độ lệch pha $\Delta \varphi$.
* **Độ lệch pha**: $\Delta \varphi = \varphi_2 - \varphi_1$ (cùng pha khi $\Delta \varphi = 2k\pi$, ngược pha khi $\Delta \varphi = (2k+1)\pi$, vuông pha khi $\Delta \varphi = (2k+1)\pi/2$).
* **Vận tốc & Gia tốc cực đại**: $v_{\max} = \omega A$, $a_{\max} = \omega^2 A$.

### Giới hạn Công cụ Toán học (Toán 11 GDPT 2018)
1. **Được phép dùng làm trọng tâm khai phóng**:
   - **Đạo hàm (Toán 11)**: Khái niệm đạo hàm là tốc độ biến thiên tức thời, hệ số góc tiếp tuyến đồ thị; đạo hàm lượng giác $(\cos \omega t)' = -\omega \sin \omega t$, $(\sin \omega t)' = \omega \cos \omega t$.
   - **Lượng giác lớp 10 & 11**: Giá trị lượng giác, cung hơn kém $\pi/2, \pi$, đồ thị hàm sin/cos, hệ thức độc lập thời gian $(x/A)^2 + (v/\omega A)^2 = 1$.
   - **Đồ thị Parabol**: Dạng đồ thị bậc hai của thế năng $W_t = \frac{1}{2}kx^2$, trực quan hóa vùng dao động nhỏ quanh đáy cân bằng bền.
2. **Tuyệt đối KHÔNG đưa vào phần nội dung bắt buộc**:
   - ❌ Phương trình vi phân cấp hai với nghiệm phức ($r^2 + \omega_0^2 = 0 \implies r = \pm i\omega$).
   - ❌ Số phức dạng mũ Euler ($e^{i\theta} = \cos\theta + i\sin\theta$).
   - ❌ Chuỗi vô hạn Taylor toán cao cấp với ký hiệu $\mathcal{O}(x^3)$.
   - ❌ Thuật ngữ cơ học đại học: Định lý Liouville, Định lý Virial, Điểm hút xoắn ốc (Spiral Attractor), Tích phân Elliptic, Thế Morse, Khối lượng rút gọn.

---

## 2. Quy Định Ngôn Ngữ & Mạch Bài Học

- **Nội dung sách (`book/`)**: Viết hoàn toàn bằng **tiếng Việt chuẩn mực, mạch lạc, trong sáng**.
- **Cấu trúc đối chiếu chặt chẽ với SGK Kết nối tri thức Chương 1**:
  - *Chủ đề 1*: Tương ứng Bài 1, 2, 3, 4 KNTT (Dao động điều hòa, Mô tả dao động, Vận tốc - Gia tốc, Bài tập đồ thị và độ lệch pha).
  - *Chủ đề 2*: Tương ứng Bài 1, 5, 7 KNTT (Động lực học con lắc lò xo, con lắc đơn, Động năng, Thế năng và Sự chuyển hóa năng lượng).
  - *Chủ đề 3*: Tương ứng Bài 6 KNTT (Dao động tắt dần, Dao động duy trì, Dao động cưỡng bức, Hiện tượng cộng hưởng).
- **Mã nguồn, Scripts, Configs**: Viết bằng tiếng Anh kèm chú thích chi tiết.
- **Git Commit Messages**: Tiếng Anh theo chuẩn Conventional Commits (`feat:`, `fix:`, `docs:`, `refactor:`, `chore:`).

---

## 3. Khung 5 Tầng Sư Phạm Dành Cho Học Sinh Lớp 11

```
┌─────────────────────────────────────────────────────────────┐
│  TẦNG 1: HIỆN TƯỢNG ĐỜI SỐNG & CÂU HỎI KHỞI ĐỘNG (SGK KNTT) │
│  - Màng loa rung, xích đu, cành cây, phuộc xe máy           │
│  - Nghịch lý trực giác: Tại sao không quay tròn mà lại có cos?│
├─────────────────────────────────────────────────────────────┤
│  TẦNG 2: MÔ HÌNH HÓA VẬT LÝ VỪA SỨC                         │
│  - Con lắc lò xo, con lắc đơn, vị trí cân bằng bền          │
│  - Lực kéo về xuất hiện khi vật rời khỏi vị trí cân bằng bền │
├─────────────────────────────────────────────────────────────┤
│  TẦNG 3: TOÁN HỌC KHAI PHÓNG (ĐẠO HÀM & ĐỒ THỊ KNTT)        │
│  - Vận tốc là đạo hàm của li độ: v(t) = x'(t)               │
│  - Gia tốc là đạo hàm của vận tốc: a(t) = v'(t) = -omega^2 x │
│  - Độ lệch pha delta phi và hệ thức độc lập thời gian        │
├─────────────────────────────────────────────────────────────┤
│  TẦNG 4: NĂNG LƯỢNG (W_đ, W_t, W) & CƠ CHẾ THỰC TẾ          │
│  - Động năng W_đ và Thế năng W_t chuyển hóa qua lại (T' = T/2)│
│  - Ma sát làm cơ năng chuyển hóa thành nhiệt (tắt dần)      │
│  - Hiện tượng cộng hưởng khi tần số ngoại lực khớp tần số riêng│
├─────────────────────────────────────────────────────────────┤
│  TẦNG 5: VÍ DỤ TÍNH SỐ THỰC TẾ & BÀI TẬP SGK KNTT           │
│  - Bài tập số liệu thực tế (xe máy, đồng hồ, màng loa)       │
│  - Cảnh báo các lỗi hiểu sai trong đề kiểm tra và thi cử     │
└─────────────────────────────────────────────────────────────┘
```

---

## 4. Pipeline Biên Dịch (Build Pipeline)

```bash
# 1. Tạo hình vẽ vector PDF và PNG chuẩn KNTT
python scripts/generate_figures.py

# 2. Biên dịch sách qua Pandoc và Typst
python scripts/build_book.py
```

---

## 5. Chế Độ Thực Thi Tự Trị (Autonomous Execution / YOLO Mode)

- Chế độ tự trị được kích hoạt: Agent chủ động thao tác file, cập nhật bản thảo, render đồ thị và biên dịch sách mà không làm gián đoạn người dùng bằng các câu hỏi xác nhận lặp lại không cần thiết.
- Sau mỗi lần chỉnh sửa nội dung hoặc script, luôn chạy kiểm thử tạo hình và biên dịch PDF để đảm bảo không có lỗi trước khi báo cáo.
