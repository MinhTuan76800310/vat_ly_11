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

### Giới hạn 4: Nguyên Tắc Sư Phạm Suy Luận Khám Phá (Deductive Discovery)
Khi dẫn xuất các công thức đạo hàm và động học:
1. **Khám phá dấu đạo hàm lượng giác qua 4 trạng thái**:
   - *Trạng thái 1 (Đỉnh đồi $t = 0$)*: Độ dốc bằng 0 ($x'(0) = 0$). Hàm ứng viên là $\sin(t)$ vì $\sin(0) = 0$. **Bắt buộc nhấn mạnh: vì $+\sin(0) = -\sin(0) = 0$, tại đỉnh đồi dấu của đạo hàm là CHƯA THỂ XÁC ĐỊNH!**
   - *Trạng thái 2 (Lao dốc qua VTCB $t = \pi/2$)*: Xe lao dốc xuống $\implies$ tiếp tuyến dốc âm ($-1$). Lúc này mới lật mở: $+\sin(\pi/2) = +1$ (loại), $-\sin(\pi/2) = -1$ (khớp). Từ đó chứng minh dấu trừ $[\cos(t)]' = -\sin(t)$.
   - *Trạng thái 3 & 4*: Dưới đáy vực (độ dốc 0) và vọt lên qua VTCB (độ dốc $+1$) để kiểm chứng.
2. **Cơ chế nhân tử $\omega$ (Cỗ máy nén thời gian)**:
   - Tần số tăng $\omega$ lần $\implies$ chu kì bị nén lại $1/\omega$.
   - Biên độ $A$ giữ nguyên mà thời gian giảm một nửa $\implies$ sườn dốc phải dựng đứng gấp đôi $\implies$ đạo hàm nhân thêm $\omega$: $[\cos(\omega t)]' = -\omega\sin(\omega t)$.
3. **Mô hình 3 Vệ tinh trên Vòng tròn Đơn vị (Đồng hồ vũ trụ)**:
   - Vệ tinh $\vec{u}_1$ (Li độ): Hai hình chiếu vuông góc lên trục $\cos$ và $\sin$ tạo thành tam giác vuông Pythagoras $\implies$ chứng minh trực quan $(x/A)^2 + (v/\omega A)^2 = 1$.
   - Vệ tinh $\vec{u}_2$ (Vận tốc): Bay trước $+90^\circ$ ($\pi/2$), chiếu lên trục $\cos$ cho $-\sin\alpha = \cos(\alpha + \pi/2) \implies$ vận tốc sớm pha $\pi/2$.
   - Vệ tinh $\vec{u}_3$ (Gia tốc): Bay đối diện $+180^\circ$ ($\pi$), chiếu lên trục $\cos$ cho $-\cos\alpha = \cos(\alpha + \pi) \implies$ gia tốc ngược pha $\pi$.

---

### Giới hạn 5: Quy Chuẩn Bản Dịch / Tài Liệu Tiếng Anh (IELTS Band 6.5 Standard)
Khi được yêu cầu viết hoặc chuyển ngữ sang tiếng Anh cho đối tượng học sinh THPT:
1. **Định chuẩn độ đọc (Lexical & Syntactic Level)**: Tương đương **IELTS Band 6.5**.
   - Dùng từ vựng học thuật tự nhiên, chính xác (*instantaneous rate of change, secant line, tangent line, steepness, crest, trough, time-compression, right-angled triangle, restoring force*).
   - Tuyệt đối không dùng từ ngữ quá hàn lâm bậc đại học hoặc văn phong khô cứng, máy móc.
2. **Cấu trúc câu & Cohesion**:
   - Sử dụng đa dạng câu ghép, câu phức và các liên từ chuyển ý tự nhiên (*Consequently, In contrast, Specifically, At first glance, As a result*).
   - Duy trì giọng văn kể chuyện (storytelling) sinh động, truyền cảm hứng và tôn trọng người đọc.

---

### Giới hạn 6: Quy Chuẩn Trực Quan Hóa & Tuyệt Đối Không Dùng Ký Tự Khung Vẽ ASCII (No-ASCII Invariant)

1. **Tuyệt đối KHÔNG sử dụng ký tự vẽ khung ASCII**:
   - ❌ **Cấm hoàn toàn**: Không dùng các ký tự Unicode/ASCII vẽ hộp (`┌`, `─`, `┐`, `│`, `├`, `┤`, `└`, `┘`, v.v.) bên trong mã nguồn Markdown (`book/*.md`) để tạo bảng so sánh hay hộp cứu nguy. Các khối này khi qua Pandoc và Typst sẽ bị biến thành code block thô ráp, làm tài liệu mất tính học thuật và thiếu thẩm mỹ.
   - ✅ **Bắt buộc dùng bảng Markdown chuẩn**: Mọi bảng so sánh dữ liệu, đối chiếu trạng thái phải viết bằng cú pháp Markdown tiêu chuẩn (`| Cột 1 | Cột 2 |`).
   - ✅ **Bắt buộc dùng Khối Cảnh Báo (Alert / Callout Block)**: Mọi hộp lưu ý, bẫy đề thi, mẹo nhớ phải dùng cú pháp blockquote (`> ⚠️ **CẢNH BÁO...**` hoặc `> [!WARNING]`) kèm công thức LaTeX hiển thị sắc nét.

2. **Yêu cầu về Mật độ & Chất lượng Hình ảnh Minh họa (Visual Richness)**:
   - **Không để bài dài "chay chữ"**: Tuyệt đối không để các phần lý thuyết mô hình hóa hoặc đối chiếu trạng thái kéo dài qua nhiều trang mà không có hình vẽ minh họa.
   - **Bắt buộc có hình vẽ cho 3 trụ cột**:
     * *Mô hình vật lý*: Luôn có hình con lắc lò xo / con lắc đơn ở các trạng thái dãn, nén, cân bằng và hướng véc-tơ lực $\vec{F}_{kv}$.
     * *Cấu trúc sóng*: Đồ thị $x(t)$ phải ghi chú rõ $A, -A, L=2A, T, T/2, T/4, x_0$, và các tiếp tuyến vận tốc tại các mốc then chốt.
     * *Đối chiếu tương đối*: Mọi so sánh pha (cùng pha, ngược pha, vuông pha) phải có đồ thị sóng thời gian song song kèm quỹ đạo không gian trạng thái (đoạn thẳng, elip).
   - **Định dạng & Phối màu**: Mọi hình ảnh phải được sinh tự động từ `scripts/generate_figures.py` ở cả 2 định dạng: **PNG 300 DPI** và **vector PDF**. Phối màu chuẩn mực: Navy `#1B365D`, Crimson `#A6192E`, Forest Green `#1E6B52`, Amber `#D97706`.

---

## 3. Checklist Tự Kiểm Định Độ Phù Hợp Lớp 11 (Audience-Fit Gate)

Trước khi xuất bản hoặc hoàn tất chương sách, tự đặt 5 câu hỏi:
1. *Một học sinh lớp 11 nắm chắc SGK có hiểu được bài viết này mà không cần tra cứu giáo trình đại học không?*
2. *Có công thức nào xuất hiện số phức, tích phân hay phương trình vi phân phức tạp không? (Nếu có $\rightarrow$ sửa ngay).*
3. *Hình vẽ và ví dụ có bám sát đời sống thực tế không?*
4. *Các ký hiệu có nhất quán với SGK GDPT 2018 không? (Dùng $x, v, a, W, W_đ, W_t, \omega, f, T$).*
5. *Tài liệu có sót ký tự vẽ khung ASCII nào không? Mỗi mục kiến thức then chốt đã có hình vẽ khoa học tương ứng minh họa chưa?*

