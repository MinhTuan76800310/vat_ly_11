// Typst document for Physics 11 Mathematical Toolkit (English Edition)
// Tailored for students and readers with an IELTS 6.5+ proficiency level

#set document(
  title: "Mathematical Toolkit for Grade 11 Physics",
  author: "Vật Lí 11 Chuyên Sâu Editorial Team",
  date: datetime.today()
)

#set page(
  paper: "a4",
  margin: (top: 2.0cm, bottom: 2.0cm, left: 2.1cm, right: 2.1cm),
  header: context {
    if counter(page).get().first() > 1 [
      #grid(
        columns: (1fr, 1fr),
        align: (left, right),
        text(size: 8.5pt, fill: rgb("64748b"), weight: "medium")[
          PHYSICS 11 • INTUITIVE CALCULUS & TRIGONOMETRY
        ],
        text(size: 8.5pt, fill: rgb("94a3b8"))[
          MATHEMATICAL TOOLKIT
        ]
      )
      #v(-3pt)
      #line(length: 100%, stroke: 0.5pt + rgb("cbd5e1"))
    ]
  },
  footer: context [
    #line(length: 100%, stroke: 0.5pt + rgb("cbd5e1"))
    #v(3pt)
    #grid(
      columns: (1fr, 1fr),
      align: (left, right),
      text(size: 8.5pt, fill: rgb("64748b"))[
        Vật Lí 11 Chuyên Sâu • English Edition (IELTS 6.5)
      ],
      text(size: 8.5pt, fill: rgb("475569"), weight: "bold")[
        Page #counter(page).display() of #counter(page).final().first()
      ]
    )
  ]
)

#set text(
  font: ("Libertinus Serif", "Cambria", "Times New Roman"),
  size: 9.8pt,
  lang: "en",
  fill: rgb("1e293b")
)

#set par(
  justify: true,
  leading: 0.62em,
  spacing: 0.95em
)

// Define custom callout boxes (unbreakable to avoid awkward page breaks)
#let callout(title: none, icon: none, color: rgb("1d4ed8"), bg: rgb("f0f6ff"), body) = {
  block(
    width: 100%,
    fill: bg,
    inset: (x: 10pt, y: 5.5pt),
    radius: 4pt,
    stroke: (left: 3pt + color, rest: 0.5pt + color.lighten(70%)),
    spacing: 0.6em,
    breakable: false,
    [
      #if title != none [
        #text(weight: "bold", fill: color, size: 8.5pt)[
          #if icon != none [#icon ]
          #upper(title)
        ]
        #v(1.5pt)
      ]
      #text(fill: rgb("1e293b"), size: 9.2pt)[#body]
    ]
  )
}

#let objective-box(body) = callout(title: "Learning Objective", icon: "💡", color: rgb("2563eb"), bg: rgb("eff6ff"), body)
#let checkpoint-box(title: "Critical Thinking Checkpoint", body) = callout(title: title, icon: "⚠️", color: rgb("d97706"), bg: rgb("fffbeb"), body)
#let discovery-box(title: "Key Scientific Discovery", body) = callout(title: title, icon: "🎯", color: rgb("059669"), bg: rgb("ecfdf5"), body)
#let insight-box(title: "Physical Insight", body) = callout(title: title, icon: "🔍", color: rgb("7c3aed"), bg: rgb("faf5ff"), body)

#let state-card(number: "", title: "", status-badge: none, badge-color: rgb("2563eb"), body) = {
  block(
    width: 100%,
    fill: rgb("f8fafc"),
    stroke: 0.6pt + rgb("cbd5e1"),
    radius: 4.5pt,
    inset: (x: 10pt, y: 5.5pt),
    spacing: 0.6em,
    breakable: false,
    [
      #grid(
        columns: (1fr, auto),
        align: (left + horizon, right + horizon),
        [
          #text(weight: "bold", fill: rgb("0f172a"), size: 9.5pt)[
            State #number: #title
          ]
        ],
        [
          #if status-badge != none [
            #box(
              fill: badge-color.lighten(85%),
              stroke: 0.8pt + badge-color,
              radius: 3pt,
              inset: (x: 5pt, y: 1.5pt),
              text(weight: "bold", size: 7pt, fill: badge-color)[#status-badge]
            )
          ]
        ]
      )
      #v(2.5pt)
      #body
    ]
  )
}

// ==========================================
// PAGE 1: TITLE BANNER & SECTION 1 FOUNDATIONS
// ==========================================
#align(center)[
  #block(
    width: 100%,
    fill: rgb("0f172a"),
    radius: 6pt,
    inset: (x: 14pt, y: 12pt),
    [
      #text(weight: "bold", size: 7.5pt, fill: rgb("38bdf8"), tracking: 1.5pt)[
        PHYSICS 11 CHUYÊN SÂU • PEDAGOGICAL FOUNDATIONS
      ]
      #v(3pt)
      #text(weight: "bold", size: 16pt, fill: white)[
        Mathematical Toolkit for Grade 11 Physics
      ]
      #v(2pt)
      #text(size: 10.5pt, fill: rgb("cbd5e1"), style: "italic")[
        Intuitive Calculus, Deductive Derivatives & The Unit Circle Celestial Clock
      ]
      #v(6pt)
      #grid(
        columns: (auto, auto, auto),
        gutter: 8pt,
        align: center,
        box(fill: rgb("1e293b"), radius: 3pt, inset: (x: 6pt, y: 2pt), text(size: 7.5pt, fill: rgb("94a3b8"))[Target: IELTS Band 6.5+]),
        box(fill: rgb("1e293b"), radius: 3pt, inset: (x: 6pt, y: 2pt), text(size: 7.5pt, fill: rgb("94a3b8"))[Curriculum: Vietnam GDPT 2018]),
        box(fill: rgb("1e293b"), radius: 3pt, inset: (x: 6pt, y: 2pt), text(size: 7.5pt, fill: rgb("94a3b8"))[Topic: Simple Harmonic Motion])
      )
    ]
  )
]

#v(2pt)

#objective-box[
  Rather than relying on mechanical rote memorization or arbitrary algebraic recipes, this toolkit guides you through the fundamental mathematical machinery that physicists utilize to describe motion: from the *instantaneous rate of change* (the derivative) to the geometric elegance of trigonometric vectors orbiting on the unit circle.
]

== 1. What is a Derivative, Really? (The Rate of Change Over Time)

=== From Average Speed to Instantaneous Speed
Imagine riding a motorbike along a straight road. You cover a spatial distance $Delta s$ within an elapsed time interval $Delta t$. The standard parameter representing your overall motion over that entire interval is known as the *average speed*:

$ v_"avg" = (Delta s) / (Delta t) $

However, consider what happens when you abruptly twist the throttle to accelerate and pass a vehicle. If you cast a rapid glance at your speedometer needle at that precise second, what value does the dial actually measure?

That reading represents your *instantaneous speed*—your rate of motion during one infinitesimally brief flash of time. To capture this concept mathematically, physicists conceptually shrink the measurement interval $Delta t$ until it approaches zero ($Delta t -> 0$). Under this limit, the ratio of distance to time converges to a definite, well-defined value, termed the *derivative of position with respect to time*:

$ v(t) = lim_(Delta t -> 0) (Delta s) / (Delta t) = s'(t) = (d s) / (d t) $

#block(
  width: 100%,
  breakable: false,
  align(center)[
    #image("figures/fig1_0a_derivative.pdf", width: 68%)
    #v(1pt)
    #text(size: 8pt, fill: rgb("475569"), style: "italic")[
      *Figure 1.0a:* Geometric foundation of the derivative. The secant line $P Q$ illustrates average speed. As $Delta t -> 0$, $Q$ glides toward $P$, morphing into the tangent line whose slope $tan theta = s'(t_0)$ defines instantaneous velocity.
    ]
  ]
)

#pagebreak()

// ==========================================
// PAGE 2: GEOMETRIC MEANING, ACCELERATION & NOTATION TABLE
// ==========================================

- *Geometric Interpretation:* On a distance-time graph (Figure 1.0a), a straight line intersecting two separate coordinates $P$ and $Q$ is called a *secant line*, representing average speed over that span. When point $Q$ slides infinitesimally close to point $P$ ($Delta t -> 0$), this secant line pivots smoothly into the *tangent line* resting against the curve at point $P$.
  - Therefore, *instantaneous velocity is geometrically equivalent to the slope ($tan theta$) of the tangent line* touching the position-time curve at that specific instant.
  - A steep upward tangent slope indicates that the object is traveling with high speed.
  - A flat, horizontal tangent line indicates zero slope, meaning the object has momentarily come to rest ($v = 0$).

=== Acceleration ($a$) — The Rate of Change of Velocity
In the exact same manner that spatial position changes over time, an object's velocity is rarely static; it increases during acceleration and drops during braking. The quantity that tracks how rapidly velocity transforms across time is called *acceleration*:

$ a(t) = lim_(Delta t -> 0) (Delta v) / (Delta t) = v'(t) = s''(t) = (d v) / (d t) $

In concise terms: *Acceleration is the first derivative of velocity*, which simultaneously establishes it as the second derivative of spatial position with respect to time.

=== International Physics Notation Guide
The alphanumeric symbols featured in secondary school textbooks originate from historic Latin roots and classical English scientific terminology:

#v(2pt)

#block(
  width: 100%,
  breakable: false,
  align(center)[
    #table(
      columns: (1.1fr, 2.3fr, 3.8fr),
      fill: (col, row) => if row == 0 { rgb("1e293b") } else if calc.odd(row) { rgb("f8fafc") } else { white },
      stroke: (col, row) => if row == 0 { none } else { (bottom: 0.5pt + rgb("e2e8f0")) },
      inset: (x: 8pt, y: 5.5pt),
      align: (col, row) => if row == 0 { center + horizon } else { left + horizon },
      table.header(
        text(weight: "bold", fill: white, size: 8.5pt)[Symbol],
        text(weight: "bold", fill: white, size: 8.5pt)[Scientific Meaning],
        text(weight: "bold", fill: white, size: 8.5pt)[Etymological Origin]
      ),
      [$t$], [Time], [English: *Time*],
      [$s$], [Distance / Arc length], [Latin: *Spatium* (Space / Distance)],
      [$x$], [Displacement coordinate], [English: *Coordinate* (along the horizontal $x$-axis)],
      [$v$], [Velocity], [Latin: *Velocitas* / English: *Velocity* (Directed speed)],
      [$a$], [Acceleration], [Latin: *Acceleratio* / English: *Acceleration*],
      [$m$], [Mass], [Latin: *Massa* / English: *Mass*],
      [$F$], [Force], [Latin: *Fortis* (Strength) / English: *Force*],
      [$A$], [Amplitude], [Latin: *Amplitudo* (Maximum displacement from equilibrium)],
      [$omega$], [Angular frequency], [Greek alphabet: *Omega* (Rotational scanning speed of phase)],
      [$T$], [Period of oscillation], [English: *Time Period* (Duration of one complete cycle)],
      [$f$], [Frequency], [English: *Frequency* (Number of oscillations per second)],
      [$W$], [Mechanical Energy / Work], [English: *Work* / German: *Werk* ($W_đ$: Kinetic, $W_t$: Potential, $W$: Total)]
    )
  ]
)

#pagebreak()

// ==========================================
// PAGE 3: SECTION 2 - ROLLER COASTER (STATES 1 & 2)
// ==========================================
== 2. A Roller Coaster on a Cosine Wave: Uncovering Trigonometric Derivatives & the $omega$ Factor

=== Transition from Section 1: Formulating the Velocity Problem
In *Section 1*, we established an indispensable physical principle:
#align(center)[
  #block(
    fill: rgb("f1f5f9"),
    inset: (x: 12pt, y: 6pt),
    radius: 4pt,
    stroke: 0.5pt + rgb("cbd5e1"),
    text(weight: "semibold", fill: rgb("0f172a"), size: 9.2pt)[
      "Instantaneous velocity is the derivative of displacement: $v(t) = x'(t)$, which geometrically corresponds to the slope of the tangent line on the position-time curve!"
    ]
  )
]

In simple harmonic motion, an oscillating particle's displacement obeys a pure cosine waveform over time:

$ x(t) = cos(t) $

This immediately presents an intriguing deductive problem: *What exact analytical expression represents the velocity function $v(t) = [cos(t)]'$?*

Rather than blindly memorizing derivative formulas from a table, let us imagine boarding a roller-coaster carriage that glides smoothly across the undulating track $x(t) = cos(t)$, carefully observing our tangent slope across four distinct checkpoints (*Figure 1.0b(a)*).

=== A 4-State Deductive Journey: Revealing the Elusive Negative Sign

#state-card(
  number: "1",
  title: "The Highest Crest",
  status-badge: "UNKNOWN SIGN (+sin or -sin?)",
  badge-color: rgb("d97706")
)[
  - *Parameters:* Time $t = 0$, Displacement $x = +1$ (Positive Amplitude).
  - The roller-coaster carriage summits the very highest peak of the hill. At this instantaneous milestone, the carriage ceases its upward ascent and pauses before tipping downward. The track at the summit is completely level and horizontal $==>$ *Tangent Slope $= 0$*.
  - Therefore: $x'(0) = 0$ (velocity at the extreme turning point is strictly zero).
  - Looking back at our repertoire of introductory trigonometric functions, which standard function evaluates to zero at $t = 0$? The sine function, since $sin(0) = 0$!
  - #text(fill: rgb("b45309"), weight: "bold")[A Critical Deduction:] Is the derivative candidate $+sin(t)$ or $-sin(t)$? Because both $+sin(0) = 0$ and $-sin(0) = 0$, *at the very peak of the hill, the sign of the derivative is strictly UNKNOWN!* The sign remains an unsolved riddle until we witness the track's descent.
]

#state-card(
  number: "2",
  title: "Plunging Downward Through Equilibrium — The Eureka Moment",
  status-badge: "EUREKA: -sin(t) CONFIRMED",
  badge-color: rgb("059669")
)[
  - *Parameters:* Time $t = pi / 2$, Displacement $x = 0$ (Equilibrium Point).
  - Departing from the summit, the carriage hurtles downward, rapidly shedding altitude. The vehicle's nose points downward toward the earth $==>$ *The tangent slope must be decisively NEGATIVE!*
  - Exactly at $t = pi / 2$, as the carriage roars through the equilibrium point $x = 0$, the track plunges at an angle of $-45^compose$, registering a steep negative slope of *$-1$*.
  - Now, let us test our two competing sign hypotheses against this physical reality:
    - *Hypothesis A (Positive Sign):* If $[cos(t)]' = +sin(t)$, then at $t = pi / 2$, we would obtain $+sin(pi / 2) = +1$ (a positive slope). This blatantly contradicts the observed downward plunge!
    - *Hypothesis B (Negative Sign):* If $[cos(t)]' = -sin(t)$, then at $t = pi / 2$, we obtain $-sin(pi / 2) = -1$ (a negative slope). This matches the physical track slope of $-1$ with flawless precision!
]

#discovery-box(title: "Groundbreaking Finding: The Negative Sign Revealed")[
  The rapid downward plunge through the equilibrium position resolves the mystery once and for all: the derivative of the cosine function *must incorporate an intrinsic minus sign*:
  $ [cos(t)]' = -sin(t) $
]

#pagebreak()

// ==========================================
// PAGE 4: STATES 3 & 4 + THE TIME-COMPRESSION MACHINE
// ==========================================

#state-card(
  number: "3",
  title: "The Deepest Trough",
  status-badge: "VERIFIED: v = 0",
  badge-color: rgb("2563eb")
)[
  - *Parameters:* Time $t = pi$, Displacement $x = -1$ (Negative Extreme).
  - The carriage reaches the lowest valley floor. For an instantaneous fraction of a second, downward descent halts prior to curving upward. The track is once again flat and horizontal $==>$ *Slope $= 0$*.
  - *Analytical Verification:* $-sin(pi) = 0$. This aligns completely with the physical fact that velocity vanishes at extreme boundaries.
]

#state-card(
  number: "4",
  title: "Rocketing Upward Through Equilibrium",
  status-badge: "VERIFIED: v = +v_max",
  badge-color: rgb("2563eb")
)[
  - *Parameters:* Time $t = (3pi) / 2$, Displacement $x = 0$ (Equilibrium Point).
  - Rocketing out of the valley, the carriage shoots upward past the central equilibrium line, tilted skyward at $+45^compose$ $==>$ *Slope achieves its positive maximum: $+1$*.
  - *Analytical Verification:* $-sin((3pi) / 2) = -(-1) = +1$. The formula is completely verified across all quadrants!
]

=== The "Time-Compression Machine": Why Does the $omega$ Factor Emerge?
In Section 1, we recognized $omega$ as the *angular frequency* (the rate at which the oscillation's phase angle advances over time). Let us now examine the generalized oscillation equation: $x(t) = cos(omega t)$.  
Why does its temporal derivative become $-omega sin(omega t)$ rather than merely $-sin(omega t)$?

#align(center)[
  #image("figures/fig1_0b_omega_derivative.pdf", width: 90%)
  #v(-2pt)
  #text(size: 8pt, fill: rgb("475569"), style: "italic")[
    *Figure 1.0b:* Storytelling trigonometric differentiation: (a) The 4-state roller-coaster expedition revealing the minus sign $[cos(t)]' = -sin(t)$; (b) The time-compression effect induced by angular frequency $omega$, which steepens the curve's profile by exactly $omega$ times.
  ]
]

Observe the side-by-side comparison in *Figure 1.0b(b)*:
- *Baseline Case ($omega = 1$):* The wave rolls gently with an extended period $T = 2pi$. Journeying from the crest ($x = 1$) to equilibrium ($x = 0$) takes an elapsed time of $Delta t = pi / 2$, generating an equilibrium slope of $-1$.
- *Compressed Case ($omega = 2$):* When the angular frequency doubles, the oscillation's period is *compressed to exactly half its former duration* ($T = pi$). The travel window from summit to equilibrium is halved to merely $Delta t = pi / 4$!
- *The Crucial Geometric Fact:* *The height of the summit (amplitude $A = 1$) remains completely unchanged!*
- Having to clear the identical vertical drop in only half the available time interval forces the hillside to become *twice as steep*!
- Because the geometric slope of the tangent line is magnified by a factor of $omega$ across every coordinate, the instantaneous rate of change (derivative) at equilibrium surges from $-1$ to $-omega = -2$:
  $ [cos(omega t + phi)]' = -omega sin(omega t + phi), quad [sin(omega t + phi)]' = omega cos(omega t + phi) $

#pagebreak()

// ==========================================
// PAGE 5: SECTION 3 - THE CELESTIAL CLOCK
// ==========================================
== 3. Three Satellites on the Celestial Clock: Decoding Phase Angles & the Pythagorean Relation

=== Connecting Sections 1 & 2: The Kinematic Triad Dilemma
By applying the differentiation mechanics rigorously unlocked in Sections 1 and 2, we establish the fundamental kinematic triad governing simple harmonic motion:

$ cases(
  x(t) = A cos(omega t + phi),
  v(t) = x'(t) = -omega A sin(omega t + phi),
  a(t) = v'(t) = -omega^2 A cos(omega t + phi)
) $

At this junction, high school physics students universally confront two intellectual barriers:
1. *The Phase Comparison Barrier:* Position is expressed in $cos$, velocity is framed in $-sin$, while acceleration appears as $-cos$. How can we translate them into a single harmonized $cos$ format to decisively determine which quantity leads or lags?
2. *The Time-Elimination Barrier:* In practical physics laboratories, detectors record position $x$ and velocity $v$ concurrently at an unknown instant. How can we construct a direct algebraic relationship connecting $x$ and $v$ without relying on a clock to measure time $t$?

Standard syllabi typically resolve these hurdles by reciting abstract trigonometric conversion identities:
$ cos(alpha + pi / 2) = -sin alpha, quad cos(alpha + pi) = -cos alpha, quad cos^2 alpha + sin^2 alpha = 1 $

Instead of straining your cognitive memory with abstract identities, let us examine the *orbital synchronized flight of three satellites navigating a unit circle of radius $R = 1$ (Figure 1.0c)*:

#v(2pt)

#align(center)[
  #image("figures/fig1_0c_trig_circle.pdf", width: 94%)
  #v(-2pt)
  #text(size: 8pt, fill: rgb("475569"), style: "italic")[
    *Figure 1.0c:* Storytelling 3 satellites orbiting the unit circle: (a) State 1: Displacement satellite $arrow(u)_1$ and the right-angled Pythagorean triangle establishing the time-independent equation; (b) State 2: Velocity satellite $arrow(u)_2$ leading ahead by $+90^compose$ ($pi / 2$); (c) State 3: Acceleration satellite $arrow(u)_3$ in diametric opposition by $+180^compose$ ($pi$).
  ]
]

#pagebreak()

// ==========================================
// PAGE 6: THE 3 SATELLITES CHOREOGRAPHY & CONCLUSION
// ==========================================
=== The 3-State Satellite Choreography on the Unit Circle

#state-card(
  number: "1",
  title: "The Displacement Satellite & The Pythagorean Symphony",
  status-badge: "TIME-INDEPENDENT EQUATION",
  badge-color: rgb("059669")
)[
  Consider a pointing vector $arrow(u)_1$ of constant unit length ($R = 1$), angled at an instantaneous phase orientation $alpha = omega t + phi$.
  - *Horizontal Projection:* Casting the shadow of $arrow(u)_1$ down onto the horizontal axis yields the *normalized displacement*: $cos alpha = x / A$.
  - *Vertical Projection:* Casting the shadow of $arrow(u)_1$ across onto the vertical axis yields the *normalized velocity magnitude*: $sin alpha = -v / (omega A)$.
  - These two perpendicular geometric shadows, combined with the hypotenuse vector $arrow(u)_1$, construct a *perfect right-angled triangle* (shaded in blue in Figure 1.0c(a))!
  - Applying the immortal *Pythagorean Theorem* ($"adjacent"^2 + "opposite"^2 = "hypotenuse"^2$):
    $ cos^2 alpha + sin^2 alpha = 1 ==> (x / A)^2 + (- v / (omega A))^2 = 1 <==> (x / A)^2 + (v / (omega A))^2 = 1 $
  #insight-box(title: "Physical Insight")[
    The revered "time-independent equation" taught across secondary physics is fundamentally nothing other than *Pythagoras' Theorem mirrored directly onto the kinematic phase plane*!
  ]
]

#state-card(
  number: "2",
  title: "The Velocity Satellite Sprinting +90° Ahead",
  status-badge: "PHASE LEAD: +pi/2 RADIANS",
  badge-color: rgb("2563eb")
)[
  Velocity is an anticipatory physical quantity that forecasts where an object's displacement will wander in the immediate future. Consequently, the velocity satellite $arrow(u)_2$ perpetually orbits ahead of the displacement satellite $arrow(u)_1$ by exactly one quarter turn ($+90^compose$ or $+pi / 2$ radians):
  - When rotated $+90^compose$ counterclockwise into the second quadrant, the original vertical altitude ($sin alpha$) tips over horizontally, landing squarely on the negative side of the horizontal axis.
  - Therefore, the horizontal abscissa of $arrow(u)_2$ is evaluated as $-sin alpha$:
    $ cos(alpha + pi / 2) = -sin alpha $
  - Substituting this fundamental geometric identity into our dynamic velocity equation:
    $ v(t) = -omega A sin(omega t + phi) = omega A cos(omega t + phi + pi / 2) $
  #insight-box(title: "Physical Insight")[
    *Velocity $v$ permanently leads displacement $x$ by a phase angle of $pi / 2$ radians ($90^compose$)!* When displacement has only just arrived at the equilibrium crossing ($x = 0$), velocity has already claimed its maximal summit ($v = v_"max"$).
  ]
]

#state-card(
  number: "3",
  title: "The Acceleration Satellite in Diametric Opposition (+180°)",
  status-badge: "OPPOSITE PHASE: +pi RADIANS",
  badge-color: rgb("dc2626")
)[
  Newton's Second Law of Motion dictates that an object's acceleration is inextricably aligned with the net restoring force ($F_"net" = m a$). Whenever an oscillating mass is displaced outward to the right, the stretched medium exerts an inward tug dragging it back to the left.  
  Accordingly, the acceleration satellite $arrow(u)_3$ orbits in direct diametric opposition, positioned a full half-turn ($+180^compose$ or $+pi$ radians) ahead of $arrow(u)_1$:
  - A rotation through $+180^compose$ translates the vector into point-reflection symmetry through the coordinate origin $O$. Its horizontal projection is inverted into its precise negative counterpart:
    $ cos(alpha + pi) = -cos alpha $
  - Substituting this geometric relation into our acceleration expression:
    $ a(t) = -omega^2 A cos(omega t + phi) = omega^2 A cos(omega t + phi + pi) = -omega^2 x(t) $
  #insight-box(title: "Physical Insight")[
    *Acceleration $a$ is completely out of phase ($pi$ radians or $180^compose$) relative to displacement $x$!* At the very instant displacement peaks at its positive extreme ($x = +A$), acceleration drops to its minimum negative value ($a = -omega^2 A$) to pull the particle backward toward equilibrium.
  ]
]

#v(4pt)

#align(center)[
  #block(
    fill: rgb("f8fafc"),
    stroke: 0.5pt + rgb("cbd5e1"),
    inset: (x: 14pt, y: 5pt),
    radius: 3pt,
    text(size: 8pt, fill: rgb("64748b"))[
      *End of Toolkit* • Prepared for Physics 11 Deep Understanding Repository • Vietnam GDPT 2018 Standard
    ]
  )
]
