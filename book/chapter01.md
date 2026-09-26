# CHƯƠNG 1: DAO ĐỘNG ĐIỀU HÒA – BẢN CHẤT VẬT LÍ, ĐẠO HÀM & HIỆN TƯỢNG ĐỜI SỐNG

---

> 📐 **HỘP CÔNG CỤ: TOÁN HỌC LỚP 11 CẦN THIẾT CHO CHƯƠNG 1**  
> Để thấu suốt bản chất chuyển động thay vì học vẹt công thức, các em chỉ cần vận dụng 3 công cụ Toán học lớp 11 rất quen thuộc:  
> 1. **Khái niệm Đạo hàm (Tốc độ biến thiên tức thời):**  
>    * Vận tốc là đạo hàm của li độ theo thời gian: $v(t) = x'(t) = \frac{dx}{dt}$.  
>    * Gia tốc là đạo hàm của vận tốc theo thời gian: $a(t) = v'(t) = \frac{dv}{dt}$.  
> 2. **Đạo hàm của hàm số lượng giác cơ bản:**  
>    $$\left[\cos(\omega t + \varphi)\right]' = -\omega \sin(\omega t + \varphi), \quad \left[\sin(\omega t + \varphi)\right]' = \omega \cos(\omega t + \varphi)$$  
> 3. **Công thức Lượng giác & Hệ thức Độc lập Thời gian:**  
>    * Cung hơn kém $\pi/2$: $-\sin\alpha = \cos(\alpha + \pi/2)$.  
>    * Cung hơn kém $\pi$: $-\cos\alpha = \cos(\alpha + \pi)$.  
>    * Hệ thức cơ bản: $\sin^2\alpha + \cos^2\alpha = 1 \implies \left(\frac{x}{A}\right)^2 + \left(\frac{v}{\omega A}\right)^2 = 1$.

---

# MODULE 1: ĐỘNG HỌC DAO ĐỘNG ĐIỀU HÒA & ĐỒ THỊ TRẠNG THÁI
*(Kinematics of Simple Harmonic Motion & State Plots)*

### 1. Mục tiêu Cần đạt
Sau khi học xong Module 1, các em sẽ:
* Hiểu rõ vì sao dao động điều hòa là chuyển động thẳng có gia tốc biến đổi liên tục, không phải là "chuyển động tròn quay ngầm".
* Tự mình dẫn xuất được công thức vận tốc, gia tốc và mối liên hệ pha ($\pi/2, \pi$) bằng phép lấy đạo hàm hàm lượng giác.
* Vẽ và đọc hiểu đồ thị trạng thái $(x, v/\omega)$, biết cách xác định ngay trạng thái của vật tại các thời điểm quan trọng ($0, T/4, T/2, 3T/4$).
* Tránh được bẫy đề thi trắc nghiệm kinh điển: *"khi vận tốc bằng 0 thì gia tốc bằng bao nhiêu?"*.

---

### 2. Mâu thuẫn Sách Giáo Khoa & Câu Hỏi Khởi Phát
* **Quan sát thực tế:** Một cành cây đu đưa trong gió, chiếc xích đu qua lại trên sân trường, hay màng loa điện thoại rung động phát ra âm thanh. Tất cả đều là những chuyển động **thẳng** (hoặc gần như thẳng), lặp đi lặp lại quanh một vị trí cân bằng.
* **Mâu thuẫn thường gặp:** Sách giáo khoa thường mở đầu bài học bằng cách lấy bóng của một điểm chuyển động tròn đều chiếu xuống đường kính. Cách tiếp cận này rất tiện về mặt hình học, nhưng vô tình khiến nhiều học sinh lầm tưởng rằng: *"Muốn có dao động điều hòa hình cosin, bên trong vật thể chắc hẳn phải có cái gì đó đang quay tròn!"*.
* **Bản chất vật lý:** Trong thực tế, chiếc màng loa hay quả lắc không hề quay tròn. Chuyển động của chúng có dạng hàm cosin là bởi vì **lực kéo vật về vị trí cân bằng luôn tỉ lệ thuận với độ lệch của vật**: lệch càng xa, lực kéo về càng mạnh. Chính quy luật này ép buộc gia tốc phải tỉ lệ ngược dấu với li độ:
  $$a(t) = -\omega^2 x(t)$$
  Một chuyển động thẳng mà gia tốc luôn thỏa mãn biểu thức trên được gọi là **dao động điều hòa**.

---

### 3. Mô hình Trực quan: Thanh truyền - Pít-tông trong Động cơ
* **Hình ảnh liên tưởng:** Hãy quan sát bộ phận **Pít-tông và Trục khuỷu** trong động cơ xe máy. Khi trục khuỷu quay tròn đều với tốc độ góc $\omega$, thanh truyền nối với pít-tông làm pít-tông chuyển động tịnh tiến thẳng tới - lui trong lòng xi-lanh.
* **Nhận xét chuyển động:**
  - Ở hai đầu xi-lanh (gọi là hai điểm chết, tương ứng với hai **Biên độ** $x = \pm A$), pít-tông phải khựng lại để đổi chiều chuyển động, nên vận tốc tại đó tức thời bằng $0$.
  - Khi lao qua điểm chính giữa (tương ứng với **Vị trí cân bằng** $x = 0$), pít-tông lao đi nhanh nhất, đạt vận tốc cực đại $v_{\max} = \omega A$.

---

### 4. Dẫn Xuất Bằng Đạo Hàm: Vận Tốc, Gia Tốc và Độ Lệch Pha

Xét một vật dao động điều hòa dọc theo trục $Ox$ với phương trình li độ:
$$x(t) = A\cos(\omega t + \varphi)$$

Trong đó:
* $x(t)$: Li độ (vị trí của vật so với gốc $O$), đơn vị mét ($\text{m}$) hoặc xentimét ($\text{cm}$).
* $A$: Biên độ dao động (độ lệch cực đại khỏi gốc $O$, luôn dương: $A > 0$).
* $\omega$: Tần số góc, đơn vị radian trên giây ($\text{rad/s}$).
* $\varphi$: Pha ban đầu tại thời điểm $t = 0$, đơn vị radian ($\text{rad}$).
* $(\omega t + \varphi)$: Pha dao động tại thời điểm $t$, cho biết trạng thái chuyển động (vị trí và chiều chuyển động) của vật.

#### Bước 1: Tìm Vận tốc $v(t)$ bằng Đạo hàm Bậc Nhất
Vận tốc là tốc độ thay đổi của tọa độ theo thời gian. Lấy đạo hàm của $x(t)$ theo biến $t$:
$$v(t) = x'(t) = \left[A\cos(\omega t + \varphi)\right]' = -A\omega \sin(\omega t + \varphi)$$

Dùng công thức lượng giác $-\sin\alpha = \cos(\alpha + \pi/2)$, ta viết lại:
$$v(t) = \omega A \cos\left(\omega t + \varphi + \frac{\pi}{2}\right)$$

> 💡 **Kết luận 1**: Vận tốc biến thiên điều hòa cùng tần số $\omega$ nhưng **sớm pha $\frac{\pi}{2}$** (tức là đi trước một phần tư chu kỳ $T/4$) so với li độ $x$.  
> Vận tốc cực đại: $v_{\max} = \omega A$.

#### Bước 2: Tìm Gia tốc $a(t)$ bằng Đạo hàm Bậc Hai
Gia tốc là tốc độ thay đổi của vận tốc theo thời gian. Lấy đạo hàm của $v(t)$ theo biến $t$:
$$a(t) = v'(t) = x''(t) = \left[-A\omega \sin(\omega t + \varphi)\right]' = -A\omega^2 \cos(\omega t + \varphi)$$

Dùng công thức lượng giác $-\cos\alpha = \cos(\alpha + \pi)$, ta viết lại:
$$a(t) = \omega^2 A \cos\left(\omega t + \varphi + \pi\right)$$

Mặt khác, vì $x(t) = A\cos(\omega t + \varphi)$, ta nhận được hệ thức cốt lõi:
$$a(t) = -\omega^2 x(t)$$

> 💡 **Kết luận 2**: Gia tốc biến thiên điều hòa cùng tần số $\omega$, **ngược pha hoàn toàn ($\pi$)** so với li độ $x$, và luôn hướng về vị trí cân bằng (ngược dấu với $x$).  
> Gia tốc cực đại: $a_{\max} = \omega^2 A$.

---

![Đồ thị động học chuẩn hóa theo thời gian của dao động điều hòa: Li độ x(t), Vận tốc v(t), và Gia tốc a(t).](figures/fig1_1_kinematics.png)

> 🔍 **DẪN DẮT MẮT ĐỌC (Hình 1.1):**  
> * **Đồ thị trên cùng (Li độ $x/A$):** Lúc $t = 0$, vật ở biên dương $x = +A$. Sau $T/4$, vật về VTCB ($x = 0$). Sau $T/2$, vật tới biên âm ($x = -A$).  
> * **Đồ thị ở giữa (Vận tốc $\frac{v}{\omega A}$):** Khi vật đang ở biên ($x = +A$ hoặc $-A$), đường nét đứt chiếu xuống cho thấy vận tốc bằng đúng $0$. Khi vật qua VTCB ($x = 0$ lúc $t = T/4$), vận tốc đạt giá trị âm cực đại $v = -\omega A$ (vật lao nhanh nhất theo chiều âm).  
> * **Đồ thị dưới cùng (Gia tốc $\frac{a}{\omega^2 A}$):** Khi vật ở biên âm ($x = -A$ lúc $t = T/2$), gia tốc vọt lên cực đại dương $a = +\omega^2 A$ để kéo giật vật quay về gốc tọa độ. Hai đường $x(t)$ và $a(t)$ hoàn toàn uốn lượn đối xứng ngược chiều nhau!

---

### 5. Đồ Thị Trạng Thái $(x, v/\omega)$ & Hệ Thức Độc Lập Thời Gian

Từ hai phương trình li độ và vận tốc:
$$\frac{x}{A} = \cos(\omega t + \varphi), \quad \frac{v}{\omega A} = -\sin(\omega t + \varphi)$$

Bình phương hai vế và cộng lại, tận dụng $\cos^2\alpha + \sin^2\alpha = 1$:
$$\left(\frac{x}{A}\right)^2 + \left(\frac{v}{\omega A}\right)^2 = 1 \iff x^2 + \frac{v^2}{\omega^2} = A^2$$

Đây chính là **Hệ thức độc lập thời gian** vô cùng nổi tiếng trong các bài thi Vật lý 11!

Nếu ta đặt trục hoành là li độ $x$, và trục tung là đại lượng vận tốc chuẩn hóa $y = \frac{v}{\omega}$, phương trình trên trở thành:
$$x^2 + y^2 = A^2$$
Đây chính là phương trình đường tròn tâm $O$ bán kính $A$!

![Đồ thị trạng thái (x, v/omega) biểu diễn quỹ đạo khép kín của dao động điều hòa theo chiều kim đồng hồ.](figures/fig1_2_phase_space.png)

> 🔍 **DẪN DẮT MẮT ĐỌC (Hình 1.2):**  
> * Điểm màu cam $S_0(t = 0)$ tại tọa độ $(+A, 0)$: Vật đang ở biên dương, đứng yên tức thời.  
> * Khi thời gian trôi, điểm trạng thái chạy trên đường tròn **thuận chiều kim đồng hồ**:  
>   - Đến $S_1(t = T/4)$: Tọa độ là $(0, -\omega A)$, tức vật qua VTCB với vận tốc âm cực đại.  
>   - Đến $S_2(t = T/2)$: Tọa độ $(-A, 0)$, vật tới biên âm, vận tốc bằng 0.  
>   - Đến $S_3(t = 3T/4)$: Tọa độ $(0, +\omega A)$, vật qua VTCB theo chiều dương.  
> * **Quy luật hình học**: Ở nửa trên mặt phẳng ($v > 0$), vật đi theo chiều dương nên $x$ phải tăng; ở nửa dưới ($v < 0$), vật đi theo chiều âm nên $x$ phải giảm. Vì vậy, mọi trạng thái dao động đều bắt buộc phải quay **thuận chiều kim đồng hồ**.

---

### 6. Bài Toán Tính Số Thực Tế 1.1

> **Bài toán:** Một màng loa của tai nghe điện thoại dao động điều hòa để tạo ra âm thanh có tần số $f = 440\text{ Hz}$ (nốt La chuẩn $A_4$). Biên độ rung của màng loa là $A = 0.5\text{ mm} = 0.5 \times 10^{-3}\text{ m}$.  
> 1. Tính tần số góc $\omega$, chu kỳ dao động $T$.  
> 2. Tính tốc độ cực đại $v_{\max}$ và gia tốc cực đại $a_{\max}$ của màng loa.  
> 3. Khi màng loa đang ở vị trí cách vị trí cân bằng $x = 0.3\text{ mm}$, tính tốc độ tức thời của màng loa.
> 
> **Lời giải chi tiết:**  
> 1. **Tính các thông số cơ bản:**  
>    * Tần số góc: $\omega = 2\pi f = 2\pi \times 440 \approx 2764.6\text{ rad/s}$.  
>    * Chu kỳ dao động: $T = \frac{1}{f} = \frac{1}{440} \approx 0.00227\text{ s} = 2.27\text{ ms}$.  
> 2. **Tính tốc độ và gia tốc cực đại:**  
>    * Tốc độ cực đại:  
>      $$v_{\max} = \omega A = (2764.6\text{ rad/s}) \times (0.5 \times 10^{-3}\text{ m}) \approx 1.38\text{ m/s}$$  
>    * Gia tốc cực đại:  
>      $$a_{\max} = \omega^2 A = (2764.6\text{ rad/s})^2 \times (0.5 \times 10^{-3}\text{ m}) \approx 3821.5\text{ m/s}^2$$  
>      *(Gia tốc này gấp gần 390 lần gia tốc trọng trường Trái Đất $g \approx 9.8\text{ m/s}^2$! Dù màng loa rung rất khẽ chỉ nửa milimét, lực quán tính tác dụng lên vật liệu màng loa là cực kỳ khủng khiếp).*  
> 3. **Tính tốc độ tức thời khi $x = 0.3\text{ mm}$:**  
>    Áp dụng hệ thức độc lập thời gian:  
>    $$x^2 + \frac{v^2}{\omega^2} = A^2 \implies |v| = \omega \sqrt{A^2 - x^2}$$  
>    Thay số (giữ nguyên đơn vị $\text{mm}$ cho $x$ và $A$):  
>    $$|v| = (2764.6) \times \sqrt{0.5^2 - 0.3^2} = 2764.6 \times 0.4 = 1105.8\text{ mm/s} \approx 1.11\text{ m/s}$$

---

> ⚠️ **CẢNH BÁO LỖI PHỔ BIẾN TRONG ĐỀ THI:**  
> Rất nhiều học sinh chọn nhầm đáp án khi gặp câu hỏi: *"Khi vật dừng lại ở biên thì gia tốc bằng bao nhiêu?"*.  
> * **Sai lầm:** Nghĩ rằng "vật dừng lại ($v = 0$) thì không có gia tốc ($a = 0$)".  
> * **Bản chất đúng:** Khi vật ở biên ($v = 0$), lò xo bị nén hoặc dãn mạnh nhất, nên lực kéo về đạt giá trị **lớn nhất**, dẫn tới gia tốc đạt **cực đại** ($a = \pm \omega^2 A$). Gia tốc chỉ bằng 0 khi vật đi qua vị trí cân bằng ($x = 0$), nơi vận tốc lại đạt giá trị cực đại!

---

# MODULE 2: ĐỘNG LỰC HỌC & BẢN CHẤT "ĐÁY CHẢO PARABOL"
*(Dynamics of Oscillations & The Parabolic Potential Well)*

### 1. Mục tiêu Cần đạt
Sau khi học xong Module 2, các em sẽ:
* Giải thích được vì sao con lắc lò xo lại dao động điều hòa bằng cách kết hợp Định luật II Newton và Định luật Hooke.
* Hiểu được bí mật lớn của tự nhiên: *Vì sao dao động nhỏ quanh bất kỳ vị trí cân bằng bền nào cũng đều là dao động điều hòa?* thông qua hình ảnh "đáy chảo parabol".
* Hiểu điều kiện góc nhỏ ($\alpha \le 10^\circ$) của con lắc đơn và biết con lắc đơn sai lệch thế nào khi dao động ở góc lớn.

---

### 2. Mâu thuẫn & Câu Hỏi Khởi Phát
* **Quan sát:** Trong phòng thí nghiệm, ta kéo dãn một lò xo rồi buông tay, quả nặng dao động điều hòa. Nhưng nếu gảy một sợi dây đàn guitar, hay ấn nhẹ đầu một chiếc thước kẻ kẹp trên mép bàn rồi buông ra, đầu thước kẻ cũng dao động điều hòa. Rõ ràng chiếc thước kẻ hay sợi dây đàn không có cái lò xo xoắn kim loại nào bên trong. Vậy lực đàn hồi $F = -kx$ từ đâu mà ra?
* **Bản chất vật lý:** Mọi vật thể rắn xung quanh ta đều được cấu tạo từ các nguyên tử liên kết với nhau. Khi vật đứng yên ổn định, các nguyên tử nằm ở **vị trí cân bằng bền**, nơi lực hút và lực đẩy giữa chúng triệt tiêu nhau. Khi ta làm biến dạng nhẹ vật thể, các liên kết nguyên tử sẽ sinh ra lực hồi phục kéo các hạt trở lại vị trí ban đầu.

---

### 3. Động Lực Học Con Lắc Lò Xo Theo Định Luật II Newton

Xét một vật nhỏ khối lượng $m$ gắn vào đầu một lò xo nhẹ có độ cứng $k$, đặt trên mặt phẳng nằm ngang không ma sát. Chọn gốc tọa độ $O$ tại vị trí cân bằng (lò xo không biến dạng), chiều dương hướng theo chiều dãn của lò xo.

1. **Xác định lực tác dụng:**  
   Khi vật lệch khỏi vị trí cân bằng một đoạn $x$, lò xo bị biến dạng một lượng $\Delta \ell = x$.  
   Lực đàn hồi do lò xo tác dụng lên vật đóng vai trò là **lực kéo về (lực hồi phục)**:
   $$F_{kv} = -kx$$
   *(Dấu trừ thể hiện: khi $x > 0$ thì $F < 0$ hướng về gốc $O$; khi $x < 0$ thì $F > 0$ cũng hướng về gốc $O$).*

2. **Áp dụng Định luật II Newton:**
   $$F = ma \iff -kx = ma \iff a = -\frac{k}{m}x$$

3. **So sánh với định nghĩa dao động điều hòa:**  
   Ở Module 1, ta đã biết dao động điều hòa luôn có quy luật gia tốc: $a = -\omega^2 x$.  
   Đối chiếu hai phương trình:
   $$\omega^2 = \frac{k}{m} \implies \omega = \sqrt{\frac{k}{m}}$$

> 💡 **Kết luận:** Chuyển động của con lắc lò xo là **dao động điều hòa** với:
> * Tần số góc riêng: $\omega_0 = \sqrt{\frac{k}{m}}\text{ (rad/s)}$.
> * Chu kỳ dao động riêng: $T_0 = \frac{2\pi}{\omega_0} = 2\pi\sqrt{\frac{m}{k}}\text{ (s)}$.
> * Tần số dao động riêng: $f_0 = \frac{1}{T_0} = \frac{1}{2\pi}\sqrt{\frac{k}{m}}\text{ (Hz)}$.
> 
> *Nhận xét quan trọng:* Chu kỳ $T$ chỉ phụ thuộc vào bản chất của hệ (khối lượng $m$ và độ cứng $k$), **hoàn toàn không phụ thuộc vào biên độ dao động $A$** hay cách kích thích ban đầu. Đây gọi là tính **đẳng thời** của dao động điều hòa.

---

### 4. Ẩn Dụ Đáy Chảo Parabol: Vì Sao Dao Động Điều Hòa Phổ Quát Trong Tự Nhiên?

Tại sao dao động điều hòa lại xuất hiện ở khắp mọi nơi trong vũ trụ, từ dao động phân tử, nguyên tử đến cầu cống, nhà cao tầng?

Hãy tưởng tượng một **hòn bi đặt trong lòng một chiếc chảo trũng**.
1. **Tại điểm sâu nhất của đáy chảo ($x_0 = 0$):** Hòn bi nằm yên thăng bằng. Đây là **Vị trí cân bằng bền**. Tại đây, thế năng của hòn bi đạt giá trị cực tiểu.
2. **Hình dáng đáy chảo:** Dù miệng chảo bên trên có méo mó hay bất đối xứng thế nào đi nữa, thì ngay tại vùng lân cận điểm đáy trũng nhất, bất kỳ một đường cong trơn nào cũng có thể áp vừa khít một đường cong **Parabol**:
   $$W_t(x) \approx \frac{1}{2} k x^2$$
3. **Xuất hiện lực hồi phục:** Khi hòn bi lăn lệch khỏi đáy một đoạn nhỏ $x$, sườn chảo dốc lên sẽ tạo ra phản lực có xu hướng đẩy hòn bi trượt trở về đáy. Vì thế năng có dạng parabol bậc hai, lực đẩy về sẽ tỉ lệ thuận với độ dời bậc nhất:
   $$F = -kx$$

![Bản chất hình học của đáy giếng thế năng: Dao động nhỏ quanh vị trí cân bằng bền luôn có thế năng dạng Parabol.](figures/fig1_3_potential_well.png)

> 🔍 **DẪN DẮT MẮT ĐỌC (Hình 1.3):**  
> * **Đường cong màu xanh đậm $W_t(x)$:** Đại diện cho năng lượng thực tế của một hệ vật lý (ví dụ liên kết phân tử), có dạng đáy trũng nhưng hai bên dốc không đều nhau.  
> * **Đường nét đứt màu đỏ Parabol $W_t \approx \frac{1}{2}kx^2$:** Là đường parabol toán học lý tưởng.  
> * **Vùng màu vàng nhạt (Biên độ nhỏ $|x| \le 0.35$):** Các em hãy nhìn kỹ vùng này — đường cong thực tế màu xanh và đường parabol màu đỏ **trùng khít lên nhau**! Điều này chứng minh: *Hầu như mọi dao động nhỏ quanh vị trí cân bằng bền trong vũ trụ đều là dao động điều hòa.*  
> * **Mũi tên đỏ góc phải:** Nếu ta kéo vật lệch quá xa ra ngoài vùng vàng, thế năng thực tế không còn là parabol nữa, dao động sẽ bị méo và không còn là điều hòa đơn giản.

---

### 5. Con Lắc Đơn & Giới Hạn Góc Nhỏ

Một con lắc đơn gồm sợi dây nhẹ không dãn chiều dài $\ell$, đầu dưới treo quả nặng khối lượng $m$. Kéo con lắc lệch góc $\alpha$ so với phương thẳng đứng rồi thả nhẹ.

1. **Lực kéo về của con lắc đơn:**  
   Trọng lực $\vec{P}$ phân tích thành hai thành phần. Thành phần tiếp tuyến với quỹ đạo cung tròn đóng vai trò lực hồi phục:
   $$F_t = -mg \sin\alpha$$
2. **Góc nhỏ ($\alpha \le 10^\circ \approx 0.175\text{ rad}$):**  
   Khi góc $\alpha$ tính bằng radian rất nhỏ, theo hình học lượng giác ta có xấp xỉ: $\sin\alpha \approx \alpha$.  
   Mặt khác, cung dịch chuyển $s = \ell \alpha \implies \alpha = \frac{s}{\ell}$.  
   Thay vào biểu thức lực:
   $$F_t \approx -mg \alpha = -\left(\frac{mg}{\ell}\right)s$$
   Đặt độ cứng tương đương $k = \frac{mg}{\ell}$, biểu thức lực lại có đúng dạng $F = -ks$!
3. **Chu kỳ con lắc đơn góc nhỏ:**
   $$T_0 = 2\pi\sqrt{\frac{m}{k}} = 2\pi\sqrt{\frac{m}{mg/\ell}} = 2\pi\sqrt{\frac{\ell}{g}}$$

> ⚡ **Lưu ý quan trọng:** Công thức $T = 2\pi\sqrt{\ell/g}$ chỉ đúng khi **góc lệch nhỏ ($\alpha_0 \le 10^\circ$)**. Nếu kéo con lắc ra góc lớn (như $60^\circ$ hoặc $90^\circ$), con lắc sẽ đi chậm lại ở gần biên, làm chu kỳ thực tế hơi dài hơn công thức trên một chút.

---

### 6. Bài Toán Tính Số Thực Tế 1.2

> **Bài toán:** Một con lắc lò xo treo thẳng đứng gồm quả cầu nhỏ khối lượng $m = 250\text{ g} = 0.25\text{ kg}$ gắn vào lò xo có độ cứng $k = 100\text{ N/m}$. Lấy $g = 9.8\text{ m/s}^2 \approx \pi^2$.  
> 1. Tại vị trí cân bằng, lò xo dãn một đoạn $\Delta \ell_0$ bằng bao nhiêu?  
> 2. Tính tần số góc $\omega$ và chu kỳ dao động $T$ của con lắc.  
> 3. Nâng vật lên vị trí lò xo không biến dạng rồi buông nhẹ không vận tốc đầu. Chọn trục tọa độ thẳng đứng hướng xuống, gốc $O$ tại vị trí cân bằng. Viết phương trình dao động của vật.
> 
> **Lời giải chi tiết:**  
> 1. **Độ dãn ở vị trí cân bằng:**  
>    Tại VTCB, lực đàn hồi cân bằng với trọng lực:  
>    $$F_{đh0} = P \iff k \Delta \ell_0 = mg \implies \Delta \ell_0 = \frac{mg}{k} = \frac{0.25 \times 9.8}{100} = 0.0245\text{ m} = 2.45\text{ cm}$$  
> 2. **Tần số góc và chu kỳ:**  
>    * Tần số góc: $\omega = \sqrt{\frac{k}{m}} = \sqrt{\frac{100}{0.25}} = \sqrt{400} = 20\text{ rad/s}$.  
>    * Chu kỳ: $T = \frac{2\pi}{\omega} = \frac{2\pi}{20} = \frac{\pi}{10} \approx 0.314\text{ s}$.  
>    *(Mẹo tính nhanh cho con lắc treo thẳng đứng: $\omega = \sqrt{\frac{g}{\Delta \ell_0}}$).*  
> 3. **Viết phương trình dao động:**  
>    * Gốc $O$ ở VTCB, chiều dương hướng xuống. Vị trí lò xo không biến dạng nằm phía trên VTCB một đoạn $\Delta \ell_0 = 2.45\text{ cm}$, tức là có tọa độ $x = -2.45\text{ cm}$.  
>    * Thả nhẹ ($v_0 = 0$) tại tọa độ này nên đây chính là biên âm: $A = 2.45\text{ cm}$.  
>    * Tại $t = 0$: $x(0) = -A = A\cos\varphi \implies \cos\varphi = -1 \implies \varphi = \pi\text{ rad}$.  
>    * Vậy phương trình dao động là:  
>      $$x(t) = 2.45\cos(20t + \pi)\text{ (cm)}$$

---

# MODULE 3: NĂNG LƯỢNG, DAO ĐỘNG TẮT DẦN & HIỆN TƯỢNG CỘNG HƯỞNG
*(Energy Conservation, Damped Oscillations & Resonance)*

### 1. Mục tiêu Cần đạt
Sau khi học xong Module 3, các em sẽ:
* Chứng minh được định luật bảo toàn cơ năng trong dao động điều hòa và phân tích được sự luân chuyển năng lượng với chu kỳ $T/2$.
* Nắm chắc vị trí mà động năng bằng thế năng ($x = \pm A/\sqrt{2}$) và giá trị trung bình của năng lượng.
* Hiểu cơ chế vi mô của dao động tắt dần (ma sát sinh nhiệt) và phân biệt 3 chế độ tắt dần trong kỹ thuật đời sống.
* Giải thích được hiện tượng cộng hưởng cơ học, phân biệt mặt lợi và mặt hại của cộng hưởng.

---

### 2. Sự Biến Đổi & Bảo Toàn Năng Lượng

Một vật dao động điều hòa có li độ $x = A\cos(\omega t + \varphi)$ và vận tốc $v = -\omega A\sin(\omega t + \varphi)$.

1. **Động năng $W_d$:**  
   $$W_d = \frac{1}{2}mv^2 = \frac{1}{2}m \omega^2 A^2 \sin^2(\omega t + \varphi) = \frac{1}{2}kA^2 \sin^2(\omega t + \varphi)$$
   *(vì $k = m\omega^2$).*

2. **Thế năng $W_t$:**  
   $$W_t = \frac{1}{2}kx^2 = \frac{1}{2}kA^2 \cos^2(\omega t + \varphi)$$

3. **Cơ năng toàn phần $W$:**  
   Cộng động năng và thế năng tại mọi thời điểm:
   $$W = W_d + W_t = \frac{1}{2}kA^2 \left[\sin^2(\omega t + \varphi) + \cos^2(\omega t + \varphi)\right] = \frac{1}{2}kA^2 = \text{const}$$

> 💡 **Kết luận 1**: Khi không có ma sát, cơ năng của vật dao động điều hòa **được bảo toàn tuyệt đối** và tỉ lệ thuận với bình phương biên độ dao động ($W \propto A^2$).  
> Cơ năng bằng động năng cực đại (khi qua VTCB) và bằng thế năng cực đại (khi ở biên):
> $$W = W_{d\max} = W_{t\max} = \frac{1}{2}kA^2 = \frac{1}{2}m v_{\max}^2$$

#### Chu kỳ Biến thiên của Động năng và Thế năng
Áp dụng công thức hạ bậc lượng giác:
$$\sin^2\alpha = \frac{1 - \cos 2\alpha}{2}, \quad \cos^2\alpha = \frac{1 + \cos 2\alpha}{2}$$
Ta thấy động năng và thế năng biến thiên tuần hoàn theo thời gian với **tần số góc gấp đôi ($2\omega$)**, tức là **chu kỳ bằng một nửa chu kỳ dao động ($T' = T/2$)** và **tần số gấp đôi ($f' = 2f$)**.

![Động năng và thế năng chuyển hóa tuần hoàn theo thời gian và phân bố theo li độ.](figures/fig1_4_energy.png)

> 🔍 **DẪN DẮT MẮT ĐỌC (Hình 1.4):**  
> * **Đồ thị (a) - Năng lượng theo thời gian:** Đường liền nét màu xanh lá (Động năng) và đường nét đứt màu xanh navy (Thế năng) liên tục nhấp nhô đổi chỗ cho nhau. Khi một bên đạt đỉnh thì bên kia chạm đáy. Nhưng đường thẳng đỏ trên cùng (Cơ năng tổng) nằm ngang tuyệt đối không hề suy suyển!  
> * **Đường chấm xám ở giữa:** Giá trị trung bình theo thời gian của động năng đúng bằng thế năng: $\bar{W}_d = \bar{W}_t = \frac{1}{2}W$.  
> * **Đồ thị (b) - Năng lượng theo li độ:** Thế năng là một parabol úp ngửa, động năng là parabol úp ngược. Điểm giao nhau màu cam chính là vị trí $x = \pm \frac{A}{\sqrt{2}} \approx \pm 0.707A$, nơi động năng bằng thế năng!

---

### 3. Dao Động Tắt Dần: Bản Chất Vi Mô & 3 Chế Độ Thực Tế

Trong thực tế đời sống, không có con lắc nào dao động vĩnh viễn nếu không được tiếp thêm năng lượng. Chiếc xích đu sau vài nhịp sẽ dừng lại, cành cây sẽ ngừng lay.

#### Cơ chế Vi mô: Năng lượng Đã Đi Đâu?
Khi vật chuyển động trong môi trường (như không khí hay dầu), bề mặt của vật liên tục va chạm với hàng triệu phân tử môi trường:
* Lực cản môi trường cản trở chuyển động của vật, sinh công âm ($A_c < 0$).
* Cơ năng của vật không mất đi mà chuyển hóa thành nhiệt năng làm nóng vật và môi trường xung quanh: $\Delta W = Q_{nhiệt}$.
* Vì cơ năng $W = \frac{1}{2}kA^2$ giảm dần theo thời gian, nên **biên độ $A$ bắt buộc phải giảm dần**. Hiện tượng này gọi là **dao động tắt dần**.

#### Ba Chế Độ Chuyển Động Thực Tế Khi Có Lực Cản

![Ba chế độ chuyển động khi có lực cản môi trường và quỹ đạo xoắn ốc trạng thái.](figures/fig1_5_damped.png)

1. **Lực cản nhỏ (Dao động tắt dần - Underdamped):**  
   * Vật vẫn dao động qua lại quanh VTCB nhiều lần với biên độ nhỏ dần theo thời gian (đường màu xanh navy).  
   * *Ví dụ:* Con lắc đơn đung đưa trong không khí, chiếc xích đu.
2. **Lực cản tới hạn (Critically Damped):**  
   * Vật trở về vị trí cân bằng **nhanh nhất** mà không hề bị dao động lắc qua phía bên kia (đường nét đứt màu xanh lá).  
   * *Ứng dụng kỹ thuật đắt giá:* **Bộ giảm xóc (phuộc nhún) xe máy và ô tô**. Khi xe đi qua ổ gà, lò xo bị nén lại, piston ngâm trong xi-lanh dầu tạo ra lực cản tới hạn giúp khung xe dập tắt chấn động ngay lập tức, người ngồi không bị say sóng do nhấp nhô liên tục.
3. **Lực cản quá lớn (Overdamped):**  
   * Vật chuyển động rất chậm chạp, ì ạch trở về vị trí cân bằng (đường màu đỏ thẫm).  
   * *Ứng dụng:* **Tay co thủy lực đóng cửa tự động**. Khi ta thả cửa, dầu bên trong hãm cửa lại, khiến cửa khép vào từ từ êm ái mà không bị giật đập mạnh làm vỡ kính.

---

### 4. Dao Động Cưỡng Bức & Hiện Tượng Cộng Hưởng Cơ Học

Nếu muốn duy trì dao động cho chiếc xích đu hay con lắc đồng hồ, ta phải tác dụng vào nó một ngoại lực tuần hoàn $F(t) = F_0 \cos(\Omega t)$.

1. **Đặc điểm của Dao động Cưỡng bức:**  
   * Sau giai đoạn quá độ ban đầu, hệ sẽ dao động ổn định với **tần số bằng đúng tần số $\Omega$ của ngoại lực**, không còn dao động với tần số riêng $\omega_0$ nữa.  
   * Biên độ của dao động cưỡng bức phụ thuộc vào:  
     - Biên độ ngoại lực $F_0$.  
     - Lực cản của môi trường.  
     - **Độ chênh lệch giữa tần số ngoại lực $\Omega$ và tần số riêng $\omega_0$:** Ngoại lực có tần số càng gần $\omega_0$ thì truyền năng lượng cho hệ càng hiệu quả, biên độ dao động càng lớn.

2. **Hiện Tượng Cộng Hưởng (Resonance):**  
   Khi tần số ngoại lực xấp xỉ bằng tần số dao động riêng của hệ:
   $$\Omega \approx \omega_0$$
   Biên độ của dao động cưỡng bức đạt giá trị **cực đại**. Hiện tượng này gọi là **hiện tượng cộng hưởng cơ học**.

![Đường cong cộng hưởng biên độ: Biên độ vọt lên cực đại khi tần số ngoại lực trùng khớp với tần số riêng của hệ.](figures/fig1_6_resonance.png)

> 🔍 **DẪN DẮT MẮT ĐỌC (Hình 1.6):**  
> * Tại vị trí $\Omega/\omega_0 = 1.0$ (trục dọc đứt nét ở giữa): Mọi đường cong biên độ đều đạt đỉnh nhọn cực đại.  
> * **Đường màu đỏ (Lực cản rất nhỏ):** Đỉnh cộng hưởng vọt lên rất cao và nhọn hoắt. Hệ hấp thụ năng lượng mãnh liệt.  
> * **Đường màu xanh navy (Lực cản lớn):** Đỉnh thoai thoải, biên độ không tăng vọt quá nhiều.

#### Lợi Ích & Tác Hại của Cộng Hưởng Trong Đời Sống
* **Mặt có lợi:**  
  - Hộp đàn guitar, violin được thiết kế để cộng hưởng với các nốt nhạc từ dây đàn, làm âm thanh phát ra to, ấm và vang xa.  
  - Hiện tượng chọn sóng trong đài radio, máy thu thanh: chỉnh núm xoay để tần số riêng của mạch dao động trùng với tần số đài phát cần nghe.
* **Mặt có hại (Hiểm họa công trình):**  
  - Nếu một đoàn quân bước đều qua cầu, tần số bước chân tình cờ trùng với tần số rung riêng của cây cầu, cầu có thể rung lắc dữ dội và gãy sập (tai nạn sập cầu treo Broughton năm 1831). Do đó, quân đội luôn có lệnh *"phải đi bước tự do khi qua cầu"*.  
  - Gió bão thổi tạo ra các luồng xoáy khí có tần số khớp với tần số xoắn của cây cầu Tacoma Narrows (Mỹ, năm 1940) đã khiến cây cầu thép khổng lồ uốn éo như dải lụa rồi đổ sụp hoàn toàn xuống biển.

---

### 5. Bài Toán Tính Số Thực Tế 1.3

> **Bài toán:** Một người có khối lượng $M = 60\text{ kg}$ ngồi trên một chiếc xe máy đi qua một đoạn đường mấp mô có các gờ giảm tốc cách đều nhau những khoảng $d = 8.0\text{ m}$. Toàn bộ khối lượng của người và xe đè lên hệ thống lò xo giảm xóc là $m_{tổng} = 160\text{ kg}$. Hệ thống lò xo có độ cứng tương đương $k = 40,000\text{ N/m}$.  
> 1. Tính tần số dao động riêng $f_0$ của hệ thống xe và người.  
> 2. Người lái xe chạy với vận tốc $v$ bằng bao nhiêu thì xe bị xóc nảy mạnh nhất (hiện tượng cộng hưởng)?
> 
> **Lời giải chi tiết:**  
> 1. **Tần số dao động riêng của xe:**  
>    * Tần số góc riêng:  
>      $$\omega_0 = \sqrt{\frac{k}{m_{tổng}}} = \sqrt{\frac{40000}{160}} = \sqrt{250} \approx 15.81\text{ rad/s}$$  
>    * Tần số riêng:  
>      $$f_0 = \frac{\omega_0}{2\pi} = \frac{15.81}{2\pi} \approx 2.52\text{ Hz}$$  
> 2. **Tìm vận tốc gây cộng hưởng mạnh nhất:**  
>    * Khi xe chạy với vận tốc $v$ qua các gờ cách nhau khoảng $d$, thời gian giữa hai lần xe va vào gờ liên tiếp là chu kỳ kích thích của ngoại lực:  
>      $$T_{ngoại lực} = \frac{d}{v}$$  
>    * Tần số kích thích của ngoại lực tác dụng lên xe:  
>      $$f_{ngoại lực} = \frac{1}{T_{ngoại lực}} = \frac{v}{d}$$  
>    * Hiện tượng cộng hưởng xảy ra mạnh nhất khi tần số va đập bằng tần số dao động riêng của xe:  
>      $$f_{ngoại lực} = f_0 \iff \frac{v}{d} = f_0 \implies v = d \cdot f_0$$  
>    * Thay số:  
>      $$v = 8.0\text{ m} \times 2.52\text{ Hz} = 20.16\text{ m/s}$$  
>      Đổi sang $\text{km/h}$:  
>      $$v = 20.16 \times 3.6 \approx 72.6\text{ km/h}$$  
>    * *Bài học thực tế:* Nếu chạy xe máy ở tốc độ khoảng $70 - 75\text{ km/h}$ qua đoạn đường có các gờ này, xe sẽ bị chấn động dữ dội và mất lái nguy hiểm do cộng hưởng. Để an toàn, người lái xe phải giảm tốc độ xuống dưới $30\text{ km/h}$ hoặc vượt hẳn ra ngoài dải tốc độ nguy hiểm trên.

---

## TỔNG KẾT BẢN CHẤT CHƯƠNG 1 (Takeaway Map)

1. **Phương trình dao động:** $x = A\cos(\omega t + \varphi)$.
2. **Mối quan hệ đạo hàm:** $v = x'$ (sớm pha $\pi/2$), $a = v' = -\omega^2 x$ (ngược pha $\pi$).
3. **Hệ thức độc lập:** $\left(\frac{x}{A}\right)^2 + \left(\frac{v}{\omega A}\right)^2 = 1 \iff x^2 + \frac{v^2}{\omega^2} = A^2$.
4. **Nguồn gốc lực:** Lực hồi phục $F = -kx$ luôn hướng về vị trí cân bằng, giải thích bản chất vì sao đáy chảo trũng sinh ra dao động điều hòa.
5. **Cơ năng bảo toàn:** $W = W_d + W_t = \frac{1}{2}kA^2 = \text{const}$. Động năng và thế năng chuyển hóa cho nhau với tần số góc $2\omega$.
6. **Thực tế:** Ma sát làm dao động tắt dần (biên độ giảm dần do sinh nhiệt). Ngoại lực tuần hoàn gây ra dao động cưỡng bức, biên độ đạt đỉnh khi có cộng hưởng ($\Omega \approx \omega_0$).
