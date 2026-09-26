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

FIG_DIR = os.path.join(os.path.dirname(__file__), '..', 'book', 'figures')
os.makedirs(FIG_DIR, exist_ok=True)

# -------------------------------------------------------------
# Figure 1.0: Math Tools (Derivatives, Unit Circle, Omega factor)
# -------------------------------------------------------------
def plot_fig1_math_tools():
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15.0, 4.8))

    # --- Panel 1: Geometric meaning of derivative: s(t) and tangent line ---
    t = np.linspace(0, 4.5, 400)
    s = 0.5 * t**2 + 0.2 * t
    ax1.plot(t, s, color='#1B365D', lw=2.2, label=r'Đồ thị quãng đường $s(t)$')

    t0 = 1.8
    s0 = 0.5 * t0**2 + 0.2 * t0
    v0 = t0 + 0.2  # derivative s'(t) = t + 0.2
    
    # Secant point Q
    dt = 1.8
    t1 = t0 + dt
    s1 = 0.5 * t1**2 + 0.2 * t1
    v_sec = (s1 - s0) / dt
    
    # Draw secant line
    t_sec = np.linspace(0.8, 4.2, 100)
    s_sec_line = s0 + v_sec * (t_sec - t0)
    ax1.plot(t_sec, s_sec_line, color='#D97706', linestyle='--', lw=1.6, 
             label=r'Cát tuyến: $v_{tb} = \frac{\Delta s}{\Delta t}$')
    
    # Draw tangent line at t0
    t_tan = np.linspace(0.5, 3.5, 100)
    s_tan_line = s0 + v0 * (t_tan - t0)
    ax1.plot(t_tan, s_tan_line, color='#1E6B52', lw=2.0,
             label=r'Tiếp tuyến: $v(t) = s^\prime(t) = \tan\theta$')

    # Scatter points P and Q
    ax1.scatter([t0, t1], [s0, s1], color='#A6192E', s=50, zorder=6)
    ax1.annotate(r'$P(t_0, s_0)$', xy=(t0, s0), xytext=(t0 - 0.7, s0 + 0.6),
                 fontsize=9.5, fontweight='bold', color='#1B365D')
    ax1.annotate(r'$Q(t_0+\Delta t, s_0+\Delta s)$', xy=(t1, s1), xytext=(t1 - 1.6, s1 + 0.5),
                 fontsize=9.5, fontweight='bold', color='#D97706')

    # Δt and Δs brackets/lines
    ax1.plot([t0, t1], [s0, s0], color='#64748B', linestyle=':', lw=1.2)
    ax1.plot([t1, t1], [s0, s1], color='#64748B', linestyle=':', lw=1.2)
    ax1.text(t0 + dt/2, s0 - 0.6, r'$\Delta t$', fontsize=9.5, ha='center', color='#475569')
    ax1.text(t1 + 0.15, s0 + (s1 - s0)/2, r'$\Delta s$', fontsize=9.5, va='center', color='#475569')

    ax1.set_xlabel(r'Thời gian $t$ (s)')
    ax1.set_ylabel(r'Quãng đường $s$ (m)')
    ax1.set_title(r'(a) Đạo hàm: Vận tốc tức thời $v = s^\prime(t)$')
    ax1.legend(loc='upper left', fontsize=8.8, framealpha=0.92)
    ax1.set_ylim(-0.5, 12.0)
    ax1.set_xlim(0, 4.5)

    # --- Panel 2: Unit Circle & Angle Shifts (Trigonometric Circle) ---
    theta_circ = np.linspace(0, 2*np.pi, 400)
    ax2.plot(np.cos(theta_circ), np.sin(theta_circ), color='#94A3B8', lw=1.5, linestyle=':')
    ax2.axhline(0, color='gray', lw=0.8, linestyle='--')
    ax2.axvline(0, color='gray', lw=0.8, linestyle='--')

    alpha = np.radians(35)
    # Vector alpha
    x_a = np.cos(alpha)
    y_a = np.sin(alpha)
    ax2.annotate('', xy=(x_a, y_a), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color='#1B365D', lw=2.2))
    # Right triangle for alpha
    ax2.plot([x_a, x_a], [0, y_a], color='#1B365D', linestyle='--', lw=1.0)
    ax2.fill_between([0, x_a], [0, 0], [0, y_a], color='#1B365D', alpha=0.1)
    ax2.text(x_a + 0.05, y_a + 0.05, r'$\vec{u}_1 (\alpha)$', fontsize=10, fontweight='bold', color='#1B365D')
    ax2.text(x_a / 2, -0.15, r'$\cos\alpha$', fontsize=9, color='#1B365D', ha='center')
    ax2.text(x_a + 0.08, y_a / 2, r'$\sin\alpha$', fontsize=9, color='#1B365D', va='center')

    # Vector alpha + pi/2 (rotate 90 deg)
    alpha_pi2 = alpha + np.pi/2
    x_p = np.cos(alpha_pi2)
    y_p = np.sin(alpha_pi2)
    ax2.annotate('', xy=(x_p, y_p), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color='#1E6B52', lw=2.2))
    ax2.plot([x_p, x_p], [0, y_p], color='#1E6B52', linestyle='--', lw=1.0)
    ax2.text(x_p - 0.2, y_p + 0.08, r'$\vec{u}_2 (\alpha + \frac{\pi}{2})$', fontsize=10, fontweight='bold', color='#1E6B52')
    ax2.annotate(r'$\cos(\alpha + \frac{\pi}{2}) = -\sin\alpha$', xy=(x_p, 0), xytext=(x_p - 0.65, -0.45),
                 arrowprops=dict(arrowstyle='->', color='#1E6B52', lw=1.2),
                 fontsize=8.8, fontweight='bold', color='#1E6B52',
                 bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.9, edgecolor='#1E6B52'))

    # Vector alpha + pi (rotate 180 deg)
    alpha_pi = alpha + np.pi
    x_pi = np.cos(alpha_pi)
    y_pi = np.sin(alpha_pi)
    ax2.annotate('', xy=(x_pi, y_pi), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color='#A6192E', lw=2.0))
    ax2.text(x_pi - 0.35, y_pi - 0.15, r'$\vec{u}_3 (\alpha + \pi)$', fontsize=9.5, fontweight='bold', color='#A6192E')
    ax2.annotate(r'$\cos(\alpha + \pi) = -\cos\alpha$', xy=(x_pi, 0), xytext=(x_pi - 0.3, 0.35),
                 arrowprops=dict(arrowstyle='->', color='#A6192E', lw=1.2),
                 fontsize=8.8, fontweight='bold', color='#A6192E',
                 bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.9, edgecolor='#A6192E'))

    # Rotation arc for +pi/2
    arc_theta = np.linspace(alpha, alpha_pi2, 50)
    ax2.plot(0.35 * np.cos(arc_theta), 0.35 * np.sin(arc_theta), color='#D97706', lw=1.5)
    ax2.text(0.18, 0.42, r'$+90^\circ$', fontsize=8.5, color='#D97706', fontweight='bold')

    ax2.set_aspect('equal')
    ax2.set_xlim(-1.45, 1.45)
    ax2.set_ylim(-1.45, 1.45)
    ax2.set_xlabel(r'Trục Hoành $\cos$')
    ax2.set_ylabel(r'Trục Tung $\sin$')
    ax2.set_title(r'(b) Đường tròn Lượng giác & Cung hơn kém')

    # --- Panel 3: Trigonometric Derivative & Angular Frequency Omega ---
    t_trig = np.linspace(0, 2*np.pi, 500)
    x_w1 = np.cos(t_trig)
    x_w2 = np.cos(2 * t_trig)

    ax3.plot(t_trig, x_w1, color='#1B365D', lw=1.8, label=r'$x_1(t) = \cos(t)$ ($\omega = 1$)')
    ax3.plot(t_trig, x_w2, color='#A6192E', linestyle='--', lw=2.0, label=r'$x_2(t) = \cos(2t)$ ($\omega = 2$)')
    ax3.axhline(0, color='gray', lw=0.8, linestyle='--')

    # Tangent at zero-crossing: t = pi/2 for w=1 -> slope = -1
    t_mid1 = np.pi/2
    tan1 = -1 * (t_trig - t_mid1)
    mask1 = (t_trig >= t_mid1 - 0.8) & (t_trig <= t_mid1 + 0.8)
    ax3.plot(t_trig[mask1], tan1[mask1], color='#1B365D', linestyle=':', lw=2.0)
    ax3.scatter([t_mid1], [0], color='#1B365D', s=40, zorder=5)
    ax3.text(t_mid1 + 0.1, 0.45, r'Độ dốc $= -1$', fontsize=8.8, color='#1B365D')

    # Tangent at zero-crossing: t = pi/4 for w=2 -> slope = -2
    t_mid2 = np.pi/4
    tan2 = -2 * (t_trig - t_mid2)
    mask2 = (t_trig >= t_mid2 - 0.6) & (t_trig <= t_mid2 + 0.6)
    ax3.plot(t_trig[mask2], tan2[mask2], color='#A6192E', linestyle=':', lw=2.0)
    ax3.scatter([t_mid2], [0], color='#A6192E', s=40, zorder=5)
    ax3.text(t_mid2 + 0.15, -0.65, r'Độ dốc $= -2$', fontsize=8.8, color='#A6192E')

    # Explanatory annotation
    ax3.annotate(r'Khi $\omega$ tăng 2 lần, đồ thị bị ép hẹp lại 2 lần' + '\n' +
                 r'$\Rightarrow$ Độ dốc (tốc độ biến thiên) tăng 2 lần!' + '\n' +
                 r'$\Rightarrow [\cos(\omega t)]^\prime = -\omega\sin(\omega t)$',
                 xy=(3.5, 0.5), xytext=(2.0, 0.85),
                 fontsize=8.5, color='#1E6B52', fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#F0FDF4', alpha=0.95, edgecolor='#1E6B52'))

    ax3.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax3.set_xticklabels([r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'])
    ax3.set_xlabel(r'Thời gian $t$ (s)')
    ax3.set_ylabel(r'Li độ $x$')
    ax3.set_title(r'(c) Vì sao xuất hiện nhân tử $\omega$ khi lấy đạo hàm?')
    ax3.legend(loc='lower left', fontsize=8.5, framealpha=0.92)
    ax3.set_ylim(-1.5, 1.8)

    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'fig1_0_math_tools.png'), dpi=300)
    fig.savefig(os.path.join(FIG_DIR, 'fig1_0_math_tools.pdf'))
    plt.close()
    print("Generated: fig1_0_math_tools")

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
    plot_fig1_math_tools()
    plot_fig1_kinematics()
    plot_fig1_phase_space()
    plot_fig1_potential_well()
    plot_fig1_energy()
    plot_fig1_damped()
    plot_fig1_resonance()
    print("All figures successfully rendered!")
