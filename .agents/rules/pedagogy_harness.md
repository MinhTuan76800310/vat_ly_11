# Pedagogy Harness — Tiêu Chuẩn Sư Phạm Sách Vật Lí 11 Chuyên Sâu

Harness này quy định tầng **văn phong và phương pháp sư phạm** khi chấp bút các chương sách trong `book/`. Sách hướng đến học sinh chuyên Vật lý, sinh viên đại học năm nhất và người yêu thích khoa học muốn hiểu bản chất sâu sắc của tự nhiên.

---

## 1. Tôn Chỉ Sư Phạm

* **Bản chất trước, Công thức sau**: Không bao giờ đưa ra một công thức mà không xuất phát từ câu hỏi trực giác hoặc mô hình vật lý cụ thể.
* **Toán học Giải tích là ngôn ngữ tự nhiên**: Sử dụng đạo hàm, tích phân, phương trình vi phân và số phức như công cụ tự nhiên để mô tả sự biến thiên của đại lượng, xóa bỏ hoàn toàn lối "học vẹt công thức".
* **Soi chiếu cơ chế vi mô**: Luôn liên hệ định luật vĩ mô với hành vi của các hạt (nguyên tử, electron, va chạm tán xạ, thế liên kết Lennard-Jones,...).

---

## 2. Quy Tắc Chấp Bút Chi Tiết

### RULE 1 — Đồng bộ 5 tầng cấu trúc bài giảng
Mỗi chuyên đề hoặc bài học lớn phải đi trọn vẹn qua 5 tầng:
1. **Tầng 1 (Trực giác & Nghịch lý)**: Nêu hiện tượng thực tế gây tò mò, chỉ ra điểm nghẽn của cách hiểu trực giác thông thường.
2. **Tầng 2 (Mô hình hóa)**: Xác lập hệ quy chiếu, bỏ qua các yếu tố nhiễu bậc cao, đưa về bài toán cơ học/điện động lực học cơ bản.
3. **Tầng 3 (Giải tích toán học)**: Thiết lập phương trình vi phân bằng định luật Newton / định luật bảo toàn. Giải tường minh phương trình.
4. **Tầng 4 (Cơ chế năng lượng & vi mô)**: Khảo sát quá trình chuyển hóa động năng - thế năng, tiêu tán năng lượng, giải thích dưới góc nhìn vi mô.
5. **Tầng 5 (Thí nghiệm tư duy & Phản biện)**: Thử nghiệm các giới hạn biên, phân tích thứ nguyên, đối chiếu với công thức SGK đại trà (chỉ ra SGK xấp xỉ điều kiện nào).

### RULE 2 — Minh bạch biến số và chuẩn hóa ký hiệu Toán học
* Mọi đại lượng vật lý ($A, \omega, \varphi, k, m, \gamma, Q, \dots$) đều phải được gọi tên bản chất và gắn đơn vị chuẩn SI khi xuất hiện lần đầu.
* Sử dụng chuẩn KaTeX / Typst rõ ràng:
  - Đạo hàm theo thời gian: $\dot{x} = \frac{dx}{dt}$, $\ddot{x} = \frac{d^2x}{dt^2}$.
  - Giá trị trung bình: $\langle E \rangle$ hoặc $\bar{E}$.
  - Vectơ: $\vec{F}, \vec{v}, \vec{E}$.

### RULE 3 — Tích hợp Đồ thị & Không gian Pha (Phase Space)
* Với mọi chuyển động dao động, không chỉ vẽ đồ thị li độ theo thời gian $x(t)$, mà **bắt buộc** phải khảo sát quỹ đạo trong không gian pha $(x, v/\omega)$.
* Với bài toán thế năng, luôn gắn liền với đồ thị giếng thế $V(x)$ và phép khai triển Taylor bậc 2 quanh vị trí cân bằng bền.

### RULE 4 — Văn phong và Giọng điệu (Tone of Voice)
* Khách quan, sắc sảo, truyền cảm hứng khám phá bản chất tự nhiên.
* Không dùng văn phong đao to búa lớn hoặc liệt kê khô khan; dẫn dắt người đọc như một nhà vật lý thực thụ đang đồng hành khám phá.

---

## 3. Checklist Tự Kiểm Định Trước Khi Hoàn Tất Bản Thảo

Trước khi chốt nội dung hoặc biên dịch PDF, hãy trả lời 5 câu hỏi:
1. *Bài viết đã có đủ 5 tầng sư phạm chưa, hay đang nhảy cóc thẳng vào công thức?*
2. *Mọi công thức đã được dẫn xuất giải tích tường minh từ định luật gốc chưa?*
3. *Đã phân tích thứ nguyên và kiểm tra các trường hợp giới hạn cực trị chưa?*
4. *Các hình vẽ minh họa tương ứng trong `book/figures/` đã được tạo và render sắc nét chưa?*
5. *Lệnh `python scripts/build_book.py` có biên dịch ra PDF hoàn chỉnh không có lỗi Typst/Pandoc nào không?*
