# Pedagogy Harness — Chuẩn Mực Sư Phạm Dành Cho Học Sinh Lớp 11 Việt Nam

Tài liệu này là "bộ lọc sư phạm" kiểm soát văn phong và mức độ tiếp thu khi biên soạn các chương sách Vật Lí 11 Chuyên Sâu.

---

## 1. Tôn Chỉ Cốt Lõi: Đơn Giản Hóa Bản Chất, Không Đánh Đố Học Sinh

> **Quy tắc vàng**: *"Một nhà vật lý giỏi là người có thể giải thích bản chất sâu xa nhất của vũ trụ cho một học sinh trung học phổ thông hiểu mà không cần núp bóng sau những phương trình phức tạp."*

Mục tiêu của sách không phải là "khoe kiến thức đại học", mà là:
1. Giúp học sinh lớp 11 **hiểu tận gốc**: Tại sao công thức SGK lại có dạng như vậy?
2. Dùng công cụ **Toán học lớp 11** (chủ đạo là Đạo hàm và Đồ thị) để chứng minh và liên kết các hiện tượng.
3. Liên hệ với các vật thể thực tế đời sống mà học sinh có thể sờ, thấy hoặc cảm nhận được (xe cộ, đàn guitar, xích đu, điện thoại thông minh).

---

## 2. Các Giới Hạn Sư Phạm Bắt Buộc

### Giới hạn 1: Bộ Công Cụ Toán Học Chuẩn Lớp 11
* **Được dùng tự nhiên**:
  - Đạo hàm: Định nghĩa $v(t) = x'(t)$ là tốc độ biến thiên của li độ; $a(t) = v'(t)$ là tốc độ biến thiên của vận tốc.
  - Công thức đạo hàm: $(\cos u)' = -u'\sin u$, $(\sin u)' = u'\cos u$.
  - Công thức lượng giác lớp 10-11: $\cos(x + \pi/2) = -\sin x$, $\cos(x + \pi) = -\cos x$, $\sin^2 x + \cos^2 x = 1$.
  - Đồ thị: Đồ thị hàm số bậc hai parabol, tiếp tuyến, diện tích dưới đồ thị đơn giản.
* **Cấm đưa vào phần chính văn**:
  - Không giải phương trình vi phân bằng phương trình đặc trưng nghiệm phức $r^2 + \omega^2 = 0 \implies r = \pm i\omega$. (Chỉ cần kiểm chứng: "Lấy đạo hàm bậc hai của $x(t) = A\cos(\omega t + \varphi)$ ta thu được ngay $x''(t) = -\omega^2 x(t)$").
  - Không dùng số phức Euler $e^{i\theta}$.
  - Không dùng công thức Taylor dạng chuỗi vô hạn với ký hiệu $\mathcal{O}(x^3)$. Thay vào đó, dùng hình ảnh trực quan: *"Xét một đoạn rất ngắn quanh đáy cân bằng, bất kỳ đường cong trơn nào cũng uốn cong như một parabol thế năng $W_t = \frac{1}{2}kx^2$"*.

### Giới hạn 2: Xóa Bỏ Thuật Ngữ Hàn Lâm Bậc Đại Học
* ❌ Cấm dùng: "Định lý Liouville", "Định lý Virial", "Điểm hút xoắn ốc (Spiral Attractor)", "Tích phân Elliptic", "Thế Morse".
* ✅ Dùng cách diễn đạt thuần túy vật lý lớp 11:
  - Thay vì "Định lý Liouville", hãy nói: *"Hệ thức độc lập thời gian giữa vị trí và vận tốc: $(x/A)^2 + (v/v_{\max})^2 = 1$ cho thấy quỹ đạo của trạng thái là một hình elip khép kín"*.
  - Thay vì "Định lý Virial", hãy nói: *"Trong một chu kỳ, cơ năng liên tục đổi chỗ giữa động năng và thế năng, và giá trị trung bình của động năng đúng bằng giá trị trung bình của thế năng: $\bar{W}_d = \bar{W}_t = \frac{1}{2}W$"*.
  - Thay vì "Thế Morse và khối lượng rút gọn", hãy dùng: *"Con lắc lò xo treo thẳng đứng, dao động của nhánh âm thoa kim loại, hay pít-tông động cơ ô tô"*.

### Giới hạn 3: Cấu Trúc Mỗi Module
Mỗi module bài học dài vừa vặn khoảng 1 giờ học (tương đương 4-6 trang in):
1. **Hiện tượng & Mâu thuẫn trực giác**: Bắt đầu bằng câu hỏi đời sống.
2. **Mô hình hóa trực quan**: Hình vẽ minh họa sắc nét, ẩn dụ gần gũi.
3. **Toán học khai sáng**: Dẫn xuất từng bước bằng đạo hàm và lượng giác (không nhảy bước, chú thích rõ đơn vị SI).
4. **Bản chất năng lượng & Thực tế**: Cơ năng, sự tiêu tán năng lượng, ứng dụng thực tế.
5. **Ví dụ tính số & Cảnh báo lỗi thi**: Bài toán số liệu thực tế, chỉ ra bẫy đề thi trắc nghiệm/tự luận hay gặp.

---

## 3. Checklist Tự Kiểm Định Độ Phù Hợp Lớp 11 (Audience-Fit Gate)

Trước khi xuất bản hoặc hoàn tất chương sách, tự đặt 4 câu hỏi:
1. *Một học sinh lớp 11 nắm chắc SGK có hiểu được bài viết này mà không cần tra cứu giáo trình đại học không?*
2. *Có công thức nào xuất hiện số phức, tích phân hay phương trình vi phân phức tạp không? (Nếu có $\rightarrow$ sửa ngay).*
3. *Hình vẽ và ví dụ có bám sát đời sống thực tế không?*
4. *Các ký hiệu có nhất quán với SGK GDPT 2018 không? (Dùng $x, v, a, W, W_d, W_t, \omega, f, T$).*
