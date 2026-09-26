# Agents Guide — vatly_11 (Vật Lí 11 Chuyên Sâu)

Tài liệu hướng dẫn quy chuẩn biên soạn và nghiên cứu khoa học cho bộ sách: **"Vật Lí 11 Chuyên Sâu: Bản Chất Vật Lí & Nền Tảng Toán Học"**.

---

## 1. Tôn Chỉ Sư Phạm & Đối Tượng Độc Giả

### Đối tượng độc giả mục tiêu
* **Học sinh lớp 11 tại Việt Nam** (theo Khung Chương trình Giáo dục Phổ thông 2018 - bộ sách Kết nối tri thức, Chân trời sáng tạo, Cánh Diều).
* Học sinh các lớp chuyên Vật lý, học sinh khá giỏi muốn hiểu cặn kẽ **bản chất vật lý** đằng sau các công thức mà không sa vào học vẹt hay mẹo giải số học.

### Giới hạn Công cụ Toán học (Mathematical Boundaries)
Sách đưa toán học trở lại vị trí ngôn ngữ tự nhiên của Vật lý, nhưng **phải tuyệt đối bám sát nền tảng Toán học của học sinh lớp 11 Việt Nam**:
1. **Toán học được phép sử dụng làm trọng tâm**:
   - **Đạo hàm cơ bản (Toán 11)**: Khái niệm đạo hàm như tốc độ biến thiên tức thời, hệ số góc tiếp tuyến đồ thị; đạo hàm hàm số lượng giác $(\sin \omega t)' = \omega \cos \omega t$, $(\cos \omega t)' = -\omega \sin \omega t$.
   - **Lượng giác lớp 10 & 11**: Giá trị lượng giác, cung liên kết (hơn kém $\pi/2$, bù, đối), đồ thị hàm số sin/cos, đường tròn lượng giác.
   - **Hình học & Đại số**: Đồ thị tọa độ, phương trình parabol đỉnh $(x_0, 0)$ của thế năng, phương trình elip/đường tròn của hệ thức độc lập thời gian $(x/A)^2 + (v/\omega A)^2 = 1$.
   - **Định luật bảo toàn cơ bản**: Bảo toàn năng lượng, định luật II Newton $\Sigma \vec{F} = m\vec{a}$.
2. **Tuyệt đối KHÔNG đưa vào phần nội dung bắt buộc**:
   - ❌ Phương trình vi phân cấp hai giải bằng đa thức đặc trưng nghiệm phức ($r^2 + \omega_0^2 = 0 \implies r = \pm i\omega$).
   - ❌ Số phức dạng mũ Euler ($e^{i\theta} = \cos\theta + i\sin\theta$) dùng để giải cơ học cổ điển.
   - ❌ Khai triển chuỗi Taylor hình thức toán cao cấp với ký hiệu đạo hàm bậc $n$ và phần dư Peano $\mathcal{O}(x^3)$. (Thay bằng trực quan: gần đáy cân bằng, mọi đường cong trơn đều xấp xỉ parabol).
   - ❌ Thuật ngữ cơ học đại học: Định lý Liouville, Định lý Virial, Điểm hút xoắn ốc (Spiral Attractor), Tích phân Elliptic, Thế Morse, Khối lượng rút gọn... (Nếu cần mở rộng cho học sinh chuyên, chỉ đặt trong mục "Góc mở rộng / Em có biết?" mang tính giới thiệu trực giác định tính).

---

## 2. Quy Định Ngôn Ngữ & Văn Phong

- **Nội dung sách (`book/`)**: Viết hoàn toàn bằng **tiếng Việt trong sáng, dễ hiểu, lôi cuốn**. Thuật ngữ tiếng Anh chỉ chú thích trong ngoặc đơn ở lần xuất hiện đầu để giúp học sinh tra cứu tài liệu quốc tế (ví dụ: *lực kéo về (restoring force)*, *dao động tắt dần (damped oscillation)*).
- **Mã nguồn, Scripts, Configs**: Viết bằng tiếng Anh kèm chú thích chi tiết.
- **Git Commit Messages**: Tiếng Anh theo chuẩn Conventional Commits (`feat:`, `fix:`, `docs:`, `refactor:`, `chore:`).

---

## 3. Khung 5 Tầng Sư Phạm Dành Cho Học Sinh Lớp 11

Mọi bài học phải được xây dựng đồng bộ theo 5 tầng nhận thức, đảm bảo vừa sâu sắc vừa vừa sức:

```
┌─────────────────────────────────────────────────────────────┐
│  TẦNG 1: HIỆN TƯỢNG ĐỜI SỐNG & CÂU HỎI KHỞI PHÁT            │
│  - Quan sát thực tế: giảm xóc xe máy, xích đu, cành cây đu đưa│
│  - Nghịch lý trực giác: Tại sao không quay tròn mà lại có cos?│
├─────────────────────────────────────────────────────────────┤
│  TẦNG 2: MÔ HÌNH HÓA VẬT LÝ VỪA SỨC                         │
│  - Con lắc lò xo, con lắc đơn, chất điểm dao động          │
│  - Lực kéo về xuất hiện khi vật rời khỏi vị trí cân bằng bền │
├─────────────────────────────────────────────────────────────┤
│  TẦNG 3: TOÁN HỌC KHAI PHÓNG (ĐẠO HÀM & ĐỒ THỊ)             │
│  - Vận tốc là đạo hàm của li độ: v(t) = x'(t)               │
│  - Gia tốc là đạo hàm của vận tốc: a(t) = v'(t) = -omega^2 x │
│  - Hệ thức độc lập: (x/A)^2 + (v/v_max)^2 = 1              │
├─────────────────────────────────────────────────────────────┤
│  TẦNG 4: NĂNG LƯỢNG, BẢN CHẤT & CƠ CHẾ THỰC TẾ              │
│  - Cơ năng: Động năng chuyển hoá qua lại với thế năng       │
│  - Ma sát làm cơ năng chuyển hóa thành nhiệt (tắt dần)      │
│  - Hiện tượng cộng hưởng khi tần số ngoại lực khớp tần số riêng│
├─────────────────────────────────────────────────────────────┤
│  TẦNG 5: VÍ DỤ TÍNH SỐ THỰC TẾ & ỨNG DỤNG ĐỜI SỐNG          │
│  - Bài tập số liệu thực tế (xe máy, đồng hồ, cảm biến điện thoại)│
│  - Cảnh báo các lỗi hiểu sai thường gặp trong các kỳ thi     │
└─────────────────────────────────────────────────────────────┘
```

---

## 4. Tiêu Chuẩn Hình Vẽ & Đồ Thị

- Sử dụng Matplotlib tạo đồ thị chất lượng cao qua `scripts/generate_figures.py`.
- **Nhãn trục và chú thích**: Tiếng Việt rõ ràng, cỡ chữ dễ đọc, màu sắc tương phản cao (Navy `#1B365D`, Đỏ thẫm `#A6192E`, Xanh lá `#1E6B52`, Cam `#D97706`).
- Tránh các thuật ngữ hàn lâm đại học trên hình; ưu tiên dẫn dắt mắt đọc trực quan.

---

## 5. Pipeline Xây Dựng Bản Phân Phối (Build Pipeline)

```bash
# 1. Tạo hình vẽ vector PDF và PNG
python scripts/generate_figures.py

# 2. Biên dịch sách qua Pandoc và Typst
python scripts/build_book.py
```

---

## 6. Chế Độ Thực Thi Tự Trị (Autonomous Execution / YOLO Mode)

- Chế độ tự trị được kích hoạt: Agent chủ động thao tác file, cập nhật bản thảo, render đồ thị và biên dịch sách mà không làm gián đoạn người dùng bằng các câu hỏi xác nhận lặp lại không cần thiết.
- Sau mỗi lần chỉnh sửa nội dung hoặc script, luôn chạy kiểm thử tạo hình và biên dịch PDF để đảm bảo không có lỗi trước khi báo cáo.
