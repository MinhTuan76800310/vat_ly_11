"""
Script to generate research-grade figures for Chapter 1: Dao dong (Oscillations).
Outputs both PDF (vector) and PNG (300 DPI, preview-ready) into book/figures/.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

# Research-grade plot styling
plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.titlesize': 14,
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Georgia'],
    'mathtext.fontset': 'cm',
    'lines.linewidth': 1.8,
    'axes.grid': True,
    'grid.alpha': 0.35,
    'grid.linestyle': ':',
    'axes.spines.top': False,
    'axes.spines.right': False,
})

FIG_DIR = os.path.join(os.path.dirname(__file__), '..', 'book', 'figures')
os.makedirs(FIG_DIR, exist_ok=True)

# -------------------------------------------------------------
# Figure 1.1: Kinematics of Harmonic Motion (x, v, a)
# -------------------------------------------------------------
def plot_fig1_kinematics():
    t = np.linspace(0, 2 * np.pi, 500)
    x = np.cos(t)
    v = -np.sin(t)      # v / (omega A)
    a = -np.cos(t)      # a / (omega^2 A)

    fig, axes = plt.subplots(3, 1, figsize=(7.5, 6.2), sharex=True)
    
    # x(t)
    axes[0].plot(t, x, color='#1B365D', label=r'$x(t) = A\cos(\omega t)$')
    axes[0].set_ylabel(r'Li độ $x/A$')
    axes[0].axhline(0, color='gray', linewidth=0.8, linestyle='--')
    axes[0].scatter([0, np.pi, 2*np.pi], [1, -1, 1], color='#1B365D', s=30, zorder=5)
    axes[0].set_ylim(-1.3, 1.3)
    axes[0].legend(loc='upper right', framealpha=0.9)

    # v(t)
    axes[1].plot(t, v, color='#1E6B52', linestyle='-', label=r'$v(t)/\omega = -A\sin(\omega t) = A\cos(\omega t + \pi/2)$')
    axes[1].set_ylabel(r'Vận tốc $\frac{v}{\omega A}$')
    axes[1].axhline(0, color='gray', linewidth=0.8, linestyle='--')
    axes[1].scatter([np.pi/2, 3*np.pi/2], [-1, 1], color='#1E6B52', s=30, zorder=5)
    axes[1].set_ylim(-1.3, 1.3)
    axes[1].legend(loc='upper right', framealpha=0.9)

    # a(t)
    axes[2].plot(t, a, color='#A6192E', linestyle='-', label=r'$a(t)/\omega^2 = -A\cos(\omega t) = A\cos(\omega t + \pi)$')
    axes[2].set_ylabel(r'Gia tốc $\frac{a}{\omega^2 A}$')
    axes[2].axhline(0, color='gray', linewidth=0.8, linestyle='--')
    axes[2].scatter([0, np.pi, 2*np.pi], [-1, 1, -1], color='#A6192E', s=30, zorder=5)
    axes[2].set_ylim(-1.3, 1.3)
    axes[2].legend(loc='upper right', framealpha=0.9)

    # X-axis ticks in terms of period T
    ticks = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    tick_labels = [r'$0$', r'$\frac{T}{4}$', r'$\frac{T}{2}$', r'$\frac{3T}{4}$', r'$T$']
    axes[2].set_xticks(ticks)
    axes[2].set_xticklabels(tick_labels)
    axes[2].set_xlabel(r'Thời gian $t$ (chu kỳ $T = 2\pi/\omega$)')

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
# Figure 1.2: Phase Space Portrait (x, v/omega)
# -------------------------------------------------------------
def plot_fig1_phase_space():
    fig, ax = plt.subplots(figsize=(6.2, 5.8))
    
    radii = [0.5, 1.0, 1.5]
    colors = ['#475569', '#1B365D', '#A6192E']
    labels = [r'$E_1$ (Biên độ $A_1$)', r'$E_2 = 4E_1$ (Biên độ $A_2 = 2A_1$)', r'$E_3 = 9E_1$ (Biên độ $A_3 = 3A_1$)']
    
    theta = np.linspace(0, 2*np.pi, 400)
    for r, c, lab in zip(radii, colors, labels):
        x = r * np.cos(theta)
        y = -r * np.sin(theta)  # Clockwise flow
        ax.plot(x, y, color=c, label=lab)
        
        # Add directional arrows along trajectory
        arrow_theta = [0, np.pi/2, np.pi, 3*np.pi/2]
        for at in arrow_theta:
            ax.annotate('', xy=(r*np.cos(at - 0.05), -r*np.sin(at - 0.05)),
                        xytext=(r*np.cos(at), -r*np.sin(at)),
                        arrowprops=dict(arrowstyle='->', color=c, lw=1.5))

    ax.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    ax.axvline(0, color='gray', linestyle='--', linewidth=0.8)
    ax.set_aspect('equal')
    ax.set_xlabel(r'Li độ $x$ (m)')
    ax.set_ylabel(r'Vận tốc chuẩn hoá $\frac{v}{\omega}$ (m)')
    ax.set_title(r'Chân dung pha (Phase Portrait) của Dao động điều hòa')
    ax.legend(loc='lower left', framealpha=0.9)
    
    # Annotation
    ax.text(1.1, 0.1, r'$(+A, 0)$', fontsize=10, color='#1B365D')
    ax.text(-1.4, 0.1, r'$(-A, 0)$', fontsize=10, color='#1B365D')
    ax.text(0.05, 1.05, r'$(0, +v_{\max}/\omega)$', fontsize=10, color='#1B365D')
    ax.text(0.05, -1.15, r'$(0, -v_{\max}/\omega)$', fontsize=10, color='#1B365D')

    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'fig1_2_phase_space.png'), dpi=300)
    fig.savefig(os.path.join(FIG_DIR, 'fig1_2_phase_space.pdf'))
    plt.close()
    print("Generated: fig1_2_phase_space")

# -------------------------------------------------------------
# Figure 1.3: Potential Well & Taylor Approximation
# -------------------------------------------------------------
def plot_fig1_potential_well():
    x = np.linspace(-1.4, 2.0, 500)
    # Lennard-Jones-like or asymmetric Morse-like well: V(x) = (1 - exp(-x))^2
    V_exact = (1 - np.exp(-x))**2
    # Taylor expansion around x0 = 0: V(0) = 0, V'(0) = 0, V''(0) = 2 -> V_harm = x^2
    V_harm = x**2

    fig, ax = plt.subplots(figsize=(6.8, 4.8))
    ax.plot(x, V_exact, color='#1B365D', label=r'Thế năng thực tế bất kỳ $V(x)$ (bất đối xứng)')
    ax.plot(x, V_harm, color='#A6192E', linestyle='--', label=r'Xấp xỉ điều hòa Parabol $V \approx \frac{1}{2}k_{eff}x^2$')
    
    # Highlight harmonic region
    ax.axvspan(-0.35, 0.35, color='#FEF08A', alpha=0.35, label=r'Vùng dao động nhỏ ($|x| \ll 1$): Trùng khớp tuyệt đối')
    
    # Energy level line
    E_level = 0.08
    ax.axhline(E_level, color='#1E6B52', linestyle=':', label=r'Mức năng lượng thấp $E_0$')
    ax.scatter([0], [0], color='#1B365D', s=50, zorder=5)
    ax.text(0.05, -0.15, r'VTCB bền $x_0$ ($V^{\prime\prime}(x_0) > 0$)', fontsize=10, color='#1B365D')
    
    ax.set_ylim(-0.2, 2.5)
    ax.set_xlim(-1.2, 1.8)
    ax.set_xlabel(r'Độ dời khỏi vị trí cân bằng $x - x_0$')
    ax.set_ylabel(r'Thế năng $V(x)$')
    ax.set_title(r'Bản chất: Khai triển Taylor Giếng thế năng quanh VTCB bền')
    ax.legend(loc='upper right', framealpha=0.9)

    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'fig1_3_potential_well.png'), dpi=300)
    fig.savefig(os.path.join(FIG_DIR, 'fig1_3_potential_well.pdf'))
    plt.close()
    print("Generated: fig1_3_potential_well")

# -------------------------------------------------------------
# Figure 1.4: Energy Evolution & Virial Equipartition
# -------------------------------------------------------------
def plot_fig1_energy():
    t = np.linspace(0, 2*np.pi, 500)
    E_tot = 1.0
    E_p = E_tot * np.cos(t)**2
    E_k = E_tot * np.sin(t)**2

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.0, 4.4))

    # Left: Energy vs Time
    ax1.plot(t, E_p, color='#1B365D', linestyle='--', label=r'Thế năng $E_t(t)$')
    ax1.plot(t, E_k, color='#1E6B52', linestyle='-', label=r'Động năng $E_d(t)$')
    ax1.axhline(E_tot, color='#A6192E', linewidth=1.5, label=r'Cơ năng $E = E_d + E_t$')
    ax1.axhline(E_tot/2, color='#475569', linestyle=':', label=r'$\langle E_d \rangle = \langle E_t \rangle = \frac{E}{2}$')
    
    ax1.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax1.set_xticklabels([r'$0$', r'$\frac{T}{4}$', r'$\frac{T}{2}$', r'$\frac{3T}{4}$', r'$T$'])
    ax1.set_xlabel(r'Thời gian $t$')
    ax1.set_ylabel(r'Năng lượng / $E$')
    ax1.set_title(r'(a) Năng lượng luân chuyển theo thời gian')
    ax1.legend(loc='lower center', bbox_to_anchor=(0.5, -0.32), framealpha=0.9, fontsize=9, ncol=2)

    # Right: Energy vs Displacement x
    x = np.linspace(-1, 1, 300)
    Ep_x = E_tot * x**2
    Ek_x = E_tot * (1 - x**2)
    ax2.plot(x, Ep_x, color='#1B365D', linestyle='--', label=r'$E_t(x) = \frac{1}{2}kx^2$')
    ax2.plot(x, Ek_x, color='#1E6B52', linestyle='-', label=r'$E_d(x) = E - \frac{1}{2}kx^2$')
    ax2.axhline(E_tot, color='#A6192E', linewidth=1.5, label=r'Cơ năng $E$')
    
    # Mark intersection x = +/- A / sqrt(2)
    x_cross = 1 / np.sqrt(2)
    ax2.scatter([x_cross, -x_cross], [E_tot/2, E_tot/2], color='#D97706', s=40, zorder=5)
    ax2.annotate(r'$x = \pm \frac{A}{\sqrt{2}} \Rightarrow E_d = E_t$', 
                 xy=(x_cross, E_tot/2), xytext=(0.05, 0.22),
                 arrowprops=dict(arrowstyle='->', color='#D97706', lw=1.2),
                 fontsize=9.5, bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8, edgecolor='none'))
    
    ax2.set_xlabel(r'Li độ $x/A$')
    ax2.set_ylabel(r'Năng lượng / $E$')
    ax2.set_title(r'(b) Phân bố năng lượng theo li độ')
    ax2.legend(loc='lower center', bbox_to_anchor=(0.5, -0.32), framealpha=0.9, fontsize=9, ncol=3)

    plt.tight_layout()
    fig.subplots_adjust(bottom=0.25)
    fig.savefig(os.path.join(FIG_DIR, 'fig1_4_energy.png'), dpi=300)
    fig.savefig(os.path.join(FIG_DIR, 'fig1_4_energy.pdf'))
    plt.close()
    print("Generated: fig1_4_energy")

# -------------------------------------------------------------
# Figure 1.5: Damped Oscillations (3 Regimes & Phase Spiral)
# -------------------------------------------------------------
def plot_fig1_damped():
    t = np.linspace(0, 25, 600)
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

    # 3. Overdamped (gamma = 4.0 > w0)
    gamma3 = 3.0
    r1 = -gamma3 + np.sqrt(gamma3**2 - w0**2)
    r2 = -gamma3 - np.sqrt(gamma3**2 - w0**2)
    # x(0) = 1, v(0) = 0 -> c1 + c2 = 1, c1*r1 + c2*r2 = 0
    c1 = -r2 / (r1 - r2)
    c2 = r1 / (r1 - r2)
    x_over = c1 * np.exp(r1 * t) + c2 * np.exp(r2 * t)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.4))

    # Time domain
    ax1.plot(t, x_under, color='#1B365D', label=r'Dưới hạn ($\gamma < \omega_0$): Tắt dần dao động')
    ax1.plot(t, env_upper, color='#1B365D', linestyle=':', alpha=0.6, label=r'Đường bao $\pm e^{-\gamma t}$')
    ax1.plot(t, env_lower, color='#1B365D', linestyle=':', alpha=0.6)
    ax1.plot(t, x_crit, color='#1E6B52', linestyle='--', linewidth=2.0, label=r'Tới hạn ($\gamma = \omega_0$): Về 0 nhanh nhất')
    ax1.plot(t, x_over, color='#A6192E', linestyle='-.', label=r'Quá hạn ($\gamma > \omega_0$): Trì hoãn dập tắt')
    
    ax1.set_xlabel(r'Thời gian $t$ (s)')
    ax1.set_ylabel(r'Li độ $x(t)$ (m)')
    ax1.set_title(r'(a) Ba chế độ động học của dao động cản')
    ax1.legend(loc='upper right', fontsize=8.5, framealpha=0.9)

    # Phase plane for underdamped: Spiral attractor
    v_under = -gamma1 * x_under - wd1 * np.exp(-gamma1 * t) * np.sin(wd1 * t)
    ax2.plot(x_under, v_under/w0, color='#1B365D', lw=1.3)
    ax2.scatter([x_under[0]], [v_under[0]/w0], color='#A6192E', s=40, zorder=5, label='Điểm xuất phát $(x_0, 0)$')
    ax2.scatter([0], [0], color='#1E6B52', s=50, marker='X', zorder=5, label='Điểm hút cân bằng $(0,0)$')
    
    # Arrows on spiral
    for idx in [50, 150, 250]:
        ax2.annotate('', xy=(x_under[idx+5], v_under[idx+5]/w0),
                     xytext=(x_under[idx], v_under[idx]/w0),
                     arrowprops=dict(arrowstyle='->', color='#1B365D', lw=1.2))

    ax2.set_xlabel(r'Li độ $x$ (m)')
    ax2.set_ylabel(r'Vận tốc chuẩn hoá $v/\omega_0$ (m)')
    ax2.set_title(r'(b) Chân dung pha: Điểm hút xoắn ốc (Spiral Attractor)')
    ax2.legend(loc='lower left', fontsize=8.5, framealpha=0.9)

    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'fig1_5_damped.png'), dpi=300, bbox_inches='tight')
    fig.savefig(os.path.join(FIG_DIR, 'fig1_5_damped.pdf'), bbox_inches='tight')
    plt.close()
    print("Generated: fig1_5_damped")

# -------------------------------------------------------------
# Figure 1.6: Resonance Response & Phase Lag
# -------------------------------------------------------------
def plot_fig1_resonance():
    w0 = 1.0
    w = np.linspace(0.1, 2.0, 500)
    F0_over_m = 1.0
    
    gamma_list = [0.05, 0.1, 0.2, 0.5]
    colors = ['#A6192E', '#D97706', '#1E6B52', '#1B365D']
    q_labels = [r'$Q = 10$', r'$Q = 5$', r'$Q = 2.5$', r'$Q = 1$']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.4))

    for g, c, ql in zip(gamma_list, colors, q_labels):
        # Amplitude
        denom = np.sqrt((w0**2 - w**2)**2 + 4 * (g**2) * (w**2))
        A = F0_over_m / denom
        ax1.plot(w / w0, A, color=c, label=ql)
        
        # Peak mark
        if w0**2 - 2 * g**2 > 0:
            w_res = np.sqrt(w0**2 - 2 * g**2)
            A_max = F0_over_m / np.sqrt((w0**2 - w_res**2)**2 + 4 * (g**2) * (w_res**2))
            ax1.scatter([w_res/w0], [A_max], color=c, s=25, zorder=5)

        # Phase lag delta = arctan2(2 gamma w, w0^2 - w^2)
        delta = np.arctan2(2 * g * w, w0**2 - w**2)
        ax2.plot(w / w0, delta / np.pi, color=c, label=ql)

    ax1.axvline(1.0, color='gray', linestyle=':', label=r'Tần số riêng $\Omega = \omega_0$')
    ax1.set_xlabel(r'Tần số kích thích chuẩn hoá $\Omega / \omega_0$')
    ax1.set_ylabel(r'Biên độ dao động xác lập $A(\Omega)$')
    ax1.set_title(r'(a) Đường cong cộng hưởng biên độ')
    ax1.legend(loc='upper right', fontsize=8.5, framealpha=0.9)

    ax2.axvline(1.0, color='gray', linestyle=':')
    ax2.axhline(0.5, color='gray', linestyle=':', label=r'Độ lệch pha $\Delta \varphi = \frac{\pi}{2}$')
    ax2.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax2.set_yticklabels([r'$0$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$'])
    ax2.set_xlabel(r'Tần số kích thích chuẩn hoá $\Omega / \omega_0$')
    ax2.set_ylabel(r'Độ trễ pha $\delta$ (rad)')
    ax2.set_title(r'(b) Bước nhảy pha qua vùng cộng hưởng')
    ax2.legend(loc='lower right', fontsize=8.5, framealpha=0.9)

    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'fig1_6_resonance.png'), dpi=300, bbox_inches='tight')
    fig.savefig(os.path.join(FIG_DIR, 'fig1_6_resonance.pdf'), bbox_inches='tight')
    plt.close()
    print("Generated: fig1_6_resonance")

if __name__ == '__main__':
    print("Rendering all research-grade figures for Chapter 1...")
    plot_fig1_kinematics()
    plot_fig1_phase_space()
    plot_fig1_potential_well()
    plot_fig1_energy()
    plot_fig1_damped()
    plot_fig1_resonance()
    print("All figures successfully rendered!")
