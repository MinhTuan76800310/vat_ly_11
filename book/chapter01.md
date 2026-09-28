# CHƯƠNG 1: DAO ĐỘNG ĐIỀU HÒA
## BẢN CHẤT VẬT LÍ, NỀN TẢNG TOÁN HỌC & ĐỐI CHIẾU SGK "KẾT NỐI TRI THỨC VỚI CUỘC SỐNG"

---

> 📚 **ĐỐI CHIẾU CHƯƠNG TRÌNH SGK KẾT NỐI TRI THỨC VỚI CUỘC SỐNG (VẬT LÍ 11):**  
> Chương này được thiết kế như một tài liệu đồng hành chuyên sâu, soi sáng bản chất và giải mã toàn bộ các bài học trong **Chương 1: Dao động** của SGK Kết nối tri thức:  
> * **Chủ đề 1 (Bài 1, 2, 3, 4 KNTT):** Mô tả dao động điều hòa, Động học giải tích ($x, v, a$), Độ lệch pha ($\Delta \varphi$) & Đồ thị trạng thái.  
> * **Chủ đề 2 (Bài 1, 5, 7 KNTT):** Động lực học con lắc lò xo, con lắc đơn & Sự chuyển hóa năng lượng ($W_đ, W_t, W$).  
> * **Chủ đề 3 (Bài 6 KNTT):** Dao động tắt dần, Dao động duy trì, Dao động cưỡng bức & Hiện tượng cộng hưởng.

---

## 📐 HỘP CÔNG CỤ TOÁN 11 DÙNG TRONG CHƯƠNG: BẢN CHẤT ĐẠO HÀM & LƯỢNG GIÁC TRỰC QUAN

> Để không bị rơi vào lối học vẹt công thức, các em cần hiểu rõ bản chất của công cụ Toán học lớp 11 mà các nhà vật lý sử dụng để mô tả thế giới: từ tốc độ biến thiên tức thời (đạo hàm) đến ý nghĩa hình học của hàm lượng giác trên đường tròn.

### 1. Đạo hàm thực chất là gì? (Tốc độ thay đổi của một đại lượng theo thời gian)
* **Từ tốc độ trung bình đến tốc độ tức thời:**  
  Khi một vật di chuyển trên quãng đường $s$ trong khoảng thời gian $\Delta t$, đại lượng thể hiện **quãng đường thay đổi theo thời gian** là tốc độ trung bình:
  $$v_{tb} = \frac{\Delta s}{\Delta t}$$
  Nhưng nếu chiếc xe máy tăng ga vọt lên, vận tốc tại đúng thời khắc các em liếc nhìn vào đồng hồ đo tốc độ (vận tốc tức thời) là bao nhiêu?  
  Ta cho khoảng thời gian $\Delta t$ co lại cực ngắn ($\Delta t \to 0$). Khi đó, tỉ số $\frac{\Delta s}{\Delta t}$ tiến dần tới một giá trị giới hạn xác định, gọi là **Đạo hàm của quãng đường theo thời gian**:
  $$v(t) = \lim_{\Delta t \to 0} \frac{\Delta s}{\Delta t} = s'(t) = \frac{ds}{dt}$$
  *Ý nghĩa hình học (Hình 1.0a):* Vận tốc tức thời $v(t)$ chính là **độ dốc (hệ số góc $\tan\theta$) của tiếp tuyến** với đồ thị quãng đường - thời gian tại thời điểm đó! Đồ thị càng dốc đứng, vật chạy càng nhanh; đồ thị nằm ngang, vật đứng yên tức thời.

* **Gia tốc $a$ — Tốc độ thay đổi của vận tốc:**  
  Tương tự, vận tốc cũng có thể tăng nhanh hoặc giảm chậm theo thời gian. Đại lượng thể hiện **vận tốc thay đổi theo thời gian** chính là gia tốc:
  $$a(t) = \lim_{\Delta t \to 0} \frac{\Delta v}{\Delta t} = v'(t) = s''(t) = \frac{dv}{dt}$$
  Gia tốc chính là đạo hàm của vận tốc (hoặc đạo hàm cấp hai của quãng đường / li độ theo thời gian).

* **Bảng giải mã nguồn gốc các ký hiệu viết tắt quốc tế:**  
  Các ký hiệu trong sách giáo khoa không phải ngẫu nhiên, mà bắt nguồn từ các từ tiếng Anh và tiếng Latinh:
  * **$t$** = **Time** *(Thời gian)*.  
  * **$s$** = **Spatium** *(Tiếng Latinh nghĩa là khoảng cách, không gian; tiếng Anh: Space / Distance)*.  
  * **$x$** = **Coordinate** *(Tọa độ / Li độ dọc theo trục $Ox$)*.  
  * **$v$** = **Velocity** *(Vận tốc - tốc độ đổi vị trí theo thời gian)*.  
  * **$a$** = **Acceleration** *(Gia tốc - tốc độ đổi vận tốc theo thời gian)*.  
  * **$m$** = **Mass** *(Khối lượng)*.  
  * **$F$** = **Force** *(Lực)*.  
  * **$A$** = **Amplitude** *(Biên độ dao động - độ dời cực đại)*.  
  * **$\omega$** = Chữ cái Hy Lạp **Omega** *(Tần số góc - tốc độ quét góc pha)*.  
  * **$T$** = **Time Period** *(Chu kì dao động)*.  
  * **$f$** = **Frequency** *(Tần số)*.  
  * **$W$** = **Work / Energy** *(Công, năng lượng; $W_đ$: Động năng, $W_t$: Thế năng, $W$: Cơ năng)*.

![Hình 1.0a: Bản chất hình học của đạo hàm: Cát tuyến $PQ$ thể hiện tốc độ trung bình, khi $\Delta t \to 0$ sẽ tiệm cận về tiếp tuyến tại $P$, có độ dốc $\tan\theta = s'(t_0)$ biểu diễn vận tốc tức thời.](figures/fig1_0a_derivative.png)

### 2. Chuyến Tàu Lượn Trên Sóng Cosin: Hành Trình Khám Phá Đạo Hàm Lượng Giác & Nhân Tử $\omega$

#### Bước chuyển từ Mục 1: Đặt vấn đề tìm quy luật vận tốc
Ở **Mục 1**, chúng ta đã rút ra kết luận cốt lõi:
> **Vận tốc tức thời chính là đạo hàm của li độ theo thời gian: $v(t) = x'(t)$**, và về mặt hình học, nó chính là **độ dốc (hệ số góc của tiếp tuyến)** của đồ thị $x(t)$ tại thời điểm đó!

Bây giờ, trong dao động điều hòa, li độ biến thiên tuần hoàn theo thời gian dưới dạng hàm cosin cơ bản:
$$x(t) = \cos(t)$$
Câu hỏi tự nhiên được đặt ra: **Vận tốc $v(t) = [\cos(t)]'$ sẽ có công thức giải tích là gì?**

Chúng ta chưa hề biết trước công thức đạo hàm của hàm cosin, nhưng chúng ta đã có công cụ trực quan mạnh mẽ từ Mục 1: **Hãy đóng vai người ngồi trên toa tàu lượn siêu tốc chạy trên đường ray $x(t) = \cos(t)$ và đo độ dốc tiếp tuyến qua từng chặng đường (Hình 1.0b(a))!**

---

#### Hành trình 4 trạng thái: Lật mở dấu của đạo hàm

* **Trạng thái 1 — Đỉnh đồi cao nhất ($t = 0, x = +1$):**  
  Toa tàu vừa leo lên chóp đỉnh cao nhất. Tại đúng thời khắc này, xe tạm dừng dâng cao để chuẩn bị đổi chiều lao xuống. Đường ray tại đỉnh nằm ngang phẳng lì $\implies$ **Độ dốc bằng $0$**.  
  - Như vậy: $x'(0) = 0$ (vận tốc tức thời tại biên bằng $0$).  
  - Nhìn lại kho tàng các hàm lượng giác quen thuộc ở lớp 10, hàm số nào cũng triệt tiêu về $0$ khi $t = 0$? Đó chính là hàm $\sin(t)$, vì $\sin(0) = 0$!  
  - ⚠️ **Khoan đã, hãy dừng lại suy ngẫm:** Liệu đạo hàm là $+\sin(t)$ hay $-\sin(t)$?  
    Vì $(+\sin 0) = 0$ mà $(-\sin 0)$ cũng bằng $0$, **nên tại đỉnh đồi, chúng ta hoàn toàn CHƯA THỂ BIẾT được dấu của kết quả đạo hàm!** Dấu của đạo hàm vẫn là một ẩn số lớn đang chờ được giải mã ở chặng tiếp theo.

* **Trạng thái 2 — Rời đỉnh, đổ đèo qua Vị trí Cân bằng ($t = \frac{\pi}{2}, x = 0$) — Khoảnh khắc lật mở dấu trừ:**  
  Rời khỏi đỉnh đồi, xe bắt đầu lao dốc, độ cao giảm dần theo thời gian. Mũi xe chúi xuống dưới, tiếp tuyến nghiêng dốc xuống $\implies$ **Độ dốc tiếp tuyến chắc chắn phải mang dấu ÂM!**  
  Đặc biệt, tại đúng thời điểm $t = \frac{\pi}{2}$ khi xe quét qua vị trí cân bằng $x = 0$, đường ray dốc đứng cắm đầu với góc nghiêng $-45^\circ$, độ dốc đạt cực tiểu âm: **$-1$**.  
  Bây giờ, hãy thử đối chiếu với hai khả năng dấu:  
  - *Nếu đạo hàm là $+\sin(t)$:* Tại $t = \frac{\pi}{2}$, ta có $+\sin(\frac{\pi}{2}) = +1$ (mang dấu Dương). Điều này **mâu thuẫn hoàn toàn** với thực tế toa xe đang lao dốc cắm đầu (độ dốc âm)!  
  - *Nếu đạo hàm là $-\sin(t)$:* Tại $t = \frac{\pi}{2}$, ta có $-\sin(\frac{\pi}{2}) = -1$ (mang dấu Âm). Điều này **khớp tuyệt đối** với độ dốc $-1$ của đường ray!  
  > 🎯 **Phát hiện mang tính bước ngoặt:** Chính cú đổ đèo qua vị trí cân bằng đã vén màn bí mật: Đạo hàm của hàm cosin **bắt buộc phải có dấu trừ đằng trước**:  
  > $$[\cos(t)]' = -\sin(t)$$

* **Trạng thái 3 — Dưới đáy vực sâu nhất ($t = \pi, x = -1$):**  
  Toa tàu chạm tới đáy vực thung lũng. Tại đáy, xe ngừng hạ độ cao, chuẩn bị vòng lên. Đường ray lại nằm ngang phẳng lì $\implies$ **Độ dốc bằng $0$**.  
  - Kiểm chứng công thức vừa tìm được: $-\sin(\pi) = 0$. Hoàn toàn khớp với thực tế $v = 0$ tại biên âm!

* **Trạng thái 4 — Vọt ngược lên trời qua Vị trí Cân bằng ($t = \frac{3\pi}{2}, x = 0$):**  
  Toa tàu lấy đà phi ngược lên dốc nhất, tiếp tuyến nghiêng $+45^\circ$ hướng lên trời $\implies$ **Độ dốc đạt cực đại dương: $+1$**.  
  - Kiểm chứng công thức: $-\sin(\frac{3\pi}{2}) = -(-1) = +1$. Hoàn toàn chính xác!

---

#### Bí mật "Cỗ máy nén thời gian": Vì sao lại xuất hiện nhân tử $\omega$?

Ở Mục 1, ta đã định nghĩa $\omega$ là **tần số góc** (tốc độ biến thiên của góc pha theo thời gian). Giờ đây, xét hàm dao động tổng quát: $x(t) = \cos(\omega t)$.  
Tại sao đạo hàm của nó không chỉ đơn giản là $-\sin(\omega t)$ mà lại xuất hiện thêm nhân tử $\omega$: $-\omega \sin(\omega t)$?

Hãy quan sát **Hình 1.0b(b)**:
* Khi $\omega = 1$: Sóng uốn lượn thong thả với chu kì $T = 2\pi$. Xe đi từ đỉnh ($x = 1$) về vị trí cân bằng ($x = 0$) mất khoảng thời gian $\Delta t = \frac{\pi}{2}$, độ dốc tại VTCB là $-1$.
* Khi $\omega = 2$: Tần số dao động tăng gấp đôi, chu kì bị **nén co hẹp lại chỉ còn một nửa** ($T = \pi$). Xe đi từ đỉnh về VTCB bị rút ngắn thời gian chỉ còn $\Delta t = \frac{\pi}{4}$!
* Nhưng hãy chú ý: **Độ cao của đỉnh đồi (biên độ $A$) vẫn giữ nguyên!**
* Cùng phải vượt qua độ cao $A = 1$, nhưng thời gian di chuyển bị ép ngắn lại gấp đôi, buộc sườn đồi phải **dựng đứng gấp đôi**!
* Vì độ dốc tiếp tuyến tại mọi thời điểm bị khuếch đại lên đúng $\omega$ lần, tốc độ biến thiên tức thời (đạo hàm) tại VTCB vọt từ $-1$ lên thành $-\omega = -2$:
  $$[\cos(\omega t + \varphi)]' = -\omega \sin(\omega t + \varphi)$$
  $$[\sin(\omega t + \varphi)]' = \omega \cos(\omega t + \varphi)$$

![Hình 1.0b: Storytelling Đạo hàm lượng giác: (a) Hành trình 4 trạng thái của toa tàu lượn lật mở dấu trừ $[\cos(t)]' = -\sin(t)$; (b) Hiệu ứng nén thời gian của tần số góc $\omega$ làm sườn đồ thị dựng đứng gấp $\omega$ lần.](figures/fig1_0b_omega_derivative.png)

### 3. Ba Vệ Tinh Trên Chiếc Đồng Hồ Vũ Trụ: Giải Mã Các Cung Lượng Giác & Hệ Thức Độc Lập

#### Mối nối từ Mục 1 & Mục 2: Nghịch lý về dạng hàm của $x, v, a$
Sau khi đã làm chủ đạo hàm ở Mục 1 và Mục 2, ta thiết lập được bộ ba phương trình động học mô tả dao động điều hòa:
$$\begin{cases} 
x(t) = A\cos(\omega t + \varphi) \\ 
v(t) = x'(t) = -\omega A \sin(\omega t + \varphi) \\ 
a(t) = v'(t) = -\omega^2 A \cos(\omega t + \varphi) 
\end{cases}$$

Đến đây, học sinh thường gặp phải hai rào cản lớn trong các bài kiểm tra:
1. **Rào cản so sánh pha:** Li độ $x$ là hàm $\cos$, nhưng vận tốc $v$ lại là $-\sin$, còn gia tốc $a$ lại là $-\cos$. Làm thế nào để đưa tất cả về cùng chuẩn hàm $\cos$ nhằm biết chính xác ai sớm pha, ai trễ pha hơn ai?
2. **Rào cản khử thời gian:** Trong thực tế thí nghiệm, người ta thường đo đồng thời li độ $x$ và vận tốc $v$ tại một vị trí bất kì. Làm sao để tìm hệ thức liên hệ trực tiếp giữa $x$ và $v$ mà không cần biết thời gian $t$?

SGK Kết nối tri thức giải quyết bằng các công thức biến đổi lượng giác:
$$\cos\left(\alpha + \frac{\pi}{2}\right) = -\sin\alpha, \quad \cos(\alpha + \pi) = -\cos\alpha, \quad \cos^2\alpha + \sin^2\alpha = 1$$

Thay vì bắt trí não phải học vẹt những công thức khô khan này, các em hãy theo dõi **cuộc rượt đuổi của 3 vệ tinh trên chiếc đồng hồ vũ trụ bán kính $R = 1$ (Hình 1.0c)**:

* **Trạng thái 1 (Hình 1.0c - Trái): Vệ tinh Li độ $\vec{u}_1$ & Bản giao hưởng Pythagoras**  
  Xét một kim đồng hồ vũ trụ (véc-tơ $\vec{u}_1$) dài $R = 1$, đang chỉ góc $\alpha = \omega t + \varphi$.
  - Chiếu bóng của $\vec{u}_1$ xuống sàn nằm ngang (trục $\cos$): ta thu được **Li độ chuẩn hóa** $\cos\alpha = \frac{x}{A}$.  
  - Chiếu bóng của $\vec{u}_1$ lên vách thẳng đứng (trục $\sin$): ta thu được **Vận tốc chuẩn hóa** $\sin\alpha = -\frac{v}{\omega A}$.  
  - Hai bóng chiếu này cùng với véc-tơ $\vec{u}_1$ tạo thành một **tam giác vuông hoàn hảo** (tô màu xanh)!  
  - Áp dụng **Định lý Pythagoras** quen thuộc $(\text{cạnh kề}^2 + \text{cạnh đối}^2 = \text{cạnh huyền}^2)$:
    $$\cos^2\alpha + \sin^2\alpha = 1 \implies \left(\frac{x}{A}\right)^2 + \left(-\frac{v}{\omega A}\right)^2 = 1 \iff \left(\frac{x}{A}\right)^2 + \left(\frac{v}{\omega A}\right)^2 = 1$$
    *Bản chất sáng tỏ:* Hệ thức độc lập thời gian trong SGK thực chất chính là **Định lý Pythagoras phản chiếu lên quỹ đạo trạng thái**!

* **Trạng thái 2 (Hình 1.0c - Giữa): Vệ tinh Vận tốc $\vec{u}_2$ bứt phá chạy trước đúng một góc vuông $+90^\circ$ ($\frac{\pi}{2}$)**  
  Vận tốc là đại lượng báo trước sự thay đổi của li độ trong tương lai gần. Vì thế, vệ tinh vận tốc $\vec{u}_2$ luôn bay đón đầu trước vệ tinh li độ $\vec{u}_1$ đúng một góc vuông $+90^\circ$ ($\alpha + \frac{\pi}{2}$):  
  - Khi quay một góc vuông $+90^\circ$ ngược chiều kim đồng hồ, chiếc bóng thẳng đứng ban đầu ($\sin\alpha$) bị ngã ập xuống nằm ngang trên trục $\cos$.  
  - Nhưng vì quay sang góc phần tư thứ hai, bóng nằm ngang này rơi trúng vào nửa âm của trục hoành $\implies$ Hoành độ của $\vec{u}_2$ là $-\sin\alpha$:
    $$\cos\left(\alpha + \frac{\pi}{2}\right) = -\sin\alpha$$
  - Thay thế vào phương trình vận tốc:
    $$v(t) = -\omega A \sin(\omega t + \varphi) = \omega A \cos\left(\omega t + \varphi + \frac{\pi}{2}\right)$$
  - *Ý nghĩa vật lý trực quan:* **Vận tốc $v$ luôn sớm pha $\frac{\pi}{2}$ so với li độ $x$!** Khi li độ mới vừa tới vị trí cân bằng ($x = 0$), thì vận tốc đã sớm cán đích cực đại ($v = v_{\max}$).

* **Trạng thái 3 (Hình 1.0c - Phải): Vệ tinh Gia tốc $\vec{u}_3$ đối đầu đối diện trọn vẹn nửa vòng tròn $+180^\circ$ ($\pi$)**  
  Theo định luật II Newton, gia tốc luôn cùng hướng với lực kéo về ($F_{kv} = ma$). Khi vật lệch sang phải, lực giật mạnh sang trái để kéo vật về. Vì thế, vệ tinh gia tốc $\vec{u}_3$ luôn bay đối đầu trực diện, đi trước $\vec{u}_1$ trọn vẹn nửa vòng tròn $+180^\circ$ ($\alpha + \pi$):  
  - Phép quay $+180^\circ$ đưa véc-tơ sang vị trí đối xứng xuyên tâm qua gốc tọa độ $O$. Chiếc bóng trên trục hoành bị lật ngược chiều $180^\circ$:
    $$\cos(\alpha + \pi) = -\cos\alpha$$
  - Thay thế vào phương trình gia tốc:
    $$a(t) = -\omega^2 A \cos(\omega t + \varphi) = \omega^2 A \cos(\omega t + \varphi + \pi) = -\omega^2 x(t)$$
  - *Ý nghĩa vật lý trực quan:* **Gia tốc $a$ luôn ngược pha $\pi$ so với li độ $x$!** Khi li độ đạt cực đại dương ở biên phải ($x = +A$), gia tốc lập tức đạt giá trị cực tiểu âm ($a = -\omega^2 A$) để giằng vật trở lại.

![Hình 1.0c: Storytelling 3 Vệ tinh trên vòng tròn đơn vị: (a) Trạng thái 1: Vệ tinh Li độ $\vec{u}_1$ & Tam giác Pythagoras chứng minh hệ thức độc lập thời gian; (b) Trạng thái 2: Vệ tinh Vận tốc $\vec{u}_2$ bứt phá trước $+90^\circ$ ($\frac{\pi}{2}$); (c) Trạng thái 3: Vệ tinh Gia tốc $\vec{u}_3$ đối đầu $+180^\circ$ ($\pi$).](figures/fig1_0c_trig_circle.png)

---

# PHẦN 1: MÔ TẢ DAO ĐỘNG ĐIỀU HÒA, ĐỘNG HỌC & ĐỘ LỆCH PHA
*(Đối chiếu và giải mã chuyên sâu Bài 1, 2, 3, 4 SGK Kết nối tri thức với cuộc sống)*

---

### 1. Bí Ẩn Bản Chất: Tại Sao Chuyển Động Thẳng Qua Lại Lại Mang Dáng Dấp Hàm Cosin?

#### Nghịch lý trực giác từ đời sống (Tầng 1 Sư phạm)
Trong cuộc sống hàng ngày, chúng ta liên tục bắt gặp những chuyển động lặp đi lặp lại quanh một vị trí đứng yên:
* Chiếc xích đu đung đưa nhịp nhàng dưới tán cây sân trường.
* Màng loa điện thoại rung động bần bật để phát ra âm thanh bản nhạc yêu thích.
* Chiếc phao câu cá dập dềnh lên xuống theo từng gợn sóng nước.
* Nhánh âm thoa kim loại rung vo ve sau khi được gõ nhẹ.

Những chuyển động có giới hạn trong không gian, lặp đi lặp lại nhiều lần quanh một **vị trí cân bằng** xác định như vậy được gọi là **dao động cơ học**. Nếu sau những khoảng thời gian bằng nhau vật lại trở về trạng thái chuyển động cũ, dao động đó là **dao động tuần hoàn**.

Đến đây, SGK đưa ra một định nghĩa mang tính kinh điển:
> **Định nghĩa SGK (Bài 1 KNTT):** *Dao động điều hòa là dao động trong đó li độ của vật là một hàm cosin (hoặc sin) của thời gian:*
> $$x(t) = A\cos(\omega t + \varphi)$$

**Một câu hỏi hóc búa được đặt ra:**  
*Hãy nhìn vào chiếc màng loa điện thoại: nó chỉ chuyển động thụt thò tịnh tiến theo một đường thẳng! Chiếc xích đu cũng chỉ lắc tới lắc lui trên một đoạn cong hẹp. Chúng KHÔNG HỀ QUAY TRÒN! Vậy tại sao các nhà vật lý lại mô tả một chuyển động qua lại thẳng tắp bằng hàm $\cos(\omega t + \varphi)$ — một hàm số vốn sinh ra từ góc quay của đường tròn? Có phải vật đang "quay tròn ngầm" ở đâu đó không?*

---

#### Tháo gỡ nghịch lý: Từ Lực kéo về đến "Siêu năng lực" của Đạo hàm (Tầng 2 & 3)
Trong SGK lớp 11, để giúp các em làm quen với hàm cosin ngay từ đầu năm học khi **chưa học đạo hàm ở môn Toán**, các thầy cô tạm thời sử dụng mô hình: *"Li độ của dao động điều hòa giống như bóng của một điểm chuyển động tròn đều in xuống đường kính"*. Đây là một cách tiếp cận trực quan cơ học, nhưng nó chỉ là **hình ảnh phản chiếu**, chưa phải là **nguyên nhân vật lý gốc rễ**!

Bản chất vật lý đích thực không cần bất kỳ chuyển động tròn nào, mà bắt nguồn từ quy luật của **Lực kéo về (Lực hồi phục)**:
1. Mỗi khi vật bị lệch khỏi vị trí cân bằng bền, môi trường xung quanh (lò xo, trọng lực, lực căng mặt ngoài) lập tức xuất hiện một lực kéo vật trở về.
2. Vật càng lệch xa khỏi vị trí cân bằng, lực kéo về càng gồng mạnh lên để giằng vật lại. Lực này tỉ lệ thuận với độ lệch nhưng luôn ngược hướng lệch:
   $$F_{kv} = -kx$$
3. Theo **Định luật II Newton** ($F = ma$), lực này ép gia tốc của vật phải luôn trái dấu và tỉ lệ thuận với li độ:
   $$a(t) = -\omega^2 x(t)$$
4. Bây giờ, hãy mở lại **Hộp công cụ Toán (Mục 1 & 2)** mà chúng ta vừa trang bị: Gia tốc chính là đạo hàm cấp hai của li độ: $a(t) = x''(t)$. Như vậy, quy luật lực tự nhiên bắt buộc hàm số $x(t)$ phải thỏa mãn phương trình:
   $$x''(t) = -\omega^2 x(t)$$

> 🎯 **Lời giải cho bí ẩn:**  
> Trong toàn bộ kho tàng các hàm số toán học (hàm đa thức, hàm mũ, hàm logarit), **chỉ có duy nhất hàm lượng giác $\cos$ và $\sin$ mới sở hữu "siêu năng lực": lấy đạo hàm hai lần thì quay trở lại đúng chính nó nhưng đổi dấu trừ!**  
> Chính quy luật lực kéo về trong tự nhiên đã "chọn" hàm cosin để vẽ nên quỹ đạo của dao động điều hòa, chứ không hề có bàn tay ma thuật nào bắt vật phải "quay tròn ngầm"!

![Hình 1.1a: Cơ chế vật lý và bản chất toán học của dao động điều hòa: (a) Lực kéo về $\vec{F}_{kv}$ của lò xo luôn có xu hướng giằng vật trở về vị trí cân bằng bền $O$; (b) Đồ thị $F_{kv} = -kx$ luôn ngược dấu với li độ, chứng minh phương trình động lực học $x''(t) = -\omega^2 x(t)$ bắt buộc nghiệm phải có dạng sóng lượng giác cosin.](figures/fig1_1a_restoring_force.png)

*Câu hỏi mở dẫn dắt sang Mục 2:*  
Một khi quy luật lực tự nhiên đã trao cho dao động bản mệnh hàm cosin $x(t) = A\cos(\omega t + \varphi)$, câu hỏi tiếp theo đặt ra: *Làm thế nào để ta đọc vị được toàn bộ thông số của chuyển động này ngoài đời thực? Mỗi kí hiệu $A, \omega, T, f, \varphi$ đại diện cho thực thể vật lý sống động nào?*

---

### 2. Giải Mã Bộ Mã Gen ADN Của Phương Trình Dao Động: Cuộc Giải Phẫu Chuyển Động
*(Trọng tâm Bài 2 SGK Kết nối tri thức)*

#### Bước chuyển từ Mục 1: Đọc vị từng thông số nhận dạng
Ở **Mục 1**, chúng ta đã chứng minh phương trình dao động điều hòa mang dạng $x(t) = A\cos(\omega t + \varphi)$. Bây giờ, hãy đóng vai một nhà vật lý thực nghiệm đứng trước một hệ dao động (như màng loa hay con lắc). Để kiểm soát và mô tả trọn vẹn chuyển động, chúng ta cần giải mã 6 thông số cấu thành — tựa như 6 đoạn gen ADN định danh trạng thái:

#### 1. Biên độ $A$ & Chiều dài quỹ đạo $L = 2A$ — "Bức tường biên giới"
Vật không thể văng ra xa mãi mãi. Khi vật chuyển động rời xa vị trí cân bằng, lực kéo về $F_{kv} = -kx$ gồng lên ngày một mạnh để hãm phanh. Cho đến một thời điểm, toàn bộ động năng của vật cạn kiệt, vật khựng lại tức thời ($v = 0$) để quay đầu.
* Vị trí xa nhất mà vật có thể vươn tới so với vị trí cân bằng được gọi là **Biên độ dao động $A$**. Vì là một khoảng cách hình học cực đại, **$A$ luôn luôn là một hằng số dương ($A > 0$)**. Đơn vị chuẩn là mét ($\text{m}$) hoặc xentimét ($\text{cm}$).
* Toàn bộ chuyển động của vật bị giam hãm giữa hai mép biên: mép biên âm ($-A$) và mép biên dương ($+A$). Đoạn thẳng nối liền hai mép biên này chính là **Chiều dài quỹ đạo chuyển động**:
  $$L = 2A$$
  *(Học sinh cần ghi nhớ sâu sắc: Chiều dài quỹ đạo luôn gấp đôi biên độ, $L = 2A$, tuyệt đối không nhầm $L = A$!)*

#### 2. Chu kì $T$ & Tần số $f$ — "Nhịp tim thời gian"
Sau khi đã giới hạn được không gian bằng $A$, ta bắt đầu bấm giờ để đo tốc độ lặp lại của chuyển động:
* **Chu kì $T$ (giây - $\text{s}$):** Ta cầm đồng hồ bấm giây và đo khoảng thời gian ngắn nhất để vật thực hiện trọn vẹn một dao động toàn phần (nghĩa là đi hết một vòng và trở lại đúng vị trí cũ theo đúng chiều chuyển động cũ).
* **Tần số $f$ ($\text{Hertz} - \text{Hz}$):** Với những vật dao động chớp nhoáng như màng loa hay dây đàn guitar, một chu kì $T$ diễn ra chỉ trong vài phần nghìn giây, mắt người không thể bấm từng nhịp. Khi đó, ta đếm xem trong trọn vẹn 1 giây tích tắc, vật thực hiện được bao nhiêu dao động toàn phần:
  $$f = \frac{1}{T}$$
  *Ví dụ đời sống:* Dây đàn piano phát ra nốt La chuẩn có tần số $f = 440\text{ Hz}$, nghĩa là trong mỗi giây đồng hồ gõ nhịp, dây đàn và khối không khí xung quanh nó đã kịp rung đúng $440$ nhịp toàn phần!

#### 3. Tần số góc $\omega$ — "Chiếc cầu nối giữa Thời gian và Góc lượng giác"
Đến đây, một nút thắt nhận thức thường khiến học sinh băn khoăn: *Tại sao đã có chu kì $T$ và tần số $f$ rồi, các nhà vật lý lại phải đẻ thêm đại lượng tần số góc $\omega = 2\pi/T = 2\pi f$ cho phức tạp?*
* Lời giải đáp nằm ở "khẩu vị toán học" của hàm cosin: **Hàm lượng giác không thể tiếp nhận biến số thời gian tính bằng giây ($s$)!** Bạn không thể ấn máy tính $\cos(3\text{ giây})$. Bên trong ruột của hàm cosin bắt buộc phải là một **góc** tính bằng radian ($\text{rad}$).
* Cứ sau đúng một chu kì $T$, trạng thái dao động lặp lại như cũ, tương ứng với việc điểm pha đã quét trọn vẹn một vòng tròn lượng giác $2\pi\text{ rad}$.
* Vì vậy, đại lượng đóng vai trò "tỉ giá hối đoái" để chuyển đổi từ thời gian trôi $t$ sang góc quét $\alpha$ chính là:
  $$\omega = \frac{2\pi}{T} = 2\pi f \quad (\text{đơn vị: rad/s})$$
* Đúng như chúng ta đã khám phá trong Hộp công cụ Toán (Mục 2), $\omega$ chính là **cỗ máy nén thời gian**: $\omega$ càng lớn, thời gian hoàn thành một chu kì càng bị nén ngắn lại, đồ thị càng dựng đứng dốc hơn và vật đổi chiều càng mãnh liệt!

#### 4. Pha ban đầu $\varphi$ — "Bức ảnh chụp thời khắc xuất phát"
Mốc thời gian $t = 0$ không phải do tự nhiên áp đặt, mà hoàn toàn do người làm thí nghiệm lựa chọn thời điểm bấm nút khởi động đồng hồ đo:
* Nếu tại thời điểm $t = 0$, ta kéo vật ra mép biên dương rồi buông tay: vật ở $x_0 = +A \implies \cos\varphi = 1 \implies \varphi = 0$.
* Nếu tại thời điểm $t = 0$, ta tác dụng lực đẩy vật từ vị trí cân bằng lao sang chiều dương: vật ở $x_0 = 0$ và đang tăng li độ $\implies \varphi = -\frac{\pi}{2}$.
* Như vậy, **Pha ban đầu $\varphi$** (thường chọn trong nửa khoảng $(-\pi, \pi]$) chính là "bức ảnh chụp đông kết" cho biết chính xác vị trí và xu hướng chuyển động của vật ở đúng thời khắc $t = 0$.

#### 5. Pha dao động $(\omega t + \varphi)$ — "Căn cước trạng thái toàn diện"
Tại bất kỳ thời điểm $t$ nào trong tương lai, biểu thức nằm trong ruột hàm cosin:
$$\Phi(t) = \omega t + \varphi$$
được gọi là **Pha dao động**. Đây là "tấm căn cước toàn năng": chỉ cần biết giá trị góc $\Phi(t)$, ta lập tức biết được:
* Vật đang ở tọa độ nào: Chiếu góc $\Phi$ lên trục hoành $\cos \implies x = A\cos\Phi$.
* Vật đang chuyển động theo chiều nào: Nhìn vào dấu của hàm $\sin\Phi$ $\implies$ nếu $\sin\Phi < 0$ thì vật đang đi theo chiều dương ($v > 0$), nếu $\sin\Phi > 0$ thì vật đang lao theo chiều âm ($v < 0$)!

![Hình 1.1b: Giải mã cấu trúc hình học (ADN) của hàm sóng cosin $x(t) = A\cos(\omega t + \varphi)$: Mối quan hệ trực quan giữa biên độ $A$, chiều dài quỹ đạo $L=2A$, chu kì $T$, tọa độ ban đầu $x_0 = A\cos\varphi$, và độ dốc tiếp tuyến (vận tốc) tại các mốc dao động then chốt.](figures/fig1_1b_cosine_anatomy.png)

*Câu hỏi mở dẫn dắt sang Mục 3:*  
Chúng ta đã kiểm soát trọn vẹn bộ mã gen ADN của MỘT dao động điều hòa độc lập. Nhưng trong thế giới tự nhiên và kỹ thuật, các dao động hiếm khi tồn tại cô độc: hai con lắc treo cạnh nhau, hai màng loa stereo trái - phải, hay sóng âm tiếng ồn và sóng âm phát ra từ tai nghe... *Khi hai dao động cùng tần số gặp nhau, điều gì quyết định chúng sẽ bắt tay tăng cường lẫn nhau hay đối đầu triệt tiêu lẫn nhau?*

---

### 3. Cuộc Rượt Đuổi Pha Của Hai Dao Động: Cùng Pha, Ngược Pha & Vuông Pha
*(Đối chiếu Bài 2 & Bài 4 KNTT)*

#### Bước chuyển từ Mục 2: Nhu cầu đo lường độ lệch nhịp
Ở **Mục 2**, chúng ta biết pha dao động $(\omega t + \varphi)$ xác định trạng thái tức thời. Khi có hai vật dao động điều hòa cùng tần số góc $\omega$:
$$x_1(t) = A_1 \cos(\omega t + \varphi_1), \quad x_2(t) = A_2 \cos(\omega t + \varphi_2)$$
Sự chênh lệch góc pha giữa hai dao động được đo bằng **Độ lệch pha**:
$$\Delta \varphi = \varphi_2 - \varphi_1$$
Độ lệch pha $\Delta\varphi$ là một hằng số không phụ thuộc vào thời gian $t$. Nó cho biết dao động này đang "chạy trước" hay "đuổi theo sau" dao động kia một khoảng cách góc là bao nhiêu. Tùy thuộc vào giá trị của $\Delta\varphi$, chúng ta có 3 kịch bản kinh điển:

---

#### 1. Hai dao động CÙNG PHA ($\Delta \varphi = 2k\pi$ với $k \in \mathbb{Z}$)
* **Hình ảnh đời sống:** Hai bạn ngồi trên hai chiếc xích đu đu song song chuẩn xác từng tích tắc: cùng vút lên đỉnh cao nhất, cùng hạ xuống vị trí thấp nhất, cùng lướt qua vị trí cân bằng theo cùng một hướng.
* **Bản chất giải tích:** Vì $\cos(\omega t + \varphi_2) = \cos(\omega t + \varphi_1)$, tỉ số li độ của hai vật luôn luôn dương và bằng đúng tỉ số hai biên độ:
  $$\frac{x_1(t)}{A_1} = \frac{x_2(t)}{A_2} \implies x_2(t) = \left(\frac{A_2}{A_1}\right) x_1(t)$$
* **Ý nghĩa hình học:** Trên hệ tọa độ $(x_1, x_2)$, đồ thị biểu diễn mối liên hệ giữa hai dao động là một **đoạn thẳng dốc lên** đi qua gốc tọa độ $O$ với hệ số góc dương.
* **Hệ quả vật lý:** Khi hai dao động cùng pha gặp nhau, chúng cộng hưởng tăng cường biên độ cực đại: $A_{tổng} = A_1 + A_2$.

#### 2. Hai dao động NGƯỢC PHA ($\Delta \varphi = (2k+1)\pi$ với $k \in \mathbb{Z}$)
* **Hình ảnh đời sống:** Hai chiếc xích đu đối đầu kịch liệt: khi bạn thứ nhất bay lên đỉnh cao nhất phía trước ($x_1 = +A_1$), thì bạn thứ hai giật lùi về điểm sâu nhất phía sau ($x_2 = -A_2$). Khi bạn này qua VTCB theo chiều dương thì bạn kia quét qua VTCB theo chiều âm.
* **Bản chất giải tích:** Vì $\cos(\omega t + \varphi_2) = -\cos(\omega t + \varphi_1)$, li độ hai vật luôn trái dấu nhau tại mọi thời điểm:
  $$\frac{x_1(t)}{A_1} = -\frac{x_2(t)}{A_2} \implies x_2(t) = -\left(\frac{A_2}{A_1}\right) x_1(t)$$
* **Ý nghĩa hình học:** Trên hệ tọa độ $(x_1, x_2)$, đồ thị là một **đoạn thẳng dốc xuống** đi qua gốc tọa độ $O$ với hệ số góc âm.
* **Ứng dụng công nghệ đột phá (Tai nghe chống ồn ANC):**  
  Đây chính là nguyên lý kỳ diệu của công nghệ chống ồn chủ động (Active Noise Cancelling - ANC) trên các dòng tai nghe hiện đại: Micro trên tai nghe thu nhận sóng âm tiếng ồn từ môi trường ($x_{ồn}$), chip xử lý âm thanh lập tức phát ra một sóng âm có cùng biên độ nhưng **ngược pha $180^\circ$ ($\pi$)**:
  $$x_{chống} = -x_{ồn} \implies x_{tổng} = x_{ồn} + x_{chống} = 0$$
  Hai sóng âm đập vào màng nhĩ triệt tiêu nhau hoàn toàn, tạo nên một không gian tĩnh lặng tuyệt đối giữa chốn ồn ào!

#### 3. Hai dao động VUÔNG PHA ($\Delta \varphi = (2k+1)\frac{\pi}{2}$ với $k \in \mathbb{Z}$)
* **Hình ảnh đời sống:** Đây là kịch bản "Kẻ khựng ở biên, người phóng qua đáy". Khi bạn thứ nhất vừa chạm mép biên và dừng lại đổi chiều ($x_1 = \pm A_1, v_1 = 0$), thì bạn thứ hai đang bay vun vút qua vị trí cân bằng với tốc độ xé gió ($x_2 = 0, |v_2| = v_{\max}$).
* **Bản chất giải tích:** Một bên là $\cos$, một bên là $\pm\sin$. Áp dụng định lý Pythagoras $\cos^2\alpha + \sin^2\alpha = 1$, ta triệt tiêu hoàn toàn biến thời gian $t$:
  $$\left(\frac{x_1}{A_1}\right)^2 + \left(\frac{x_2}{A_2}\right)^2 = 1$$
* **Ý nghĩa hình học:** Đồ thị biểu diễn mối quan hệ giữa $x_1$ và $x_2$ là một **đường Elip chuẩn mực** nhận gốc tọa độ $O$ làm tâm đối xứng!

| Trạng thái pha | Độ lệch pha $\Delta \varphi$ | Mối liên hệ giải tích | Dạng đồ thị tương quan $(x_1, x_2)$ | Ứng dụng & Hiện tượng tiêu biểu |
| :--- | :--- | :--- | :--- | :--- |
| **CÙNG PHA** | $\Delta \varphi = 2k\pi$ | $\frac{x_1}{A_1} = \frac{x_2}{A_2}$ | Đoạn thẳng dốc lên qua $O$ | Hai loa cộng hưởng tăng cường âm thanh |
| **NGƯỢC PHA** | $\Delta \varphi = (2k+1)\pi$ | $\frac{x_1}{A_1} = -\frac{x_2}{A_2}$ | Đoạn thẳng dốc xuống qua $O$ | Tai nghe chống ồn chủ động (ANC) |
| **VUÔNG PHA** | $\Delta \varphi = (2k+1)\frac{\pi}{2}$ | $\left(\frac{x_1}{A_1}\right)^2 + \left(\frac{x_2}{A_2}\right)^2 = 1$ | Đường Elip đối xứng qua $O$ | Tương quan giữa Li độ và Vận tốc |

![Hình 1.1c: So sánh trực quan 3 trạng thái lệch pha kinh điển giữa hai dao động: (a) Cùng pha ($\Delta\varphi = 0$); (b) Ngược pha ($\Delta\varphi = \pi$) với hiện tượng sóng triệt tiêu trong tai nghe ANC; (c) Vuông pha ($\Delta\varphi = \pi/2$) với quỹ đạo trạng thái elip đặc trưng.](figures/fig1_1c_phase_comparison.png)

*Câu hỏi mở dẫn dắt sang Mục 4:*  
Hiện tượng vuông pha và ngược pha ở trên là sự so sánh giữa HAI vật dao động khác nhau. Nhưng có bao giờ các em tự hỏi: *Ngay trong bản thân MỘT vật dao động duy nhất, vận tốc $v(t)$ và gia tốc $a(t)$ có quan hệ pha như thế nào với li độ $x(t)$? Tại sao khi vật dừng lại ở biên thì gia tốc lại đạt giá trị khổng lồ nhất?*

---

### 4. Động Học Giải Tích: Dẫn Xuất Vận Tốc, Gia Tốc & Bản Chất Lực Trong 4 Cung Chuyển Động
*(Đối chiếu và giải mã chuyên sâu Bài 3 KNTT)*

#### Bước chuyển từ Mục 3: Mối quan hệ nội tại giữa $x, v, a$
Ở **Mục 3**, chúng ta đã khám phá sự vuông pha tạo nên hệ thức Elip và sự ngược pha tạo nên sự đảo dấu hoàn toàn. Bây giờ, vận dụng **Hộp công cụ Toán (Mục 1, 2, 3)**, chúng ta sẽ chứng kiến một sự thật kỳ vĩ: **Trong một vật dao động điều hòa, Vận tốc vuông pha với Li độ, và Gia tốc ngược pha với Li độ!**

#### 1. Dẫn xuất Vận tốc tức thời $v(t)$
Theo định nghĩa ở Mục 1, vận tốc tức thời chính là đạo hàm của li độ theo thời gian:
$$v(t) = x'(t) = [A\cos(\omega t + \varphi)]'$$
Áp dụng quy tắc đạo hàm và phát hiện dấu trừ từ chuyến tàu lượn siêu tốc ở Mục 2:
$$v(t) = -\omega A \sin(\omega t + \varphi)$$
Để so sánh pha với li độ chuẩn $\cos$, ta dùng vệ tinh vận tốc $\vec{u}_2$ bay trước một góc vuông $+90^\circ$ ($\frac{\pi}{2}$) trên đường tròn ở Mục 3 ($-\sin\alpha = \cos(\alpha + \pi/2)$):
$$v(t) = \omega A \cos\left(\omega t + \varphi + \frac{\pi}{2}\right)$$
* **Tốc độ cực đại:** $v_{\max} = \omega A$ (đạt được khi vật đi qua vị trí cân bằng $x = 0$).
* **Mối quan hệ pha:** **Vận tốc $v(t)$ sớm pha $\frac{\pi}{2}$ (vuông pha) so với li độ $x(t)$**.

#### 2. Dẫn xuất Gia tốc tức thời $a(t)$
Gia tốc tức thời là đạo hàm của vận tốc theo thời gian:
$$a(t) = v'(t) = [-\omega A \sin(\omega t + \varphi)]' = -\omega^2 A \cos(\omega t + \varphi)$$
Dùng mô hình vệ tinh gia tốc $\vec{u}_3$ bay đối đầu trọn vẹn nửa vòng tròn $+180^\circ$ ($\pi$) ở Mục 3 ($-\cos\alpha = \cos(\alpha + \pi)$):
$$a(t) = \omega^2 A \cos\left(\omega t + \varphi + \pi\right)$$
Mặt khác, vì $x(t) = A\cos(\omega t + \varphi)$, ta rút ra hệ thức động lực học nền tảng:
$$a(t) = -\omega^2 x(t)$$
* **Độ lớn gia tốc cực đại:** $a_{\max} = \omega^2 A$ (đạt được khi vật ở hai mép biên $x = \pm A$).
* **Mối quan hệ pha:** **Gia tốc $a(t)$ ngược pha hoàn toàn ($\pi$) so với li độ $x(t)$**, và **sớm pha $\frac{\pi}{2}$ so với vận tốc $v(t)$**.

---

#### Đào sâu bản chất động lực học: Phá tan ngộ nhận "Nhanh dần đều / Chậm dần đều"
Một trong những lỗi sai phổ biến và tai hại nhất của học sinh lớp 11 khi làm bài thi là phát biểu: *"Vật chuyển động nhanh dần đều từ biên về VTCB, và chậm dần đều từ VTCB ra biên"*.  
> ⚠️ **ĐÂY LÀ SAI LẦM CHÍ MẠNG VỀ BẢN CHẤT CƠ HỌC!**  
> Chuyển động biến đổi **đều** đòi hỏi gia tốc phải là một hằng số không đổi ($a = \text{const}$). Nhưng ở đây, gia tốc $a(t) = -\omega^2 x(t)$ biến thiên liên tục từng micro-giây theo li độ $x$! Do đó, dao động điều hòa là **chuyển động biến đổi KHÔNG ĐỀU**.

Hãy mổ xẻ cơ chế lực và công cơ học qua **4 cung phần tư chuyển động** trong một chu kì:

* **Cung 1 ($0 \to \frac{T}{4}$ — Từ Biên Dương $+A$ về VTCB $0$):**  
  * Vật chuyển động theo chiều âm $\implies v < 0$.  
  * Vật ở phía dương ($x > 0$), lò xo bị dãn nên lực kéo về giằng vật về phía âm $\implies F_{kv} < 0 \implies a < 0$.  
  * Vì $\vec{v}$ và $\vec{a}$ cùng chiều ($v \cdot a > 0$), vật chuyển động **NHANH DẦN (KHÔNG ĐỀU)**. Lực kéo về cùng hướng chuyển động nên sinh công dương ($A_F > 0$), liên tục "bơm" cơ năng thành động năng cho vật, kéo tốc độ tăng từ $0$ lên $v_{\max}$!
* **Cung 2 ($\frac{T}{4} \to \frac{T}{2}$ — Từ VTCB $0$ ra Biên Âm $-A$):**  
  * Do quán tính, vật tiếp tục lao theo chiều âm $\implies v < 0$.  
  * Nhưng lúc này vật sang phía âm ($x < 0$), lò xo bị nén lại nên lực kéo về đổi chiều, đẩy vật sang phía dương $\implies F_{kv} > 0 \implies a > 0$.  
  * Vì $\vec{v}$ và $\vec{a}$ ngược chiều ($v \cdot a < 0$), vật chuyển động **CHẬM DẦN (KHÔNG ĐỀU)**. Lực kéo về ngược hướng chuyển động nên sinh công âm ($A_F < 0$), đóng vai trò chiếc phanh hãm rút cạn động năng nạp vào thế năng đàn hồi, ép tốc độ giảm từ $v_{\max}$ về $0$!
* **Cung 3 ($\frac{T}{2} \to \frac{3T}{4}$ — Từ Biên Âm $-A$ về VTCB $0$):**  
  * Lò xo bung ra đẩy vật lao theo chiều dương $\implies v > 0$.  
  * Lực kéo về hướng theo chiều dương $\implies a > 0$.  
  * Tích $v \cdot a > 0 \implies$ Vật chuyển động **NHANH DẦN (KHÔNG ĐỀU)**, lực sinh công dương, tốc độ tăng từ $0$ lên $v_{\max}$.
* **Cung 4 ($\frac{3T}{4} \to T$ — Từ VTCB $0$ ra Biên Dương $+A$):**  
  * Quán tính đưa vật tiếp tục sang chiều dương $\implies v > 0$.  
  * Lò xo dãn ra giật ngược về chiều âm $\implies a < 0$.  
  * Tích $v \cdot a < 0 \implies$ Vật chuyển động **CHẬM DẦN (KHÔNG ĐỀU)**, lực sinh công âm hãm phanh, tốc độ giảm từ $v_{\max}$ về $0$.

---

#### Bảng Tổng Hợp 4 Trạng Thái Mốc Then Chốt (Hình 1.1)

| Mốc thời gian | Trạng thái chuyển động | Li độ $x$ | Vận tốc $v$ (Độ dốc tiếp tuyến) | Gia tốc $a$ (Lực kéo về $F_{kv}$) | Ý nghĩa cơ học & Năng lượng |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **$t = 0$** | **Biên dương** | $x = +A$ (cực đại) | $v = 0$ (tiếp tuyến ngang) | $a = -\omega^2 A$ (âm cực đại) | Vật đổi chiều; lò xo dãn mạnh nhất; thế năng đạt cực đại. |
| **$t = \frac{T}{4}$** | **Qua VTCB theo chiều âm** | $x = 0$ | $v = -\omega A$ (dốc âm cắm đầu) | $a = 0$ (lực triệt tiêu) | Lực kéo về sinh trọn vẹn công dương; động năng đạt cực đại. |
| **$t = \frac{T}{2}$** | **Biên âm** | $x = -A$ (cực tiểu) | $v = 0$ (tiếp tuyến ngang) | $a = +\omega^2 A$ (dương cực đại) | Vật đổi chiều; lò xo nén chặt nhất; thế năng đạt cực đại. |
| **$t = \frac{3T}{4}$** | **Qua VTCB theo chiều dương** | $x = 0$ | $v = +\omega A$ (dốc dương hướng lên) | $a = 0$ (lực triệt tiêu) | Vật lao nhanh nhất theo chiều dương; động năng đạt cực đại. |

![Hình 1.1: Đồ thị động học chuẩn hóa theo thời gian của dao động điều hòa: Li độ x(t) (xanh navy), Vận tốc v(t) (xanh lá), và Gia tốc a(t) (đỏ thẫm) qua 4 mốc thời gian kinh điển 0, T/4, T/2, 3T/4.](figures/fig1_1_kinematics.png)

*Câu hỏi mở dẫn dắt sang Mục 5:*  
Tất cả các phương trình động học ở trên đều gắn chặt với biến thời gian $t$. Nhưng trong phòng thí nghiệm, nếu chiếc đồng hồ bấm giây bị gián đoạn và chúng ta chỉ đo được vị trí $x$ của vật, làm thế nào để ta biết ngay lập tức vận tốc $v$ mà không cần biết thời gian $t$?

---

### 5. Hệ Thức Độc Lập Thời Gian & Không Gian Trạng Thái $(x, v/\omega)$
*(Bài 3 & Bài 4 KNTT)*

#### Khử biến thời gian $t$ bằng Định lý Pythagoras
Trong thực tế nghiên cứu, các cảm biến đo lường vị trí (như cảm biến laser hoặc siêu âm) ghi nhận vị trí tức thời $x$ của vật tại một điểm trên đường ray. Để tìm vận tốc tức thời $v$ mà không phải đo biến số thời gian $t$, ta sử dụng tính chất vuông pha giữa $x$ và $v$.

Từ hai phương trình chuẩn hóa:
$$\frac{x}{A} = \cos(\omega t + \varphi), \quad \frac{v}{\omega A} = -\sin(\omega t + \varphi)$$
Bình phương hai vế rồi cộng lại, tận dụng hằng đẳng thức vàng lượng giác $\cos^2\alpha + \sin^2\alpha = 1$:
$$\left(\frac{x}{A}\right)^2 + \left(\frac{v}{\omega A}\right)^2 = \cos^2(\omega t + \varphi) + \sin^2(\omega t + \varphi) = 1$$
Nhân cả hai vế với $A^2$, ta thu được **Hệ thức độc lập thời gian**:
$$x^2 + \frac{v^2}{\omega^2} = A^2 \iff A = \sqrt{x^2 + \frac{v^2}{\omega^2}} \iff |v| = \omega\sqrt{A^2 - x^2}$$

Hoàn toàn tương tự, vì gia tốc $a(t) = -\omega^2 x(t) \implies \frac{x}{A} = -\frac{a}{\omega^2 A}$, ta có hệ thức độc lập giữa gia tốc $a$ và vận tốc $v$:
$$\left(\frac{a}{\omega^2 A}\right)^2 + \left(\frac{v}{\omega A}\right)^2 = 1 \iff \frac{a^2}{\omega^4} + \frac{v^2}{\omega^2} = A^2 \iff |v| = \frac{1}{\omega}\sqrt{a_{\max}^2 - a^2}$$

---

#### Không gian trạng thái Phase Space $(x, v/\omega)$ (Hình 1.2)
Hệ thức độc lập thời gian mở ra một góc nhìn hình học tuyệt mỹ trong vật lý hiện đại: **Không gian trạng thái (Phase Space)**.

![Hình 1.2: Đồ thị không gian trạng thái (x, v/omega). Quỹ đạo của dao động điều hòa là một đường tròn bán kính A quay thuận chiều kim đồng hồ, quét qua 4 mốc động học S0, S1, S2, S3.](figures/fig1_2_phase_space.png)

> 🔍 **DẪN DẮT MẮT ĐỌC (Hình 1.2):**  
> * Nếu ta chọn trục hoành là li độ $x$ và trục tung là vận tốc chuẩn hóa $y = \frac{v}{\omega}$, hệ thức độc lập $\left(\frac{x}{A}\right)^2 + \left(\frac{v}{\omega A}\right)^2 = 1$ biến thành phương trình đường tròn hoàn mỹ:
>   $$x^2 + y^2 = A^2$$
> * Khi vật dao động qua lại trên đoạn thẳng $2A$ ngoài đời thực, thì trong không gian trạng thái, **điểm trạng thái $(x, v/\omega)$ lại quay tròn đều đặn thuận chiều kim đồng hồ**:
>   * $S_0(t = 0)$: Vật ở biên dương $(+A, 0)$ $\implies$ Nằm trên trục hoành bên phải.
>   * $S_1(t = T/4)$: Vật qua VTCB theo chiều âm $(0, -A)$ $\implies$ Rơi xuống cực đáy trục tung.
>   * $S_2(t = T/2)$: Vật tới biên âm $(-A, 0)$ $\implies$ Nằm trên trục hoành bên trái.
>   * $S_3(t = 3T/4)$: Vật qua VTCB theo chiều dương $(0, +A)$ $\implies$ Vọt lên đỉnh cao nhất trục tung.
> * Các vòng tròn đồng tâm tương ứng với các mức năng lượng và biên độ khác nhau: biên độ càng lớn ($A_3 > A_2 > A_1$), quỹ đạo trạng thái càng mở rộng ra ngoài!

---

### 6. Bài Toán Tính Số Thực Tế 1.1: Màng Loa Điện Thoại & Gia Tốc Khổng Lồ
*(Bài tập vận dụng thực tế theo chuẩn Bài 4 SGK Kết nối tri thức)*

> 🎧 **BÀI TOÁN THỰC TẾ:**  
> Một chiếc màng loa tai nghe in-ear dao động điều hòa phát ra nốt La chuẩn có tần số $f = 440\text{ Hz}$. Khi đo bằng thiết bị laser giao thoa, người ta ghi nhận biên độ rung của màng loa là $A = 0.5\text{ mm} = 0.5 \times 10^{-3}\text{ m}$.  
> 1. Tính tần số góc $\omega$ và chu kì dao động $T$ của màng loa.  
> 2. Tính tốc độ cực đại $v_{\max}$ và gia tốc cực đại $a_{\max}$ mà màng loa đạt được.  
> 3. Khi màng loa đang ở li độ $x = 0.3\text{ mm}$, hãy tính tốc độ tức thời của màng loa.  
> 4. Hãy so sánh gia tốc cực đại của màng loa với gia tốc trọng trường $g \approx 9.8\text{ m/s}^2$ và giải thích nghịch lý: vì sao màng loa mỏng manh lại chịu nổi gia tốc khủng khiếp như vậy?
> 
> ---
> 
> 📝 **HƯỚNG DẪN GIẢI CHI TIẾT:**  
> 1. **Tần số góc $\omega$ và chu kì $T$:**  
>    * $\omega = 2\pi f = 2\pi \times 440 \approx 2764.6\text{ rad/s}$.  
>    * $T = \frac{1}{f} = \frac{1}{440} \approx 0.00227\text{ s} = 2.27\text{ ms}$.  
>    *(Mỗi nhịp rung toàn phần của màng loa diễn ra chỉ vỏn vẹn trong hơn 2 phần nghìn giây!)*  
> 
> 2. **Tốc độ cực đại $v_{\max}$ và gia tốc cực đại $a_{\max}$:**  
>    * $v_{\max} = \omega A = 2764.6 \times (0.5 \times 10^{-3}) \approx 1.38\text{ m/s} \approx 5\text{ km/h}$.  
>    * $a_{\max} = \omega^2 A = (2764.6)^2 \times (0.5 \times 10^{-3}) \approx 3821.5\text{ m/s}^2$.  
> 
> 3. **Tốc độ tức thời khi $x = 0.3\text{ mm}$:**  
>    Áp dụng hệ thức độc lập thời gian Pythagoras:  
>    $$x^2 + \frac{v^2}{\omega^2} = A^2 \implies |v| = \omega \sqrt{A^2 - x^2}$$  
>    Thay số trực tiếp với đơn vị thống nhất ($\text{mm}$):  
>    $$|v| = 2764.6 \times \sqrt{0.5^2 - 0.3^2} = 2764.6 \times 0.4 = 1105.8\text{ mm/s} \approx 1.11\text{ m/s}$$  
> 
> 4. **Giải mã nghịch lý gia tốc khổng lồ:**  
>    * So sánh với gia tốc trọng trường: $\frac{a_{\max}}{g} = \frac{3821.5}{9.8} \approx 390\text{ g}$!  
>    * *Nghịch lý:* Một phi hành gia trên tàu vũ trụ chỉ có thể chịu được gia tốc tối đa khoảng $9g - 10g$ trước khi bất tỉnh. Vậy tại sao chiếc màng loa mỏng dính như cánh ve lại chịu được gia tốc lên tới $390g$ mà không bị rách toạc?  
>    * *Bản chất vật lý:* Theo định luật II Newton, lực tác dụng gây phá hủy vật liệu là $F = ma$. Màng loa tai nghe có khối lượng cực kỳ nhỏ (chỉ vài miligam: $m \sim 10^{-5}\text{ kg}$). Do đó, lực quán tính tác dụng lên nó chỉ cỡ $F \approx 10^{-5} \times 3820 \approx 0.038\text{ N}$ — một lực rất nhỏ bé, tương đương sức nặng của một mẩu giấy nhỏ, nên màng loa hoàn toàn bền vững!

---

### 7. Hộp Cứu Nguy: 3 "Tử Huyệt" Dễ Mắc Bẫy Nhất Trong Đề Thi

> ⚠️ **CẢNH BÁO BẪY ĐỀ KIỂM TRA & KÌ THI TỐT NGHIỆP THPT: 3 "TỬ HUYỆT" THƯỜNG GẶP**
>
> * **TỬ HUYỆT 1: "Ở biên vật đứng lại ($v = 0$) nên gia tốc cũng bằng $0$ (?)"**  
>   ➔ **SAI LẦM PHỔ BIẾN NHẤT!**  
>   • *Bản chất đúng:* Ở biên, vận tốc bằng $0$ vì đồ thị $x(t)$ nằm ngang (độ dốc tiếp tuyến triệt tiêu). Nhưng lúc này vật lệch xa nhất khỏi VTCB, lò xo bị nén/dãn cực đại nên **LỰC KÉO VỀ ĐẠT CỰC ĐẠI** ➔ Gia tốc đạt **ĐỘ LỚN CỰC ĐẠI**:  
>   $$|a| = a_{\max} = \omega^2 A$$
>
> * **TỬ HUYỆT 2: "Qua VTCB lực bằng $0$ ($a = 0$) nên vật tạm dừng ($v = 0$) (?)"**  
>   ➔ **SAI LẦM TAI HẠI!**  
>   • *Bản chất đúng:* Qua VTCB, lò xo không bị biến dạng nên lực kéo về bằng $0 \implies a = 0$. Nhưng suốt quãng đường lao dốc trước đó, lực kéo về đã liên tục tăng tốc cho vật, tích lũy động năng lên mức đỉnh điểm. Do quán tính, vật lao vút qua VTCB với **TỐC ĐỘ LỚN NHẤT**:  
>   $$|v| = v_{\max} = \omega A$$
>
> * **TỬ HUYỆT 3: Quên mất dấu âm trong hệ thức gia tốc: $a = \omega^2 x$ (?)**  
>   ➔ **SAI VỀ BẢN CHẤT LỰC HỒI PHỤC!**  
>   • *Bản chất đúng:* Bắt buộc phải là:  
>   $$a(t) = -\omega^2 x(t)$$  
>   Dấu trừ mang ý nghĩa sống còn: **véc-tơ gia tốc LUÔN LUÔN HƯỚNG VỀ VỊ TRÍ CÂN BẰNG**, ngược chiều với véc-tơ li độ! Nếu mang dấu dương, lực sẽ đẩy vật văng ra xa mãi mãi thay vì tạo ra chuyển động dao động!


---

# PHẦN 2: ĐỘNG LỰC HỌC & SỰ CHUYỂN HÓA NĂNG LƯỢNG
*(Đối chiếu và giải mã chuyên sâu Bài 1, 5, 7 SGK Kết nối tri thức)*

### 1. Động Lực Học Con Lắc Lò Xo & Con Lắc Đơn

#### Con lắc lò xo
Xét quả cầu nhỏ khối lượng $m$ gắn vào lò xo có độ cứng $k$ trượt không ma sát.  
* **Lực kéo về:** $F_{kv} = -kx$.  
* **Định luật II Newton:** $F = ma \iff -kx = ma \implies a = -\frac{k}{m}x$.  
* So sánh với $a = -\omega^2 x$, ta thu được công thức tần số góc và chu kì của con lắc lò xo:
  $$\omega = \sqrt{\frac{k}{m}}, \quad T = 2\pi\sqrt{\frac{m}{k}}$$

#### Con lắc đơn
Xét sợi dây chiều dài $\ell$ treo vật nặng $m$. Khi góc lệch $\alpha$ nhỏ ($\alpha \le 10^\circ \approx 0.175\text{ rad}$), $\sin\alpha \approx \alpha = \frac{s}{\ell}$.  
* **Lực kéo về:** $F_t = -mg\sin\alpha \approx -\left(\frac{mg}{\ell}\right)s$.  
* Chu kì dao động điều hòa của con lắc đơn:
  $$T = 2\pi\sqrt{\frac{\ell}{g}}$$

---

### 2. Ẩn Dụ Đáy Chảo Parabol: Nguồn Gốc Sâu Xa của Dao Động Điều Hòa

Tại sao từ cành cây, dây đàn đến cầu treo hay nguyên tử đều dao động điều hòa?

* **Hình ảnh chiếc chảo:** Hãy hình dung một **hòn bi nằm dưới đáy một chiếc chảo trũng**.  
  1. Điểm sâu nhất của đáy chảo ($x_0 = 0$) là **Vị trí cân bằng bền**, nơi thế năng của vật đạt giá trị cực tiểu.  
  2. Gần đáy chảo, bất kỳ đường cong trơn nào cũng có thể áp vừa khít một đường cong **Parabol** bậc hai:
     $$W_t(x) \approx \frac{1}{2}kx^2$$
  3. Khi hòn bi lệch khỏi đáy một đoạn nhỏ $x$, phản lực dốc của thành chảo sẽ đẩy hòn bi trở về với lực tỉ lệ với độ dời: $F = -kx$.

![Bản chất hình học của đáy giếng thế năng: Dao động nhỏ quanh vị trí cân bằng bền luôn có thế năng dạng Parabol.](figures/fig1_3_potential_well.png)

> 🔍 **DẪN DẮT MẮT ĐỌC (Hình 1.3):**  
> Trong vùng màu vàng nhạt ($|x| \le 0.35$), đường cong thế năng thực tế màu xanh và parabol màu đỏ **hoàn toàn trùng khít lên nhau**. Điều này giải thích chân lý: *Mọi dao động nhỏ quanh vị trí cân bằng bền trong vũ trụ đều là dao động điều hòa!*

---

### 3. Động Năng, Thế Năng & Cơ Năng (Bài 5 & 7 KNTT)

Theo chuẩn ký hiệu của SGK Kết nối tri thức:

1. **Động năng $W_đ$:**
   $$W_đ = \frac{1}{2}mv^2 = \frac{1}{2}m\omega^2 A^2 \sin^2(\omega t + \varphi) = \frac{1}{2}kA^2 \sin^2(\omega t + \varphi)$$
2. **Thế năng $W_t$:**
   $$W_t = \frac{1}{2}kx^2 = \frac{1}{2}kA^2 \cos^2(\omega t + \varphi)$$
3. **Cơ năng toàn phần $W$:**
   $$W = W_đ + W_t = \frac{1}{2}kA^2 \left[\sin^2(\omega t + \varphi) + \cos^2(\omega t + \varphi)\right] = \frac{1}{2}kA^2 = \frac{1}{2}m v_{\max}^2 = \text{const}$$

> 💡 **Quy luật bảo toàn (Bài 5 KNTT):** Khi bỏ qua ma sát, cơ năng của vật dao động điều hòa được bảo toàn tuyệt đối, tỉ lệ thuận với bình phương biên độ dao động ($W \propto A^2$).

#### Chu kì biến thiên của Động năng và Thế năng
Dùng công thức hạ bậc lượng giác:
$$\sin^2\alpha = \frac{1 - \cos 2\alpha}{2}, \quad \cos^2\alpha = \frac{1 + \cos 2\alpha}{2}$$
* Động năng và thế năng biến thiên tuần hoàn với **tần số góc gấp đôi ($2\omega$)**, **chu kì bằng một nửa ($T' = T/2$)** và **tần số gấp đôi ($f' = 2f$)** so với dao động điều hòa của li độ $x$.

![Động năng W_đ và Thế năng W_t chuyển hóa tuần hoàn theo thời gian và phân bố theo li độ x.](figures/fig1_4_energy.png)

> 🔍 **DẪN DẮT MẮT ĐỌC (Hình 1.4):**  
> * **Đồ thị (a):** Đường màu xanh lá ($W_đ$) và đường màu xanh navy ($W_t$) liên tục đổi chỗ cho nhau nhưng tổng của chúng luôn nằm trên đường thẳng đỏ $W$. Đường chấm xám ở giữa thể hiện giá trị trung bình theo thời gian: $\bar{W}_đ = \bar{W}_t = \frac{1}{2}W$.  
> * **Đồ thị (b):** Vị trí hai parabol cắt nhau ứng với điểm **Động năng bằng Thế năng**:  
>   $$W_đ = W_t \implies W_t = \frac{W}{2} \iff \frac{1}{2}kx^2 = \frac{1}{2}\left(\frac{1}{2}kA^2\right) \implies x = \pm \frac{A}{\sqrt{2}}$$

---

### 4. Bài Toán Tính Số Thực Tế 1.2 (Theo Dạng Bài 7 KNTT)

> **Bài toán:** Một con lắc lò xo gồm vật nặng $m = 200\text{ g} = 0.2\text{ kg}$ gắn vào lò xo có độ cứng $k = 50\text{ N/m}$ dao động điều hòa với biên độ $A = 6\text{ cm} = 0.06\text{ m}$.  
> 1. Tính cơ năng $W$ của con lắc.  
> 2. Tính vận tốc cực đại $v_{\max}$ của vật.  
> 3. Tìm li độ $x$ của vật khi động năng gấp 3 lần thế năng ($W_đ = 3W_t$).  
> 
> **Lời giải chi tiết:**  
> 1. **Cơ năng của con lắc:**  
>    $$W = \frac{1}{2}kA^2 = \frac{1}{2} \times 50 \times (0.06)^2 = 0.09\text{ J} = 90\text{ mJ}$$  
> 2. **Vận tốc cực đại:**  
>    $$W = \frac{1}{2}m v_{\max}^2 \implies v_{\max} = \sqrt{\frac{2W}{m}} = \sqrt{\frac{2 \times 0.09}{0.2}} = \sqrt{0.9} \approx 0.949\text{ m/s} = 94.9\text{ cm/s}$$  
> 3. **Vị trí có $W_đ = 3W_t$:**  
>    Áp dụng bảo toàn cơ năng:  
>    $$W = W_đ + W_t = 3W_t + W_t = 4W_t$$  
>    $$\frac{1}{2}kA^2 = 4\left(\frac{1}{2}kx^2\right) \implies x^2 = \frac{A^2}{4} \implies x = \pm \frac{A}{2} = \pm \frac{6}{2} = \pm 3\text{ cm}$$

---

# PHẦN 3: DAO ĐỘNG TẮT DẦN, CƯỠNG BỨC & CỘNG HƯỞNG
*(Đối chiếu và giải mã chuyên sâu Bài 6 SGK Kết nối tri thức)*

### 1. Dao Động Tắt Dần & Sự Tiêu Tán Cơ Năng

* **Định nghĩa SGK (Bài 6 KNTT):** *Dao động tắt dần là dao động có biên độ và cơ năng giảm dần theo thời gian*.
* **Cơ chế vi mô:** Do có lực ma sát hoặc lực cản môi trường, cơ năng của hệ liên tục sinh công âm và biến thành nhiệt năng ($Q_{nhiệt}$) tỏa ra môi trường. Vì cơ năng $W = \frac{1}{2}kA^2$ giảm liên tục, biên độ $A$ bắt buộc phải thu hẹp dần cho đến khi dừng hẳn.

![Ba chế độ chuyển động khi có lực cản môi trường và đồ thị trạng thái xoắn ốc.](figures/fig1_5_damped.png)

#### Ba Chế Độ Cản Trong Đời Sống Thực Tế
1. **Lực cản nhỏ (Dao động tắt dần):** Vật vẫn dao động qua lại quanh VTCB nhiều lần trước khi dừng hẳn (như con lắc đung đưa trong không khí).
2. **Lực cản tới hạn:** Vật trở về VTCB **nhanh nhất** mà không hề bị vọt lố hay lắc qua lắc lại.  
   * **Ứng dụng đắt giá:** **Bộ giảm xóc (phuộc nhún) xe máy và ô tô**. Khi bánh xe đập vào ổ gà, lò xo bị nén; dầu giảm chấn trong xi-lanh dập tắt dao động ngay lập tức trong nhịp đầu tiên, giúp xe giữ thăng bằng và êm ái.
3. **Lực cản quá lớn:** Vật chuyển động rất ì ạch, chậm chạp trở về VTCB.  
   * **Ứng dụng:** **Tay co thủy lực đóng cửa tự động**, giữ cửa khép từ từ, tránh va đập mạnh làm vỡ kính.

---

### 2. Dao Động Duy Trì (Con Lắc Đồng Hồ)

* Để một hệ dao động mãi với tần số riêng $\omega_0$ mà không bị tắt dần, ta phải cung cấp năng lượng cho hệ trong mỗi chu kì để bù đắp đúng bằng phần năng lượng tiêu hao do ma sát.
* **Đặc điểm:** Tần số dao động duy trì vẫn bằng đúng tần số dao động riêng $\omega_0$ của hệ.
* **Ví dụ:** Đồng hồ quả lắc dùng quả tạ hoặc dây cót truyền lực đẩy khẽ vào con lắc qua cơ cấu bánh cóc (ngựa đồng hồ) mỗi khi con lắc đi qua vị trí cân bằng.

---

### 3. Dao Động Cưỡng Bức & Hiện Tượng Cộng Hưởng

Nếu ta tác dụng vào hệ một ngoại lực tuần hoàn $F(t) = F_0 \cos(\Omega t)$:

1. **Đặc điểm của Dao động Cưỡng bức:**
   * Hệ sẽ dao động với **tần số bằng tần số $\Omega$ của ngoại lực**, không còn giữ tần số riêng $\omega_0$.
   * Biên độ dao động cưỡng bức phụ thuộc vào biên độ ngoại lực $F_0$, lực cản môi trường và đặc biệt là **khoảng cách giữa tần số ngoại lực $\Omega$ và tần số riêng $\omega_0$**.

2. **Hiện Tượng Cộng Hưởng (Resonance):**
   * Khi tần số ngoại lực xấp xỉ bằng tần số dao động riêng của hệ:
     $$\Omega \approx \omega_0$$
     Biên độ của dao động cưỡng bức vọt lên đạt giá trị **cực đại**. Hiện tượng này gọi là **hiện tượng cộng hưởng**.

![Đường cong cộng hưởng biên độ đạt đỉnh khi tần số ngoại lực trùng khớp với tần số riêng.](figures/fig1_6_resonance.png)

> 🔍 **DẪN DẮT MẮT ĐỌC (Hình 1.6):**  
> * Trục đứng tại vị trí $\Omega/\omega_0 = 1.0$ là vị trí cộng hưởng.  
> * Đường màu đỏ (lực cản nhỏ) có đỉnh cộng hưởng nhọn hoắt và biên độ vọt lên rất cao.  
> * Đường màu xanh navy (lực cản lớn) có đỉnh thoai thoải, biên độ không tăng vọt nguy hiểm.

#### Ứng Dụng & Tác Hại của Cộng Hưởng
* **Ứng dụng có lợi:**
  - Hộp cộng hưởng của đàn guitar, violin, đàn bầu giúp khuếch đại âm thanh phát ra to và vang.
  - Chỉnh núm xoay mạch thu sóng radio để tần số riêng của máy trùng với tần số của đài phát cần nghe.
* **Tác hại cần tránh:**
  - Binh lính bước đều qua cầu làm tần số bước chân trùng tần số dao động của cầu gây sập cầu (lệnh quân sự bắt buộc: *bước tự do khi qua cầu*).
  - Gió bão thổi tạo luồng khí xoáy trùng tần số rung làm sập cầu Tacoma Narrows năm 1940.
  - Máy giặt khi vắt ở tốc độ cao nếu tần số quay của lồng giặt trùng với tần số riêng của vỏ máy sẽ làm máy rung lắc dữ dội và kêu ầm ĩ.

---

### 4. Bài Toán Tính Số Thực Tế 1.3 (Bài Toán Gờ Giảm Tốc KNTT)

> **Bài toán:** Một chiếc xe máy chở người có tổng khối lượng $m = 160\text{ kg}$. Hệ thống giảm xóc có độ cứng tương đương $k = 40,000\text{ N/m}$. Xe chạy trên một đoạn đường có các gờ giảm tốc cách đều nhau một khoảng $d = 8.0\text{ m}$.  
> 1. Tính tần số dao động riêng $f_0$ của khung xe máy.  
> 2. Người lái xe chạy với tốc độ $v$ bằng bao nhiêu thì xe bị rung lắc nảy lên dữ dội nhất?
> 
> **Lời giải chi tiết:**  
> 1. **Tần số dao động riêng của xe:**  
>    * Tần số góc riêng:  
>      $$\omega_0 = \sqrt{\frac{k}{m}} = \sqrt{\frac{40000}{160}} = \sqrt{250} \approx 15.81\text{ rad/s}$$  
>    * Tần số riêng:  
>      $$f_0 = \frac{\omega_0}{2\pi} = \frac{15.81}{2\pi} \approx 2.52\text{ Hz}$$  
> 2. **Tốc độ gây rung nảy mạnh nhất (Cộng hưởng):**  
>    * Thời gian xe chạy qua hai gờ liên tiếp là chu kì kích thích của ngoại lực: $T = \frac{d}{v}$.  
>    * Tần số kích thích của các gờ giảm tốc: $f = \frac{1}{T} = \frac{v}{d}$.  
>    * Xe rung lắc mạnh nhất khi xảy ra hiện tượng cộng hưởng: $f = f_0$.  
>      $$\frac{v}{d} = f_0 \implies v = d \cdot f_0 = 8.0\text{ m} \times 2.52\text{ Hz} = 20.16\text{ m/s}$$  
>    * Đổi sang $\text{km/h}$:  
>      $$v = 20.16 \times 3.6 \approx 72.6\text{ km/h}$$  
>    * *Bài học thực tế:* Người lái xe cần tránh chạy ở dải tốc độ nguy hiểm khoảng $70 - 75\text{ km/h}$ khi đi qua đoạn đường này; nên giảm tốc độ xuống dưới $30\text{ km/h}$ để bảo đảm an toàn.

---

## BẢNG TỔNG KẾT BẢN CHẤT CHƯƠNG 1 (THEO CHUẨN KNTT)

| Đại lượng / Hiện tượng | Công thức cốt lõi | Ý nghĩa bản chất & Lưu ý kiểm tra |
| :--- | :--- | :--- |
| **Li độ** | $x = A\cos(\omega t + \varphi)$ | Tọa độ của vật so với VTCB tại thời điểm $t$. |
| **Vận tốc** | $v = x'(t) = \omega A\cos(\omega t + \varphi + \pi/2)$ | Vận tốc sớm pha $\pi/2$ so với li độ; $v_{\max} = \omega A$ tại VTCB. |
| **Gia tốc** | $a = v'(t) = -\omega^2 x$ | Gia tốc ngược pha $\pi$ so với li độ; luôn hướng về VTCB; $a_{\max} = \omega^2 A$ ở biên. |
| **Hệ thức độc lập** | $x^2 + \frac{v^2}{\omega^2} = A^2$ | Tính nhanh không qua thời gian $t$; liên hệ giữa vị trí và vận tốc. |
| **Độ lệch pha** | $\Delta \varphi = \varphi_2 - \varphi_1$ | Cùng pha ($2k\pi$), ngược pha ($(2k+1)\pi$), vuông pha ($(2k+1)\pi/2$). |
| **Động năng** | $W_đ = \frac{1}{2}mv^2$ | Biến thiên tuần hoàn với tần số góc $2\omega$, chu kì $T/2$. |
| **Thế năng** | $W_t = \frac{1}{2}kx^2 = \frac{1}{2}m\omega^2 x^2$ | Đạt cực đại ở biên; bằng 0 ở vị trí cân bằng. |
| **Cơ năng** | $W = W_đ + W_t = \frac{1}{2}kA^2 = \text{const}$ | Bảo toàn tuyệt đối khi không ma sát; tỉ lệ thuận với $A^2$. |
| **Vị trí $W_đ = W_t$** | $x = \pm \frac{A}{\sqrt{2}}$ | Vị trí động năng bằng một nửa cơ năng ($W_đ = W/2$). |
| **Cộng hưởng** | $\Omega \approx \omega_0$ | Biên độ dao động cưỡng bức vọt lên cực đại. |
