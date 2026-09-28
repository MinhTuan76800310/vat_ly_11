# Pedagogy Harness — Chuẩn Mực Sư Phạm Dành Cho Học Sinh Lớp 11 Việt Nam

Tài liệu này là "bộ lọc sư phạm" và cẩm nang phương pháp luận kiểm soát văn phong, tư duy dẫn dắt và mức độ tiếp thu khi biên soạn các chương sách Vật Lí 11 Chuyên Sâu.

---

### 1. Hệ Thống 5 Rules Biên Soạn Sư Phạm Chuẩn Hóa (Storytelling & Inductive Discovery)

Mọi bài học, mục giải thích lý thuyết hay tài liệu chuyên đề bắt buộc phải tuân thủ nghiêm ngặt 5 quy tắc chuẩn hóa theo cấu trúc 3 phần: **(1) Định nghĩa Quy tắc & Điều Cấm/Bắt buộc**, **(2) Ngữ cảnh áp dụng**, và **(3) Ví dụ đối chiếu & Ánh xạ**.

---

### Rule 1: Khám Phá Quy Luật Tự Nhiên (Inductive Discovery Invariant)

#### 1. Định nghĩa Quy tắc (The Core Invariant)
* Tuyệt đối **KHÔNG BAO GIỜ** áp đặt công thức, định lý hay dấu của kết quả trước rồi mới đi chứng minh hay kiểm tra lại.
* ❌ **CẤM (Anti-Pattern)**: Viết công thức trước ở đầu mục $\to$ vẽ đồ thị/làm thí nghiệm kiểm chứng $\to$ kết luận.
* ✅ **BẮT BUỘC (Required Invariant)**: Luôn đi theo chuỗi 5 bước: Khởi đầu từ công cụ đã biết ở bài trước $\to$ Nhập vai trải nghiệm $\to$ **Tạo nút thắt nhận thức (Mystery: Tại điểm mấu chốt, chưa đủ dữ kiện để biết kết quả!)** $\to$ **Thời khắc lật mở chân lý (Revelation: Sang trạng thái mới, loại trừ khả năng sai để tìm ra quy luật tất yếu)** $\to$ Kiểm chứng củng cố ở các trạng thái còn lại.

#### 2. Ngữ cảnh áp dụng (Context & Trigger Conditions)
* **Thời điểm kích hoạt**: Khi bắt đầu dẫn xuất bất kỳ công thức toán học, định luật vật lý hay quy luật định lượng mới nào trong bài.
* **Phạm vi áp dụng**: Mọi bài học trong Vật Lí 11 (Đạo hàm dao động, Phương trình sóng, Định luật Coulomb, Cường độ điện trường, Định luật khúc xạ...).

#### 3. Ví dụ đối chiếu (Anti-pattern vs. Good pattern)
* ❌ **Ví dụ sai (Áp đặt trước)**: *"Đạo hàm của hàm cosin là $[\cos(t)]' = -\sin(t)$. Bây giờ ta hãy vẽ đồ thị tiếp tuyến để kiểm tra công thức này."*
* ✅ **Ví dụ chuẩn (Chương 1: Dao động điều hòa)**:
  - *Bước 1*: Đã biết vận tốc là độ dốc tiếp tuyến $v(t) = x'(t)$ (Mục 1). Giờ tìm vận tốc của $x(t) = \cos(t)$ khi chưa biết đạo hàm lượng giác.
  - *Bước 2*: Đóng vai người đi tàu lượn siêu tốc trên ray $\cos(t)$ đo độ dốc.
  - *Bước 3 (Nút thắt)*: Tại đỉnh đồi ($t=0$), tiếp tuyến nằm ngang $\implies$ độ dốc bằng $0$. Hàm triệt tiêu tại 0 là $\sin(t)$. **Nhưng vì $(+\sin 0) = (-\sin 0) = 0$, tại đỉnh ta CHƯA THỂ BIẾT dấu của đạo hàm là cộng hay trừ!**
  - *Bước 4 (Lật mở)*: Sang trạng thái 2 (lao dốc qua VTCB tại $t = \pi/2$), mũi xe chúi xuống $\implies$ độ dốc tiếp tuyến chắc chắn ÂM ($-1$). Thử hai khả năng: $+\sin(\pi/2) = +1$ (Dương $\implies$ loại); $-\sin(\pi/2) = -1$ (Âm $\implies$ khớp). Dấu trừ lộ diện: $[\cos(t)]' = -\sin(t)$!
  - *Bước 5*: Kiểm chứng tiếp tại đáy vực (dốc 0) và vọt lên qua VTCB (dốc $+1$).
* 💡 **Ánh xạ sang chương khác (Chương 2: Sóng cơ — Định nghĩa & Công thức Bước sóng $\lambda = v/f$)**:
  - ❌ *Không viết*: "Bước sóng là khoảng cách sóng truyền trong 1 chu kì $\lambda = v.T = v/f$, giờ ta xét sóng trên mặt nước...".
  - ✅ *Dẫn dắt theo Rule*: Quan sát người ném đá xuống hồ, gợn sóng tròn lan ra xa $\to$ Thả chiếc phao câu đứng yên một chỗ, phao chỉ nhấp nhô lên xuống tại chỗ với chu kì $T$ $\to$ Đặt câu hỏi tò mò: *Trong đúng 1 nhịp phao lặn xuống rồi ngoi lên trở lại trạng thái cũ, gợn sóng thứ nhất đã kịp bò đi được một quãng đường bao xa trên mặt nước?* $\to$ Quãng đường = Vận tốc $\times$ Thời gian $\implies \lambda = v \times T = \frac{v}{f}$. Khái niệm bước sóng ra đời như một nhu cầu đo lường tất yếu!

---

### Rule 2: Mạch Nối Hữu Cơ Giữa Các Mục (Organic Thread / Bridge Invariant)

#### 1. Định nghĩa Quy tắc (The Core Invariant)
* Tuyệt đối **KHÔNG** viết các mục như những ốc đảo kiến thức độc lập, rời rạc.
* ❌ **CẤM (Anti-Pattern)**: Kết thúc mục trước bằng dấu chấm lửng/kẻ vạch ngang, sang mục sau nhảy dù vào một chủ đề mới toanh mà không giải thích mối liên hệ.
* ✅ **BẮT BUỘC (Required Invariant)**:
  - *Cuối mục trước*: Luôn kết thúc bằng một câu hỏi bỏ ngỏ, một rào cản tính toán hoặc một nút thắt thực tế.
  - *Đầu mục sau*: Bắt buộc có phần **"Bước chuyển / Mối nối từ Mục trước"**, nhắc lại vũ khí vừa đạt được và chỉ rõ vũ khí đó dẫn tới câu hỏi tự nhiên nào ở mục này.

#### 2. Ngữ cảnh áp dụng (Context & Trigger Conditions)
* **Thời điểm kích hoạt**: Tại ranh giới giữa hai mục nội dung liên tiếp (Heading 2, Heading 3) hoặc giữa hai chủ đề kế tiếp nhau.

#### 3. Ví dụ đối chiếu (Anti-pattern vs. Good pattern)
* ❌ **Ví dụ sai**: Hết Mục 1 (Đạo hàm là tốc độ biến thiên) $\implies$ sang Mục 2 ghi: *"2. Đạo hàm lượng giác. Cho hàm số x = cos(t)..."*
* ✅ **Ví dụ chuẩn (Chương 1: Dao động điều hòa)**:
  - Cuối Mục 1: Khẳng định vận tốc là độ dốc tiếp tuyến.
  - Đầu Mục 2 ghi rõ: *"Bước chuyển từ Mục 1: Ở Mục 1, chúng ta đã rút ra: Vận tốc tức thời chính là độ dốc của tiếp tuyến v(t) = x'(t). Bây giờ, trong dao động điều hòa, li độ biến thiên theo hàm cos(t). Câu hỏi tự nhiên đặt ra: Vận tốc v(t) = [cos(t)]' sẽ có công thức giải tích là gì? Hãy dùng lại công cụ độ dốc vừa học để đi tìm nó..."*
* 💡 **Ánh xạ sang chương khác (Chương 3: Điện trường — Từ Định luật Coulomb sang Khái niệm Điện trường)**:
  - *Cuối Mục 1 (Định luật Coulomb)*: Đặt nút thắt: "Công thức $F = k\frac{|q_1 q_2|}{r^2}$ cho thấy hai điện tích hút/đẩy nhau. Nhưng làm thế nào $q_1$ có thể truyền lực tác dụng lên $q_2$ xuyên qua khoảng chân không vũ trụ trống rỗng mà không có bất kỳ dây nối hay vật chất hữu hình nào chạm vào nhau?".
  - *Đầu Mục 2 (Điện trường)*: *"Bước chuyển từ Mục 1: Để giải quyết bài toán tương tác xuyên không gian ở Mục 1, các nhà vật lý nhận ra điện tích $q_1$ không tác dụng trực tiếp từ xa, mà nó đã tạo ra một môi trường vật chất đặc biệt bao quanh nó gọi là Điện trường..."*

---

### Rule 3: Đào Sâu Bản Chất Động Lực Học Gốc Rễ (Root-Cause Dynamics Invariant)

#### 1. Định nghĩa Quy tắc (The Core Invariant)
* Luôn khởi đầu bằng **Nghịch lý Trực giác (Intuitive Paradox)** từ đời sống. Tuyệt đối **KHÔNG** dừng lại ở sự miêu tả hình thức hay mô hình phản chiếu bề ngoài; **BẮT BUỘC** phải giải thích bằng **Động lực học và Lực tương tác gốc rễ** (Lực hồi phục, Định luật Newton, Chuyển hóa năng lượng).
* ❌ **CẤM (Anti-Pattern)**: Dùng các hình ảnh phản chiếu hình học làm nguyên nhân vật lý (ví dụ: "vật dao động điều hòa vì nó là bóng của chuyển động tròn đều").
* ✅ **BẮT BUỘC (Required Invariant)**: Chứng minh bằng phương trình động lực học: Ngoại lực lệch cân bằng sinh ra lực kéo về $F_{kv} = -kx \implies$ Định luật II Newton $a = x'' = -\omega^2 x \implies$ Chỉ có hàm lượng giác mới thỏa mãn tính chất đạo hàm hai lần đổi dấu.

#### 2. Ngữ cảnh áp dụng (Context & Trigger Conditions)
* **Thời điểm kích hoạt**: Khi giải thích căn nguyên vật lý của một hiện tượng tuần hoàn, cân bằng, hoặc lan truyền năng lượng.

#### 3. Ví dụ đối chiếu (Anti-pattern vs. Good pattern)
* ❌ **Ví dụ sai**: *"Một điểm chuyển động tròn đều với tốc độ góc $\omega$. Chiếu lên đường kính ta được $x = A\cos(\omega t)$. Vì vậy dao động điều hòa có phương trình là hàm cosin."* (Không trả lời được vì sao cái lò xo không quay mà lại ra hàm cos!).
* ✅ **Ví dụ chuẩn (Chương 1: Dao động điều hòa)**: Đặt nghịch lý: Màng loa chỉ thụt thò thẳng tắp, tại sao lại dùng hàm $\cos$ của đường tròn? $\to$ Giải mã: Lệch VTCB sinh lực kéo về $F_{kv} = -kx \implies a = -\omega^2 x \implies x''(t) = -\omega^2 x(t)$. Trong toàn bộ toán học, chỉ có hàm $\cos, \sin$ mới đạo hàm 2 lần đổi dấu trừ $\implies$ Tự nhiên chọn hàm cosin vì quy luật lực, không phải vì vật quay tròn ngầm!
* 💡 **Ánh xạ sang chương khác (Chương 2: Sóng cơ — Bản chất lan truyền sóng)**:
  - ❌ *Không giải thích bề ngoài*: "Sóng là sự lan truyền dao động theo thời gian trong không gian."
  - ✅ *Đào sâu gốc rễ*: Đặt nghịch lý: Khi ta gõ vào một đầu thanh kim loại, ta chỉ tác dụng lực vào lớp nguyên tử đầu tiên, tại sao đầu kia lại rung lên? $\to$ Bản chất động lực học: Giữa các nguyên tử luôn có **lực liên kết đàn hồi tĩnh điện**. Lớp 1 bị đẩy lệch khỏi VTCB bền $\implies$ lực đàn hồi giằng lớp 2 chuyển động theo nhưng trễ pha $\Delta t$. Sóng thực chất là sự chuyển giao lực đàn hồi và cơ năng liên tục giữa các phần tử!

---

### Rule 4: Trực Quan Hóa Đa Trạng Thái (State-Based Multi-Dimensional Invariant)

#### 1. Định nghĩa Quy tắc (The Core Invariant)
* Mọi tiến trình biến thiên theo thời gian hoặc chu kì **BẮT BUỘC** phải chia thành chuỗi **trạng thái mốc then chốt (Milestones)**. Tại mỗi mốc, phải phân tích đồng thời **4 chiều đối chiếu**:
  1. *Li độ / Tọa độ không gian* ($x$).
  2. *Vận tốc / Xu hướng biến thiên* (Độ dốc tiếp tuyến $v = x'$).
  3. *Lực tác dụng / Gia tốc* (Xu hướng giằng kéo $F_{kv}, a$).
  4. *Ý nghĩa cơ học & Năng lượng thực tế* (Động năng, thế năng, cảm nhận đời sống).
* Bắt buộc có hình vẽ khoa học trực quan (PNG 300 DPI + vector PDF) đi kèm, không được phân tích "chay chữ".
* ❌ **CẤM (Anti-Pattern)**: Chỉ đưa ra công thức tổng quát mà không phân tích cụ thể hành vi tại các điểm mốc biên, cân bằng.
* ✅ **BẮT BUỘC (Required Invariant)**: Bảng và hình vẽ phải hiển thị rõ các mốc $t = 0, T/4, T/2, 3T/4$ hoặc các trạng thái pha tương ứng.

#### 2. Ngữ cảnh áp dụng (Context & Trigger Conditions)
* **Thời điểm kích hoạt**: Khi mô tả một chu kì dao động, đồ thị động học, quá trình chuyển hóa động năng - thế năng, hoặc so sánh tương quan giữa hai dao động (cùng pha, ngược pha, vuông pha).

#### 3. Ví dụ đối chiếu (Anti-pattern vs. Good pattern)
* ❌ **Ví dụ sai**: Đưa ra công thức $v(t) = -\omega A \sin(\omega t)$ rồi nói chung chung: khi sin = 0 thì v = 0, khi sin = 1 thì v = v_max.
* ✅ **Ví dụ chuẩn (Chương 1: Dao động điều hòa)**: Phân tích 4 mốc:
  - $t = 0$: Biên dương ($x = +A$, tiếp tuyến ngang $v = 0$, lò xo dãn cực đại giằng về âm $a = -\omega^2 A$, thế năng cực đại).
  - $t = T/4$: Qua VTCB theo chiều âm ($x = 0$, tiếp tuyến dốc âm cắm đầu $v = -\omega A$, lực triệt tiêu $a = 0$, động năng cực đại).
  - $t = T/2$: Biên âm ($x = -A$, tiếp tuyến ngang $v = 0$, lò xo nén chặt đẩy sang dương $a = +\omega^2 A$, thế năng cực đại).
  - $t = 3T/4$: Qua VTCB theo chiều dương ($x = 0$, tiếp tuyến dốc lên $v = +\omega A$, lực triệt tiêu $a = 0$, động năng cực đại).
* 💡 **Ánh xạ sang chương khác (Chương 4: Mạch dao động LC — Quá trình phóng nạp điện)**:
  - Khảo sát 4 mốc:
    - $t = 0$: Tụ điện tích điện cực đại ($q = Q_0$), dòng điện chưa chạy ($i = 0$), năng lượng điện trường trong tụ cực đại $W_C = \max$, năng lượng từ trường trong cuộn cảm $W_L = 0$.
    - $t = T/4$: Tụ phóng hết điện ($q = 0$), dòng điện qua cuộn cảm đạt cực đại ($i = I_0$), $W_C = 0, W_L = \max$.
    - $t = T/2$: Tụ nạp điện ngược chiều ($q = -Q_0$), dòng điện khựng lại $i = 0$, $W_C = \max, W_L = 0$.
    - $t = 3T/4$: Tụ lại phóng hết điện ($q = 0$), dòng điện đạt cực đại theo chiều ngược lại ($i = -I_0$), $W_C = 0, W_L = \max$.

---

### Rule 5: Ẩn Dụ Hình Tượng & Phá Bẫy Tử Huyệt (Conceptual Anchors & Misconception Busters)

#### 1. Định nghĩa Quy tắc (The Core Invariant)
* Mọi đại lượng/công thức trừu tượng phải có một **Hình tượng Neo giữ (Conceptual Anchor / Metaphor)** cụ thể để người học ghi nhớ lâu dài.
* Mọi chuyên đề phải có mục **"Hộp Cứu Nguy: Tử Huyệt Nhận Thức"**: Chỉ rõ học sinh thường suy luận sai ở đâu, vì sao trực giác thường ngày đánh lừa họ, và dùng định luật vật lý để bẻ gãy ngộ nhận đó.
* **Quy chuẩn hình thức**: Tuyệt đối **CẤM DÙNG MÃ VẼ KHUNG ASCII** (`┌──┐`, `│`, `├`); bắt buộc dùng bảng Markdown (`| ... |`) và Alert Block (`> ⚠️ **...**`).

#### 2. Ngữ cảnh áp dụng (Context & Trigger Conditions)
* **Thời điểm kích hoạt**: Khi giới thiệu đại lượng mới (để neo giữ trí nhớ); và khi kết thúc phần lý thuyết (để rà soát bẫy thi cử).

#### 3. Ví dụ đối chiếu (Anti-pattern vs. Good pattern)
* ❌ **Ví dụ sai**: *"Câu 1: Chọn C. Học sinh chú ý không nhầm lẫn giữa tần số góc và tần số."* (Không giải thích được vì sao học sinh hay nhầm và cách khắc phục).
* ✅ **Ví dụ chuẩn (Chương 1: Dao động điều hòa)**:
  - *Ẩn dụ*: Tần số góc $\omega$ là "cỗ máy nén thời gian" (nén thời gian làm sườn đồ thị dốc gấp $\omega$ lần $\implies [\cos(\omega t)]' = -\omega\sin(\omega t)$); 3 vệ tinh trên đồng hồ vũ trụ; bộ mã gen ADN; chống ồn ANC.
  - *Phá bẫy*: Tử huyệt 1: "Ở biên vật đứng lại ($v = 0$) nên gia tốc bằng 0 (?)". Lật tẩy ngộ nhận: Học sinh nhầm giữa *chuyển động* ($v$) và *sự giằng kéo của lực* ($a$). Ở biên đồ thị nằm ngang nên $v = 0$, nhưng lò xo dãn cực đại nên lực giằng kéo mạnh nhất $\implies |a| = a_{\max} = \omega^2 A$!
* 💡 **Ánh xạ sang chương khác (Chương 3: Cường độ điện trường $E = F/q$)**:
  - *Ẩn dụ Neo giữ*: Điện trường là "mùi hương nước hoa tỏa ra trong phòng" hoặc "độ dốc của mặt đồi".
  - *Phá bẫy Tử huyệt*: Học sinh nhìn công thức $E = F/q$ và kết luận: "Khi đưa $q = 0$ vào thì $E = 0$, tức là không có điện tích thử thì không có điện trường (?)". Bẻ gãy bẫy: Điện trường $E$ do điện tích nguồn $Q$ sinh ra và tồn tại sẵn trong không gian (như mùi nước hoa đã có sẵn trong phòng), điện tích thử $q$ chỉ là "chiếc mũi" đặt vào để đo độ nồng của mùi hương. Điện trường $E$ hoàn toàn không phụ thuộc vào độ lớn của $q$!

---

---

## 2. Tôn Chỉ Sư Phạm Cốt Lõi: Đơn Giản Hóa Bản Chất, Không Đánh Đố Học Sinh

> **Quy tắc vàng**: *"Một nhà vật lý giỏi là người có thể giải thích bản chất sâu xa nhất của vũ trụ cho một học sinh trung học phổ thông hiểu mà không cần núp bóng sau những phương trình phức tạp."*

Mục tiêu của sách không phải là "khoe kiến thức đại học", mà là:
1. Giúp học sinh lớp 11 **hiểu tận gốc**: Tại sao công thức SGK lại có dạng như vậy?
2. Dùng công cụ **Toán học lớp 11** (chủ đạo là Đạo hàm và Đồ thị) để chứng minh và liên kết các hiện tượng.
3. Liên hệ với các vật thể thực tế đời sống mà học sinh có thể sờ, thấy hoặc cảm nhận được (xe cộ, đàn guitar, xích đu, điện thoại thông minh).

---

## 3. Các Giới Hạn Sư Phạm Bắt Buộc

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

## 4. Checklist Tự Kiểm Định Độ Phù Hợp Lớp 11 (Audience-Fit Gate)

Trước khi xuất bản hoặc hoàn tất chương sách, tự đặt 5 câu hỏi:
1. *Một học sinh lớp 11 nắm chắc SGK có hiểu được bài viết này mà không cần tra cứu giáo trình đại học không?*
2. *Có công thức nào xuất hiện số phức, tích phân hay phương trình vi phân phức tạp không? (Nếu có $\rightarrow$ sửa ngay).*
3. *Hình vẽ và ví dụ có bám sát đời sống thực tế không?*
4. *Các ký hiệu có nhất quán với SGK GDPT 2018 không? (Dùng $x, v, a, W, W_đ, W_t, \omega, f, T$).*
5. *Tài liệu có sót ký tự vẽ khung ASCII nào không? Mỗi mục kiến thức then chốt đã có hình vẽ khoa học tương ứng minh họa chưa?*

