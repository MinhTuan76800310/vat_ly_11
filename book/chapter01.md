# CHƯƠNG 1: DAO ĐỘNG ĐIỀU HÒA – BẢN CHẤT ĐỘNG LỰC HỌC, KHÔNG GIAN PHA & BÀI TOÁN ĐÁNH ĐỔI KỸ THUẬT

---

> 📐 **HỘP CÔNG CỤ: TOÁN HỌC TỐI THIỂU CHO CHƯƠNG 1 (Mathematical Prerequisites)**  
> Trước khi đi vào động học và động lực học, người học cần nắm chắc 4 công cụ giải tích nền tảng:  
> 1. **Đạo hàm hàm hợp theo thời gian *(Time Derivatives)*:**  
>    $$\frac{d}{dt}\cos(\omega t + \varphi) = -\omega \sin(\omega t + \varphi), \quad \frac{d}{dt}\sin(\omega t + \varphi) = \omega \cos(\omega t + \varphi)$$  
> 2. **Khai triển chuỗi Taylor *(Taylor Series Expansion)*:** Xấp xỉ hàm khả vi $f(x)$ quanh điểm cực tiểu $x_0$:  
>    $$f(x) = f(x_0) + f'(x_0)(x - x_0) + \frac{1}{2!}f''(x_0)(x - x_0)^2 + \mathcal{O}((x - x_0)^3)$$  
> 3. **Phương trình vi phân tuyến tính cấp hai hệ số hằng *(Second-Order Linear ODE)*:**  
>    $$\ddot{x} + \omega_0^2 x = 0 \implies r^2 + \omega_0^2 = 0 \implies r = \pm i\omega_0 \implies x(t) = A\cos(\omega_0 t + \varphi)$$  
> 4. **Hàm mũ phức Euler *(Euler's Complex Formula)*:** $e^{i\theta} = \cos\theta + i\sin\theta$. Nhân với số ảo $i = e^{i\pi/2}$ tương đương một phép quay góc $\pi/2$ ngược chiều kim đồng hồ trên mặt phẳng phức.

---

# MODULE 1 (1 GIỜ): ĐỘNG HỌC DAO ĐỘNG ĐIỀU HÒA & KHÔNG GIAN PHA
*(Kinematics of Simple Harmonic Motion & Phase Space Dynamics)*

### 1. Mục tiêu Đầu ra (Learning Objectives)
Sau khi hoàn thành Module 1, người học có khả năng:
* Giải thích được vì sao dao động điều hòa là một chuyển động gia tốc biến đổi liên tục chứ không phải "chuyển động tròn đều ngầm".
* Dẫn xuất tường minh mối quan hệ pha giữa li độ, vận tốc và gia tốc bằng phép toán vi phân.
* Dựng chân dung pha *(Phase Portrait)*, giải thích quỹ đạo elip khép kín và tính bảo toàn trạng thái theo Định lý Liouville.
* Ứng dụng quan hệ không gian pha để xác định trạng thái tức thời của một hệ cơ học.

---

### 2. Mâu thuẫn Sách giáo khoa & Cơ chế Ngầm (The Conflict & Underlying Mechanism)
* **Mâu thuẫn (The Conflict):** Trong sách giáo khoa hiện hành, phương trình dao động $x = A\cos(\omega t + \varphi)$ thường được áp đặt bằng cách chiếu chuyển động của một chất điểm trên đường tròn tưởng tượng xuống một trục tọa độ. Điều này khiến người học lầm tưởng rằng một quả lắc hay một phân tử muốn dao động điều hòa thì phải "quay ngầm" trong một quỹ đạo tròn bí ẩn nào đó.
* **Cơ chế ngầm (Underlying Mechanism):** Trong tự nhiên, không có đường tròn nào cả. Một vật dao động điều hòa hoàn toàn do **lực hồi phục *(Restoring Force)*** luôn kéo vật trở về vị trí cân bằng, tạo ra một gia tốc luôn tỉ lệ thuận nhưng ngược chiều với độ dời:
  $$a(t) = -\omega^2 x(t)$$
  Chính quy luật động lực học tuyến tính này ép buộc nghiệm của phương trình chuyển động phải là hàm sin/cos.

---

### 3. Mô hình Tư duy & Giới hạn Ẩn dụ (Grounded Mental Model)
* **Ẩn dụ chuẩn xác (The Metaphor):** Hãy hình dung cơ cấu **Thanh truyền - Piston *(Piston-Crankshaft Mechanism)*** trong động cơ ô tô. Khi trục khuỷu quay tròn đều với tốc độ góc $\omega$, đầu thanh truyền nối với piston bị giam hãm trong xi-lanh thẳng tắp. Piston không quay; nó chỉ tịnh tiến qua lại. Tốc độ của piston bị hãm về $0$ ở hai điểm chết (biên độ), và lao vút qua điểm chính giữa với vận tốc cực đại.
* ⚠️ **Giới hạn của ẩn dụ (Analogy Boundary):** Piston cơ học bị ràng buộc cơ học cứng bởi thanh truyền thép. Trong dao động điều hòa tự do của con lắc lò xo hay phân tử, không có thanh truyền cứng; sự ràng buộc chỉ đến từ **trường thế năng đàn hồi mềm** của các liên kết nguyên tử. Nếu biên độ kéo quá lớn, lò xo sẽ bị dão hoặc phân tử sẽ bị bẻ gãy liên kết (phân ly).

---

### 4. Dẫn xuất Toán học: Vận tốc, Gia tốc và Độ lệch pha

Ta định nghĩa chuyển động dao động bằng tọa độ li độ *(Displacement)* $x(t)$ theo thời gian $t$:
$$x(t) = A\cos(\omega t + \varphi)$$

> 📐 **DẪN XUẤT TOÁN HỌC (Mathematical Proof): Đạo hàm Vận tốc và Gia tốc**  
> Áp dụng quy tắc đạo hàm hàm hợp theo thời gian:
> 
> 1. **Vận tốc tức thời *(Instantaneous Velocity)* $v(t)$:**
>    $$v(t) = \dot{x}(t) = \frac{dx}{dt} = -A\omega \sin(\omega t + \varphi)$$
>    Biến đổi lượng giác bằng công thức $-\sin\theta = \cos(\theta + \pi/2)$:
>    $$v(t) = \omega A \cos\left(\omega t + \varphi + \frac{\pi}{2}\right)$$
> 2. **Gia tốc tức thời *(Instantaneous Acceleration)* $a(t)$:**
>    $$a(t) = \dot{v}(t) = \ddot{x}(t) = \frac{d^2x}{dt^2} = -A\omega^2 \cos(\omega t + \varphi)$$
>    Biến đổi lượng giác bằng công thức $-\cos\theta = \cos(\theta + \pi)$:
>    $$a(t) = \omega^2 A \cos(\omega t + \varphi + \pi)$$
> 
> **Ý nghĩa biến số và đơn vị chuẩn SI:**
> * $x(t)$: Li độ tức thời, đơn vị mét ($\text{m}$).
> * $A$: Biên độ dao động (độ dời cực đại), đơn vị mét ($\text{m}$).
> * $\omega$: Tần số góc *(Angular Frequency)*, đơn vị radian trên giây ($\text{rad/s}$).
> * $\varphi$: Pha ban đầu tại thời điểm $t = 0$, đơn vị radian ($\text{rad}$).
> * $v(t)$: Vận tốc tức thời, đơn vị mét trên giây ($\text{m/s}$). Vận tốc cực đại $v_{\max} = \omega A$.
> * $a(t)$: Gia tốc tức thời, đơn vị mét trên giây bình phương ($\text{m/s}^2$). Gia tốc cực đại $a_{\max} = \omega^2 A$.

![Đồ thị động học chuẩn hóa theo thời gian của dao động điều hòa: Li độ $x(t)$, Vận tốc $v(t)/\omega$, và Gia tốc $a(t)/\omega^2$.](figures/fig1_1_kinematics.png)

> 🔬 **BẢN CHẤT VẬT LÝ & DẪN DẮT MẮT ĐỌC (Hình 1.1):**  
> * **Hãy nhìn vào đường màu xanh navy ở đồ thị trên cùng (Li độ $x/A$):** Tại thời điểm $t_0 = 0$, vật ở biên dương $P_0(x = +A)$. Khi trôi qua $t_1 = T/4$, vật về vị trí cân bằng $P_1(x = 0)$, và tới $t_2 = T/2$, vật chạm biên âm $P_2(x = -A)$.  
> * **Di chuyển mắt xuống đồ thị giữa màu xanh lá cây (Vận tốc $\frac{v}{\omega A}$):** Khi vật đang lao qua vị trí cân bằng ($x = 0$ tại $t_1 = T/4$), vận tốc đạt giá trị âm cực đại $v = -\omega A$. Vận tốc **sớm pha $\pi/2$** so với li độ, nghĩa là mọi biến cố của vận tốc đều diễn ra trước li độ một phần tư chu kỳ ($T/4$).  
> * **Nhìn vào đồ thị dưới cùng màu đỏ thẫm (Gia tốc $\frac{a}{\omega^2 A}$):** Tại $t_2 = T/2$, khi vật ở tận cùng biên âm ($x = -A$), gia tốc vọt lên cực đại dương $a = +\omega^2 A$ để kéo giật vật quay trở lại. Gia tốc **ngược pha hoàn toàn ($\pi$)** với li độ ($a = -\omega^2 x$).

---

### 5. Khái niệm Không gian Pha (Phase Space) & Chân dung Pha

Trong cơ học, nếu chỉ biết vị trí $x$, ta không biết được hệ đang tiến hay lùi. Trạng thái cơ học đầy đủ đòi hỏi cặp biến độc lập: **(Vị trí $x$, Vận tốc $v$)**. 

Chia phương trình li độ và vận tốc cho biên độ cực đại tương ứng:
$$\frac{x}{A} = \cos(\omega t + \varphi), \quad \frac{v}{\omega A} = -\sin(\omega t + \varphi)$$
Bình phương và cộng hai vế:
$$\left(\frac{x}{A}\right)^2 + \left(\frac{v}{\omega A}\right)^2 = \cos^2(\omega t + \varphi) + \sin^2(\omega t + \varphi) = 1$$

Đặt biến vận tốc chuẩn hóa $y = \frac{v}{\omega}$, ta có phương trình đường tròn chính tắc:
$$x^2 + y^2 = A^2$$

![Chân dung pha (Phase Portrait) của dao động điều hòa với các mức năng lượng khác nhau và chiều dòng trạng thái thuận chiều kim đồng hồ.](figures/fig1_2_phase_space.png)

> 🔬 **BẢN CHẤT VẬT LÝ & DẪN DẮT MẮT ĐỌC (Hình 1.2):**  
> * **Hãy quan sát quỹ đạo elip màu xanh navy ứng với mức năng lượng $E_2$:**  
>   - Điểm màu cam $S_0(t = 0): (+A, 0)$ là trạng thái thả vật tại biên dương (vận tốc bằng 0).  
>   - Khi thời gian trôi, điểm làm việc trượt theo chiều kim đồng hồ tới $S_1(t = T/4): (0, -\omega A)$, nơi thế năng đã giải phóng hoàn toàn thành động năng âm cực đại.  
>   - Tiếp tục trượt qua $S_2(t = T/2): (-A, 0)$ và $S_3(t = 3T/4): (0, +\omega A)$.  
> * **Quy luật bất biến:** Ở nửa trên trục hoành ($v > 0$), li độ buộc phải tăng ($\dot{x} > 0$); ở nửa dưới ($v < 0$), li độ buộc phải giảm ($\dot{x} < 0$). Do đó, **mọi hệ tự nhiên trong không gian pha đều quay thuận chiều kim đồng hồ**.  
> * **Định lý Liouville:** Diện tích bao bởi đường cong pha $\mathcal{A} = \pi A (A\omega) \propto E$ không đổi theo thời gian. Hai quỹ đạo ứng với hai mức năng lượng khác nhau không bao giờ cắt nhau.

---

### 6. Bài toán Tính số Thực tế (Worked Numerical Example 1.1)

> **Đề bài:** Một cảm biến đo gia tốc vi cơ điện tử *(MEMS Accelerometer)* có khối lượng con lắc vi mô $m = 2 \times 10^{-9}\text{ kg}$ (2 microgam), dao động điều hòa với tần số $f = 2.5\text{ kHz}$ và biên độ dịch chuyển tối đa $A = 4.0\text{ }\mu\text{m}$.  
> 1. Tính tần số góc $\omega$, vận tốc cực đại $v_{\max}$ và gia tốc cực đại $a_{\max}$ tác dụng lên cấu trúc vi cơ.  
> 2. Xác định bán trục của quỹ đạo trong không gian pha $(x, v)$ và $(x, v/\omega)$.
> 
> **Lời giải từng bước:**  
> 1. **Tính các thông số động học:**  
>    * Tần số góc: $\omega = 2\pi f = 2\pi \times 2500\text{ Hz} \approx 15,708\text{ rad/s}$.  
>    * Vận tốc cực đại:  
>      $$v_{\max} = \omega A = (15,708\text{ rad/s}) \times (4.0 \times 10^{-6}\text{ m}) \approx 0.0628\text{ m/s} = 62.8\text{ mm/s}$$  
>    * Gia tốc cực đại:  
>      $$a_{\max} = \omega^2 A = (15,708\text{ rad/s})^2 \times (4.0 \times 10^{-6}\text{ m}) \approx 987\text{ m/s}^2 \approx 100.6\text{ g}$$  
>      *(với $g = 9.8\text{ m/s}^2$, con lắc chịu tải gia tốc gấp hơn 100 lần trọng trường Trái Đất!)*  
> 2. **Xác định chân dung pha:**  
>    * Trong không gian $(x, v)$, quỹ đạo là hình elip với bán trục theo $x$ là $A = 4.0\text{ }\mu\text{m}$ và bán trục theo $v$ là $v_{\max} = 0.0628\text{ m/s}$.  
>    * Trong không gian chuẩn hóa $(x, v/\omega)$, quỹ đạo là đường tròn bán kính $R = A = 4.0\text{ }\mu\text{m}$.

---

> ⚡ **GÓC NHÌN KỸ SƯ & BÀI TOÁN ĐÁNH ĐỔI (Engineering Takeaway 1.1):**  
> * **Bài toán Đánh đổi giữa Độ nhạy *(Sensitivity)* và Dải đo *(Dynamic Range)* trong cảm biến MEMS:**  
>   Li độ $x = \frac{a_{ext}}{\omega^2}$. Để cảm biến nhạy với các gia tốc nhỏ (tăng độ dời $x$ để mạch đo điện dung dễ phát hiện), kỹ sư phải giảm tần số riêng $\omega$ (làm lò xo vi mô mềm hơn). Tuy nhiên, giảm $\omega$ làm giảm tần số đáp ứng của cảm biến (cảm biến phản ứng chậm, không đo được dao động tần số cao). Kỹ sư bắt buộc phải đánh đổi giữa **Độ nhạy đo lường** và **Băng thông hoạt động**.

> ⚠️ **CẢNH BÁO LỖI PHỔ BIẾN (Common Pitfall 1.1):**  
> Nhiều học sinh nhầm lẫn rằng: *"Khi vận tốc bằng 0 thì gia tốc cũng bằng 0"*. Thực tế hoàn toàn ngược lại: Khi vật ở biên ($v = 0$), lò xo bị kéo giãn cực đại nên lực hồi phục và gia tốc đạt giá trị **cực đại** ($a = \pm \omega^2 A$). Gia tốc chỉ bằng 0 khi vật đi qua vị trí cân bằng ($x = 0$), nơi vận tốc lại đạt cực đại!

---

# MODULE 2 (1 GIỜ): ĐỘNG LỰC HỌC & BẢN CHẤT GIẾNG THẾ NĂNG TAYLOR
*(Dynamics, Harmonic Approximations & Potential Wells)*

### 1. Mục tiêu Đầu ra (Learning Objectives)
Sau khi hoàn thành Module 2, người học có khả năng:
* Thiết lập và giải phương trình vi phân dao động con lắc lò xo từ Định luật II Newton.
* Giải thích được câu hỏi bản chất: *Vì sao dao động điều hòa xuất hiện ở khắp mọi nơi trong tự nhiên?* bằng khai triển chuỗi Taylor quanh đáy giếng thế năng.
* Xác định độ cứng hiệu dụng $k_{eff} = V''(x_0)$ và tần số góc của một hệ vật lý bất kỳ khi biết hàm thế năng $V(x)$.
* Phân biệt vùng xấp xỉ tuyến tính và vùng phi tuyến tính trong con lắc đơn góc lớn.

---

### 2. Mâu thuẫn & Cơ chế Ngầm (The Conflict & Underlying Mechanism)
* **Mâu thuẫn (The Conflict):** Học sinh thường nghĩ chỉ có lò xo cơ học bằng kim loại mới có lực đàn hồi $F = -kx$. Nhưng liên kết giữa hai nguyên tử trong phân tử khí $H_2$, hay dao động của cây cầu treo, con tàu lắc lư trên sóng nước đều biểu hiện dao động điều hòa. Không hề có cái lò xo nào gắn giữa hai nguyên tử hydro!
* **Cơ chế ngầm (Underlying Mechanism):** Bản chất của lực hồi phục không nằm ở lò xo, mà nằm ở **hình học đáy của giếng thế năng *(Potential Well)***. Mọi trạng thái cân bằng bền trong vũ trụ đều tương ứng với một điểm cực tiểu của năng lượng thế. 

---

### 3. Mô hình Tư duy & Giới hạn Ẩn dụ (Grounded Mental Model)
* **Ẩn dụ chuẩn xác (The Metaphor):** Hãy tưởng tượng một **hòn bi đặt trong lòng chiếc chảo tròn trũng đáy**. Dù hình dáng mép trên của chiếc chảo có méo mó, bất đối xứng đến đâu, thì ngay tại điểm trũng nhất (đáy chảo), bất kỳ một đoạn cong vi mô trơn nào cũng có thể áp vừa khít một đường cong parabol $y = cx^2$. Khi ta đẩy nhẹ hòn bi ra khỏi đáy, sườn chảo cong dốc lên tác dụng phản lực đẩy hòn bi lăn trượt trở về đáy.
* ⚠️ **Giới hạn của ẩn dụ (Analogy Boundary):** Ẩn dụ hòn bi trong chảo chỉ đúng khi biên độ dịch chuyển nhỏ ($|x| \ll 1$). Nếu ta truyền cho hòn bi một cú hích cực mạnh, hòn bi sẽ bay vọt qua thành chảo và rơi ra ngoài. Trong vật lý phân tử, điều này tương đương với hiện tượng **phân ly liên kết hóa học *(Molecular Dissociation)*** khi năng lượng kích thích vượt qua năng lượng liên kết.

---

### 4. Dẫn xuất Toán học: Định luật Newton & Khai triển Taylor

> 📐 **DẪN XUẤT TOÁN HỌC (Mathematical Proof): Phương trình Vi phân Newton**  
> Xét vật khối lượng $m$ gắn lò xo độ cứng $k$ trượt không ma sát.  
> Lực kéo về theo định luật Hooke: $F = -kx$. Áp dụng Định luật II Newton $\Sigma F = m\ddot{x}$:
> $$m\ddot{x} = -kx \iff m\ddot{x} + kx = 0 \iff \ddot{x} + \frac{k}{m}x = 0$$
> Đặt $\omega_0^2 = \frac{k}{m}$ (với $\omega_0 > 0$), phương trình có dạng chuẩn tắc:
> $$\ddot{x} + \omega_0^2 x = 0$$
> Phương trình đặc trưng tương ứng: $r^2 + \omega_0^2 = 0 \implies r = \pm i\omega_0$.  
> Nghiệm thực là tổ hợp tuyến tính của hai nghiệm cơ sở:
> $$x(t) = A\cos(\omega_0 t + \varphi)$$
> với tần số góc riêng $\omega_0 = \sqrt{\frac{k}{m}}\text{ (rad/s)}$ và chu kỳ riêng $T_0 = 2\pi\sqrt{\frac{m}{k}}\text{ (s)}$.

---

### 5. Khai triển Taylor & Lời Giải Thích Bản Chất Phổ Quát của Dao Động Điều Hòa

Xét một hệ vật lý chuyển động trong một trường thế năng một chiều tổng quát $V(x)$. Lực tác dụng lên hạt liên hệ với thế năng qua đạo hàm:
$$F(x) = -\frac{dV}{dx}$$

Vị trí $x_0$ là **Vị trí Cân bằng (VTCB)** khi lực tổng hợp triệt tiêu:
$$F(x_0) = 0 \iff V'(x_0) = \left.\frac{dV}{dx}\right|_{x = x_0} = 0$$

Ta khai triển hàm thế năng $V(x)$ thành chuỗi Taylor xung quanh vị trí cân bằng $x_0$:
$$V(x) = V(x_0) + V'(x_0)(x - x_0) + \frac{1}{2!}V''(x_0)(x - x_0)^2 + \frac{1}{3!}V'''(x_0)(x - x_0)^3 + \dots$$

1. Chọn mốc thế năng tại đáy giếng: $V(x_0) = 0$.
2. Tại VTCB: $V'(x_0) = 0$ (đạo hàm bậc nhất triệt tiêu).
3. Vì $x_0$ là vị trí cân bằng bền, thế năng đạt cực tiểu, nên đạo hàm bậc hai phải dương:
   $$k_{eff} \equiv V''(x_0) = \left.\frac{d^2V}{dx^2}\right|_{x = x_0} > 0$$
4. Khi độ dời rất nhỏ ($|x - x_0| \ll 1$), các số hạng bậc cao $(x - x_0)^3, (x - x_0)^4 \approx 0$.

Do đó, thế năng thực tế thu hẹp về dạng parabol:
$$V(x) \approx \frac{1}{2} k_{eff} (x - x_0)^2$$
Lực hồi phục tương ứng:
$$F(x) = -\frac{dV}{dx} \approx -k_{eff}(x - x_0)$$

![Khai triển Taylor của giếng thế năng bất kỳ quanh vị trí cân bằng bền. Vùng màu vàng là miền dao động nhỏ nơi mô hình điều hòa chính xác tuyệt đối.](figures/fig1_3_potential_well.png)

> 🔬 **BẢN CHẤT VẬT LÝ & DẪN DẮT MẮT ĐỌC (Hình 1.3):**  
> * **Hãy nhìn vào đường cong màu xanh navy đậm $V(x)$:** Đây là thế năng liên kết phân tử thực tế, có dạng bất đối xứng (dốc đứng ở bên trái do lực đẩy đẩy Coulomb giữa các lõi nguyên tử, và là là ở bên phải khi kéo giãn phân tử).  
> * **Quan sát đường parabol nét đứt màu đỏ thẫm $V \approx \frac{1}{2}k_{eff}x^2$:** Đây là phép xấp xỉ Taylor bậc hai.  
> * **Hãy nhìn vào vùng phủ màu vàng nhạt ($|x| \le 0.35$):** Trong phạm vi biên độ nhỏ này, đường parabol đỏ và đường thực tế xanh **hoàn toàn trùng khít lên nhau**! Hạt vật lý màu cam chịu lực hồi phục $\vec{F} = -\frac{dV}{dx}\hat{i}$ hướng thẳng về đáy $x_0$.  
> * **Quan sát mũi tên đỏ ở góc phải:** Khi biên độ dạt ra ngoài vùng vàng ($x > 0.8$), đường cong thực tế tách rời khỏi parabol. Mô hình dao động điều hòa bị phá vỡ, tính phi tuyến tính xuất hiện!

---

### 6. Con lắc Đơn: Ví dụ về Giới hạn Góc Nhỏ

Phương trình động lực học chính xác của con lắc đơn chiều dài $\ell$, vật nặng $m$:
$$\ddot{\theta} + \frac{g}{\ell}\sin\theta = 0$$
Khai triển Taylor của $\sin\theta = \theta - \frac{\theta^3}{6} + \frac{\theta^5}{120} - \dots$
* **Khi góc nhỏ ($\theta \ll 1\text{ rad}$, thường lấy $\theta \le 10^\circ \approx 0.175\text{ rad}$):** Ta bỏ qua số hạng bậc ba $\theta^3/6$, phương trình trở thành tuyến tính điều hòa:
  $$\ddot{\theta} + \omega_0^2 \theta = 0 \implies \omega_0 = \sqrt{\frac{g}{\ell}}, \quad T_0 = 2\pi\sqrt{\frac{\ell}{g}}$$
* **Khi góc lớn ($\theta_0 > 10^\circ$):** Số hạng phi tuyến $-\theta^3/6$ làm giảm lực kéo về thực tế so với xấp xỉ tuyến tính. Con lắc đi chậm hơn ở biên, làm chu kỳ dao động bị kéo dài ra theo công thức hiệu chỉnh Borda:
  $$T \approx T_0 \left(1 + \frac{\theta_0^2}{16}\right)$$

---

### 7. Bài toán Tính số Thực tế (Worked Numerical Example 1.2)

> **Đề bài:** Một phân tử khí gồm hai nguyên tử có tương tác thế năng được mô tả gần đúng bởi thế Morse:
> $$V(r) = D_e \left[1 - e^{-a(r - r_0)}\right]^2$$
> Cho biết năng lượng liên kết $D_e = 7.0 \times 10^{-19}\text{ J}$, hằng số độ rộng $a = 2.0 \times 10^{10}\text{ m}^{-1}$, khoảng cách cân bằng $r_0 = 0.12\text{ nm} = 1.2 \times 10^{-10}\text{ m}$, và khối lượng rút gọn của phân tử $\mu = 1.5 \times 10^{-26}\text{ kg}$.  
> 1. Tính độ cứng hiệu dụng $k_{eff}$ của liên kết phân tử khi dao động nhỏ quanh $r_0$.  
> 2. Tính tần số dao động tự nhiên $f_0$ của phân tử.
> 
> **Lời giải từng bước:**  
> 1. **Tính độ cứng hiệu dụng bằng đạo hàm cấp 2:**  
>    * Đạo hàm cấp 1:  
>      $$V'(r) = 2 D_e \left[1 - e^{-a(r - r_0)}\right] \cdot \left[a e^{-a(r - r_0)}\right] = 2 a D_e \left[e^{-a(r - r_0)} - e^{-2a(r - r_0)}\right]$$  
>      Tại $r = r_0$, $V'(r_0) = 0$ (đúng là VTCB).  
>    * Đạo hàm cấp 2:  
>      $$V''(r) = 2 a D_e \left[-a e^{-a(r - r_0)} + 2a e^{-2a(r - r_0)}\right] = 2 a^2 D_e \left[2 e^{-2a(r - r_0)} - e^{-a(r - r_0)}\right]$$  
>      Thay $r = r_0$:  
>      $$k_{eff} = V''(r_0) = 2 a^2 D_e [2(1) - 1] = 2 a^2 D_e$$  
>    * Thay số thực tế:  
>      $$k_{eff} = 2 \times (2.0 \times 10^{10}\text{ m}^{-1})^2 \times (7.0 \times 10^{-19}\text{ J}) = 560\text{ N/m}$$  
> 2. **Tính tần số dao động:**  
>    * Tần số góc: $\omega_0 = \sqrt{\frac{k_{eff}}{\mu}} = \sqrt{\frac{560}{1.5 \times 10^{-26}}} \approx 6.11 \times 10^{13}\text{ rad/s}$.  
>    * Tần số dao động: $f_0 = \frac{\omega_0}{2\pi} \approx 9.72 \times 10^{12}\text{ Hz} = 9.72\text{ THz}$ (nằm trong vùng phổ hồng ngoại).

---

> ⚡ **GÓC NHÌN KỸ SƯ & BÀI TOÁN ĐÁNH ĐỔI (Engineering Takeaway 1.2):**  
> * **Bài toán Thiết kế Cầu treo & Hệ thống Chống Rung:**  
>   Mọi kết cấu công trình dân dụng (cầu treo, dầm nhà, chân đế turbine) chỉ hoạt động ổn định khi dao động nằm trong vùng tuyến tính của khai triển Taylor ($|x| \ll x_{linear}$). Khi biên độ dao động do gió bão vượt quá vùng tuyến tính, các hiệu ứng phi tuyến xuất hiện làm suy giảm độ cứng $k_{eff}$, gây ra hiện tượng mỏi kim loại *(Metal Fatigue)* hoặc sụp đổ cấu trúc dẻo. Kỹ sư phải thiết kế hệ số an toàn sao cho biên độ cực đại không bao giờ chạm đến ngưỡng phi tuyến.

> ⚠️ **CẢNH BÁO LỖI PHỔ BIẾN (Common Pitfall 1.2):**  
> Rất nhiều học sinh áp dụng công thức chu kỳ con lắc đơn $T = 2\pi\sqrt{\ell/g}$ cho góc lệch bất kỳ (ví dụ góc $60^\circ$ hoặc $90^\circ$). Ở góc $60^\circ$ ($\theta_0 \approx 1.047\text{ rad}$), sai số của công thức này lên tới hơn $7\%$. Công thức SGK chỉ là một **nghiệm xấp xỉ tuyến tính bậc nhất**, không phải chân lý tuyệt đối!

---

# MODULE 3 (1 GIỜ): NĂNG LƯỢNG BẢO TOÀN, ĐỊNH LÝ VIRIAL & TIÊU TÁN VI MÔ TẮT DẦN
*(Energy Conservation, Virial Theorem & Microscopic Dissipation)*

### 1. Mục tiêu Đầu ra (Learning Objectives)
Sau khi hoàn thành Module 3, người học có khả năng:
* Chứng minh định luật bảo toàn cơ năng bằng phép đạo hàm theo thời gian $\frac{dE}{dt} = 0$.
* Phân tích sự luân chuyển năng lượng với tần số gấp đôi $2\omega$ và chứng minh Định lý Virial $\langle E_d \rangle = \langle E_t \rangle = \frac{1}{2}E$.
* Giải thích cơ chế tiêu tán vi mô của lực cản nhớt và giải phương trình vi phân có cản.
* Phân biệt rõ ràng 3 chế độ vật lý: Dưới hạn *(Underdamped)*, Tới hạn *(Critically Damped)*, và Quá hạn *(Overdamped)*.

---

### 2. Mâu thuẫn & Cơ chế Ngầm (The Conflict & Underlying Mechanism)
* **Mâu thuẫn (The Conflict):** Mô hình cơ học lý tưởng bảo toàn năng lượng vĩnh cửu. Tuy nhiên, trong thực tế, không có con lắc nào dao động mãi mãi nếu không được cấp năng lượng. Năng lượng cơ học đã biến đi đâu?
* **Cơ chế ngầm (Underlying Mechanism):** Khi vật chuyển động trong không khí hoặc chất lỏng, bề mặt vật liên tục đâm sầm vào hàng tỷ phân tử chất lưu ngẫu nhiên. Mỗi va chạm truyền một phần động năng có trật tự của vật vĩ mô thành động năng chuyển động nhiệt hỗn loạn của các phân tử môi trường. Quá trình này tuân theo Định luật II Nhiệt động lực học: Năng lượng có trật tự (cơ năng) bị suy biến một chiều thành năng lượng hỗn loạn (nhiệt năng).

---

### 3. Mô hình Tư duy & Giới hạn Ẩn dụ (Grounded Mental Model)
* **Ẩn dụ chuẩn xác (The Metaphor):** Hãy hình dung năng lượng của hệ như **nước luân chuyển giữa hai bình thông nhau** (bình Động năng và bình Thế năng). Mỗi chu kỳ, nước chảy từ bình này sang bình kia hai lần. Khi có ma sát nhớt, đáy ống nối bị rò rỉ một lỗ nhỏ: mỗi lần nước chảy qua chảy lại, một lượng nước bị rỉ ra ngoài (nhiệt tiêu tán) cho đến khi hai bình cạn khô.
* ⚠️ **Giới hạn của ẩn dụ (Analogy Boundary):** Ẩn dụ lực cản nhớt tuyến tính $F_c = -bv$ chỉ đúng khi dòng chảy quanh vật là dòng chảy tầng *(Laminar Flow)* ở số Reynolds nhỏ ($Re < 1$). Khi vật chuyển động rất nhanh, dòng xoáy hỗn loạn *(Turbulent Flow)* xuất hiện, lực cản sẽ nhảy vọt lên tỉ lệ với bình phương vận tốc $F_c \propto v^2$, khiến tốc độ tiêu tán năng lượng nhanh hơn rất nhiều.

---

### 4. Dẫn xuất Toán học: Bảo toàn Cơ năng & Định lý Virial

Cơ năng toàn phần của hệ dao động:
$$E = E_d + E_t = \frac{1}{2}m v^2 + \frac{1}{2}k x^2$$

> 📐 **DẪN XUẤT TOÁN HỌC (Mathematical Proof): Đạo hàm Thời gian của Cơ năng**  
> Lấy đạo hàm hai vế của $E$ theo thời gian $t$:
> $$\frac{dE}{dt} = \frac{d}{dt}\left(\frac{1}{2}m v^2\right) + \frac{d}{dt}\left(\frac{1}{2}k x^2\right) = m v \frac{dv}{dt} + k x \frac{dx}{dt}$$
> Nhận thấy $\frac{dv}{dt} = \ddot{x}$ và $\frac{dx}{dt} = v$, đặt thừa số chung $v$:
> $$\frac{dE}{dt} = v(m\ddot{x} + kx)$$
> Nhưng từ phương trình vi phân chuyển động Newton, $m\ddot{x} + kx \equiv 0$ tại mọi thời điểm!  
> Do đó:
> $$\frac{dE}{dt} = 0 \iff E(t) = \text{const} = \frac{1}{2}kA^2 = \frac{1}{2}m\omega^2 A^2$$
> Cơ năng được bảo toàn tuyệt đối.

Thay $x = A\cos(\omega t + \varphi)$ và $v = -\omega A\sin(\omega t + \varphi)$:
$$E_t(t) = \frac{1}{2}kA^2 \cos^2(\omega t + \varphi) = \frac{1}{4}kA^2 [1 + \cos(2\omega t + 2\varphi)]$$
$$E_d(t) = \frac{1}{2}kA^2 \sin^2(\omega t + \varphi) = \frac{1}{4}kA^2 [1 - \cos(2\omega t + 2\varphi)]$$

* **Tần số biến thiên:** Cả động năng và thế năng đều dao động tuần hoàn với tần số góc $\omega_E = 2\omega$ và chu kỳ $T_E = T/2$.
* **Định lý Virial:** Lấy tích phân trung bình theo một chu kỳ thời gian $T$:
  $$\langle E_d \rangle = \frac{1}{T}\int_0^T E_d(t) dt = \frac{1}{4}kA^2 = \frac{1}{2}E, \quad \langle E_t \rangle = \frac{1}{4}kA^2 = \frac{1}{2}E \implies \langle E_d \rangle = \langle E_t \rangle = \frac{1}{2}E$$

![Dòng năng lượng trong dao động điều hòa: (a) Luân chuyển tuần hoàn theo thời gian; (b) Phân bố không gian theo li độ.](figures/fig1_4_energy.png)

> 🔬 **BẢN CHẤT VẬT LÝ & DẪN DẮT MẮT ĐỌC (Hình 1.4):**  
> * **Hãy nhìn vào đồ thị bên trái (a):** Đường nét đứt màu xanh navy $E_t(t)$ và đường liền màu xanh lá $E_d(t)$ dao động bù trừ nhau hoàn hảo dưới đường cơ năng bảo toàn màu đỏ $E = \text{const}$. Đường chấm màu xám nằm ngang chính xác tại $0.5E$ là giá trị trung bình thời gian theo Định lý Virial.  
> * **Di chuyển mắt sang đồ thị bên phải (b):** Đường parabol ngửa là thế năng $E_t(x)$, đường parabol úp là động năng $E_d(x)$.  
> * **Quan sát hai điểm màu cam tại $x = \pm A/\sqrt{2}$:** Đây là tọa độ duy nhất mà hai đường cong giao nhau, nghĩa là tại đó động năng bằng đúng thế năng: $E_d = E_t = E/2$.

---

### 5. Dao động Tắt dần & Ba Chế độ Vật lý

Khi có lực cản nhớt $\vec{F}_c = -b\vec{v}$ ($b > 0$, đơn vị $\text{N}\cdot\text{s/m}$ hay $\text{kg/s}$):
$$m\ddot{x} + b\dot{x} + kx = 0 \iff \ddot{x} + 2\gamma\dot{x} + \omega_0^2 x = 0$$
trong đó $\omega_0 = \sqrt{k/m}$ và $\gamma = \frac{b}{2m}$ là **hệ số tắt dần *(Damping Factor)***.

Phương trình đặc trưng: $r^2 + 2\gamma r + \omega_0^2 = 0 \implies r_{1,2} = -\gamma \pm \sqrt{\gamma^2 - \omega_0^2}$. Tự nhiên phân nhánh thành **3 chế độ**:

1. **Chế độ Dưới hạn *(Underdamped: $\gamma < \omega_0$)***:  
   $$x(t) = A_0 e^{-\gamma t}\cos(\omega_d t + \varphi) \quad \text{với } \omega_d = \sqrt{\omega_0^2 - \gamma^2}$$
   Hệ dao động với biên độ suy giảm theo hàm mũ bao quanh $A(t) = A_0 e^{-\gamma t}$.
2. **Chế độ Tới hạn *(Critically Damped: $\gamma = \omega_0$)***:  
   $$x(t) = (C_1 + C_2 t)e^{-\gamma t}$$
   Hệ trở về vị trí cân bằng trong **thời gian ngắn nhất mà không bị vọt lố *(No Overshoot)***.
3. **Chế độ Quá hạn *(Overdamped: $\gamma > \omega_0$)***:  
   $$x(t) = C_1 e^{r_1 t} + C_2 e^{r_2 t} \quad (r_1, r_2 < 0)$$
   Lực cản quá mạnh khiến hệ chuyển động chậm chạp, ì ạch bò về vị trí cân bằng.

![Ba chế độ động học của dao động cản (a) và chân dung pha điểm hút xoắn ốc (Spiral Attractor) (b).](figures/fig1_5_damped.png)

> 🔬 **BẢN CHẤT VẬT LÝ & DẪN DẮT MẮT ĐỌC (Hình 1.5):**  
> * **Hãy quan sát đường liền nét màu xanh lá ở đồ thị (a):** Đây là chế độ tới hạn ($\gamma = \omega_0$). Đường dốc lao thẳng xuống 0 nhanh nhất mà không hề cắt qua trục hoành.  
> * **Nhìn vào đường màu đỏ gạch chấm gạch:** Chế độ quá hạn mất rất nhiều thời gian mới bò dần về 0.  
> * **Quan sát chân dung pha bên phải (b):** Quỹ đạo màu xanh bắt đầu từ điểm đỏ $S_0(x_0, 0)$ xoắn ốc cuộn tròn dần vào gốc tọa độ $(0, 0)$ (điểm chữ X màu xanh lá). Gốc tọa độ đóng vai trò là một **Điểm hút xoắn ốc *(Spiral Attractor)***. Năng lượng cơ học bị triệt tiêu hoàn toàn.

---

### 6. Bài toán Tính số Thực tế (Worked Numerical Example 1.3)

> **Đề bài:** Một cụm giảm xóc của bánh xe ô tô có khối lượng tải hiệu dụng đè lên $m = 250\text{ kg}$, độ cứng lò xo $k = 40,000\text{ N/m}$.  
> 1. Tính hệ số cản tới hạn $b_c$ của ống nhún dầu thủy lực để hệ triệt tiêu dao động nhanh nhất mà không vọt lố.  
> 2. Nếu sau một thời gian sử dụng, dầu giảm xóc bị rò rỉ khiến hệ số cản thực tế tụt xuống chỉ còn $b = 1,200\text{ N}\cdot\text{s/m}$:  
>    a) Tính tần số góc tự nhiên $\omega_0$, hệ số tắt dần $\gamma$ và tần số dao động thực tế $\omega_d$.  
>    b) Tính độ giảm lượng loga $\delta$ và tỷ số biên độ giữa hai đỉnh dao động liên tiếp cách nhau một chu kỳ.
> 
> **Lời giải từng bước:**  
> 1. **Tính hệ số cản tới hạn:**  
>    * Tần số góc tự nhiên: $\omega_0 = \sqrt{\frac{k}{m}} = \sqrt{\frac{40,000}{250}} = \sqrt{160} \approx 12.65\text{ rad/s}$.  
>    * Điều kiện cản tới hạn: $\gamma_c = \omega_0 \implies \frac{b_c}{2m} = \omega_0$.  
>    * Suy ra:  
>      $$b_c = 2m\omega_0 = 2 \times 250\text{ kg} \times 12.65\text{ rad/s} \approx 6,325\text{ N}\cdot\text{s/m}$$  
> 2. **Khi bị rò rỉ dầu ($b = 1,200\text{ N}\cdot\text{s/m} < b_c$):**  
>    * Hệ số tắt dần: $\gamma = \frac{b}{2m} = \frac{1,200}{2 \times 250} = 2.40\text{ s}^{-1}$.  
>    * Tần số dao động thực tế:  
>      $$\omega_d = \sqrt{\omega_0^2 - \gamma^2} = \sqrt{160 - 2.4^2} = \sqrt{160 - 5.76} = \sqrt{154.24} \approx 12.42\text{ rad/s}$$  
>    * Chu kỳ dao động: $T_d = \frac{2\pi}{\omega_d} = \frac{2\pi}{12.42} \approx 0.506\text{ s}$.  
>    * Độ giảm lượng loga *(Logarithmic Decrement)*:  
>      $$\delta = \gamma T_d = (2.40\text{ s}^{-1}) \times (0.506\text{ s}) \approx 1.214$$  
>    * Tỷ số suy giảm biên độ giữa hai đỉnh liên tiếp:  
>      $$\frac{A(t)}{A(t + T_d)} = e^{\delta} = e^{1.214} \approx 3.37$$  
>      *(Nghĩa là sau mỗi lần nhún nảy 0.5 giây, biên độ dao động của xe chỉ giảm được khoảng 3.37 lần, xe sẽ bị bồng bềnh lắc lư vài nhịp trước khi dừng hẳn!)*

---

> ⚡ **GÓC NHÌN KỸ SƯ & BÀI TOÁN ĐÁNH ĐỔI (Engineering Takeaway 1.3):**  
> * **Bài toán Đánh đổi Thiết kế Hệ thống Treo Ô tô *(Suspension Design Trade-off)*:**  
>   Lý thuyết điều khiển chỉ ra rằng chế độ cản tới hạn ($\gamma = \omega_0$) dập tắt dao động nhanh nhất không vọt lố. Nhưng trong kỹ nghệ ô tô thực tế, các kỹ sư thường cố tình chọn chế độ **hơi dưới hạn một chút** ($\zeta = \frac{\gamma}{\omega_0} \approx 0.6 - 0.7$).  
>   * *Vì sao?* Nếu thiết lập $\gamma = \omega_0$, giảm xóc quá cứng, khi bánh xe va vào ổ gà dốc đứng, lực cản nhớt cực lớn $F_c = bv$ sẽ truyền thẳng xung lực va đập lên sàn xe, làm hành khách bị dằn xóc đau lưng. Chấp nhận cho xe nhún nhẹ 1 nhịp ($\zeta \approx 0.7$) là **sự đánh đổi tối ưu giữa Độ êm ái *(Passenger Comfort)* và Thời gian ổn định xe *(Settling Time)***.

> ⚠️ **CẢNH BÁO LỖI PHỔ BIẾN (Common Pitfall 1.3):**  
> Học sinh thường nghĩ chu kỳ dao động tắt dần $T_d = 2\pi/\sqrt{\omega_0^2 - \gamma^2}$ bằng chu kỳ riêng $T_0$. Thực tế, **lực cản luôn luôn làm chu kỳ dao động kéo dài ra** ($T_d > T_0$). Khi lực cản tăng đến mức $\gamma \to \omega_0$, chu kỳ $T_d \to \infty$, hệ hoàn toàn ngừng dao động!

---

# MODULE 4 (1 GIỜ): DAO ĐỘNG CƯỠNG BỨC, CỘNG HƯỞNG & ĐÁNH ĐỔI HỆ SỐ Q
*(Forced Oscillations, Resonance & Q-Factor Trade-offs)*

### 1. Mục tiêu Đầu ra (Learning Objectives)
Sau khi hoàn thành Module 4, người học có khả năng:
* Thiết lập phương trình vi phân dao động cưỡng bức và tìm nghiệm xác lập.
* Giải thích bản chất vật lý cốt lõi của hiện tượng cộng hưởng thông qua góc nhìn **bơm công suất tức thời cực đại** ($\vec{F}_{ext} \parallel \vec{v}$).
* Phân tích ý nghĩa vật lý của Hệ số phẩm chất $Q$ *(Quality Factor)*.
* Giải quyết bài toán đánh đổi kỹ thuật giữa Độ nhạy chọn lọc tần số và Băng thông đáp ứng trong các bộ lọc cơ học và mạch điện tử.

---

### 2. Mâu thuẫn & Cơ chế Ngầm (The Conflict & Underlying Mechanism)
* **Mâu thuẫn (The Conflict):** Khi ta đẩy một chiếc xích đu với lực rất nhỏ, tại sao chỉ cần chọn đúng nhịp thì chiếc xích đu có thể bay lên rất cao, nhưng nếu đẩy quá nhanh hoặc quá chậm thì xích đu gần như đứng yên? 
* **Cơ chế ngầm (Underlying Mechanism):** Đa số người học chỉ nhìn vào mẫu số toán học triệt tiêu khi tần số kích thích bằng tần số riêng $\Omega \to \omega_0$. Nhưng cơ chế ngầm thực sự nằm ở **sự ăn khớp về pha giữa Lực và Vận tốc**. Khi xảy ra cộng hưởng, góc trễ pha giữa li độ và ngoại lực đạt đúng $\pi/2$, điều này khiến cho **ngoại lực luôn luôn cùng hướng với vận tốc chuyển động** tại mọi thời điểm vi mô, đảm bảo tốc độ bơm công năng vào hệ đạt cực đại dương liên tục.

---

### 3. Mô hình Tư duy & Giới hạn Ẩn dụ (Grounded Mental Model)
* **Ẩn dụ chuẩn xác (The Metaphor):** Hãy hình dung bạn đang **đẩy một người ngồi trên xích đu**. Nếu bạn đẩy tới khi xích đu đang lao ngược về phía bạn, lực của bạn sẽ hãm xích đu lại (công âm). Nếu bạn đẩy khi xích đu đã lên tới đỉnh và bắt đầu rơi xuống, cú đẩy của bạn tiếp thêm động năng. Khi bạn căn đúng nhịp: cứ mỗi khi xích đu vừa đổi chiều và lao về phía trước, tay bạn đẩy đúng theo hướng nó đang chuyển động, mỗi cú đẩy đều cộng dồn năng lượng trọn vẹn vào hệ!
* ⚠️ **Giới hạn của ẩn dụ (Analogy Boundary):** Ẩn dụ xích đu là kích thích dạng xung rời rạc. Trong dao động cưỡng bức tuyến tính liên tục, lực tác dụng là sóng sin liên tục $F_0\cos(\Omega t)$. Nếu hệ có lực cản rất nhỏ ($Q \to \infty$), biên độ cộng hưởng trên lý thuyết sẽ tiến tới vô cùng, dẫn tới phá hủy kết cấu giòn (như hiện tượng vỡ ly thủy tinh khi gặp sóng âm đúng tần số).

---

### 4. Dẫn xuất Toán học: Nghiệm Xác lập & Công suất Bơm Năng lượng

Phương trình vi phân có ngoại lực tuần hoàn:
$$\ddot{x} + 2\gamma\dot{x} + \omega_0^2 x = \frac{F_0}{m}\cos(\Omega t)$$
trong đó $F_0$ là biên độ ngoại lực ($\text{N}$), $\Omega$ là tần số góc kích thích ($\text{rad/s}$).

Nghiệm xác lập lâu dài *(Steady-state Solution)* có dạng:
$$x_{ss}(t) = A(\Omega)\cos(\Omega t - \delta)$$

> 📐 **DẪN XUẤT TOÁN HỌC (Mathematical Proof): Biên độ và Độ trễ pha**  
> Dùng phương pháp biểu diễn số phức: Li độ $z = A e^{i(\Omega t - \delta)}$, ngoại lực $\mathcal{F} = \frac{F_0}{m}e^{i\Omega t}$.  
> Đạo hàm: $\dot{z} = i\Omega z$, $\ddot{z} = -\Omega^2 z$. Thay vào phương trình vi phân:
> $$(-\Omega^2 + 2i\gamma\Omega + \omega_0^2) A e^{i(\Omega t - \delta)} = \frac{F_0}{m}e^{i\Omega t} \implies [(\omega_0^2 - \Omega^2) + 2i\gamma\Omega] A e^{-i\delta} = \frac{F_0}{m}$$
> Lấy môđun hai vế:
> $$A(\Omega) = \frac{F_0/m}{\sqrt{(\omega_0^2 - \Omega^2)^2 + 4\gamma^2\Omega^2}}$$
> Lấy acgumen suy ra độ trễ pha $\delta$:
> $$\tan\delta = \frac{2\gamma\Omega}{\omega_0^2 - \Omega^2} \quad (0 \le \delta \le \pi)$$

![Đường cong cộng hưởng biên độ với các hệ số phẩm chất Q (a) và bước nhảy pha qua vùng cộng hưởng (b).](figures/fig1_6_resonance.png)

---

### 5. Giải mã Bản chất: Tốc độ Bơm Công suất Tức thời

Công suất tức thời mà ngoại lực truyền cho vật dao động:
$$P(t) = \vec{F}_{ext}(t) \cdot \vec{v}(t) = [F_0 \cos(\Omega t)] \cdot [-\Omega A \sin(\Omega t - \delta)]$$
Dùng công thức tích thành tổng:
$$P(t) = F_0 \Omega A \cos(\Omega t) \sin(\delta - \Omega t) = F_0 \Omega A [\sin\delta \cos^2(\Omega t) - \cos\delta \sin(\Omega t)\cos(\Omega t)]$$

Lấy trung bình theo một chu kỳ kích thích $T = 2\pi/\Omega$:
$$\langle P \rangle = \frac{1}{2} F_0 \Omega A(\Omega) \sin\delta$$

> 🔬 **BẢN CHẤT VẬT LÝ & DẪN DẮT MẮT ĐỌC (Hình 1.6):**  
> * **Hãy nhìn vào đồ thị bên phải (b) tại vị trí $\Omega = \omega_0$:** Đường màu cam đứt nét đánh dấu bước nhảy pha $\delta = \pi/2$.  
>   - Khi $\delta = \pi/2$, $\sin\delta = 1$ (đạt cực đại tuyệt đối!).  
>   - Vận tốc của vật: $v(t) = -\Omega A \sin(\Omega t - \pi/2) = \Omega A \cos(\Omega t)$.  
>   - Ngoại lực: $F_{ext}(t) = F_0 \cos(\Omega t)$.  
>   - $\implies \vec{F}_{ext}$ và $\vec{v}$ **cùng pha tuyệt đối tại mọi tích tắc thời gian**! Lực luôn luôn đẩy xuôi theo chiều chuyển động, bơm công suất vào hệ với hiệu suất 100%.  
> * **Nhìn sang đồ thị bên trái (a):** Tại $\Omega \approx \omega_0$, biên độ vọt lên thành một đỉnh nhọn hoắt. Đỉnh càng cao và càng nhọn khi hệ số phẩm chất $Q$ càng lớn (đường đỏ $Q = 10$).  
> * **Nhìn vào hai vùng rìa của Hình 1.6a:**  
>   - Vùng tĩnh ($\Omega \ll \omega_0$): Biên độ thấp không đổi $A \approx \frac{F_0}{k}$.  
>   - Vùng cách ly rung ($\Omega \gg \omega_0$): Biên độ suy giảm nhanh về 0 theo quy luật $A \propto 1/\Omega^2$ (nguyên lý của bệ chống rung cho kính hiển vi).

---

### 6. Hệ số Phẩm chất Q (Quality Factor)

Hệ số phẩm chất $Q$ được định nghĩa bằng tỷ số giữa năng lượng tích trữ và năng lượng tiêu tán trong một radian dao động:
$$Q \equiv 2\pi \frac{\text{Năng lượng tích trữ}}{\text{Năng lượng tiêu hao trong 1 chu kỳ}} = \frac{\omega_0}{2\gamma} = \frac{\sqrt{mk}}{b}$$

* Độ rộng dải thông tại nửa công suất *(Half-power Bandwidth)*: $\Delta \omega \approx \frac{\omega_0}{Q}$.

---

### 7. Bài toán Tính số Thực tế (Worked Numerical Example 1.4)

> **Đề bài:** Một bộ dao động tinh thể thạch anh *(Quartz Crystal Resonator)* trong đồng hồ điện tử có khối lượng hiệu dụng $m = 1.0 \times 10^{-6}\text{ kg}$, tần số dao động danh định $f_0 = 32.768\text{ kHz}$, và hệ số phẩm chất rất cao $Q = 100,000$.  
> 1. Tính độ cứng hiệu dụng $k_{eff}$ và hệ số cản nội tại $b$ của tinh thể.  
> 2. Tính độ rộng dải thông $\Delta f$ của bộ cộng hưởng. Giải thích ý nghĩa của con số này đối với độ chính xác của đồng hồ.
> 
> **Lời giải từng bước:**  
> 1. **Tính độ cứng và hệ số cản:**  
>    * Tần số góc riêng: $\omega_0 = 2\pi f_0 = 2\pi \times 32,768\text{ Hz} \approx 205,887\text{ rad/s}$.  
>    * Độ cứng hiệu dụng:  
>      $$k_{eff} = m\omega_0^2 = (1.0 \times 10^{-6}\text{ kg}) \times (205,887\text{ rad/s})^2 \approx 42,390\text{ N/m}$$  
>    * Hệ số cản nội tại:  
>      $$Q = \frac{m\omega_0}{b} \implies b = \frac{m\omega_0}{Q} = \frac{1.0 \times 10^{-6} \times 205,887}{100,000} \approx 2.06 \times 10^{-6}\text{ N}\cdot\text{s/m}$$  
>      *(Lực cản tiêu tán nội tại vô cùng bé!)*  
> 2. **Tính dải thông và độ chính xác:**  
>    * Độ rộng dải thông:  
>      $$\Delta f = \frac{f_0}{Q} = \frac{32,768\text{ Hz}}{100,000} \approx 0.328\text{ Hz}$$  
>    * **Ý nghĩa:** Đường cong cộng hưởng của tinh thể cực kỳ sắc nhọn. Nếu có bất kỳ nhiễu loạn cơ học hoặc nhiệt độ nào lệch khỏi tần số $32,768\text{ Hz}$ quá $0.33\text{ Hz}$, tinh thể sẽ từ chối dao động. Điều này giúp đồng hồ chỉ sai số chưa tới 1 giây sau mỗi tháng hoạt động!

---

> ⚡ **GÓC NHÌN KỸ SƯ & BÀI TOÁN ĐÁNH ĐỔI (Engineering Takeaway 1.4):**  
> * **Bài toán Đánh đổi giữa Độ chọn lọc *(Selectivity)* và Băng thông *(Bandwidth)*:**  
>   $$\Delta \omega = \frac{\omega_0}{Q}$$  
>   - **Khi thiết kế Bộ chọn đài Radio / Cảm biến tần số:** Kỹ sư muốn $Q$ cực lớn để dải thông $\Delta \omega$ thật hẹp, giúp lọc sạch kênh cần nghe mà không bị lẫn sóng từ đài phát lân cận.  
>   - **Khi thiết kế Loa âm thanh / Cảm biến rung địa chấn:** Kỹ sư cần $Q$ thấp (khoảng $0.5 - 1.0$) để băng thông rộng, đảm bảo loa phát đều mọi nốt nhạc trầm bổng từ $20\text{ Hz}$ đến $20\text{ kHz}$ mà không bị "hét to" cục bộ ở một nốt cộng hưởng nào!

> ⚠️ **CẢNH BÁO LỖI PHỔ BIẾN (Common Pitfall 1.4):**  
> Nhiều tài liệu viết rằng: *"Tần số xảy ra cộng hưởng biên độ luôn bằng đúng tần số riêng $\omega_0$"*. Điều này chỉ đúng khi không có ma sát ($\gamma = 0$). Khi có lực cản, đỉnh cộng hưởng biên độ thực sự bị lệch về phía tần số thấp hơn một khoảng:
> $$\Omega_R = \sqrt{\omega_0^2 - 2\gamma^2} = \omega_0\sqrt{1 - \frac{1}{2Q^2}}$$
> Chỉ khi hệ có $Q \gg 1$ thì $\Omega_R \approx \omega_0$.

---

# BỘ CÂU HỎI PHẢN XẠ TÌNH HUỐNG THỰC CHIẾN (DIAGNOSTIC SCENARIO TESTING)

### Tình huống 1: Thiết kế Giảm chấn Khối lượng cho Tòa nhà Chọc trời (Tuned Mass Damper - TMD)
> Tòa tháp Taipei 101 (cao 508 m) tại Đài Loan chịu tải trọng gió bão cực mạnh khiến đỉnh tháp dao động với chu kỳ tự nhiên $T_1 \approx 7.0\text{ s}$. Để chống rung, các kỹ sư treo một quả cầu thép khổng lồ nặng 660 tấn ở tầng 87 đóng vai trò là một con lắc phụ.  
> 1. Kỹ sư phải chọn chiều dài dây treo $\ell$ của quả cầu bằng bao nhiêu để quả cầu dao động đồng điệu với nhịp lắc của tòa nhà?  
> 2. Hãy giải thích cơ chế năng lượng: Vì sao quả cầu lắc lư lại triệt tiêu được dao động của tòa tháp? Quả cầu hút năng lượng từ đâu và xả năng lượng đi đâu qua các piston thủy lực gắn quanh nó?

### Tình huống 2: Đánh đổi trong Thiết kế Cảm biến Đo Rung Động (Seismometer vs Accelerometer)
> Cùng một cấu trúc lò xo - khối nặng $m$ - vật cản $b$, nhưng:  
> - Máy đo địa chấn *(Seismometer)* dùng để đo độ dời của vỏ Trái Đất.  
> - Gia tốc kế *(Accelerometer)* dùng để đo gia tốc của xe hơi.  
> Dựa vào đồ thị đáp ứng biên độ Hình 1.6a, hãy giải thích:  
> 1. Vì sao máy đo địa chấn phải có tần số riêng $\omega_0$ rất bé (hoạt động ở vùng quán tính $\Omega \gg \omega_0$)?  
> 2. Vì sao gia tốc kế phải có tần số riêng $\omega_0$ rất lớn (hoạt động ở vùng tĩnh $\Omega \ll \omega_0$)? Kỹ sư phải đánh đổi điều gì khi tăng $\omega_0$?

### Tình huống 3: Bản chất Tự dao động của Nhịp tim và Đồng hồ Quả lắc (Van der Pol Oscillator)
> Một con lắc đồng hồ quả lắc không bao giờ bị dừng lại dù có ma sát, nhưng cũng không cần cắm điện xoay chiều có tần số kích thích $\Omega$. Nó lấy năng lượng từ một quả tạ rơi chậm thông qua cơ cấu hồi chuyển *(Escapement mechanism)*.  
> 1. Hãy phân tích cơ chế: Quả tạ rơi cung cấp năng lượng liên tục một chiều, tại sao cơ cấu hồi lại biến thành dao động tuần hoàn?  
> 2. Trong không gian pha, tại sao hệ này không cuộn vào điểm hút $(0,0)$ như dao động tắt dần, mà lại tự ổn định trên một đường cong chu trình kín gọi là **Chu trình Giới hạn *(Limit Cycle)***?

---

## BẢNG ĐỐI SOÁT TỔNG KẾT NGUYÊN LÝ 3 TẦNG CHƯƠNG 1

| Hiện tượng | Tầng 1: Bản chất Vật lý Vi mô | Tầng 2: Mô hình Toán & Lượng hóa | Tầng 3: Quyết định Thiết kế & Đánh đổi |
| :--- | :--- | :--- | :--- |
| **Dao động điều hòa** | Lực hồi phục kéo hạt về VTCB; thế năng parabol giam hãm. | $\ddot{x} + \omega_0^2 x = 0 \implies x = A\cos(\omega_0 t + \varphi)$. Khai triển Taylor đáy giếng: $k_{eff} = V''(x_0)$. | Đánh đổi giữa Độ nhạy $\propto 1/\omega_0^2$ và Băng thông đáp ứng $\omega_0$ trong cảm biến MEMS. |
| **Không gian Pha** | Cặp biến trạng thái $(x, v)$ xác định tương lai tất định. | $x^2 + (v/\omega)^2 = A^2$. Định lý Liouville bảo toàn diện tích pha. | Kiểm soát quỹ đạo trạng thái trong các bộ chấp hành cơ điện tử. |
| **Tắt dần** | Va chạm phân tử tán xạ động năng có trật tự thành nhiệt hỗn loạn. | $\ddot{x} + 2\gamma\dot{x} + \omega_0^2 x = 0$. Ba chế độ từ nghiệm đa thức đặc trưng. | Hệ thống treo xe hơi: chọn $\gamma \approx 0.7\omega_0$ để cân bằng giữa Thời gian dập tắt và Độ êm ái. |
| **Cộng hưởng** | Ngoại lực đồng pha vận tốc ($\delta = \pi/2$), bơm công suất tức thời cực đại. | $A(\Omega) = \frac{F_0/m}{\sqrt{(\omega_0^2-\Omega^2)^2+4\gamma^2\Omega^2}}$, $\langle P \rangle = \frac{1}{2}F_0\Omega A \sin\delta$. | Bộ lọc/Cảm biến: Đánh đổi giữa Độ chọn lọc sắc nhọn ($Q$ cao) và Băng thông truyền dữ liệu ($Q$ thấp). |
