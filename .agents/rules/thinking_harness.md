# Cognitive & Reasoning Harness (Pro-Emulation Cho Vật Lí 11)

Quy trình tư duy 5 pha giúp model suy luận sắc bén, chặt chẽ nhưng luôn bám sát ngưỡng tiếp thu của **học sinh lớp 11 Việt Nam (GDPT 2018)**.

---

## 5 Pha Tư Duy Bắt Buộc

### Pha 1: Giải Mã Yêu Cầu & Giới Hạn Khung Năng Lực Lớp 11
- **Đối tượng tiếp nhận**: Học sinh lớp 11 Việt Nam. Tự hỏi: *"Kiến thức này học sinh đã học ở Toán 10 hay Toán 11 chưa?"*.
- **Giới hạn công cụ**: Tuyệt đối không dùng phương trình vi phân đại học, không dùng số phức, không dùng chuỗi vô hạn Taylor toán cao cấp.
- **Tập trung vào bản chất**: Giải thích nguyên nhân vật lý bằng từ ngữ mộc mạc, chuẩn xác, dựa trên định luật Newton và định luật bảo toàn.

### Pha 2: Neo Giữ Bản Chất Vật Lý Từ Nguyên Lý Khởi Nguyên
- **Định luật II Newton**: $\Sigma \vec{F} = m\vec{a}$. Lực kéo về luôn hướng về VTCB: $F = -kx$.
- **Đạo hàm là tốc độ biến thiên**: Vận tốc $v = x'$, gia tốc $a = v' = x'' = -\omega^2 x$.
- **Bảo toàn cơ năng**: Cơ năng $W = W_d + W_t$ không đổi trong hệ kín. Khi có ma sát, cơ năng biến thành nhiệt năng làm dao động tắt dần.
- **Trạng thái cân bằng bền**: Trọng lực và lực đàn hồi triệt tiêu; lệch khỏi cân bằng xuất hiện lực kéo về.

### Pha 3: Đơn Giản Hóa Toán Học & Ẩn Dụ Trực Quan
- **Thay thế công cụ khó bằng ẩn dụ thực tế**:
  - Không giải phương trình vi phân bậc hai $\rightarrow$ Hãy kiểm tra bằng phép đạo hàm hai lần hàm $x(t) = A\cos(\omega t + \varphi)$.
  - Không dùng chuỗi Taylor $\rightarrow$ Dùng hình ảnh "hòn bi dưới đáy chảo", đáy cong trơn rất giống parabol $W_t = \frac{1}{2}kx^2$.
  - Không dùng tích phân $\rightarrow$ Dùng diện tích hình học hoặc trung bình cộng trực quan giữa động năng và thế năng.

### Pha 4: Kiểm Tra Thứ Nguyên & Đơn Vị Đo Chuẩn
- Kiểm tra tính đồng nhất thứ nguyên: Mọi vế trong phương trình phải cùng đơn vị đo SI ($[x] = \text{m}$, $[v] = \text{m/s}$, $[a] = \text{m/s}^2$, $[\omega] = \text{rad/s}$, $[W] = \text{J}$).
- Thử nghiệm các giới hạn thực tế: Khi không có ma sát ($b = 0$), khi vật ở biên ($v = 0, a = \pm a_{\max}$), khi qua VTCB ($x = 0, v = \pm v_{\max}$).

### Pha 5: Thực Thi Từng Bước & Tự Rà Soát Sư Phạm
- Trình bày dẫn xuất toán học mạch lạc, có giải thích từng dòng biến đổi lượng giác.
- Kiểm tra lại: Không còn sót thuật ngữ đại học (Liouville, Virial, Elliptic, Morse, Spiral Attractor).
- Tự động chạy tạo hình và biên dịch PDF để kiểm tra chất lượng in ấn.
