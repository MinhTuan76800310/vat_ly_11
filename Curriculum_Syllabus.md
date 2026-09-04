# KHUNG CHƯƠNG TRÌNH & LỘ TRÌNH BIÊN SOẠN
## VẬT LÍ 11 CHUYÊN SÂU: BẢN CHẤT VẬT LÍ & NỀN TẢNG TOÁN HỌC
*(Dựa trên Chương trình GDPT 2018 - Đối chiếu SGK Kết nối tri thức, Cánh Diều, Chân trời sáng tạo)*

---

## I. MỤC TIÊU CỐT LÕI CỦA BỘ TÀI LIỆU

1. **Xóa bỏ tư duy "học vẹt công thức & mẹo giải số học":** Học sinh thường chỉ biết ráp số vào công thức mà không hiểu công thức sinh ra từ đâu, điều kiện biên của nó là gì và khi nào nó sụp đổ.
2. **Khôi phục ngôn ngữ tự nhiên của Vật lý – Toán học Giải tích:** 
   - SGK hiện hành phải né tránh vi tích phân do khung phân phối môn Toán. Bộ tài liệu này đưa công cụ toán học (đạo hàm, vi phân, tích phân, phương trình vi phân tuyến tính sơ cấp, đại số số phức) trở lại đúng vị trí của nó: *chiếc chìa khóa mở cánh cửa bản chất*.
3. **Làm rõ Cơ chế vi mô (Microscopic mechanism):** Mọi định luật vĩ mô (nhiệt Joule, điện trở, sóng đàn hồi, phân cực...) đều được soi chiếu từ hành vi của các hạt (nguyên tử, electron, photon).
4. **Sợi chỉ đỏ xuyên suốt:** Quy tụ mọi hiện tượng về các nguyên lý phổ quát của vũ trụ:
   - **Nguyên lý cực trị & Tính đối xứng**
   - **Định luật bảo toàn năng lượng và động lượng**
   - **Trạng thái cân bằng bền và giếng thế năng**

---

## II. PHƯƠNG PHÁP BIÊN SOẠN: CHUẨN MỰC "5 TẦNG TƯ DUY" (5-LAYER PEDAGOGY)

Mỗi bài học trong bộ tài liệu sẽ được biên soạn đồng bộ theo 5 tầng cấu trúc:

```
┌─────────────────────────────────────────────────────────────┐
│  TẦNG 1: HIỆN TƯỢNG, TRỰC GIÁC & CÂU HỎI KHỞI PHÁT          │
│  - Quan sát thực tế, nghịch lý thị giác/nhận thức.          │
│  - Câu hỏi "Tại sao?" thúc đẩy nhu cầu tìm hiểu bản chất.   │
├─────────────────────────────────────────────────────────────┤
│  TẦNG 2: MÔ HÌNH HÓA VẬT LÝ (PHYSICAL MODELING)             │
│  - Lý tưởng hóa hệ vật lý (bỏ qua ma sát, điện tích điểm...).│
│  - Xác lập hệ quy chiếu và các định luật cơ sở (Newton,...).│
├─────────────────────────────────────────────────────────────┤
│  TẦNG 3: NGÔN NGỮ TOÁN HỌC & GIẢI TÍCH (MATHEMATICAL RIGOR) │
│  - Thiết lập phương trình vi phân / tích phân.               │
│  - Dẫn xuất tường minh nghiệm (không thừa nhận công thức).  │
├─────────────────────────────────────────────────────────────┤
│  TẦNG 4: BẢN CHẤT VẬT LÝ, NĂNG LƯỢNG & CƠ CHẾ VI MÔ         │
│  - Năng lượng biến đổi thế nào? Dòng năng lượng đi đâu?      │
│  - Cơ chế va chạm, tương tác hạt vi mô đằng sau hiện tượng.  │
├─────────────────────────────────────────────────────────────┤
│  TẦNG 5: THÍ NGHIỆM TƯ DUY, PHẢN BIỆN & ỨNG DỤNG MỞ RỘNG     │
│  - Phân tích thứ nguyên (Dimensional Analysis).             │
│  - Kiểm tra các trường hợp giới hạn (x -> 0, x -> ∞).       │
│  - Ứng dụng thực tiễn trong kỹ thuật hiện đại.               │
└─────────────────────────────────────────────────────────────┘
```

---

## III. NỘI DUNG CHI TIẾT 4 CHỦ ĐỀ TRỌNG TÂM

---

### CHỦ ĐỀ 1: DAO ĐỘNG (OSCILLATIONS)

#### Bài 1.1: Động học Dao động Điều hòa – Từ Phép Đạo hàm đến Không gian Pha
* **SGK hiện hành:** Đưa công thức $x = A\cos(\omega t + \varphi)$, suy ra $v$ và $a$ bằng hình chiếu chuyển động tròn đều hoặc công thức có sẵn.
* **Nội dung bổ sung sâu:**
  - Định nghĩa chuẩn: Dao động điều hòa là nghiệm của mối quan hệ gia tốc tỉ lệ nghịch với li độ: $a(t) = -\omega^2 x(t)$.
  - Đạo hàm tường minh: $v(t) = \frac{dx}{dt}$, $a(t) = \frac{d^2x}{dt^2}$.
  - Biểu diễn số phức (Euler): $z(t) = A e^{i(\omega t + \varphi)}$, $x(t) = \text{Re}\{z(t)\}$. Mối quan hệ hình học của nhân tử $i = e^{i\pi/2}$ với sự sớm pha $\pi/2$.
  - **Không gian pha (Phase Space):** Khảo sát quỹ đạo trong hệ toạ độ $(x, v/\omega)$. Quỹ đạo ellipse khép kín và tính bảo toàn diện tích pha (Định lý Liouville sơ cấp).

#### Bài 1.2: Động lực học Dao động & Bản chất Giếng Thế Năng (Potential Well)
* **SGK hiện hành:** Áp dụng định luật II Newton cho lò xo $F = -kx$.
* **Nội dung bổ sung sâu:**
  - Thiết lập phương trình vi phân thuần nhất bậc 2 hệ số hằng:
    $$\frac{d^2 x}{dt^2} + \omega_0^2 x = 0 \quad (\text{với } \omega_0 = \sqrt{k/m})$$
  - Phương pháp đa thức đặc trưng tìm nghiệm dạng hàm điều hòa.
  - **Bản chất của Vị trí Cân bằng:** Khai triển chuỗi Taylor hàm thế năng $V(x)$ quanh điểm cực tiểu $x_0$:
    $$V(x) = V(x_0) + V'(x_0)(x - x_0) + \frac{1}{2} V''(x_0)(x - x_0)^2 + \mathcal{O}((x - x_0)^3)$$
    Vì tại VTCB $V'(x_0) = 0$ và $V''(x_0) > 0$ (cực tiểu), nên với dao động nhỏ:
    $$V(x) \approx \frac{1}{2} k_{eff} (x - x_0)^2 \quad \Rightarrow F_{eff} = -\frac{dV}{dx} = -k_{eff}(x - x_0)$$
    $\rightarrow$ **Chân lý vật lý cốt lõi:** *Hầu như mọi dao động nhỏ quanh vị trí cân bằng bền trong vũ trụ đều là dao động điều hoà.*

#### Bài 1.3: Con lắc Đơn & Giới hạn Góc Nhỏ (Non-linear Oscillations)
* **SGK hiện hành:** Thừa nhận $\sin\alpha \approx \alpha$ khi $\alpha < 10^\circ$.
* **Nội dung bổ sung sâu:**
  - Phương trình vi phân chính xác: $\ddot{\theta} + \frac{g}{\ell} \sin\theta = 0$.
  - Đánh giá sai số khi dùng xấp xỉ Taylor $\sin\theta \approx \theta - \frac{\theta^3}{6}$.
  - Sự phụ thuộc của chu kỳ vào biên độ góc lớn (Tích phân elliptic loại 1 sơ cấp): $T \approx T_0 \left(1 + \frac{\theta_0^2}{16}\right)$.

#### Bài 1.4: Năng lượng trong Dao động – Bảo toàn, Biến thiên & Giá trị Trung bình
* **SGK hiện hành:** $E = \frac{1}{2}mv^2 + \frac{1}{2}kx^2 = \text{const}$.
* **Nội dung bổ sung sâu:**
  - Chứng minh bảo toàn bằng giải tích: $\frac{dE}{dt} = v(m a + k x) = v \cdot 0 = 0$.
  - Tính tích phân lấy giá trị trung bình theo một chu kỳ:
    $$\langle E_d \rangle = \frac{1}{T}\int_0^T E_d(t) dt = \frac{1}{4}kA^2 = \frac{1}{2}E, \quad \langle E_t \rangle = \frac{1}{2}E$$
  - Định lý Virial áp dụng cho dao động điều hòa: $\langle E_d \rangle = \langle E_t \rangle$.

#### Bài 1.5: Dao động Tắt dần & Tiêu tán Năng lượng (Damped Oscillations)
* **SGK hiện hành:** Nêu ma sát làm biên độ giảm dần theo thời gian.
* **Nội dung bổ sung sâu:**
  - Lực cản nhớt tỉ lệ bậc nhất với vận tốc: $F_c = -b v$.
  - Phương trình vi phân: $\ddot{x} + 2\gamma \dot{x} + \omega_0^2 x = 0$ (với $\gamma = \frac{b}{2m}$).
  - Khảo sát 3 chế độ vật lý từ nghiệm phương trình đặc trưng:
    1. Tắt dần dưới hạn ($\gamma < \omega_0$): Dao động với biên độ giảm theo hàm mũ $e^{-\gamma t}$.
    2. Tới hạn ($\gamma = \omega_0$): Hệ về VTCB nhanh nhất không qua dao động (ứng dụng giảm xóc ô tô, con trỏ cân điện tử).
    3. Quá hạn ($\gamma > \omega_0$): Hệ chuyển động chậm chạp về VTCB.
  - Cơ chế vi mô: Động năng có trật tự của vật bị tán xạ thành nhiệt năng hỗn loạn của các phân tử môi trường.

#### Bài 1.6: Dao động Cưỡng bức & Hiện tượng Cộng hưởng (Resonance & Q-factor)
* **SGK hiện hành:** Khi tần số ngoại lực bằng tần số riêng $f = f_0$ thì biên độ cực đại.
* **Nội dung bổ sung sâu:**
  - Phương trình vi phân cưỡng bức: $\ddot{x} + 2\gamma \dot{x} + \omega_0^2 x = \frac{F_0}{m}\cos(\Omega t)$.
  - Nghiệm xác lập (Steady-state solution): Biên độ $A(\Omega) = \frac{F_0/m}{\sqrt{(\omega_0^2 - \Omega^2)^2 + 4\gamma^2\Omega^2}}$.
  - Tần số cộng hưởng biên độ thực sự: $\Omega_R = \sqrt{\omega_0^2 - 2\gamma^2}$ (khác biệt với $\omega_0$ khi có cản).
  - Bản chất vật lý của cộng hưởng: Pha của ngoại lực ăn khớp với vận tốc ($\vec{F}_{ext}$ cùng chiều $\vec{v}$), công suất tức thời $P(t) = \vec{F}_{ext} \cdot \vec{v}$ luôn dương $\rightarrow$ tốc độ bơm năng lượng vào hệ đạt cực đại.
  - Hệ số phẩm chất $Q = \frac{\omega_0}{2\gamma}$ và độ sắc nhọn của đường cong cộng hưởng.

---

### CHỦ ĐỀ 2: SÓNG (WAVES)

#### Bài 2.1: Bản chất Sóng Cơ & Phương trình Vi phân Sóng 1D (Wave Equation)
* **SGK hiện hành:** Nêu sóng là dao động lan truyền trong không gian. Viết phương trình $u = A\cos(\omega t - \frac{2\pi x}{\lambda})$.
* **Nội dung bổ sung sâu:**
  - Khái niệm hàm hai biến $u(x, t)$: Phân biệt vận tốc dao động phần tử $v_{pt} = \frac{\partial u}{\partial t}$ với tốc độ truyền pha $v_{pha} = \frac{\lambda}{T} = \frac{\omega}{k}$.
  - Độ dốc sóng (Strain): $\frac{\partial u}{\partial x}$.
  - **Dẫn xuất Phương trình Sóng từ Định luật II Newton cho chuỗi lò xo vi mô:**
    $$\frac{\partial^2 u}{\partial t^2} = v^2 \frac{\partial^2 u}{\partial x^2}$$
  - Nghiệm tổng quát d'Alembert: $u(x, t) = f(x - vt) + g(x + vt)$ (sóng chạy sang phải và sang trái).

#### Bài 2.2: Sóng Ngang, Sóng Dọc & Môi trường Đàn hồi Vi mô
* **SGK hiện hành:** Mô tả định tính sóng ngang vuông góc, sóng dọc trùng phương truyền.
* **Nội dung bổ sung sâu:**
  - Cơ chế vi mô: Sóng truyền được nhờ liên kết giữa các nguyên tử lân cận.
  - Vì sao sóng ngang chỉ truyền được trong chất rắn (và mặt thoáng chất lỏng do căng bề mặt)? $\rightarrow$ Khả năng chống lại biến dạng trượt (Shear modulus).
  - Vì sao chất khí và lòng chất lỏng chỉ truyền sóng dọc? $\rightarrow$ Chất lưu chỉ có tính đàn hồi thể tích (Bulk modulus), không có lực hồi phục khi bị trượt.
  - Năng lượng và Mật độ dòng năng lượng (Vectơ Umov sơ cấp).

#### Bài 2.3: Sóng Dừng – Hiện tượng Giam hãm Năng lượng & Bài toán Biên
* **SGK hiện hành:** Nêu nút, bụng, điều kiện chiều dài dây $L = k\frac{\lambda}{2}$.
* **Nội dung bổ sung sâu:**
  - Cơ chế phản xạ sóng tại ranh giới:
    + Đầu cố định: Lực phản kháng của điểm tựa tạo sóng phản xạ ngược pha ($\Delta \varphi = \pi$).
    + Đầu tự do: Sóng phản xạ cùng pha ($\Delta \varphi = 0$).
  - Toán học của sóng dừng (Tách biến Fourier):
    $$u(x, t) = A\cos(\omega t - kx) - A\cos(\omega t + kx) = [2A\sin(kx)] \sin(\omega t)$$
  - Bản chất vật lý: Sóng dừng **không truyền năng lượng đi xa**; năng lượng dao động bị giam hãm luân chuyển tuần hoàn giữa thế năng biến dạng và động năng tại mỗi khoang sóng.

#### Bài 2.4: Giao thoa Sóng – Nguyên lý Chồng chất & Tái Phân bố Năng lượng
* **SGK hiện hành:** Công thức cực đại $\Delta d = k\lambda$, cực tiểu $\Delta d = (k+0.5)\lambda$.
* **Nội dung bổ sung sâu:**
  - Nguyên lý chồng chất tuyến tính (Linear Superposition Principle).
  - Độ lệch pha do hiệu quang trình: $\Delta \varphi = \frac{2\pi}{\lambda}(d_2 - d_1)$.
  - **Bảo toàn năng lượng trong giao thoa:** Tại cực tiểu triệt tiêu, năng lượng không mất đi; tại cực đại, năng lượng gấp 4 lần mỗi sóng thành phần chứ không phải gấp đôi ($I \propto A^2$). Tích phân năng lượng trên toàn bộ không gian được bảo toàn tuyệt đối $\rightarrow$ Giao thoa là sự *tái phân bố không gian của mật độ năng lượng*.

#### Bài 2.5: Sóng Điện từ & Bản chất Trường Maxwell Sơ cấp
* **SGK hiện hành:** Thang sóng điện từ, tính chất truyền trong chân không.
* **Nội dung bổ sung sâu:**
  - Sự thống nhất Điện - Từ: Điện trường biến thiên sinh ra từ trường xoáy; từ trường biến thiên sinh ra điện trường xoáy.
  - Bản chất sóng ngang tự lan truyền trong chân không với tốc độ $c = \frac{1}{\sqrt{\varepsilon_0 \mu_0}}$.
  - Bộ ba vectơ trực giao định hướng: $\vec{E} \perp \vec{B} \perp \vec{v}$ tuân theo quy tắc bàn tay phải.
  - Vectơ Poynting $\vec{S} = \frac{1}{\mu_0} (\vec{E} \times \vec{B})$: Mật độ dòng năng lượng điện từ.

#### Bài 2.6: Tán sắc, Nhiễu xạ & Giao thoa Ánh sáng (Thí nghiệm Young)
* **SGK hiện hành:** Công thức khoảng vân $i = \frac{\lambda D}{a}$.
* **Nội dung bổ sung sâu:**
  - Dẫn xuất hình học và giải tích của hiệu đường đi $\Delta d \approx \frac{ax}{D}$ khi $D \gg a$.
  - Phân bố cường độ sáng theo góc: $I(\theta) = I_0 \cos^2\left(\frac{\pi a \sin\theta}{\lambda}\right)$.
  - Bản chất lưỡng tính sóng - hạt của ánh sáng: Giao thoa từng photon đơn lẻ (Bản chất xác suất lượng tử sơ cấp).

---

### CHỦ ĐỀ 3: ĐIỆN TRƯỜNG (ELECTRIC FIELD)

#### Bài 3.1: Định luật Coulomb & Bản chất của Khái niệm "Trường"
* **SGK hiện hành:** Công thức $F = k\frac{|q_1 q_2|}{r^2}$.
* **Nội dung bổ sung sâu:**
  - Vì sao Newton bế tắc với khái niệm "Tác dụng tức thời từ xa" (Action-at-a-distance)?
  - Khái niệm **Trường (Field)** của Faraday: Điện tích tạo ra trường xung quanh nó; trường này lan truyền với vận tốc hữu hạn $c$; trường cục bộ tại vị trí hạt thứ hai tác dụng lực lên hạt đó.
  - Viết dưới dạng vectơ chuẩn: $\vec{F}_{12} = \frac{1}{4\pi\varepsilon_0}\frac{q_1 q_2}{r_{12}^2}\hat{r}_{12}$.
  - Nguyên lý chồng chất điện trường $\vec{E} = \sum \vec{E}_i$.

#### Bài 3.2: Cường độ Điện trường & Định luật Gauss Sơ cấp (Gauss's Law)
* **SGK hiện hành:** Tính $E$ cho điện tích điểm và điện trường đều giữa 2 bản tụ.
* **Nội dung bổ sung sâu:**
  - Điện trường của phân bố điện tích liên tục: $d\vec{E} = \frac{1}{4\pi\varepsilon_0}\frac{dq}{r^2}\hat{r} \Rightarrow \vec{E} = \int d\vec{E}$.
  - Ý niệm Thông lượng điện trường (Electric Flux): $\Phi_E = \int \vec{E} \cdot d\vec{S}$.
  - **Định luật Gauss (Dạng tích phân trực quan):**
    $$\oint_{\mathcal{S}} \vec{E} \cdot d\vec{S} = \frac{Q_{\text{trong}}}{\varepsilon_0}$$
  - Ứng dụng tính điện trường các cấu hình có tính đối xứng cao: Mặt phẳng vô hạn tích điện đều, mặt cầu tích điện, dây dẫn thẳng dài vô hạn.

#### Bài 3.3: Công Lực Điện, Điện thế & Gradient Điện trường
* **SGK hiện hành:** Công $A = qEd$, điện thế $U = Ed$ trong điện trường đều.
* **Nội dung bổ sung sâu:**
  - Tích phân đường của công lực điện: $A_{AB} = \int_A^B q \vec{E} \cdot d\vec{r}$.
  - Chứng minh lực tĩnh điện là **lực thế**: $\oint \vec{E} \cdot d\vec{r} = 0$ (trường không có xoáy tĩnh).
  - Định nghĩa Điện thế: $V(r) = -\int_\infty^r \vec{E} \cdot d\vec{r}$.
  - Mối liên hệ vi phân: Cường độ điện trường là Gradient của điện thế (chiều hướng từ thế cao xuống thế thấp):
    $$E_x = -\frac{dV}{dx} \quad (\text{hay } \vec{E} = -\nabla V)$$
  - Bản chất mặt đẳng thế: Vì $dV = -\vec{E} \cdot d\vec{r} = 0$ nên $\vec{E}$ luôn vuông góc với mặt đẳng thế.

#### Bài 3.4: Vật dẫn & Điện môi trong Điện trường Tĩnh
* **SGK hiện hành:** Nêu tính chất vật dẫn cân bằng điện, hằng số điện môi $\varepsilon$.
* **Nội dung bổ sung sâu:**
  - **Vật dẫn cân bằng tĩnh điện:**
    + Vì các electron tự do di động tức thời cho đến khi lực tác dụng lên chúng triệt tiêu $\Rightarrow \vec{E}_{\text{trong}} = 0$.
    + Điện tích dư chỉ phân bố trên bề mặt ngoài (chứng minh qua định luật Gauss).
    + Toàn bộ vật dẫn là một khối đẳng thế.
  - **Chất điện môi & Sự phân cực điện:**
    + Mô hình phân tử: Lưỡng cực điện vĩnh cửu hoặc cảm ứng.
    + Sự xuất hiện của điện tích liên kết bề mặt tạo ra điện trường ngược chiều $\vec{E}'$, làm yếu điện trường ban đầu: $\vec{E} = \frac{\vec{E}_0}{\varepsilon}$.

#### Bài 3.5: Tụ điện & Bản chất Năng lượng Định xứ trong Điện trường
* **SGK hiện hành:** Công thức $C = \frac{Q}{U}$, năng lượng $W = \frac{1}{2}CU^2$.
* **Nội dung bổ sung sâu:**
  - Quá trình nạp điện giải tích: Công dịch chuyển từng vi phân điện tích $dq$:
    $$W = \int_0^Q V(q) dq = \int_0^Q \frac{q}{C} dq = \frac{Q^2}{2C} = \frac{1}{2} C U^2$$
  - **Năng lượng nằm ở đâu?** Biến đổi công thức tụ phẳng:
    $$W = \frac{1}{2} \left(\frac{\varepsilon_0 \varepsilon S}{d}\right) (E d)^2 = \frac{1}{2}\varepsilon_0 \varepsilon E^2 (S d) = w_E \cdot \text{Thể tích}$$
  - $\rightarrow$ **Chân lý vật lý:** Năng lượng điện không nằm ở các điện tích hay bản kim loại, mà **nằm trong chính không gian có điện trường** với mật độ:
    $$w_E = \frac{1}{2}\varepsilon_0 \varepsilon E^2 \quad [\text{J/m}^3]$$

#### Bài 3.6: Chuyển động của Điện tích trong Điện trường
* **SGK hiện hành:** Bài toán electron bay vào điện trường đều (tương tự ném ngang).
* **Nội dung bổ sung sâu:**
  - Tích phân quỹ đạo giải tích từ phương trình vi phân vector: $m \frac{d^2\vec{r}}{dt^2} = q \vec{E}$.
  - Định lý động năng áp dụng cho hạt mang điện: $\Delta E_d = q U$.
  - Ứng dụng thực tế: Cơ chế lái tia trong ống phóng điện tử (CRT), máy gia tốc hạt, phổ khối lượng.

---

### CHỦ ĐỀ 4: DÒNG ĐIỆN KHÔNG ĐỔI & MẠCH ĐIỆN (DIRECT CURRENT & CIRCUITS)

#### Bài 4.1: Bản chất Dòng điện & Mô hình Khí Electron Tự do (Drude Model)
* **SGK hiện hành:** Công thức $I = n q v_d S$.
* **Nội dung bổ sung sâu:**
  - Định nghĩa vi phân: $I(t) = \frac{dq}{dt}$. Vectơ mật độ dòng $\vec{j} = n q \vec{v}_d$.
  - **Nghịch lý nhận thức lớn nhất:**
    + Tốc độ chuyển động nhiệt hỗn loạn của electron: $v_{th} \sim 10^5 - 10^6\text{ m/s}$.
    + Tốc độ trôi định hướng $v_d$: Chỉ cỡ $10^{-4}\text{ m/s}$ (vài milimét mỗi giây!).
    + *Tại sao bật công tắc cách xa hàng chục mét thì đèn sáng ngay lập tức?*
  - **Giải mã:** Tốc độ dòng điện không phải là tốc độ chạy của electron, mà là tốc độ lan truyền của **sóng điện trường** trong dây dẫn ($v \approx c \approx 3 \cdot 10^8\text{ m/s}$). Electron ở gần bóng đèn đã có sẵn ở đó và bị điện trường đẩy ngay lập tức.

#### Bài 4.2: Định luật Ohm Vi phân & Điện trở suất Vi mô
* **SGK hiện hành:** $R = \rho \frac{\ell}{S}$, định luật Ohm $I = \frac{U}{R}$.
* **Nội dung bổ sung sâu:**
  - Dẫn xuất mô hình Drude: Thời gian bay tự do trung bình $\tau$ giữa hai lần va chạm liên tiếp.
  - Gia tốc hạt: $a = \frac{qE}{m} \Rightarrow v_d = a \tau = \frac{q\tau}{m} E$.
  - Mật độ dòng: $j = n q v_d = \left(\frac{n q^2 \tau}{m}\right) E$.
  - **Định luật Ohm dạng vi phân:**
    $$\vec{j} = \sigma \vec{E} \quad \left(\text{với độ dẫn điện } \sigma = \frac{n q^2 \tau}{m}, \, \text{điện trở suất } \rho = \frac{1}{\sigma}\right)$$
  - Bản chất nhiệt độ làm tăng điện trở: Khi nhiệt độ tăng, mạng tinh thể dao động mạnh hơn (nhiều phonon hơn) $\rightarrow$ electron va chạm thường xuyên hơn $\rightarrow \tau$ giảm $\rightarrow \rho$ tăng.

#### Bài 4.3: Suất Điện Động, Nguồn Điện & Bản chất của "Lực Lạ"
* **SGK hiện hành:** Định nghĩa $\mathcal{E} = \frac{A_{\text{lạ}}}{q}$, định luật Ohm toàn mạch $I = \frac{\mathcal{E}}{R + r}$.
* **Nội dung bổ sung sâu:**
  - **Nghịch lý lực Coulomb:** Vì lực tĩnh điện có tính thế ($\oint \vec{E} \cdot d\vec{l} = 0$), lực Coulomb không thể nào duy trì dòng điện chạy vòng kín liên tục.
  - **Bản chất của "Lực lạ" (Non-electrostatic force $\vec{E}^*$):**
    + Nguồn điện là một chiếc "máy bơm thế năng" (hóa học trong pin, nhiệt điện, quang điện).
    + Lực lạ tác dụng ngược chiều lực tĩnh điện bên trong nguồn để kéo điện tích dương từ cực âm về cực dương (leo dốc thế năng).
  - Tích phân đường trên toàn mạch kín:
    $$\oint (\vec{E} + \vec{E}^*) \cdot d\vec{l} = \oint \vec{E}^* \cdot d\vec{l} = \mathcal{E} = I(R + r)$$
  - Định luật bảo toàn thế vòng kín (Định luật Kirchhoff 2).

#### Bài 4.4: Năng lượng, Công suất & Định luật Joule-Lenz Vi mô
* **SGK hiện hành:** $Q = I^2 R t$.
* **Nội dung bổ sung sâu:**
  - Dạng vi phân của định luật Joule: Mật độ công suất tỏa nhiệt tại mỗi điểm trong dây dẫn:
    $$p = \frac{dP}{dV} = \vec{j} \cdot \vec{E} = \sigma E^2 = \rho j^2$$
  - Cơ chế vi mô: Điện trường truyền động năng cho electron $\rightarrow$ electron va chạm không đàn hồi với các ion nút mạng $\rightarrow$ truyền động năng thành năng lượng dao động mạng tinh thể $\rightarrow$ biểu hiện vĩ mô là nhiệt độ tăng.

#### Bài 4.5: Mạch Điện Phức Tạp & Phương pháp Giải tích Mạng Điện
* **SGK hiện hành:** Ghép nối tiếp, song song cơ bản.
* **Nội dung bổ sung sâu:**
  - Hệ định luật Kirchhoff:
    1. Định luật nút dòng (Bảo toàn điện tích): $\sum I_k = 0$.
    2. Định luật vòng thế (Bảo toàn năng lượng): $\sum \mathcal{E}_k = \sum I_k R_k$.
  - Mạch cầu Wheaststone và nguyên lý đối xứng trong mạng điện phức tạp.

#### Bài 4.6: Quá trình Quá độ trong Mạch RC (Cầu nối giữa Điện và Dao động)
* **SGK hiện hành:** Bỏ qua hoàn toàn (chỉ xét dòng ổn định).
* **Nội dung bổ sung sâu:**
  - Phương trình vi phân phóng/nạp tụ qua điện trở:
    $$\mathcal{E} - i R - \frac{q}{C} = 0 \iff R \frac{dq}{dt} + \frac{q}{C} = \mathcal{E}$$
  - Nghiệm hàm mũ: $q(t) = C\mathcal{E}(1 - e^{-t/\tau})$ với hằng số thời gian $\tau = RC$.
  - Phân tích năng lượng nạp tụ: Nguồn sinh công $A = Q\mathcal{E} = C\mathcal{E}^2$, năng lượng tích trong tụ chỉ là $\frac{1}{2}C\mathcal{E}^2$. Nửa năng lượng còn lại đã đi đâu? $\rightarrow$ *Tích phân chứng minh chính xác $\frac{1}{2}C\mathcal{E}^2$ đã bị tỏa nhiệt trên điện trở $R$, bất kể $R$ lớn hay nhỏ!*

---

## IV. CÁC CHUYÊN ĐỀ MỞ RỘNG (BRIDGE TO OLYMPIAD & HIGHER PHYSICS)

1. **Chuyên đề A: Tương tự Trường Hấp dẫn & Trường Tĩnh điện**
   - So sánh định luật Vạn vật hấp dẫn Newton và Định luật Coulomb.
   - Thế hấp dẫn vs Điện thế.
   - Khái niệm khối lượng quán tính vs Khối lượng hấp dẫn (Mở đường cho Thuyết tương đối rộng).
2. **Chuyên đề B: Phương pháp Phân tích Thứ nguyên (Dimensional Analysis)**
   - Định lý Buckingham $\Pi$: Đoán trước dạng công thức vật lý mà không cần giải phương trình vi phân phức tạp.
3. **Chuyên đề C: Phương pháp Xấp xỉ và Thí nghiệm Tư duy (Thought Experiments)**
   - Nghịch lý Feynman trong điện từ học.
   - Thí nghiệm con tàu Einstein và sự tương đối của đồng thời.

---

## V. QUY CHUẨN ĐỊNH DẠNG & CÔNG CỤ XÂY DỰNG BÀI VIẾT

Để bộ tài liệu đạt chất lượng sư phạm xuất sắc nhất:
- **Công thức Toán:** Trình bày chuẩn LaTeX (KaTeX) trực quan, có giải thích từng ký hiệu và đơn vị đo.
- **Sơ đồ & Lưu đồ:** Dùng Mermaid diagram để mô tả dòng năng lượng, sơ đồ khối logic tư duy.
- **Mã mô phỏng (Visual Simulation):** Mỗi bài đi kèm một đoạn mã Python ngắn (sử dụng `numpy`, `matplotlib`) để vẽ đồ thị hàm sóng, quỹ đạo không gian pha $(x, v)$, hoặc phân bố điện trường, giúp người học "nhìn thấy" phương trình cử động.
- **Hệ thống câu hỏi bản chất (Conceptual Checkpoints):** Không hỏi bài tập tính toán số học khô khan; tập trung hỏi: *"Điều gì xảy ra nếu...?"*, *"Tại sao không thể là...?"*.

---

## VI. LỘ TRÌNH THỰC HIỆN BIÊN SOẠN (PHASE-BY-PHASE ROADMAP)

* [ ] **Giai đoạn 1 (Chủ đề 1: Dao động):** Biên soạn từ Bài 1.1 đến Bài 1.6 + Mã mô phỏng không gian pha.
* [ ] **Giai đoạn 2 (Chủ đề 2: Sóng):** Biên soạn từ Bài 2.1 đến Bài 2.6 + Mô phỏng giao thoa và sóng dừng.
* [ ] **Giai đoạn 3 (Chủ đề 3: Điện trường):** Biên soạn từ Bài 3.1 đến Bài 3.6 + Định luật Gauss và bài toán nạp tụ.
* [ ] **Giai đoạn 4 (Chủ đề 4: Dòng điện & Mạch điện):** Biên soạn từ Bài 4.1 đến Bài 4.6 + Mô hình Drude và quá trình quá độ RC.
* [ ] **Giai đoạn 5 (Tổng kết & Hiệu đính):** Đóng gói thành cẩm nang hoàn chỉnh kèm phụ lục toán học bổ trợ.
