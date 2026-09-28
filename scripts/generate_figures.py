"""
Script to generate publication-quality figures for Chapter 1: Dao dong dieu hoa (Oscillations).
Designed specifically for 11th-grade Vietnamese physics students:
- Intuitive physical labels and clear SI units
- Visual connections between displacement, velocity, acceleration, and energy
- High-contrast color palette: Navy (#1B365D), Forest Green (#1E6B52), Crimson (#A6192E), Amber (#D97706)
Outputs both PDF (vector) and PNG (300 DPI) into book/figures/.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Professional, legible plot styling
plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9.5,
    'figure.titlesize': 14,
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Georgia'],
    'mathtext.fontset': 'cm',
    'lines.linewidth': 2.0,
    'axes.grid': True,
    'grid.alpha': 0.35,
    'grid.linestyle': ':',
    'axes.spines.top': False,
    'axes.spines.right': False,
})

FIG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'book', 'figures'))
os.makedirs(FIG_DIR, exist_ok=True)

# -------------------------------------------------------------
# Figure 1.0a: Derivative Essence (Tangent slope & Instantaneous Velocity)
# -------------------------------------------------------------
def plot_fig1_0a_derivative():
    fig, ax = plt.subplots(figsize=(8.0, 5.2))

    t = np.linspace(0, 4.5, 400)
    s = 0.5 * t**2 + 0.2 * t
    ax.plot(t, s, color='#1B365D', lw=2.4, label=r'Đồ thị quãng đường theo thời gian $s(t)$')

    t0 = 1.8
    s0 = 0.5 * t0**2 + 0.2 * t0
    v0 = t0 + 0.2  # s'(t) = t + 0.2 -> v(1.8) = 2.0
    
    # Secant point Q
    dt = 1.6
    t1 = t0 + dt
    s1 = 0.5 * t1**2 + 0.2 * t1
    v_sec = (s1 - s0) / dt
    
    # Draw secant line
    t_sec = np.linspace(0.8, 4.2, 100)
    s_sec_line = s0 + v_sec * (t_sec - t0)
    ax.plot(t_sec, s_sec_line, color='#D97706', linestyle='--', lw=1.8, 
            label=r'Cát tuyến $PQ$: Tốc độ trung bình $v_{tb} = \frac{\Delta s}{\Delta t}$')
    
    # Draw tangent line at t0
    t_tan = np.linspace(0.4, 3.6, 100)
    s_tan_line = s0 + v0 * (t_tan - t0)
    ax.plot(t_tan, s_tan_line, color='#1E6B52', lw=2.2,
            label=r'Tiếp tuyến tại $P$: Vận tốc tức thời $v(t_0) = s^\prime(t_0) = \tan\theta$')

    # Scatter points P and Q
    ax.scatter([t0, t1], [s0, s1], color='#A6192E', s=60, zorder=6)
    ax.annotate(r'$P(t_0, s_0)$', xy=(t0, s0), xytext=(t0 - 0.75, s0 + 0.6),
                fontsize=10.5, fontweight='bold', color='#1B365D')
    ax.annotate(r'$Q(t_0+\Delta t, s_0+\Delta s)$', xy=(t1, s1), xytext=(t1 - 1.5, s1 + 0.6),
                fontsize=10.5, fontweight='bold', color='#D97706')

    # Δt and Δs brackets/lines
    ax.plot([t0, t1], [s0, s0], color='#64748B', linestyle=':', lw=1.4)
    ax.plot([t1, t1], [s0, s1], color='#64748B', linestyle=':', lw=1.4)
    ax.text(t0 + dt/2, s0 - 0.6, r'$\Delta t$', fontsize=10.5, ha='center', color='#475569', fontweight='bold')
    ax.text(t1 + 0.15, s0 + (s1 - s0)/2, r'$\Delta s$', fontsize=10.5, va='center', color='#475569', fontweight='bold')

    # Explain limit
    ax.annotate(r'Khi $\Delta t \to 0$, điểm $Q \to P$' + '\n' +
                r'Cát tuyến $PQ \to$ Tiếp tuyến tại $P$' + '\n' +
                r'$\Rightarrow v(t) = \lim_{\Delta t \to 0} \frac{\Delta s}{\Delta t} = s^\prime(t)$',
                xy=(1.0, 7.5), xytext=(0.4, 7.2),
                fontsize=9.5, color='#1E6B52', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#F0FDF4', alpha=0.95, edgecolor='#1E6B52'))

    ax.set_xlabel(r'Thời gian $t$ (s)', fontsize=12)
    ax.set_ylabel(r'Quãng đường $s$ (m)', fontsize=12)
    ax.set_title(r'Hình 1.0a: Bản chất Đạo hàm — Vận tốc tức thời là độ dốc của tiếp tuyến', fontsize=12.5)
    ax.legend(loc='upper left', fontsize=9.2, framealpha=0.92)
    ax.set_ylim(-0.5, 12.0)
    ax.set_xlim(0, 4.5)

    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'fig1_0a_derivative.png'), dpi=300)
    fig.savefig(os.path.join(FIG_DIR, 'fig1_0a_derivative.pdf'))
    plt.close()
    print("Generated: fig1_0a_derivative")

# -------------------------------------------------------------
# Figure 1.0b: Storytelling: Roller Coaster States on Cosine Wave & Omega Compression
# -------------------------------------------------------------
def plot_fig1_0b_omega_derivative():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.0, 5.2))

    # --- Subplot (a): 4 Trạng thái trên chuyến tàu lượn Cosin ---
    t = np.linspace(0, 2*np.pi, 600)
    x = np.cos(t)
    ax1.plot(t, x, color='#1B365D', lw=2.4, label=r'Đường ray tàu lượn: $x(t) = \cos(t)$')
    ax1.axhline(0, color='#94A3B8', lw=1.0, linestyle='--')

    # Trạng thái 1: Đỉnh đồi (t = 0, x = 1)
    ax1.scatter([0], [1], color='#2563EB', s=80, zorder=6)
    t_tan1 = np.linspace(0, 0.9, 50)
    ax1.plot(t_tan1, np.ones_like(t_tan1), color='#2563EB', linestyle=':', lw=2.4)
    ax1.annotate('[TT1] Đỉnh đồi (t = 0)\n' + 
                 r'Dốc $= 0 \Rightarrow x^\prime(0) = 0$' + '\n' + 
                 'Hàm triệt tiêu tại 0: ' + r'$\sin(0) = 0$' + '\n' +
                 r'(Chưa rõ dấu: $+\sin$ hay $-\sin$?)',
                 xy=(0, 1), xytext=(0.12, 1.15),
                 fontsize=8.5, color='#1E40AF', fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.25', facecolor='#EFF6FF', edgecolor='#2563EB', alpha=0.95))

    # Trạng thái 2: Đang đổ dốc qua VTCB (t = pi/2, x = 0)
    t_mid1 = np.pi/2
    ax1.scatter([t_mid1], [0], color='#DC2626', s=80, zorder=6)
    t_tan2 = np.linspace(t_mid1 - 0.7, t_mid1 + 0.7, 50)
    ax1.plot(t_tan2, -1 * (t_tan2 - t_mid1), color='#DC2626', linestyle=':', lw=2.5)
    ax1.annotate(r'[TT2] Đang đổ dốc qua VTCB ($t = \frac{\pi}{2}$)' + '\n' + 
                 'Xe lao dốc cắm đầu: Dốc ' + r'$= -1$' + ' (Âm!)\n' +
                 r'Lật mở: $+\sin(\frac{\pi}{2}) = +1$ (sai dấu)' + '\n' + 
                 r'$\Rightarrow$ Bắt buộc: $[\cos(t)]^\prime = -\sin(t)$',
                 xy=(t_mid1, 0), xytext=(t_mid1 - 1.1, -0.95),
                 fontsize=8.5, color='#991B1B', fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.25', facecolor='#FEF2F2', edgecolor='#DC2626', alpha=0.95))

    # Trạng thái 3: Đáy vực (t = pi, x = -1)
    ax1.scatter([np.pi], [-1], color='#D97706', s=80, zorder=6)
    t_tan3 = np.linspace(np.pi - 0.5, np.pi + 0.5, 50)
    ax1.plot(t_tan3, -np.ones_like(t_tan3), color='#D97706', linestyle=':', lw=2.4)
    ax1.annotate(r'[TT3] Đáy vực ($t = \pi$)' + '\n' + 
                 r'Dốc $= 0 \Rightarrow -\sin(\pi) = 0$' + '\n' +
                 '(Tiếp tuyến phẳng, đổi chiều leo lên)',
                 xy=(np.pi, -1), xytext=(np.pi - 0.6, -1.55),
                 fontsize=8.5, color='#92400E', fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.25', facecolor='#FFFBEB', edgecolor='#D97706', alpha=0.95))

    # Trạng thái 4: Vọt lên qua VTCB (t = 3pi/2, x = 0)
    t_mid3 = 3*np.pi/2
    ax1.scatter([t_mid3], [0], color='#16A34A', s=80, zorder=6)
    t_tan4 = np.linspace(t_mid3 - 0.7, t_mid3 + 0.7, 50)
    ax1.plot(t_tan4, +1 * (t_tan4 - t_mid3), color='#16A34A', linestyle=':', lw=2.5)
    ax1.annotate(r'[TT4] Leo dốc qua VTCB ($t = \frac{3\pi}{2}$)' + '\n' + 
                 'Xe vọt lên trời: Dốc ' + r'$= +1$' + ' (Dương!)\n' + 
                 r'Kiểm chứng: $-\sin(\frac{3\pi}{2}) = -(-1) = +1$',
                 xy=(t_mid3, 0), xytext=(t_mid3 - 1.15, 0.55),
                 fontsize=8.5, color='#166534', fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.25', facecolor='#F0FDF4', edgecolor='#16A34A', alpha=0.95))

    ax1.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax1.set_xticklabels([r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'], fontsize=11)
    ax1.set_xlabel(r'Thời gian $t$ (rad hoặc s)', fontsize=11.5)
    ax1.set_ylabel(r'Li độ $x(t)$ (m)', fontsize=11.5)
    ax1.set_title(r'(a) Hành trình khám phá đạo hàm $[\cos(t)]^\prime = -\sin(t)$', fontsize=11.5, fontweight='bold')
    ax1.set_ylim(-1.8, 1.8)

    # --- Subplot (b): Cỗ máy nén thời gian omega ---
    t_b = np.linspace(0, np.pi, 400)
    x1 = np.cos(t_b)
    x2 = np.cos(2 * t_b)

    ax2.plot(t_b, x1, color='#1B365D', lw=2.2, label=r'Chế độ chuẩn: $\omega = 1\text{ rad/s}$ ($T = 2\pi$)')
    ax2.plot(t_b, x2, color='#A6192E', linestyle='--', lw=2.2, label=r'Tua nhanh gấp đôi: $\omega = 2\text{ rad/s}$ ($T = \pi$)')
    ax2.axhline(0, color='#94A3B8', lw=1.0, linestyle='--')

    # Dốc w=1 tại t=pi/2: dốc = -1
    t_v1 = np.pi/2
    ax2.scatter([t_v1], [0], color='#1B365D', s=60, zorder=5)
    ax2.plot([t_v1-0.5, t_v1+0.5], [0.5, -0.5], color='#1B365D', linestyle=':', lw=2.2)
    ax2.text(t_v1 + 0.1, 0.45, r'Độ dốc $= -1$', fontsize=9.5, color='#1B365D', fontweight='bold')

    # Dốc w=2 tại t=pi/4: dốc = -2
    t_v2 = np.pi/4
    ax2.scatter([t_v2], [0], color='#A6192E', s=60, zorder=5)
    ax2.plot([t_v2-0.35, t_v2+0.35], [0.7, -0.7], color='#A6192E', linestyle=':', lw=2.2)
    ax2.text(t_v2 + 0.08, -0.7, r'Độ dốc $= -2$', fontsize=9.5, color='#A6192E', fontweight='bold')

    # Box lý giải
    ax2.annotate('Bí quyết nén thời gian ' + r'$\omega$:' + '\n' +
                 'Cùng độ cao ' + r'$A$' + ', nhưng sóng bị nén' + '\n' +
                 'co hẹp lại 1/2 ' + r'$\Rightarrow$' + ' Sườn đồi dốc gấp 2!' + '\n' +
                 r'$\Rightarrow [\cos(\omega t)]^\prime = -\omega \sin(\omega t)$',
                 xy=(1.8, 0.2), xytext=(1.45, 0.65),
                 fontsize=9.2, color='#1E6B52', fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.35', facecolor='#F0FDF4', edgecolor='#1E6B52', alpha=0.95))

    ax2.set_xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
    ax2.set_xticklabels([r'$0$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$'], fontsize=10.5)
    ax2.set_xlabel(r'Thời gian $t$ (s)', fontsize=11.5)
    ax2.set_ylabel(r'Li độ $x$', fontsize=11.5)
    ax2.set_title(r'(b) Nén thời gian: Đồ thị dốc gấp $\omega$ lần', fontsize=11.5, fontweight='bold')
    ax2.legend(loc='lower left', fontsize=9.0, framealpha=0.92)
    ax2.set_ylim(-1.5, 1.5)

    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'fig1_0b_omega_derivative.png'), dpi=300)
    fig.savefig(os.path.join(FIG_DIR, 'fig1_0b_omega_derivative.pdf'))
    plt.close()
    print("Generated: fig1_0b_omega_derivative")

# -------------------------------------------------------------
# Figure 1.0c: Storytelling: 3 Satellite States on the Unit Circle
# -------------------------------------------------------------
def plot_fig1_0c_trig_circle():
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(14.2, 4.8))

    theta_circ = np.linspace(0, 2*np.pi, 300)
    alpha = np.radians(35)
    x_a = np.cos(alpha)
    y_a = np.sin(alpha)

    for ax in (ax1, ax2, ax3):
        ax.plot(np.cos(theta_circ), np.sin(theta_circ), color='#94A3B8', lw=1.4, linestyle=':')
        ax.axhline(0, color='#64748B', lw=0.8, linestyle='--')
        ax.axvline(0, color='#64748B', lw=0.8, linestyle='--')
        ax.set_aspect('equal')
        ax.set_xlim(-1.45, 1.45)
        ax.set_ylim(-1.45, 1.45)
        ax.set_xlabel(r'Trục hoành $\cos$', fontsize=11)
        ax.set_ylabel(r'Trục tung $\sin$', fontsize=11)

    # --- PANEL 1: Trạng thái 1: Vệ tinh Li độ u_1 & Hệ thức Pythagoras ---
    ax1.annotate('', xy=(x_a, y_a), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color='#1B365D', lw=2.4))
    # Right triangle
    ax1.plot([x_a, x_a], [0, y_a], color='#1B365D', linestyle='--', lw=1.3)
    ax1.fill_between([0, x_a], [0, 0], [0, y_a], color='#1B365D', alpha=0.15)
    ax1.text(x_a + 0.06, y_a + 0.05, r'$\vec{u}_1(\alpha)$', fontsize=11.5, fontweight='bold', color='#1B365D')
    ax1.text(x_a / 2, -0.18, r'$\cos\alpha = \frac{x}{A}$', fontsize=9.5, color='#1B365D', ha='center', fontweight='bold')
    ax1.text(x_a + 0.06, y_a / 2, r'$\sin\alpha = -\frac{v}{\omega A}$', fontsize=9.5, color='#1B365D', va='center', fontweight='bold')
    ax1.text(x_a / 2 - 0.15, y_a / 2 + 0.15, r'$R=1$', fontsize=9.5, color='#1B365D', fontstyle='italic')

    # Pythagoras badge
    ax1.annotate('Định lý Pythagoras:\n' +
                 r'$\cos^2\alpha + \sin^2\alpha = 1$' + '\n' +
                 r'$\Rightarrow \left(\frac{x}{A}\right)^2 + \left(\frac{v}{\omega A}\right)^2 = 1$',
                 xy=(0, -0.85), xytext=(-1.35, -1.35),
                 fontsize=8.8, color='#1B365D', fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.25', facecolor='#EFF6FF', edgecolor='#1B365D', alpha=0.95))
    ax1.set_title(r'(a) Trạng thái 1: Vệ tinh Li độ $\vec{u}_1$' + '\n' + r'& Hệ thức độc lập Pythagoras', fontsize=10.5, fontweight='bold')

    # --- PANEL 2: Trạng thái 2: Vệ tinh Vận tốc u_2 chạy trước +90 deg ---
    # Draw ghost u_1
    ax2.annotate('', xy=(x_a, y_a), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color='#94A3B8', lw=1.5, linestyle=':'))
    ax2.text(x_a + 0.05, y_a, r'$\vec{u}_1$', fontsize=10, color='#94A3B8')

    # Vector u_2 at alpha + pi/2
    alpha_pi2 = alpha + np.pi/2
    x_p = np.cos(alpha_pi2)
    y_p = np.sin(alpha_pi2)
    ax2.annotate('', xy=(x_p, y_p), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color='#1E6B52', lw=2.4))
    ax2.plot([x_p, x_p], [0, y_p], color='#1E6B52', linestyle='--', lw=1.2)
    ax2.text(x_p - 0.28, y_p + 0.08, r'$\vec{u}_2(\alpha + \frac{\pi}{2})$', fontsize=11, fontweight='bold', color='#1E6B52')

    # Rotation arc +90 deg
    arc_theta = np.linspace(alpha, alpha_pi2, 40)
    ax2.plot(0.35 * np.cos(arc_theta), 0.35 * np.sin(arc_theta), color='#D97706', lw=1.6)
    ax2.text(0.12, 0.42, r'$+90^\circ$', fontsize=9.2, color='#D97706', fontweight='bold')

    # Badge for u_2
    ax2.annotate('Chạy trước góc vuông:\n' +
                 r'$\cos(\alpha + \frac{\pi}{2}) = -\sin\alpha$' + '\n' +
                 r'$\Rightarrow v$' + ' sớm pha ' + r'$\frac{\pi}{2}$' + ' so với ' + r'$x$',
                 xy=(x_p, 0), xytext=(-1.35, -1.35),
                 fontsize=8.8, color='#1E6B52', fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.25', facecolor='#F0FDF4', edgecolor='#1E6B52', alpha=0.95))
    ax2.set_title(r'(b) Trạng thái 2: Vệ tinh Vận tốc $\vec{u}_2$' + '\n' + r'Bứt phá trước $+90^\circ$ ($\pi/2$)', fontsize=10.5, fontweight='bold')

    # --- PANEL 3: Trạng thái 3: Vệ tinh Gia tốc u_3 đối đầu +180 deg ---
    # Draw ghost u_1
    ax3.annotate('', xy=(x_a, y_a), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color='#94A3B8', lw=1.5, linestyle=':'))
    ax3.text(x_a + 0.05, y_a, r'$\vec{u}_1$', fontsize=10, color='#94A3B8')

    # Vector u_3 at alpha + pi
    alpha_pi = alpha + np.pi
    x_pi = np.cos(alpha_pi)
    y_pi = np.sin(alpha_pi)
    ax3.annotate('', xy=(x_pi, y_pi), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color='#A6192E', lw=2.4))
    ax3.plot([x_pi, x_pi], [0, y_pi], color='#A6192E', linestyle='--', lw=1.2)
    ax3.text(x_pi - 0.42, y_pi - 0.12, r'$\vec{u}_3(\alpha + \pi)$', fontsize=11, fontweight='bold', color='#A6192E')

    # Rotation arc +180 deg
    arc_pi = np.linspace(alpha, alpha_pi, 60)
    ax3.plot(0.28 * np.cos(arc_pi), 0.28 * np.sin(arc_pi), color='#D97706', lw=1.6)
    ax3.text(-0.25, 0.35, r'$+180^\circ$', fontsize=9.2, color='#D97706', fontweight='bold')

    # Badge for u_3
    ax3.annotate('Đối xứng đối đầu:\n' +
                 r'$\cos(\alpha + \pi) = -\cos\alpha$' + '\n' +
                 r'$\Rightarrow a$' + ' ngược pha ' + r'$\pi$' + ' so với ' + r'$x$',
                 xy=(x_pi, 0), xytext=(-1.35, -1.35),
                 fontsize=8.8, color='#A6192E', fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.25', facecolor='#FEF2F2', edgecolor='#A6192E', alpha=0.95))
    ax3.set_title(r'(c) Trạng thái 3: Vệ tinh Gia tốc $\vec{u}_3$' + '\n' + r'Kéo giật lùi đối đầu $+180^\circ$ ($\pi$)', fontsize=10.5, fontweight='bold')

    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'fig1_0c_trig_circle.png'), dpi=300)
    fig.savefig(os.path.join(FIG_DIR, 'fig1_0c_trig_circle.pdf'))
    plt.close()
    print("Generated: fig1_0c_trig_circle")

# -------------------------------------------------------------
# Figure 1.1a: Restoring Force Mechanism & Dynamic Equation
# -------------------------------------------------------------
def plot_fig1_1a_restoring_force():
    def draw_spring(ax, x_start, x_end, y, n_coils=9, width=0.15, color='#475569', lw=1.8):
        length = x_end - x_start
        lead = 0.22 * min(length, 0.8)
        coil_len = length - 2 * lead
        xs = [x_start, x_start + lead]
        ys = [y, y]
        for i in range(n_coils):
            xi = x_start + lead + (i + 0.5) / n_coils * coil_len
            yi = y + (width if i % 2 == 0 else -width)
            xs.append(xi)
            ys.append(yi)
        xs.extend([x_end - lead, x_end])
        ys.extend([y, y])
        ax.plot(xs, ys, color=color, lw=lw)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 5.0))

    # --- Panel 1: Physical Model ---
    ax1.set_xlim(-3.6, 2.8)
    ax1.set_ylim(-0.9, 3.4)
    ax1.axis('off')

    # Left wall
    ax1.plot([-3.2, -3.2], [-0.3, 3.2], color='#334155', lw=3.0)
    for y_hatch in np.linspace(-0.2, 3.1, 15):
        ax1.plot([-3.45, -3.2], [y_hatch - 0.15, y_hatch], color='#64748B', lw=1.5)

    # Reference dashed lines for -A, O, +A
    for x_ref, col, lbl in zip([-1.6, 0.0, 1.6], ['#A6192E', '#64748B', '#1B365D'], [r'Biên âm $-A$', r'VTCB $O$', r'Biên dương $+A$']):
        ax1.plot([x_ref, x_ref], [-0.5, 3.2], color=col, linestyle='--', lw=1.2, alpha=0.7)
        ax1.text(x_ref, 3.25, lbl, color=col, ha='center', fontsize=9.5, fontweight='bold')

    # State 1: Stretched (Top, y=2.4)
    y1 = 2.4
    draw_spring(ax1, -3.2, 1.2, y1, n_coils=10, width=0.14, color='#1E6B52')
    rect1 = patches.Rectangle((1.2, y1 - 0.25), 0.8, 0.5, facecolor='#1B365D', edgecolor='#0F172A', lw=1.5, zorder=5)
    ax1.add_patch(rect1)
    ax1.text(1.6, y1, r'$m$', color='white', ha='center', va='center', fontweight='bold', fontsize=11, zorder=6)
    # Force arrow from front face of block
    ax1.annotate('', xy=(0.3, y1), xytext=(1.2, y1), arrowprops=dict(arrowstyle='->', lw=2.2, color='#A6192E'))
    ax1.text(0.75, y1 + 0.15, r'$\vec{F}_{kv} < 0$', color='#A6192E', ha='center', fontsize=9.5, fontweight='bold')
    ax1.text(-1.0, y1 + 0.38, 'Lò xo dãn: ' + r'$\vec{F}_{kv}$' + ' giằng ngược về VTCB', color='#1B365D', fontsize=9.0, fontweight='bold')

    # State 2: Equilibrium (Middle, y=1.4)
    y2 = 1.4
    draw_spring(ax1, -3.2, -0.4, y2, n_coils=8, width=0.14, color='#64748B')
    rect2 = patches.Rectangle((-0.4, y2 - 0.25), 0.8, 0.5, facecolor='#475569', edgecolor='#0F172A', lw=1.5, zorder=5)
    ax1.add_patch(rect2)
    ax1.text(0.0, y2, r'$m$', color='white', ha='center', va='center', fontweight='bold', fontsize=11, zorder=6)
    ax1.text(-1.0, y2 + 0.38, 'VTCB: Lò xo tự nhiên, ' + r'$F_{kv} = 0, a = 0$', color='#475569', fontsize=9.0, fontweight='bold')

    # State 3: Compressed (Bottom, y=0.4)
    y3 = 0.4
    draw_spring(ax1, -3.2, -2.0, y3, n_coils=6, width=0.14, color='#A6192E')
    rect3 = patches.Rectangle((-2.0, y3 - 0.25), 0.8, 0.5, facecolor='#A6192E', edgecolor='#0F172A', lw=1.5, zorder=5)
    ax1.add_patch(rect3)
    ax1.text(-1.6, y3, r'$m$', color='white', ha='center', va='center', fontweight='bold', fontsize=11, zorder=6)
    # Force arrow from front face of block
    ax1.annotate('', xy=(-0.3, y3), xytext=(-1.2, y3), arrowprops=dict(arrowstyle='->', lw=2.2, color='#A6192E'))
    ax1.text(-0.75, y3 + 0.15, r'$\vec{F}_{kv} > 0$', color='#A6192E', ha='center', fontsize=9.5, fontweight='bold')
    ax1.text(-1.0, y3 + 0.38, 'Lò xo nén: ' + r'$\vec{F}_{kv}$' + ' đẩy xuôi về VTCB', color='#A6192E', fontsize=9.0, fontweight='bold')

    # Coordinate axis Ox at bottom
    ax1.annotate('', xy=(2.6, -0.5), xytext=(-3.2, -0.5), arrowprops=dict(arrowstyle='->', lw=1.8, color='black'))
    ax1.text(2.65, -0.5, r'$x$', color='black', va='center', fontsize=12, fontweight='bold')
    for x_tick, tick_lbl in zip([-1.6, 0.0, 1.6], [r'$-A$', r'$0$', r'$+A$']):
        ax1.plot([x_tick, x_tick], [-0.55, -0.45], color='black', lw=1.5)
        ax1.text(x_tick, -0.72, tick_lbl, ha='center', fontsize=10.5, fontweight='bold')

    ax1.set_title(r'(a) Mô hình vật lý: Lực kéo về luôn hướng về VTCB', fontsize=11.5, fontweight='bold')

    # --- Panel 2: Mathematical Graph F_kv = -kx ---
    x_pts = np.linspace(-2.0, 2.0, 200)
    k = 1.5
    F_pts = -k * x_pts

    ax2.axhline(0, color='black', lw=1.2)
    ax2.axvline(0, color='black', lw=1.2)

    # Shading quadrants
    ax2.fill_between([0, 2.0], [0, 0], [-3.2, -3.2], facecolor='#FEF2F2', alpha=0.5, label='Vùng lệch phải ' + r'($x > 0 \Rightarrow F < 0$)')
    ax2.fill_between([-2.0, 0], [0, 0], [3.2, 3.2], facecolor='#F0FDF4', alpha=0.5, label='Vùng lệch trái ' + r'($x < 0 \Rightarrow F > 0$)')

    # Graph line
    ax2.plot(x_pts, F_pts, color='#A6192E', lw=2.4, label=r'Lực kéo về $F_{kv} = -k x$')

    # Points -A, +Fmax and +A, -Fmax
    A_val = 1.6
    F_max = k * A_val
    ax2.scatter([-A_val, 0, A_val], [F_max, 0, -F_max], color='#A6192E', s=60, zorder=5)

    # Dashed projections
    ax2.plot([-A_val, -A_val, 0], [0, F_max, F_max], color='#64748B', linestyle='--', lw=1.0)
    ax2.plot([A_val, A_val, 0], [0, -F_max, -F_max], color='#64748B', linestyle='--', lw=1.0)

    ax2.set_xticks([-A_val, 0, A_val])
    ax2.set_xticklabels([r'$-A$', r'$0$', r'$+A$'], fontsize=11)
    ax2.set_yticks([-F_max, 0, F_max])
    ax2.set_yticklabels([r'$-F_{\max}$', r'$0$', r'$+F_{\max}$'], fontsize=11)

    ax2.set_xlabel(r'Li độ $x$ (m)', fontsize=11.5)
    ax2.set_ylabel(r'Lực kéo về $F_{kv}$ (N)', fontsize=11.5)
    ax2.set_title(r'(b) Đồ thị Lực kéo về: Luôn ngược dấu với li độ', fontsize=11.5, fontweight='bold')
    ax2.legend(loc='lower left', fontsize=8.8, framealpha=0.92)

    # Explanatory callout
    ax2.annotate('Bản chất toán học:\n' +
                 r'$F_{kv} = m a = -k x$' + '\n' +
                 r'$\Rightarrow a = x^{\prime\prime}(t) = -\omega^2 x(t)$' + '\n' +
                 r'Chỉ hàm $\cos(\omega t + \varphi)$ mới có' + '\n' +
                 r'đạo hàm bậc 2 đổi dấu: $(x)^{\prime\prime} = -\omega^2 x$!',
                 xy=(0.2, 1.4), xytext=(0.15, 0.8),
                 fontsize=9.0, color='#1B365D', fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.35', facecolor='#F8FAFC', edgecolor='#1B365D', alpha=0.95))

    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'fig1_1a_restoring_force.png'), dpi=300)
    fig.savefig(os.path.join(FIG_DIR, 'fig1_1a_restoring_force.pdf'))
    plt.close()
    print("Generated: fig1_1a_restoring_force")

# -------------------------------------------------------------
# Figure 1.1b: Anatomy of Cosine Waveform
# -------------------------------------------------------------
def plot_fig1_1b_cosine_anatomy():
    fig, ax = plt.subplots(figsize=(11.0, 5.8))

    A = 4.0
    T = 2.0
    omega = 2 * np.pi / T  # pi
    phi = -np.pi / 3

    t = np.linspace(0, 2.6, 600)
    x = A * np.cos(omega * t + phi)

    ax.plot(t, x, color='#1B365D', lw=2.6, label=r'Đồ thị li độ: $x(t) = A\cos(\omega t + \varphi)$')

    # Horizontal boundary guides
    ax.axhline(A, color='#1E6B52', linestyle='--', lw=1.2, alpha=0.8)
    ax.axhline(-A, color='#A6192E', linestyle='--', lw=1.2, alpha=0.8)
    ax.axhline(0, color='black', lw=1.0)

    # Vertical span: L = 2A and Amplitude A
    ax.annotate('', xy=(-0.25, A), xytext=(-0.25, -A), arrowprops=dict(arrowstyle='<->', color='#1B365D', lw=1.6))
    ax.text(-0.28, 0, 'Chiều dài quỹ đạo\n' + r'$L = 2A = 8\text{ cm}$', color='#1B365D', ha='right', va='center', fontsize=8.8, fontweight='bold')

    ax.annotate('', xy=(-0.10, A), xytext=(-0.10, 0), arrowprops=dict(arrowstyle='<->', color='#1E6B52', lw=1.6))
    ax.text(-0.12, A/2, r'Biên độ $A = 4\text{ cm}$', color='#1E6B52', ha='right', va='center', fontsize=8.8, fontweight='bold')

    # Initial point at t=0
    x0 = A * np.cos(phi)
    ax.scatter([0], [x0], color='#D97706', s=70, zorder=6)
    ax.annotate('Xuất phát lúc ' + r'$t = 0$:' + '\n' +
                r'$x_0 = A\cos\varphi = 2\text{ cm}$' + '\n' +
                'Dốc lên ' + r'$\Rightarrow v_0 > 0$',
                xy=(0, x0), xytext=(0.08, 0.5),
                fontsize=8.5, color='#B45309', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='#D97706', lw=1.2),
                bbox=dict(boxstyle='round,pad=0.25', facecolor='#FEF3C7', edgecolor='#D97706', alpha=0.95))

    # Peak 1 (t = 1/3)
    t_p1 = 1.0 / 3.0
    ax.scatter([t_p1], [A], color='#1E6B52', s=70, zorder=6)
    ax.plot([t_p1 - 0.2, t_p1 + 0.2], [A, A], color='#1E6B52', lw=2.2)
    ax.annotate('Biên dương ' + r'($x = +A$):' + '\n' + 'Tiếp tuyến ngang ' + r'$\Rightarrow v = 0$',
                xy=(t_p1, A), xytext=(t_p1 - 0.15, A + 0.65),
                fontsize=8.5, color='#166534', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.25', facecolor='#F0FDF4', edgecolor='#16A34A', alpha=0.95))

    # Peak 2 (t = 7/3)
    t_p2 = t_p1 + T
    ax.scatter([t_p2], [A], color='#1E6B52', s=70, zorder=6)
    ax.plot([t_p2 - 0.2, t_p2 + 0.2], [A, A], color='#1E6B52', lw=2.2)

    # Period T double arrow between Peak 1 and Peak 2
    ax.annotate('', xy=(t_p1, A + 0.4), xytext=(t_p2, A + 0.4), arrowprops=dict(arrowstyle='<->', color='#1B365D', lw=1.8))
    ax.text((t_p1 + t_p2)/2, A + 0.52, r'Chu kì $T = 2\text{ s}$ (1 dao động toàn phần)', color='#1B365D', ha='center', fontsize=9.2, fontweight='bold')

    # Descending VTCB (t = 5/6)
    t_v1 = t_p1 + T/4
    ax.scatter([t_v1], [0], color='#A6192E', s=70, zorder=6)
    dt_tan = 0.15
    v_slope = -omega * A
    ax.plot([t_v1 - dt_tan, t_v1 + dt_tan], [-dt_tan * v_slope * 0.35, dt_tan * v_slope * 0.35], color='#A6192E', lw=2.2)
    ax.annotate('Qua VTCB theo chiều âm ' + r'($x = 0$):' + '\n' +
                'Dốc xuống nhất ' + r'$\Rightarrow v = -v_{\max} = -\omega A$',
                xy=(t_v1, 0), xytext=(t_v1 + 0.08, -1.8),
                fontsize=8.5, color='#991B1B', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='#A6192E', lw=1.2),
                bbox=dict(boxstyle='round,pad=0.25', facecolor='#FEF2F2', edgecolor='#EF4444', alpha=0.95))

    # T/4 arrow between Peak 1 and Descending VTCB
    ax.plot([t_p1, t_p1], [-0.8, A], color='#94A3B8', linestyle=':', lw=1.0)
    ax.plot([t_v1, t_v1], [-0.8, 0], color='#94A3B8', linestyle=':', lw=1.0)
    ax.annotate('', xy=(t_p1, -0.6), xytext=(t_v1, -0.6), arrowprops=dict(arrowstyle='<->', color='#475569', lw=1.4))
    ax.text((t_p1 + t_v1)/2, -0.45, r'$\frac{T}{4}$', color='#475569', ha='center', fontsize=9.2, fontweight='bold')

    # Trough 1 (t = 4/3)
    t_tr1 = t_p1 + T/2
    ax.scatter([t_tr1], [-A], color='#A6192E', s=70, zorder=6)
    ax.plot([t_tr1 - 0.2, t_tr1 + 0.2], [-A, -A], color='#A6192E', lw=2.2)
    ax.annotate('Biên âm ' + r'($x = -A$):' + '\n' + 'Tiếp tuyến ngang ' + r'$\Rightarrow v = 0$',
                xy=(t_tr1, -A), xytext=(t_tr1 - 0.2, -A - 0.95),
                fontsize=8.5, color='#991B1B', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.25', facecolor='#FEF2F2', edgecolor='#EF4444', alpha=0.95))

    # T/2 arrow between Peak 1 and Trough 1
    ax.plot([t_tr1, t_tr1], [-A, 2.2], color='#94A3B8', linestyle=':', lw=1.0)
    ax.annotate('', xy=(t_p1, 2.0), xytext=(t_tr1, 2.0), arrowprops=dict(arrowstyle='<->', color='#1E6B52', lw=1.4))
    ax.text((t_p1 + t_tr1)/2, 2.15, r'Nửa chu kì $\frac{T}{2} = 1\text{ s}$', color='#1E6B52', ha='center', fontsize=9.0, fontweight='bold')

    # Ascending VTCB (t = 11/6)
    t_v2 = t_p1 + 3*T/4
    ax.scatter([t_v2], [0], color='#16A34A', s=70, zorder=6)
    ax.plot([t_v2 - 0.12, t_v2 + 0.12], [-0.12 * v_slope * 0.35, 0.12 * v_slope * 0.35], color='#16A34A', lw=2.2)
    ax.annotate('Qua VTCB theo chiều dương ' + r'($x = 0$):' + '\n' +
                'Dốc lên nhất ' + r'$\Rightarrow v = +v_{\max} = +\omega A$',
                xy=(t_v2, 0), xytext=(t_v2 - 0.38, 1.4),
                fontsize=8.5, color='#166534', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='#16A34A', lw=1.2),
                bbox=dict(boxstyle='round,pad=0.25', facecolor='#F0FDF4', edgecolor='#16A34A', alpha=0.95))

    # Summary DNA box
    dna_text = ('BẢNG MÃ GEN (ADN) DAO ĐỘNG:\n' +
                r'• $x(t)$: Li độ tức thời tại thời điểm $t$' + '\n' +
                r'• $A = 4\text{ cm}$: Biên độ ($A > 0$), nửa chiều dài quỹ đạo $L = 2A$' + '\n' +
                r'• $T = 2\text{ s}$: Chu kì; Tần số $f = 1/T = 0.5\text{ Hz}$' + '\n' +
                r'• $\omega = \pi\text{ rad/s}$: Tần số góc (tốc độ quét góc pha)' + '\n' +
                r'• $\varphi = -\pi/3$: Pha ban đầu (xác định vị trí và chiều lúc $t=0$)' + '\n' +
                r'• $(\omega t + \varphi)$: Pha dao động (xác định trạng thái tại thời điểm $t$)')

    ax.text(2.60, -2.8, dna_text, fontsize=8.8, color='#1B365D', ha='right',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#F8FAFC', edgecolor='#1B365D', lw=1.2, alpha=0.96))

    ax.set_xlim(-0.6, 2.7)
    ax.set_ylim(-5.5, 5.5)
    ax.set_xlabel(r'Thời gian $t$ (giây)', fontsize=11.5)
    ax.set_ylabel(r'Li độ $x$ (cm)', fontsize=11.5)
    ax.set_yticks([-A, -A/2, 0, A/2, A])
    ax.set_yticklabels([r'$-A = -4$', r'$-2$', r'$0$', r'$+2$', r'$+A = +4$'], fontsize=10.5)
    ax.set_title(r'Giải mã cấu trúc hình học của sóng cosin: $x(t) = A\cos(\omega t + \varphi)$', fontsize=12.5, fontweight='bold')

    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'fig1_1b_cosine_anatomy.png'), dpi=300)
    fig.savefig(os.path.join(FIG_DIR, 'fig1_1b_cosine_anatomy.pdf'))
    plt.close()
    print("Generated: fig1_1b_cosine_anatomy")

# -------------------------------------------------------------
# Figure 1.1c: 3 Classic Phase Difference Scenarios
# -------------------------------------------------------------
def plot_fig1_1c_phase_comparison():
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(13.2, 5.0))

    T = 2.0
    omega = 2 * np.pi / T  # pi
    t = np.linspace(0, 2 * T, 500)

    A1 = 3.5
    A2 = 2.0

    # ----------------- PANEL 1: CÙNG PHA -----------------
    x1_cung = A1 * np.cos(omega * t)
    x2_cung = A2 * np.cos(omega * t)

    ax1.plot(t, x1_cung, color='#1B365D', lw=2.2, label=r'$x_1(t) = A_1\cos(\omega t)$')
    ax1.plot(t, x2_cung, color='#1E6B52', lw=2.0, linestyle='--', label=r'$x_2(t) = A_2\cos(\omega t)$')
    ax1.axhline(0, color='gray', lw=0.8, linestyle='--')

    ax1.set_title(r'(a) CÙNG PHA: $\Delta\varphi = 2k\pi$', fontsize=11.5, fontweight='bold', color='#1B365D')
    ax1.set_xlabel(r'Thời gian $t$ (s)')
    ax1.set_ylabel(r'Li độ $x$ (cm)')
    ax1.set_ylim(-4.8, 5.2)
    ax1.legend(loc='lower left', fontsize=8.5, framealpha=0.92)

    # Inset plot for x1 - x2 trajectory
    ins1 = ax1.inset_axes([0.62, 0.62, 0.34, 0.34])
    ins1.set_facecolor('#FFFFFF')
    ins1.set_zorder(10)
    x1_domain = np.linspace(-A1, A1, 100)
    ins1.plot(x1_domain, (A2 / A1) * x1_domain, color='#1B365D', lw=2.0)
    ins1.scatter([-A1, 0, A1], [-A2, 0, A2], color='#1E6B52', s=20)
    ins1.axhline(0, color='gray', lw=0.5, linestyle=':')
    ins1.axvline(0, color='gray', lw=0.5, linestyle=':')
    ins1.set_title(r'Đồ thị $x_1 - x_2$', fontsize=8.5, pad=2)
    ins1.set_xlabel(r'$x_1$', fontsize=8.0, labelpad=1)
    ins1.set_ylabel(r'$x_2$', fontsize=8.0, labelpad=1)
    ins1.tick_params(labelsize=7)

    ax1.annotate('Đặc trưng cùng pha:\n' +
                 r'• $\Delta\varphi = \varphi_2 - \varphi_1 = 2k\pi$' + '\n' +
                 r'• $\frac{x_1(t)}{A_1} = \frac{x_2(t)}{A_2}$' + '\n' +
                 '• Cùng lên đỉnh, cùng về 0,\n  cùng đổi chiều chuyển động!',
                 xy=(0.05, 0.95), xycoords='axes fraction', va='top',
                 fontsize=8.5, color='#1B365D',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#F0F9FF', edgecolor='#0284C7', alpha=0.95))

    # ----------------- PANEL 2: NGƯỢC PHA -----------------
    x1_nguoc = A1 * np.cos(omega * t)
    x2_nguoc = A2 * np.cos(omega * t + np.pi)  # = -A2 cos(omega t)

    ax2.plot(t, x1_nguoc, color='#1B365D', lw=2.2, label=r'$x_1(t) = A_1\cos(\omega t)$')
    ax2.plot(t, x2_nguoc, color='#A6192E', lw=2.0, linestyle='--', label=r'$x_2(t) = -A_2\cos(\omega t)$')
    x_sum = x1_nguoc + x2_nguoc
    ax2.plot(t, x_sum, color='#64748B', lw=1.4, linestyle=':', label=r'Tổng $x_1 + x_2$ (Triệt tiêu)')
    ax2.axhline(0, color='gray', lw=0.8, linestyle='--')

    ax2.set_title(r'(b) NGƯỢC PHA: $\Delta\varphi = (2k+1)\pi$', fontsize=11.5, fontweight='bold', color='#A6192E')
    ax2.set_xlabel(r'Thời gian $t$ (s)')
    ax2.set_ylim(-4.8, 5.2)
    ax2.legend(loc='lower left', fontsize=8.2, framealpha=0.92)

    # Inset plot for x1 - x2 trajectory
    ins2 = ax2.inset_axes([0.62, 0.62, 0.34, 0.34])
    ins2.set_facecolor('#FFFFFF')
    ins2.set_zorder(10)
    ins2.plot(x1_domain, -(A2 / A1) * x1_domain, color='#A6192E', lw=2.0)
    ins2.scatter([-A1, 0, A1], [A2, 0, -A2], color='#A6192E', s=20)
    ins2.axhline(0, color='gray', lw=0.5, linestyle=':')
    ins2.axvline(0, color='gray', lw=0.5, linestyle=':')
    ins2.set_title(r'Đồ thị $x_1 - x_2$', fontsize=8.5, pad=2)
    ins2.set_xlabel(r'$x_1$', fontsize=8.0, labelpad=1)
    ins2.set_ylabel(r'$x_2$', fontsize=8.0, labelpad=1)
    ins2.tick_params(labelsize=7)

    ax2.annotate('Đặc trưng ngược pha:\n' +
                 r'• $\Delta\varphi = (2k+1)\pi$' + '\n' +
                 r'• $\frac{x_1(t)}{A_1} = -\frac{x_2(t)}{A_2}$' + '\n' +
                 '• Kẻ lên đỉnh, người chạm đáy!\n' +
                 '• Ứng dụng: Tai nghe chống ồn (ANC)\n  phát sóng âm ngược pha!',
                 xy=(0.05, 0.95), xycoords='axes fraction', va='top',
                 fontsize=8.5, color='#991B1B',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#FEF2F2', edgecolor='#EF4444', alpha=0.95))

    # ----------------- PANEL 3: VUÔNG PHA -----------------
    x1_vuong = A1 * np.cos(omega * t)
    x2_vuong = A2 * np.cos(omega * t + np.pi/2)  # = -A2 sin(omega t)

    ax3.plot(t, x1_vuong, color='#1B365D', lw=2.2, label=r'$x_1(t) = A_1\cos(\omega t)$')
    ax3.plot(t, x2_vuong, color='#D97706', lw=2.0, linestyle='--', label=r'$x_2(t) = -A_2\sin(\omega t)$')
    ax3.axhline(0, color='gray', lw=0.8, linestyle='--')

    ax3.set_title(r'(c) VUÔNG PHA: $\Delta\varphi = (2k+1)\frac{\pi}{2}$', fontsize=11.5, fontweight='bold', color='#D97706')
    ax3.set_xlabel(r'Thời gian $t$ (s)')
    ax3.set_ylim(-4.8, 5.2)
    ax3.legend(loc='lower left', fontsize=8.5, framealpha=0.92)

    # Inset plot for x1 - x2 trajectory (Ellipse)
    ins3 = ax3.inset_axes([0.62, 0.62, 0.34, 0.34])
    ins3.set_facecolor('#FFFFFF')
    ins3.set_zorder(10)
    theta_el = np.linspace(0, 2*np.pi, 200)
    ins3.plot(A1 * np.cos(theta_el), -A2 * np.sin(theta_el), color='#D97706', lw=2.0)
    ins3.axhline(0, color='gray', lw=0.5, linestyle=':')
    ins3.axvline(0, color='gray', lw=0.5, linestyle=':')
    ins3.set_title(r'Elip $\frac{x_1^2}{A_1^2} + \frac{x_2^2}{A_2^2} = 1$', fontsize=8.0, pad=2)
    ins3.set_xlabel(r'$x_1$', fontsize=8.0, labelpad=1)
    ins3.set_ylabel(r'$x_2$', fontsize=8.0, labelpad=1)
    ins3.tick_params(labelsize=7)

    ax3.annotate('Đặc trưng vuông pha:\n' +
                 r'• $\Delta\varphi = (2k+1)\frac{\pi}{2}$' + '\n' +
                 r'• $(\frac{x_1}{A_1})^2 + (\frac{x_2}{A_2})^2 = 1$' + '\n' +
                 r'• Kẻ ở biên ($v=0$) thì' + '\n' +
                 r'  người phóng qua VTCB ($|v|=v_{\max}$)!' + '\n' +
                 '• Nối kết: Vận tốc vuông pha li độ!',
                 xy=(0.05, 0.95), xycoords='axes fraction', va='top',
                 fontsize=8.5, color='#B45309',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#FEF3C7', edgecolor='#D97706', alpha=0.95))

    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'fig1_1c_phase_comparison.png'), dpi=300)
    fig.savefig(os.path.join(FIG_DIR, 'fig1_1c_phase_comparison.pdf'))
    plt.close()
    print("Generated: fig1_1c_phase_comparison")

# -------------------------------------------------------------
# Figure 1.1: Kinematics of Harmonic Motion (x, v, a)
# -------------------------------------------------------------
def plot_fig1_kinematics():
    t = np.linspace(0, 2 * np.pi, 600)
    x = np.cos(t)
    v = -np.sin(t)      # v / (omega A)
    a = -np.cos(t)      # a / (omega^2 A)

    fig, axes = plt.subplots(3, 1, figsize=(8.2, 7.2), sharex=True)
    
    # x(t)
    axes[0].plot(t, x, color='#1B365D', label=r'Li độ $x(t) = A\cos(\omega t)$')
    axes[0].set_ylabel(r'Li độ $\frac{x}{A}$')
    axes[0].axhline(0, color='gray', linewidth=0.8, linestyle='--')
    axes[0].scatter([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], [1, 0, -1, 0, 1], color='#1B365D', s=35, zorder=5)
    axes[0].annotate(r'$P_0(t=0): x=+A$', xy=(0, 1), xytext=(0.25, 1.08), fontsize=9, color='#1B365D',
                     arrowprops=dict(arrowstyle='->', color='#1B365D', lw=1.0))
    axes[0].annotate(r'$P_1(t=T/4): x=0$', xy=(np.pi/2, 0), xytext=(np.pi/2 + 0.2, 0.35), fontsize=9, color='#1B365D',
                     arrowprops=dict(arrowstyle='->', color='#1B365D', lw=1.0))
    axes[0].annotate(r'$P_2(t=T/2): x=-A$', xy=(np.pi, -1), xytext=(np.pi + 0.15, -0.75), fontsize=9, color='#1B365D',
                     arrowprops=dict(arrowstyle='->', color='#1B365D', lw=1.0))
    axes[0].set_ylim(-1.35, 1.4)
    axes[0].legend(loc='upper right', framealpha=0.92)

    # v(t)
    axes[1].plot(t, v, color='#1E6B52', linestyle='-', label=r'Vận tốc $\frac{v(t)}{\omega A} = \cos(\omega t + \pi/2)$ (Sớm pha $\pi/2$ so với $x$)')
    axes[1].set_ylabel(r'Vận tốc $\frac{v}{\omega A}$')
    axes[1].axhline(0, color='gray', linewidth=0.8, linestyle='--')
    axes[1].scatter([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], [0, -1, 0, 1, 0], color='#1E6B52', s=35, zorder=5)
    axes[1].annotate(r'Vận tốc cực đại theo chiều âm: $v = -\omega A$', xy=(np.pi/2, -1), xytext=(np.pi/2 + 0.2, -0.65), fontsize=9, color='#1E6B52',
                     arrowprops=dict(arrowstyle='->', color='#1E6B52', lw=1.0))
    axes[1].annotate(r'Vận tốc cực đại theo chiều dương: $v = +\omega A$', xy=(3*np.pi/2, 1), xytext=(3*np.pi/2 - 1.6, 1.08), fontsize=9, color='#1E6B52',
                     arrowprops=dict(arrowstyle='->', color='#1E6B52', lw=1.0))
    axes[1].set_ylim(-1.35, 1.4)
    axes[1].legend(loc='upper right', framealpha=0.92)

    # a(t)
    axes[2].plot(t, a, color='#A6192E', linestyle='-', label=r'Gia tốc $\frac{a(t)}{\omega^2 A} = \cos(\omega t + \pi)$ (Ngược pha $\pi$ so với $x$)')
    axes[2].set_ylabel(r'Gia tốc $\frac{a}{\omega^2 A}$')
    axes[2].axhline(0, color='gray', linewidth=0.8, linestyle='--')
    axes[2].scatter([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], [-1, 0, 1, 0, -1], color='#A6192E', s=35, zorder=5)
    axes[2].annotate(r'Gia tốc kéo về cực đại: $a = +\omega^2 A$', xy=(np.pi, 1), xytext=(np.pi + 0.2, 0.65), fontsize=9, color='#A6192E',
                     arrowprops=dict(arrowstyle='->', color='#A6192E', lw=1.0))
    axes[2].set_ylim(-1.35, 1.4)
    axes[2].legend(loc='upper right', framealpha=0.92)

    # X-axis ticks in terms of period T
    ticks = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    tick_labels = [r'$0$', r'$\frac{T}{4}$', r'$\frac{T}{2}$', r'$\frac{3T}{4}$', r'$T$']
    axes[2].set_xticks(ticks)
    axes[2].set_xticklabels(tick_labels)
    axes[2].set_xlabel(r'Thời gian $t$ tính theo chu kỳ $T$ ($T = 2\pi/\omega$)')

    for ax in axes:
        ax.axvline(np.pi/2, color='#94A3B8', linestyle=':', alpha=0.7)
        ax.axvline(np.pi, color='#94A3B8', linestyle=':', alpha=0.7)
        ax.axvline(3*np.pi/2, color='#94A3B8', linestyle=':', alpha=0.7)

    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'fig1_1_kinematics.png'), dpi=300)
    fig.savefig(os.path.join(FIG_DIR, 'fig1_1_kinematics.pdf'))
    plt.close()
    print("Generated: fig1_1_kinematics")

# -------------------------------------------------------------
# Figure 1.2: State Orbit (x, v/omega) based on Independent Relation
# -------------------------------------------------------------
def plot_fig1_phase_space():
    fig, ax = plt.subplots(figsize=(6.8, 6.2))
    
    radii = [0.6, 1.2, 1.8]
    colors = ['#64748B', '#1B365D', '#A6192E']
    labels = [r'Biên độ nhỏ $A_1$', r'Biên độ chuẩn $A_2$', r'Biên độ lớn $A_3$']
    
    theta = np.linspace(0, 2*np.pi, 400)
    for r, c, lab in zip(radii, colors, labels):
        x = r * np.cos(theta)
        y = -r * np.sin(theta)  # Clockwise flow
        ax.plot(x, y, color=c, label=lab)
        
        # Add directional arrows along trajectory
        arrow_theta = [0, np.pi/2, np.pi, 3*np.pi/2]
        for at in arrow_theta:
            ax.annotate('', xy=(r*np.cos(at - 0.08), -r*np.sin(at - 0.08)),
                        xytext=(r*np.cos(at), -r*np.sin(at)),
                        arrowprops=dict(arrowstyle='->', color=c, lw=1.6))

    # Mark dynamic milestones on middle trajectory A2
    r_mid = 1.2
    pts = [
        (r_mid, 0, r'$S_0(t=0): (+A, 0)$', (0.1, 0.15)),
        (0, -r_mid, r'$S_1(t=\frac{T}{4}): (0, -\omega A)$', (0.1, -0.25)),
        (-r_mid, 0, r'$S_2(t=\frac{T}{2}): (-A, 0)$', (-1.1, 0.15)),
        (0, r_mid, r'$S_3(t=\frac{3T}{4}): (0, +\omega A)$', (0.1, 0.15))
    ]
    for px, py, plabel, (dx, dy) in pts:
        ax.scatter([px], [py], color='#D97706', s=55, zorder=6)
        ax.annotate(plabel, xy=(px, py), xytext=(px + dx, py + dy),
                    fontsize=9.5, fontweight='bold', color='#1B365D',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.85, edgecolor='#D97706'))

    ax.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    ax.axvline(0, color='gray', linestyle='--', linewidth=0.8)
    ax.set_aspect('equal')
    ax.set_xlabel(r'Li độ $x$ (m)')
    ax.set_ylabel(r'Vận tốc chuẩn hoá $\frac{v}{\omega}$ (m)')
    ax.set_title(r'Đồ thị trạng thái $(x, v/\omega)$ từ hệ thức: $(x/A)^2 + (v/\omega A)^2 = 1$')
    ax.legend(loc='lower left', framealpha=0.92, fontsize=9)
    
    ax.set_xlim(-2.3, 2.3)
    ax.set_ylim(-2.3, 2.3)

    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'fig1_2_phase_space.png'), dpi=300)
    fig.savefig(os.path.join(FIG_DIR, 'fig1_2_phase_space.pdf'))
    plt.close()
    print("Generated: fig1_2_phase_space")

# -------------------------------------------------------------
# Figure 1.3: Potential Well & Parabolic Approximation
# -------------------------------------------------------------
def plot_fig1_potential_well():
    x = np.linspace(-1.4, 2.0, 500)
    # Generic realistic well
    V_exact = (1 - np.exp(-x))**2
    V_harm = x**2

    fig, ax = plt.subplots(figsize=(7.5, 5.2))
    ax.plot(x, V_exact, color='#1B365D', lw=2.2, label=r'Thế năng thực tế $W_t(x)$ (Dạng đáy chảo trũng)')
    ax.plot(x, V_harm, color='#A6192E', linestyle='--', lw=2.0, label=r'Đường cong Parabol xấp xỉ $W_t \approx \frac{1}{2}kx^2$')
    
    # Boundary of linear/harmonic region
    ax.axvspan(-0.35, 0.35, color='#FEF08A', alpha=0.45, label=r'Vùng dao động nhỏ ($|x| \ll 1$): Mô hình điều hòa chuẩn xác')
    ax.axvline(-0.35, color='#CA8A04', linestyle=':', lw=1.2)
    ax.axvline(0.35, color='#CA8A04', linestyle=':', lw=1.2)

    # Particle rolling in potential well (Mental Model)
    x_ball = 0.55
    V_ball = (1 - np.exp(-x_ball))**2
    ax.scatter([x_ball], [V_ball], color='#D97706', s=80, zorder=6, label=r'Vật đang trượt tại li độ $x$')
    # Force vector pointing toward x0
    ax.annotate(r'Lực kéo về hướng về đáy $x_0$', xy=(x_ball - 0.25, V_ball - 0.05),
                xytext=(x_ball + 0.1, V_ball + 0.35),
                arrowprops=dict(arrowstyle='->', color='#D97706', lw=1.8),
                fontsize=9.5, fontweight='bold', color='#D97706')

    # Energy level line
    E_level = 0.12
    ax.axhline(E_level, color='#1E6B52', linestyle=':', lw=1.4, label=r'Cơ năng $W$ của vật')
    ax.scatter([0], [0], color='#1B365D', s=60, zorder=5)
    ax.text(0.05, -0.16, r'Đáy giếng - Vị trí cân bằng bền ($x_0 = 0$)', fontsize=9.5, color='#1B365D', fontweight='bold')
    
    # Non-linear divergence annotation
    ax.annotate(r'Biên độ lớn: Đường cong thực tách rời Parabol' + '\n' + r'(Không còn là dao động điều hòa đơn giản)',
                xy=(1.3, 1.8), xytext=(0.7, 2.15),
                arrowprops=dict(arrowstyle='->', color='#A6192E', lw=1.2),
                fontsize=9, color='#A6192E')

    ax.set_ylim(-0.25, 2.6)
    ax.set_xlim(-1.25, 1.85)
    ax.set_xlabel(r'Độ dời khỏi vị trí cân bằng $x$ (m)')
    ax.set_ylabel(r'Thế năng $W_t(x)$ (J)')
    ax.set_title(r'Bản chất: Vì sao dao động nhỏ quanh vị trí cân bằng bền là điều hòa?')
    ax.legend(loc='upper right', framealpha=0.92, fontsize=8.8)

    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'fig1_3_potential_well.png'), dpi=300)
    fig.savefig(os.path.join(FIG_DIR, 'fig1_3_potential_well.pdf'))
    plt.close()
    print("Generated: fig1_3_potential_well")

# -------------------------------------------------------------
# Figure 1.4: Energy Evolution & Equipartition
# -------------------------------------------------------------
def plot_fig1_energy():
    t = np.linspace(0, 2*np.pi, 500)
    E_tot = 1.0
    E_p = E_tot * np.cos(t)**2
    E_k = E_tot * np.sin(t)**2

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.6))

    # Left: Energy vs Time
    ax1.plot(t, E_p, color='#1B365D', linestyle='--', label=r'Thế năng $W_t(t) = \frac{1}{2}kx^2$')
    ax1.plot(t, E_k, color='#1E6B52', linestyle='-', label=r'Động năng $W_{đ}(t) = \frac{1}{2}mv^2$')
    ax1.axhline(E_tot, color='#A6192E', linewidth=1.8, label=r'Cơ năng bảo toàn $W = W_{đ} + W_t$')
    ax1.axhline(E_tot/2, color='#475569', linestyle=':', lw=1.5, label=r'Giá trị trung bình $\bar{W}_{đ} = \bar{W}_t = \frac{1}{2}W$')
    
    # Energy exchange arrow
    ax1.annotate('Chuyển hóa liên tục\nĐộng năng ' + r'$\leftrightarrow$' + ' Thế năng',
                 xy=(np.pi/4, 0.5), xytext=(np.pi/4 + 0.3, 0.72),
                 arrowprops=dict(arrowstyle='->', color='#D97706', lw=1.2),
                 fontsize=8.5, color='#D97706')

    ax1.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax1.set_xticklabels([r'$0$', r'$\frac{T}{4}$', r'$\frac{T}{2}$', r'$\frac{3T}{4}$', r'$T$'])
    ax1.set_xlabel(r'Thời gian $t$ theo chu kỳ $T$')
    ax1.set_ylabel(r'Năng lượng / $W$')
    ax1.set_title(r'(a) Động năng và Thế năng biến thiên theo thời gian')
    ax1.legend(loc='lower center', bbox_to_anchor=(0.5, -0.34), framealpha=0.92, fontsize=8.8, ncol=2)

    # Right: Energy vs Displacement x
    x = np.linspace(-1, 1, 300)
    Ep_x = E_tot * x**2
    Ek_x = E_tot * (1 - x**2)
    ax2.plot(x, Ep_x, color='#1B365D', linestyle='--', label=r'$W_t(x) = \frac{1}{2}kx^2$')
    ax2.plot(x, Ek_x, color='#1E6B52', linestyle='-', label=r'$W_{đ}(x) = W - \frac{1}{2}kx^2$')
    ax2.axhline(E_tot, color='#A6192E', linewidth=1.8, label=r'Cơ năng $W$')
    
    # Mark intersection x = +/- A / sqrt(2)
    x_cross = 1 / np.sqrt(2)
    ax2.scatter([x_cross, -x_cross], [E_tot/2, E_tot/2], color='#D97706', s=45, zorder=5)
    ax2.annotate(r'$x = \pm \frac{A}{\sqrt{2}} \Rightarrow W_{đ} = W_t = \frac{W}{2}$', 
                 xy=(x_cross, E_tot/2), xytext=(-0.15, 0.22),
                 arrowprops=dict(arrowstyle='->', color='#D97706', lw=1.2),
                 fontsize=9.2, fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.9, edgecolor='#D97706'))
    
    ax2.set_xlabel(r'Li độ chuẩn hoá $x/A$')
    ax2.set_ylabel(r'Năng lượng / $W$')
    ax2.set_title(r'(b) Phân bố năng lượng theo vị trí $x$')
    ax2.legend(loc='lower center', bbox_to_anchor=(0.5, -0.34), framealpha=0.92, fontsize=8.8, ncol=3)

    plt.tight_layout()
    fig.subplots_adjust(bottom=0.26)
    fig.savefig(os.path.join(FIG_DIR, 'fig1_4_energy.png'), dpi=300)
    fig.savefig(os.path.join(FIG_DIR, 'fig1_4_energy.pdf'))
    plt.close()
    print("Generated: fig1_4_energy")

# -------------------------------------------------------------
# Figure 1.5: Damped Oscillations (3 Regimes)
# -------------------------------------------------------------
def plot_fig1_damped():
    t = np.linspace(0, 25, 700)
    w0 = 2.0

    # 1. Underdamped (gamma = 0.2 < w0)
    gamma1 = 0.2
    wd1 = np.sqrt(w0**2 - gamma1**2)
    x_under = np.exp(-gamma1 * t) * np.cos(wd1 * t)
    env_upper = np.exp(-gamma1 * t)
    env_lower = -np.exp(-gamma1 * t)

    # 2. Critically damped (gamma = w0)
    gamma2 = w0
    x_crit = (1 + w0 * t) * np.exp(-w0 * t)

    # 3. Overdamped (gamma = 3.0 > w0)
    gamma3 = 3.0
    r1 = -gamma3 + np.sqrt(gamma3**2 - w0**2)
    r2 = -gamma3 - np.sqrt(gamma3**2 - w0**2)
    c1 = -r2 / (r1 - r2)
    c2 = r1 / (r1 - r2)
    x_over = c1 * np.exp(r1 * t) + c2 * np.exp(r2 * t)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.6))

    # Time domain
    ax1.plot(t, x_under, color='#1B365D', label=r'Lực cản nhỏ: Dao động tắt dần')
    ax1.plot(t, env_upper, color='#1B365D', linestyle=':', alpha=0.65, label=r'Đường bao giảm biên độ')
    ax1.plot(t, env_lower, color='#1B365D', linestyle=':', alpha=0.65)
    ax1.plot(t, x_crit, color='#1E6B52', linestyle='--', linewidth=2.2, label=r'Lực cản tới hạn: Về VTCB nhanh nhất (Bộ giảm xóc)')
    ax1.plot(t, x_over, color='#A6192E', linestyle='-.', label=r'Lực cản quá lớn: Trì trệ trở về (Cửa chống sập)')
    
    # Mark settling region
    ax1.axhline(0.05, color='#94A3B8', linestyle='--', alpha=0.6)
    ax1.axhline(-0.05, color='#94A3B8', linestyle='--', alpha=0.6)
    ax1.annotate(r'Dải dừng $\pm 5\%$ biên độ ban đầu', xy=(18, 0.05), xytext=(11, 0.35),
                 arrowprops=dict(arrowstyle='->', color='#475569', lw=1.0),
                 fontsize=8.5, color='#475569')

    ax1.set_xlabel(r'Thời gian $t$ (s)')
    ax1.set_ylabel(r'Li độ $x(t)$ (m)')
    ax1.set_title(r'(a) Ba chế độ chuyển động khi có lực cản môi trường')
    ax1.legend(loc='upper right', fontsize=8.2, framealpha=0.92)

    # Phase plane for underdamped: Spiral towards origin
    v_under = -gamma1 * x_under - wd1 * np.exp(-gamma1 * t) * np.sin(wd1 * t)
    ax2.plot(x_under, v_under/w0, color='#1B365D', lw=1.4)
    ax2.scatter([x_under[0]], [v_under[0]/w0], color='#A6192E', s=50, zorder=6, label=r'Trạng thái ban đầu $(x_0, 0)$')
    ax2.scatter([0], [0], color='#1E6B52', s=70, marker='X', zorder=6, label=r'Dừng lại tại VTCB $(0,0)$')
    
    # Trajectory arrows
    for idx in [40, 140, 240, 340]:
        ax2.annotate('', xy=(x_under[idx+6], v_under[idx+6]/w0),
                     xytext=(x_under[idx], v_under[idx]/w0),
                     arrowprops=dict(arrowstyle='->', color='#1B365D', lw=1.3))

    ax2.set_xlabel(r'Li độ $x$ (m)')
    ax2.set_ylabel(r'Vận tốc chuẩn hoá $v/\omega_0$ (m)')
    ax2.set_title(r'(b) Quỹ đạo xoắn ốc thu nhỏ dần về gốc toạ độ')
    ax2.legend(loc='lower left', fontsize=8.5, framealpha=0.92)

    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'fig1_5_damped.png'), dpi=300)
    fig.savefig(os.path.join(FIG_DIR, 'fig1_5_damped.pdf'))
    plt.close()
    print("Generated: fig1_5_damped")

# -------------------------------------------------------------
# Figure 1.6: Forced Resonance (Amplitude & Phase Lag)
# -------------------------------------------------------------
def plot_fig1_resonance():
    w0 = 1.0
    w = np.linspace(0.1, 2.0, 600)
    F0_over_m = 1.0
    
    gamma_list = [0.05, 0.1, 0.2, 0.5]
    colors = ['#A6192E', '#D97706', '#1E6B52', '#1B365D']
    q_labels = [r'Lực cản rất nhỏ (Biên độ vọt rất cao)', r'Lực cản nhỏ', r'Lực cản trung bình', r'Lực cản lớn (Đỉnh thoai thoải)']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.6))

    for g, c, ql in zip(gamma_list, colors, q_labels):
        # Amplitude
        A = F0_over_m / np.sqrt((w0**2 - w**2)**2 + 4 * (g**2) * (w**2))
        ax1.plot(w / w0, A, color=c, label=ql)
        
        # Resonance peak marker
        if w0**2 - 2 * g**2 > 0:
            w_res = np.sqrt(w0**2 - 2 * g**2)
            A_max = F0_over_m / np.sqrt((w0**2 - w_res**2)**2 + 4 * (g**2) * (w_res**2))
            ax1.scatter([w_res/w0], [A_max], color=c, s=30, zorder=5)

        # Phase lag delta
        delta = np.arctan2(2 * g * w, w0**2 - w**2)
        ax2.plot(w / w0, delta / np.pi, color=c, label=ql)

    ax1.axvline(1.0, color='gray', linestyle=':', label=r'Tần số riêng $\Omega = \omega_0$')
    ax1.set_xlabel(r'Tần số ngoại lực chuẩn hoá $\Omega / \omega_0$')
    ax1.set_ylabel(r'Biên độ dao động xác lập $A$ (m)')
    ax1.set_title(r'(a) Hiện tượng cộng hưởng: Đỉnh biên độ khi $\Omega \approx \omega_0$')
    ax1.legend(loc='upper right', fontsize=8.2, framealpha=0.92)

    # Operating regions annotations
    ax1.text(0.25, 8.5, 'Vùng tần số thấp\n' + r'$\Omega \ll \omega_0$', fontsize=8.5, color='#475569', ha='center')
    ax1.text(1.7, 8.5, 'Vùng tần số cao\n' + r'$\Omega \gg \omega_0$', fontsize=8.5, color='#475569', ha='center')

    ax2.axvline(1.0, color='gray', linestyle=':')
    ax2.axhline(0.5, color='#D97706', linestyle='--', lw=1.2, label=r'Độ lệch pha $\frac{\pi}{2}$ tại cộng hưởng')
    ax2.scatter([1.0, 1.0, 1.0, 1.0], [0.5, 0.5, 0.5, 0.5], color='#D97706', s=50, zorder=6)
    ax2.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax2.set_yticklabels([r'$0$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$'])
    ax2.set_xlabel(r'Tần số ngoại lực chuẩn hoá $\Omega / \omega_0$')
    ax2.set_ylabel(r'Độ trễ pha giữa ngoại lực và li độ $\delta / \pi$')
    ax2.set_title(r'(b) Bước nhảy pha qua vùng cộng hưởng')
    ax2.legend(loc='lower right', fontsize=8.2, framealpha=0.92)

    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'fig1_6_resonance.png'), dpi=300)
    fig.savefig(os.path.join(FIG_DIR, 'fig1_6_resonance.pdf'))
    plt.close()
    print("Generated: fig1_6_resonance")

if __name__ == '__main__':
    print("Rendering updated research-grade figures for 11th-grade physics...")
    plot_fig1_0a_derivative()
    plot_fig1_0b_omega_derivative()
    plot_fig1_0c_trig_circle()
    plot_fig1_1a_restoring_force()
    plot_fig1_1b_cosine_anatomy()
    plot_fig1_1c_phase_comparison()
    plot_fig1_kinematics()
    plot_fig1_phase_space()
    plot_fig1_potential_well()
    plot_fig1_energy()
    plot_fig1_damped()
    plot_fig1_resonance()
    print("All figures successfully rendered!")
