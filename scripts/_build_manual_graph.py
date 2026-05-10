"""
Manual knowledge graph builder for Maths grades 6-12.
Built by expert curriculum analysis of 417 raw topics across NCERT + state boards.
Run locally:  python scripts/_build_manual_graph.py
Output:       data/output/knowledge_graph/maths_v2.json
"""

import json
from collections import defaultdict
from pathlib import Path

# ─── CONCEPT DEFINITIONS ──────────────────────────────────────────────────────
# Each entry: (slug, canonical_name, grades, area, prerequisites, description)
CONCEPTS = [

    # ══════════════════════════════════════════════════════════
    # GRADE 6 — FOUNDATIONS
    # ══════════════════════════════════════════════════════════

    ("whole-numbers", "Whole Numbers", [6],
     "Number Systems", [],
     "Non-negative integers 0, 1, 2, 3, … forming the basis of all arithmetic"),

    ("number-patterns", "Number Patterns", [6],
     "Patterns and Sequences", [],
     "Identifying, extending and describing sequences of numbers that follow a rule"),

    ("integers", "Integers", [6],
     "Number Systems", ["whole-numbers"],
     "Positive and negative whole numbers including zero: …-2, -1, 0, 1, 2, …"),

    ("fractions", "Fractions", [6],
     "Number Systems", ["whole-numbers"],
     "Numbers representing parts of a whole, written as p/q where q ≠ 0"),

    ("equivalent-fractions", "Equivalent Fractions", [6],
     "Number Systems", ["fractions"],
     "Different fractions that represent the same value, e.g. 1/2 = 2/4 = 3/6"),

    ("comparing-fractions", "Comparing Fractions", [6],
     "Number Systems", ["equivalent-fractions"],
     "Ordering fractions using LCM of denominators or cross-multiplication"),

    ("addition-subtraction-of-fractions", "Addition and Subtraction of Fractions", [6],
     "Number Systems", ["comparing-fractions"],
     "Adding and subtracting fractions with like and unlike denominators"),

    ("prime-numbers", "Prime Numbers", [6],
     "Number Theory", ["whole-numbers"],
     "Natural numbers > 1 with no positive divisors other than 1 and themselves: 2, 3, 5, 7, 11, …"),

    ("divisibility-rules", "Divisibility Rules", [6],
     "Number Theory", ["prime-numbers"],
     "Shortcuts to test divisibility by 2, 3, 4, 5, 6, 8, 9, 10, 11 without full division"),

    ("prime-factorisation", "Prime Factorisation", [6],
     "Number Theory", ["prime-numbers", "divisibility-rules"],
     "Expressing any integer > 1 as a unique product of prime numbers (Fundamental Theorem of Arithmetic)"),

    ("lcm-and-gcd", "LCM and GCD", [6],
     "Number Theory", ["prime-factorisation"],
     "Lowest Common Multiple and Greatest Common Divisor computed via prime factorisation"),

    ("angles", "Angles", [6],
     "Geometry", [],
     "Measure of rotation between two rays sharing a vertex, measured in degrees"),

    ("types-of-angles", "Types of Angles", [6],
     "Geometry", ["angles"],
     "Acute (< 90°), right (= 90°), obtuse (90°–180°), straight (180°), reflex (> 180°)"),

    ("line-of-symmetry", "Line of Symmetry", [6],
     "Geometry", ["angles"],
     "A line dividing a figure into two congruent mirror-image halves"),

    ("rotational-symmetry", "Rotational Symmetry", [6],
     "Geometry", ["line-of-symmetry"],
     "A figure has rotational symmetry of order n if it maps onto itself n times in a full 360° rotation"),

    ("perimeter", "Perimeter", [6],
     "Mensuration", ["whole-numbers"],
     "Total length of the boundary of a closed 2D figure"),

    ("area", "Area", [6],
     "Mensuration", ["perimeter"],
     "Amount of 2D space enclosed within a boundary, measured in square units"),

    ("data-collection-and-organisation", "Data Collection and Organisation", [6],
     "Statistics", [],
     "Gathering, recording and organising raw data using tally charts, tables and frequency distributions"),

    ("bar-graphs-and-pictographs", "Bar Graphs and Pictographs", [6],
     "Statistics", ["data-collection-and-organisation"],
     "Visual representations of categorical data using bars of proportional height or scaled pictures"),

    ("ratios-and-proportions", "Ratios and Proportions", [6],
     "Number Systems", ["fractions"],
     "Comparing two quantities; proportion states that two ratios are equal (a:b = c:d)"),

    ("percentage", "Percentage", [6, 8],
     "Number Systems", ["fractions", "ratios-and-proportions"],
     "A ratio expressed as a fraction of 100; 40% = 40/100 = 2/5"),

    ("decimals", "Decimals", [6, 7],
     "Number Systems", ["fractions"],
     "Numbers expressed using a decimal point; represent fractions of powers of 10"),

    # ══════════════════════════════════════════════════════════
    # GRADE 7
    # ══════════════════════════════════════════════════════════

    ("decimal-place-value", "Decimal Place Value", [7],
     "Number Systems", ["decimals"],
     "Tenths (10⁻¹), hundredths (10⁻²), thousandths (10⁻³); comparing and locating decimals on number line"),

    ("multiplication-division-of-fractions", "Multiplication and Division of Fractions", [7],
     "Number Systems", ["addition-subtraction-of-fractions"],
     "Multiplying fractions (a/b × c/d = ac/bd); dividing by multiplying by reciprocal"),

    ("rational-numbers", "Rational Numbers", [7],
     "Number Systems", ["fractions", "decimals", "integers"],
     "Numbers expressible as p/q where p, q are integers and q ≠ 0; includes all terminating and recurring decimals"),

    ("algebraic-expressions", "Algebraic Expressions", [7],
     "Algebra", ["number-patterns"],
     "Mathematical expressions containing variables, constants and arithmetic operations; terms, like terms, degree"),

    ("simplification-of-algebraic-expressions", "Simplification of Algebraic Expressions", [7],
     "Algebra", ["algebraic-expressions"],
     "Combining like terms, expanding brackets, applying distributive property"),

    ("algebraic-identities", "Algebraic Identities", [7, 9],
     "Algebra", ["simplification-of-algebraic-expressions"],
     "Standard identities: (a+b)²=a²+2ab+b², (a-b)²=a²-2ab+b², (a+b)(a-b)=a²-b², (x+a)(x+b)=x²+(a+b)x+ab"),

    ("simple-equations", "Simple Equations", [7],
     "Algebra", ["algebraic-expressions"],
     "Linear equations in one variable; solving by transposition, balance method; word problems"),

    ("parallel-lines-and-transversals", "Parallel Lines and Transversals", [7],
     "Geometry", ["angles", "types-of-angles"],
     "Corresponding angles (equal), alternate interior angles (equal), co-interior angles (supplementary)"),

    ("types-of-triangles", "Types of Triangles", [7],
     "Geometry", ["angles"],
     "Classified by sides: scalene, isosceles, equilateral; by angles: acute, right, obtuse"),

    ("properties-of-triangles", "Properties of Triangles", [7, 9],
     "Geometry", ["types-of-triangles", "parallel-lines-and-transversals"],
     "Angle sum = 180°; exterior angle = sum of remote interior angles; triangle inequality"),

    ("congruence-of-triangles", "Congruence of Triangles", [7, 9],
     "Geometry", ["types-of-triangles"],
     "Identical triangles in shape and size; congruence criteria: SSS, SAS, ASA, AAS, RHS"),

    ("similar-triangles", "Similar Triangles", [7, 10],
     "Geometry", ["types-of-triangles", "ratios-and-proportions"],
     "Same shape, different size; AA, SSS, SAS similarity criteria; corresponding sides in proportion"),

    ("mean-median-mode", "Mean, Median and Mode", [7],
     "Statistics", ["data-collection-and-organisation", "fractions"],
     "Mean = sum/count; Median = middle value when sorted; Mode = most frequent value"),

    ("theoretical-probability", "Theoretical Probability", [7],
     "Probability", ["fractions"],
     "P(E) = number of favourable outcomes / total number of equally likely outcomes"),

    ("experimental-probability", "Experimental Probability", [7],
     "Probability", ["theoretical-probability", "mean-median-mode"],
     "Relative frequency from repeated experiments; approaches theoretical probability as trials increase"),

    ("fibonacci-virahanka-sequence", "Fibonacci–Virahanka Sequence", [7],
     "Sequences", ["number-patterns"],
     "1, 1, 2, 3, 5, 8, 13, 21, … each term is sum of two preceding; golden ratio connection"),

    # ══════════════════════════════════════════════════════════
    # GRADE 8
    # ══════════════════════════════════════════════════════════

    ("square-and-cube-numbers", "Square and Cube Numbers", [8],
     "Number Theory", ["prime-factorisation"],
     "Perfect squares (1,4,9,16,…) and perfect cubes (1,8,27,…); square roots and cube roots by prime factorisation"),

    ("exponents-and-powers", "Exponents and Powers", [8],
     "Algebra", ["square-and-cube-numbers"],
     "aⁿ = a×a×…×a (n times); laws of exponents; zero exponent; negative exponents; scientific notation"),

    ("pythagorean-theorem", "Pythagorean Theorem", [7, 8],
     "Geometry", ["congruence-of-triangles", "area"],
     "In a right triangle: a² + b² = c²; Proof; converse; Pythagorean triples (3,4,5), (5,12,13)"),

    ("quadrilaterals", "Quadrilaterals", [8],
     "Geometry", ["angles", "types-of-triangles"],
     "Four-sided polygons; sum of interior angles = 360°; types: parallelogram, rectangle, rhombus, square, kite, trapezium"),

    ("unitary-method-and-direct-proportion", "Unitary Method and Direct Proportion", [7, 8],
     "Proportional Reasoning", ["ratios-and-proportions"],
     "Finding value per unit then scaling; direct proportion y ∝ x means y = kx for constant k"),

    ("inverse-proportion", "Inverse Proportion", [8],
     "Proportional Reasoning", ["unitary-method-and-direct-proportion"],
     "When one quantity increases the other decreases proportionally; product xy remains constant"),

    ("area-of-triangles", "Area of Triangles", [7, 8],
     "Mensuration", ["area", "types-of-triangles"],
     "Area = ½ × base × height; valid for all triangle types regardless of orientation"),

    ("area-of-trapezium", "Area of Trapezium", [7],
     "Mensuration", ["area-of-triangles"],
     "Area = ½ × (a + b) × h where a, b are the parallel sides and h is the perpendicular height"),

    ("heron-s-formula", "Heron's Formula", [7, 9],
     "Mensuration", ["area-of-triangles"],
     "Area = √(s(s−a)(s−b)(s−c)) where s = (a+b+c)/2 (semi-perimeter); useful when height unknown"),

    ("visualising-3d-shapes", "Visualising 3D Shapes", [8],
     "Mensuration", ["area"],
     "Nets of 3D solids; cross-sections; isometric views of cuboids, cylinders, cones and spheres"),

    ("arithmetic-progressions", "Arithmetic Progressions", [8, 9, 10],
     "Sequences", ["number-patterns", "algebraic-expressions"],
     "Sequence with constant common difference d; nth term: aₙ = a + (n−1)d; sum: Sₙ = n/2(2a + (n−1)d)"),

    ("circles", "Circles", [8, 9],
     "Geometry", ["angles", "pythagorean-theorem"],
     "Locus of all points equidistant from a fixed centre; radius, diameter, chord, arc, sector, segment"),

    ("circumference-and-area-of-circle", "Circumference and Area of Circle", [7, 10],
     "Mensuration", ["circles", "ratios-and-proportions"],
     "Circumference C = 2πr; Area A = πr²; the irrational constant π ≈ 3.14159"),

    # ══════════════════════════════════════════════════════════
    # GRADE 9
    # ══════════════════════════════════════════════════════════

    ("irrational-numbers", "Irrational Numbers", [9],
     "Number Systems", ["rational-numbers"],
     "Numbers whose decimal expansion is non-terminating and non-recurring; e.g. √2, √3, π, e"),

    ("real-numbers", "Real Numbers", [9],
     "Number Systems", ["rational-numbers", "irrational-numbers"],
     "The complete number line; union of rational and irrational numbers; density property"),

    ("laws-of-exponents", "Laws of Exponents for Real Numbers", [9],
     "Algebra", ["exponents-and-powers", "real-numbers"],
     "Extended laws including rational exponents: a^(1/n) = ⁿ√a; aᵐ × aⁿ = aᵐ⁺ⁿ; (aᵐ)ⁿ = aᵐⁿ"),

    ("polynomials-in-one-variable", "Polynomials in One Variable", [9],
     "Algebra", ["algebraic-expressions", "algebraic-identities"],
     "Expressions aₙxⁿ + … + a₁x + a₀; degree, leading coefficient; linear, quadratic, cubic polynomials"),

    ("zeroes-of-a-polynomial", "Zeroes of a Polynomial", [9, 10],
     "Algebra", ["polynomials-in-one-variable"],
     "Values of x making p(x) = 0; geometrically the x-intercepts; relationship between zeroes and coefficients"),

    ("factorisation-of-polynomials", "Factorisation of Polynomials", [9],
     "Algebra", ["polynomials-in-one-variable", "algebraic-identities"],
     "Remainder theorem, factor theorem; splitting into irreducible factors; use of algebraic identities"),

    ("quadratic-equations", "Quadratic Equations", [9, 10],
     "Algebra", ["polynomials-in-one-variable", "algebraic-identities"],
     "ax² + bx + c = 0; solutions by factorisation, completing the square, quadratic formula x = (−b ± √D)/2a"),

    ("nature-of-roots", "Nature of Roots of Quadratic Equations", [10],
     "Algebra", ["quadratic-equations"],
     "Discriminant D = b²−4ac: D>0 → two distinct real roots; D=0 → equal roots; D<0 → complex conjugate roots"),

    ("linear-equations-in-two-variables", "Linear Equations in Two Variables", [9],
     "Algebra", ["simple-equations", "cartesian-coordinate-system"],
     "ax + by + c = 0; each solution is a point (x, y); all solutions lie on a straight line"),

    ("pair-of-linear-equations", "Pair of Linear Equations", [10],
     "Algebra", ["linear-equations-in-two-variables"],
     "Simultaneous equations; graphical method (intersection), substitution, elimination, cross-multiplication"),

    ("cartesian-coordinate-system", "Cartesian Coordinate System", [9],
     "Coordinate Geometry", ["real-numbers", "integers"],
     "2D plane defined by perpendicular x- and y-axes; four quadrants; plotting ordered pairs (x, y)"),

    ("euclid-definitions-axioms-postulates", "Euclid's Definitions, Axioms and Postulates", [9],
     "Geometry", ["angles"],
     "Foundations of Euclidean geometry; five postulates; the axiomatic method; equivalent forms of parallel postulate"),

    ("properties-of-parallelogram", "Properties of a Parallelogram", [9],
     "Geometry", ["quadrilaterals"],
     "Opposite sides equal and parallel; opposite angles equal; diagonals bisect each other"),

    ("mid-point-theorem", "Mid-Point Theorem", [9],
     "Geometry", ["properties-of-parallelogram"],
     "Line segment joining midpoints of two sides of a triangle is parallel to the third side and half its length"),

    ("circle-theorems", "Circle Theorems", [9],
     "Geometry", ["circles", "angles"],
     "Angle at centre = 2× angle at circumference; angles in same segment equal; angle in semicircle = 90°; equal chords"),

    ("cyclic-quadrilaterals", "Cyclic Quadrilaterals", [9],
     "Geometry", ["circle-theorems", "quadrilaterals"],
     "Quadrilateral inscribed in a circle; opposite angles sum to 180°; exterior angle = opposite interior angle"),

    ("surface-area-of-solids", "Surface Area of Solids", [9],
     "Mensuration", ["area", "circles"],
     "Formulae for cuboid (2(lb+bh+lh)), cylinder (2πr(r+h)), cone (πr(r+l)), sphere (4πr²)"),

    ("volume-of-solids", "Volume of Solids", [9],
     "Mensuration", ["surface-area-of-solids"],
     "Cuboid (lwh), cylinder (πr²h), cone (⅓πr²h), sphere (⁴⁄₃πr³); comparing volumes"),

    ("trigonometric-ratios", "Trigonometric Ratios", [9, 10],
     "Trigonometry", ["pythagorean-theorem", "similar-triangles"],
     "sin θ = opp/hyp, cos θ = adj/hyp, tan θ = opp/adj and their reciprocals; values at 0°,30°,45°,60°,90°"),

    ("geometric-progressions", "Geometric Progressions", [9, 11],
     "Sequences", ["arithmetic-progressions", "ratios-and-proportions"],
     "Sequence with constant common ratio r; aₙ = arⁿ⁻¹; Sₙ = a(rⁿ−1)/(r−1); sum to infinity for |r|<1"),

    # ══════════════════════════════════════════════════════════
    # GRADE 10
    # ══════════════════════════════════════════════════════════

    ("fundamental-theorem-of-arithmetic", "Fundamental Theorem of Arithmetic", [10],
     "Number Theory", ["prime-factorisation", "lcm-and-gcd"],
     "Every integer > 1 is either prime or can be expressed as a unique product of primes"),

    ("tangent-to-a-circle", "Tangent to a Circle", [10],
     "Geometry", ["circle-theorems", "pythagorean-theorem"],
     "Line touching circle at exactly one point; tangent ⊥ radius; equal tangents from external point theorem"),

    ("area-of-sector-and-segment", "Area of Sector and Segment of a Circle", [10],
     "Mensuration", ["circumference-and-area-of-circle", "trigonometric-ratios"],
     "Sector area = (θ/360°)πr²; arc length = (θ/360°)2πr; segment area = sector − triangle"),

    ("surface-area-volume-combinations", "Surface Area and Volume of Combined Solids", [10],
     "Mensuration", ["surface-area-of-solids", "volume-of-solids"],
     "Solids formed by combining/removing basic 3D shapes; frustum of a cone"),

    ("distance-formula", "Distance Formula", [10],
     "Coordinate Geometry", ["cartesian-coordinate-system", "pythagorean-theorem"],
     "d(P₁,P₂) = √((x₂−x₁)² + (y₂−y₁)²); direct application of Pythagorean theorem in the plane"),

    ("section-formula", "Section Formula", [10],
     "Coordinate Geometry", ["distance-formula", "ratios-and-proportions"],
     "Point dividing (x₁,y₁)–(x₂,y₂) in ratio m:n: P = ((mx₂+nx₁)/(m+n), (my₂+ny₁)/(m+n))"),

    ("trigonometric-identities", "Trigonometric Identities", [10],
     "Trigonometry", ["trigonometric-ratios"],
     "sin²θ + cos²θ = 1; 1 + tan²θ = sec²θ; 1 + cot²θ = cosec²θ; proving and using identities"),

    ("heights-and-distances", "Heights and Distances", [10],
     "Trigonometry", ["trigonometric-identities"],
     "Angle of elevation and depression; solving real-world problems involving heights and horizontal distances"),

    ("mean-of-grouped-data", "Mean of Grouped Data", [10],
     "Statistics", ["mean-median-mode"],
     "Mean using class marks and frequencies; direct method, assumed mean method, step-deviation method"),

    ("probability-theoretical-approach", "Probability — Theoretical Approach", [10],
     "Probability", ["theoretical-probability"],
     "Classical probability; complementary events P(Ā) = 1 − P(A); equally likely outcomes"),

    ("nth-term-and-sum-of-ap", "nth Term and Sum of Arithmetic Progression", [10],
     "Sequences", ["arithmetic-progressions"],
     "aₙ = a + (n−1)d; Sₙ = n/2[2a + (n−1)d] = n/2[first + last]; word problems"),

    # ══════════════════════════════════════════════════════════
    # GRADE 11
    # ══════════════════════════════════════════════════════════

    ("sets", "Sets", [11],
     "Set Theory", [],
     "Well-defined collections; roster and set-builder notation; types: empty, finite, infinite, equal, universal"),

    ("venn-diagrams", "Venn Diagrams", [11],
     "Set Theory", ["sets"],
     "Pictorial representation of sets; union (A∪B), intersection (A∩B), complement (A'), difference (A−B)"),

    ("relations-and-functions", "Relations and Functions", [11],
     "Algebra", ["sets", "cartesian-coordinate-system"],
     "Cartesian product A×B; relation as subset; function as special relation with unique image for each preimage"),

    ("types-of-functions", "Types of Functions", [11, 12],
     "Algebra", ["relations-and-functions"],
     "One-one (injective), onto (surjective), bijective; composition of functions; invertible functions"),

    ("trigonometric-functions", "Trigonometric Functions", [11],
     "Trigonometry", ["trigonometric-ratios", "angles"],
     "Extension to all real numbers using unit circle; radian measure; graphs, period, amplitude; domain and range"),

    ("trigonometric-addition-formulas", "Trigonometric Addition Formulas", [11],
     "Trigonometry", ["trigonometric-functions"],
     "sin(A±B), cos(A±B), tan(A±B); double angle formulas; half angle formulas; product-to-sum"),

    ("complex-numbers", "Complex Numbers", [11],
     "Algebra", ["quadratic-equations", "real-numbers"],
     "z = a + bi where i = √(−1); Argand plane; modulus |z|, conjugate z̄, argument arg(z); polar form r(cosθ + i sinθ)"),

    ("inequalities", "Inequalities", [11],
     "Algebra", ["simple-equations", "real-numbers"],
     "Linear inequalities in one variable (solution on number line) and two variables (solution as half-plane)"),

    ("fundamental-principle-of-counting", "Fundamental Principle of Counting", [11],
     "Combinatorics", ["sets"],
     "Multiplication principle: m choices for first event × n choices for second = mn total; tree diagrams"),

    ("permutations", "Permutations", [11],
     "Combinatorics", ["fundamental-principle-of-counting"],
     "Arrangements where order matters; ⁿPᵣ = n!/(n−r)!; permutations of non-distinct objects; circular permutations"),

    ("combinations", "Combinations", [11],
     "Combinatorics", ["permutations"],
     "Selections where order does not matter; ⁿCᵣ = n!/(r!(n−r)!); Pascal's triangle; ⁿCᵣ = ⁿCₙ₋ᵣ"),

    ("binomial-theorem", "Binomial Theorem", [11],
     "Algebra", ["combinations", "algebraic-identities"],
     "(a+b)ⁿ = Σ ⁿCᵣ aⁿ⁻ʳ bʳ; binomial coefficients; general term T(r+1); middle term; properties"),

    ("sequences-and-series", "Sequences and Series", [11],
     "Sequences", ["arithmetic-progressions", "geometric-progressions"],
     "General sequences; arithmetic-geometric series; special sums Σr = n(n+1)/2; Σr² = n(n+1)(2n+1)/6"),

    ("straight-lines", "Straight Lines", [11],
     "Coordinate Geometry", ["distance-formula", "relations-and-functions"],
     "Slope; equations (slope-intercept, point-slope, intercept, normal forms); parallel/perpendicular lines; distance from point to line"),

    ("conic-sections", "Conic Sections", [11],
     "Coordinate Geometry", ["circles", "straight-lines"],
     "Curves from cone-plane intersections; standard equations: circle, ellipse x²/a²+y²/b²=1, parabola y²=4ax, hyperbola"),

    ("three-dimensional-geometry", "Three-Dimensional Geometry", [11, 12],
     "Coordinate Geometry", ["cartesian-coordinate-system"],
     "3D coordinate axes; direction cosines (l,m,n) and direction ratios; equations of lines and planes in space"),

    ("limits", "Limits", [11],
     "Calculus", ["real-numbers", "relations-and-functions"],
     "lim(x→a) f(x); limit laws; standard limits: sin x/x → 1, (aⁿ−1)/x → ln a as x→0; left and right limits"),

    ("derivatives", "Derivatives", [11, 12],
     "Calculus", ["limits"],
     "f'(x) = lim(h→0)[f(x+h)−f(x)]/h; geometric meaning as slope of tangent; standard derivatives"),

    ("measures-of-dispersion", "Measures of Dispersion", [11],
     "Statistics", ["mean-median-mode", "mean-of-grouped-data"],
     "Range, mean deviation, variance σ² = Σ(xᵢ−x̄)²/n, standard deviation σ; coefficient of variation"),

    ("axiomatic-probability", "Axiomatic Approach to Probability", [11],
     "Probability", ["sets", "theoretical-probability"],
     "Sample space S, events as subsets; Kolmogorov axioms; addition theorem P(A∪B) = P(A)+P(B)−P(A∩B)"),

    # ══════════════════════════════════════════════════════════
    # GRADE 12
    # ══════════════════════════════════════════════════════════

    ("inverse-trigonometric-functions", "Inverse Trigonometric Functions", [12],
     "Trigonometry", ["trigonometric-functions", "types-of-functions"],
     "sin⁻¹, cos⁻¹, tan⁻¹ and their reciprocals; restricted domains ensuring injectivity; properties and identities"),

    ("matrices", "Matrices", [12],
     "Linear Algebra", ["linear-equations-in-two-variables"],
     "Rectangular arrays of numbers; addition, subtraction, scalar multiplication, matrix multiplication; transpose"),

    ("types-of-matrices", "Types of Matrices", [12],
     "Linear Algebra", ["matrices"],
     "Zero, identity, diagonal, square, row, column, symmetric and skew-symmetric matrices"),

    ("determinants", "Determinants", [12],
     "Linear Algebra", ["matrices"],
     "Scalar det(A) associated with square matrix; cofactor expansion; properties; area of triangle; Cramer's rule"),

    ("inverse-of-a-matrix", "Inverse of a Matrix", [12],
     "Linear Algebra", ["determinants"],
     "A⁻¹ = adj(A)/det(A); exists iff det(A) ≠ 0; solving systems of equations AX = B using A⁻¹"),

    ("continuity-of-functions", "Continuity of Functions", [12],
     "Calculus", ["limits"],
     "f continuous at a iff lim(x→a)f(x) = f(a); algebra of continuous functions; types of discontinuity"),

    ("differentiation-rules", "Differentiation Rules", [12],
     "Calculus", ["derivatives"],
     "Chain rule, product rule, quotient rule; implicit differentiation; parametric differentiation; second derivatives"),

    ("increasing-decreasing-functions", "Increasing and Decreasing Functions", [12],
     "Calculus", ["differentiation-rules"],
     "f increasing on I iff f'(x) > 0 for all x in I; identifying and proving monotonicity intervals"),

    ("maxima-and-minima", "Maxima and Minima", [12],
     "Calculus", ["increasing-decreasing-functions"],
     "Local extrema via first-derivative test; second-derivative test; absolute extrema on closed intervals; word problems"),

    ("integration", "Integration", [12],
     "Calculus", ["derivatives"],
     "Antiderivative F where F'=f; indefinite integral ∫f(x)dx = F(x)+C; standard integrals table"),

    ("methods-of-integration", "Methods of Integration", [12],
     "Calculus", ["integration"],
     "Integration by substitution (u-substitution); integration by partial fractions; integration of rational functions"),

    ("integration-by-parts", "Integration by Parts", [12],
     "Calculus", ["methods-of-integration"],
     "∫u dv = uv − ∫v du; ILATE order of preference; applied to products of functions"),

    ("definite-integrals", "Definite Integrals", [12],
     "Calculus", ["integration"],
     "∫ₐᵇ f(x)dx; fundamental properties; evaluation by substitution; special properties like ∫₀ᵃ f(x)dx = ∫₀ᵃ f(a−x)dx"),

    ("fundamental-theorem-of-calculus", "Fundamental Theorem of Calculus", [12],
     "Calculus", ["definite-integrals", "derivatives"],
     "Part 1: d/dx[∫ₐˣ f(t)dt] = f(x); Part 2: ∫ₐᵇ f(x)dx = F(b)−F(a); links differentiation and integration"),

    ("area-under-curves", "Area Under Curves", [12],
     "Calculus", ["definite-integrals"],
     "Area between curve and x-axis = ∫ₐᵇ |f(x)| dx; area between two curves ∫ₐᵇ |f(x)−g(x)| dx"),

    ("differential-equations", "Differential Equations", [12],
     "Calculus", ["derivatives", "integration"],
     "Equations involving a function and its derivatives; order, degree; variable separable, homogeneous, linear first-order (IF method)"),

    ("vectors", "Vectors", [12],
     "Vectors", ["three-dimensional-geometry", "straight-lines"],
     "Directed quantities with magnitude and direction; position vectors; unit vectors; vector addition; triangle and parallelogram law"),

    ("dot-product-and-cross-product", "Dot Product and Cross Product of Vectors", [12],
     "Vectors", ["vectors"],
     "Dot product a·b = |a||b|cosθ (scalar); cross product a×b magnitude |a||b|sinθ (vector); applications in geometry"),

    ("linear-programming", "Linear Programming", [12],
     "Optimisation", ["linear-equations-in-two-variables", "inequalities"],
     "Maximising/minimising a linear objective function z = ax + by subject to linear constraints; feasible region; corner point theorem"),

    ("conditional-probability", "Conditional Probability", [12],
     "Probability", ["axiomatic-probability"],
     "P(A|B) = P(A∩B)/P(B); multiplication theorem P(A∩B) = P(A)·P(B|A); independent events P(A∩B)=P(A)P(B)"),

    ("bayes-theorem", "Bayes' Theorem", [12],
     "Probability", ["conditional-probability"],
     "P(Aᵢ|B) = P(B|Aᵢ)P(Aᵢ) / Σⱼ P(B|Aⱼ)P(Aⱼ); partition of sample space; prior and posterior probabilities"),

    ("bernoulli-trials", "Bernoulli Trials", [12],
     "Probability", ["axiomatic-probability"],
     "n independent trials, each with probability p of success and q=1−p of failure; satisfies five conditions"),

    ("binomial-distribution", "Binomial Distribution", [12],
     "Probability", ["bernoulli-trials", "binomial-theorem"],
     "P(X=k) = ⁿCₖ pᵏ (1−p)ⁿ⁻ᵏ; mean = np; variance = npq; normal approximation for large n"),

    # ══════════════════════════════════════════════════════════
    # GRADE 6 — NEW ADDITIONS
    # ══════════════════════════════════════════════════════════

    ("natural-numbers", "Natural Numbers", [6],
     "Number Systems", [],
     "Counting numbers 1, 2, 3, …; closed under addition and multiplication; smallest natural number is 1"),

    ("place-value", "Place Value and Indian Number System", [6],
     "Number Systems", ["whole-numbers"],
     "Face value vs place value; ones, tens, hundreds, …; Indian system (lakhs, crores) vs international system"),

    ("integer-operations", "Operations on Integers", [6],
     "Number Systems", ["integers"],
     "Addition, subtraction, multiplication and division of integers; sign rules; number line model"),

    ("composite-numbers", "Composite Numbers", [6],
     "Number Theory", ["prime-numbers"],
     "Natural numbers > 1 that are not prime; have at least one factor other than 1 and themselves"),

    ("number-line", "Number Line", [6],
     "Number Systems", ["integers"],
     "A line with points representing real numbers; integers marked at equal intervals; comparing and ordering numbers"),

    ("figurate-numbers", "Figurate Numbers", [6],
     "Number Theory", ["number-patterns", "whole-numbers"],
     "Numbers that can be represented as geometric shapes: triangular (1,3,6,10,…), square (1,4,9,…), pentagonal"),

    ("units-of-measurement", "Units of Measurement", [6],
     "Mensuration", ["whole-numbers"],
     "Metric system: kilo-, centi-, milli- prefixes; conversions between km/m/cm/mm; kg/g/mg; L/mL"),

    ("geometric-constructions", "Geometric Constructions", [6],
     "Geometry", ["angles", "types-of-angles"],
     "Compass and straightedge constructions: bisecting angles, perpendicular bisectors, constructing equal angles"),

    ("estimation-and-rounding", "Estimation and Rounding", [6],
     "Number Systems", ["place-value"],
     "Rounding to nearest 10, 100, 1000; significant figures; estimating sums, products and quotients"),

    # ══════════════════════════════════════════════════════════
    # GRADE 7 — NEW ADDITIONS
    # ══════════════════════════════════════════════════════════

    ("profit-loss-percentage", "Profit, Loss and Percentage", [7],
     "Proportional Reasoning", ["percentage", "unitary-method-and-direct-proportion"],
     "Profit = SP − CP; loss = CP − SP; profit% and loss% on CP; discount, marked price; real-world problems"),

    ("simple-interest", "Simple Interest", [7],
     "Proportional Reasoning", ["profit-loss-percentage", "percentage"],
     "SI = PRT/100; finding P, R, T when other quantities are known; time in years/months/days"),

    ("recurring-decimals", "Recurring Decimals", [7],
     "Number Systems", ["rational-numbers"],
     "Repeating decimals (0.333…, 0.142857…); converting recurring decimals to p/q form using algebra"),

    ("exterior-angles-of-polygons", "Exterior Angles of Polygons", [7],
     "Geometry", ["properties-of-triangles", "types-of-angles"],
     "Sum of exterior angles of any convex polygon = 360°; each exterior angle of regular n-gon = 360°/n"),

    ("perimeter-of-polygons", "Perimeter of Polygons", [7],
     "Mensuration", ["perimeter", "types-of-triangles"],
     "Perimeter of regular and irregular polygons; composite figures; unknown side lengths from perimeter"),

    ("pie-chart", "Pie Charts", [7],
     "Statistics", ["bar-graphs-and-pictographs", "percentage"],
     "Circular chart divided into sectors; sector angle = (frequency/total) × 360°; reading and drawing pie charts"),

    ("scale-drawing", "Scale Drawing", [7],
     "Geometry", ["ratios-and-proportions", "similar-triangles"],
     "Maps and plans using scale ratios; enlargement and reduction; finding actual lengths from scale drawings"),

    ("isosceles-equilateral-properties", "Properties of Isosceles and Equilateral Triangles", [7],
     "Geometry", ["types-of-triangles", "congruence-of-triangles"],
     "Base angles of isosceles triangle equal; all angles of equilateral = 60°; axis of symmetry"),

    # ══════════════════════════════════════════════════════════
    # GRADE 8 — NEW ADDITIONS
    # ══════════════════════════════════════════════════════════

    ("square-root-methods", "Methods of Finding Square Roots", [8],
     "Number Theory", ["square-and-cube-numbers", "prime-factorisation"],
     "Square root by prime factorisation; long-division method for non-perfect squares; estimating √n"),

    ("surds", "Surds and Irrational Square Roots", [8, 9],
     "Number Systems", ["square-root-methods", "rational-numbers"],
     "√2, √3, √5 are irrational; simplifying surds; like and unlike surds; rationalising denominators using conjugates"),

    ("absolute-value", "Absolute Value", [8],
     "Number Systems", ["integers", "number-line"],
     "|x| = x if x ≥ 0, −x if x < 0; distance interpretation; |a−b| = distance between a and b on number line"),

    ("linear-graphs", "Linear Graphs", [8],
     "Coordinate Geometry", ["simple-equations", "ratios-and-proportions"],
     "Graphing linear equations; distance-time and speed-time graphs; slope as rate of change; y-intercept"),

    ("euler-formula-polyhedra", "Euler's Formula for Polyhedra", [8],
     "Geometry", ["visualising-3d-shapes"],
     "V − E + F = 2 for any convex polyhedron; verified for cube, tetrahedron, octahedron; Euler characteristic"),

    ("percentage-applications", "Percentage Applications", [8],
     "Proportional Reasoning", ["profit-loss-percentage", "percentage"],
     "VAT, discount, commission, depreciation, population growth and bank interest using percentage"),

    ("compound-interest", "Compound Interest", [8],
     "Proportional Reasoning", ["simple-interest", "exponents-and-powers"],
     "A = P(1+R/100)ⁿ; comparing SI and CI; compound interest when compounded half-yearly/quarterly"),

    ("factorisation-expressions", "Factorisation of Algebraic Expressions", [8],
     "Algebra", ["algebraic-identities", "polynomials-in-one-variable"],
     "Common factor method; grouping; using identities (a²−b², a²±2ab+b²); trinomial factorisation"),

    ("division-of-polynomials", "Division of Polynomials", [8],
     "Algebra", ["factorisation-expressions"],
     "Dividing a polynomial by a monomial or binomial; long division; relationship between dividend, divisor, quotient, remainder"),

    ("data-representation-grouped", "Grouped Data and Frequency Tables", [8],
     "Statistics", ["data-collection-and-organisation", "bar-graphs-and-pictographs"],
     "Class intervals, class marks, tally frequency; frequency histograms and polygons; cumulative frequency"),

    ("linear-equations-two-variables", "Linear Equations in Two Variables", [8],
     "Algebra", ["simple-equations", "algebraic-expressions"],
     "ax + by = c; finding solutions as ordered pairs; graphical representation; infinitely many solutions"),

    # ══════════════════════════════════════════════════════════
    # GRADE 9 — NEW ADDITIONS
    # ══════════════════════════════════════════════════════════

    ("decimal-expansions-real", "Decimal Expansions of Real Numbers", [9],
     "Number Systems", ["rational-numbers", "irrational-numbers"],
     "Rational numbers terminate or recur; irrational numbers neither terminate nor recur; representing on number line"),

    ("rationalisation-surds", "Rationalisation of Surds", [9],
     "Number Systems", ["surds", "algebraic-identities"],
     "Rationalising denominators with √a: multiply by √a/√a; conjugate rationalisation: 1/(√a+√b) × (√a−√b)/(√a−√b)"),

    ("euclidean-algorithm", "Euclidean Algorithm", [9],
     "Number Theory", ["lcm-and-gcd", "prime-factorisation"],
     "GCD(a,b) = GCD(b, a mod b); repeated division until remainder 0; efficiency over prime factorisation"),

    ("basic-proportionality-theorem", "Basic Proportionality Theorem", [9],
     "Geometry", ["similar-triangles", "parallel-lines-and-transversals"],
     "A line parallel to one side of a triangle divides the other two sides proportionally (Thales' theorem)"),

    ("triangle-concurrency", "Triangle Concurrency Points", [9],
     "Geometry", ["properties-of-triangles", "mid-point-theorem"],
     "Centroid (medians), orthocentre (altitudes), circumcentre (perp bisectors), incentre (angle bisectors); Euler line"),

    ("similar-triangles-advanced", "Similarity Criteria and Applications", [9, 10],
     "Geometry", ["similar-triangles", "basic-proportionality-theorem"],
     "AA, SAS, SSS similarity; ratio of areas equals square of ratio of corresponding sides; applications"),

    ("lines-angles-theorems", "Lines and Angles — Theorems", [9],
     "Geometry", ["parallel-lines-and-transversals", "euclid-definitions-axioms-postulates"],
     "Vertically opposite angles; linear pair; angles formed by transversal cutting parallel lines; proofs"),

    ("triangle-theorems", "Triangle Theorems", [9],
     "Geometry", ["properties-of-triangles", "congruence-of-triangles"],
     "Angle bisector theorem; perpendicular from vertex to base; medians; relationship between sides and angles"),

    ("probability-basic", "Probability — Basic Concepts", [9],
     "Probability", ["theoretical-probability", "data-collection-and-organisation"],
     "Experiment, outcome, event; sample space; impossible and certain events; complement rule"),

    ("statistics-measures", "Statistical Measures for Ungrouped Data", [9],
     "Statistics", ["mean-median-mode"],
     "Mean, median, mode for ungrouped data; range; choosing appropriate measure of central tendency"),

    ("principle-of-mathematical-induction", "Principle of Mathematical Induction", [9, 11],
     "Number Theory", ["natural-numbers", "algebraic-expressions"],
     "Base case + inductive step; proving divisibility, inequalities and summation formulas; well-ordering principle"),

    ("logarithms", "Logarithms", [9, 11],
     "Algebra", ["exponents-and-powers", "real-numbers"],
     "logₐx = y iff aʸ = x; laws: log(mn)=log m+log n; log(m/n)=log m−log n; log mⁿ=n log m; change of base"),

    ("coordinate-geometry-area", "Area of Triangle via Coordinates", [9],
     "Coordinate Geometry", ["cartesian-coordinate-system", "area-of-triangles"],
     "Area = ½|x₁(y₂−y₃)+x₂(y₃−y₁)+x₃(y₁−y₂)|; collinearity condition when area = 0"),

    # ══════════════════════════════════════════════════════════
    # GRADE 10 — NEW ADDITIONS
    # ══════════════════════════════════════════════════════════

    ("rational-decimal-connection", "Rational Numbers and Decimal Expansions", [10],
     "Number Theory", ["fundamental-theorem-of-arithmetic", "recurring-decimals"],
     "p/q terminates iff q = 2ᵐ×5ⁿ; otherwise decimal recurs; using FTA to predict decimal type"),

    ("completing-the-square", "Completing the Square", [10],
     "Algebra", ["algebraic-identities", "quadratic-equations"],
     "Rewriting ax²+bx+c in form a(x−h)²+k; vertex of parabola; deriving the quadratic formula"),

    ("vieta-formulas", "Vieta's Formulas", [10],
     "Algebra", ["quadratic-equations", "nature-of-roots"],
     "For ax²+bx+c=0: sum of roots = −b/a; product of roots = c/a; forming equations from roots"),

    ("complementary-angle-identities", "Complementary Angle Trigonometric Identities", [10],
     "Trigonometry", ["trigonometric-identities"],
     "sin θ = cos(90°−θ); tan θ = cot(90°−θ); sec θ = cosec(90°−θ); solving problems using these"),

    ("frustum-of-cone", "Frustum of a Cone", [10],
     "Mensuration", ["surface-area-volume-combinations"],
     "Cone with apex removed by plane cut; volume = πh/3(R²+Rr+r²); slant height l = √(h²+(R−r)²)"),

    ("tangent-secant-theorem", "Tangent-Secant and Chord Theorems", [10],
     "Geometry", ["tangent-to-a-circle", "circle-theorems"],
     "PA² = PB·PC (tangent-secant); two chords intersecting inside/outside circle; angle in alternate segment"),

    ("median-mode-grouped", "Median and Mode of Grouped Data", [10],
     "Statistics", ["mean-of-grouped-data", "data-representation-grouped"],
     "Median = l + ((n/2−cf)/f)×h; mode = l + (f₁−f₀)/(2f₁−f₀−f₂)×h; ogive for median estimation"),

    ("arithmetic-progressions-advanced", "Arithmetic Progressions — Advanced Problems", [10],
     "Sequences", ["nth-term-and-sum-of-ap"],
     "Word problems; finding n when sum/term given; APs in real life; sum of first n odd numbers = n²"),

    ("polynomial-long-division", "Polynomial Long Division", [10],
     "Algebra", ["division-of-polynomials", "factorisation-of-polynomials"],
     "Dividing degree-n polynomial by degree-m (m<n); quotient and remainder; verifying factor theorem"),

    # ══════════════════════════════════════════════════════════
    # GRADE 11 — NEW ADDITIONS
    # ══════════════════════════════════════════════════════════

    ("set-operations", "Set Operations", [11],
     "Set Theory", ["sets", "venn-diagrams"],
     "Union, intersection, difference, complement; De Morgan's laws (A∪B)'=A'∩B'; number of elements formula"),

    ("subsets-and-power-sets", "Subsets and Power Sets", [11],
     "Set Theory", ["sets"],
     "A⊆B iff every element of A is in B; power set P(A) has 2ⁿ subsets; proper subsets; null set subset of every set"),

    ("cartesian-product-sets", "Cartesian Product of Sets", [11],
     "Set Theory", ["sets"],
     "A×B = {(a,b) : a∈A, b∈B}; |A×B| = |A|·|B|; A×B ≠ B×A in general; basis for defining relations"),

    ("relations", "Relations", [11],
     "Algebra", ["cartesian-product-sets"],
     "Subset of A×B; domain and range; types: reflexive, symmetric, transitive, equivalence relations"),

    ("functions", "Functions", [11],
     "Algebra", ["relations"],
     "f: A→B mapping each element of A to exactly one element of B; domain, codomain, range; vertical line test"),

    ("types-of-relations", "Types of Relations", [11],
     "Algebra", ["relations"],
     "Empty, universal, identity relations; reflexive, symmetric, transitive; equivalence classes and partitions"),

    ("special-functions", "Special Functions", [11],
     "Algebra", ["functions"],
     "Constant, identity, modulus |x|, signum, greatest integer [x] (floor), fractional part functions; their graphs"),

    ("even-odd-functions", "Even and Odd Functions", [11],
     "Algebra", ["functions"],
     "Even: f(−x)=f(x), symmetric about y-axis; Odd: f(−x)=−f(x), symmetric about origin; neither; decomposition"),

    ("radian-measure", "Radian Measure", [11],
     "Trigonometry", ["trigonometric-ratios", "circles"],
     "1 radian = angle subtending arc length equal to radius; 360° = 2π rad; conversion formula; arc length s=rθ"),

    ("unit-circle", "Unit Circle", [11],
     "Trigonometry", ["radian-measure", "cartesian-coordinate-system"],
     "Circle of radius 1 centred at origin; coordinates (cosθ, sinθ); all six trig functions defined geometrically"),

    ("trigonometric-equations", "Trigonometric Equations", [11],
     "Trigonometry", ["trigonometric-addition-formulas", "unit-circle"],
     "General solutions: sin x = k → x = nπ+(−1)ⁿα; cos x = k → x = 2nπ±α; tan x = k → x = nπ+α"),

    ("argand-plane", "Argand Plane", [11],
     "Algebra", ["complex-numbers", "cartesian-coordinate-system"],
     "z=a+bi plotted as point (a,b); modulus as distance from origin; conjugate as reflection in real axis"),

    ("polar-form-complex", "Polar Form of Complex Numbers", [11],
     "Algebra", ["argand-plane"],
     "z = r(cosθ+i sinθ) = reⁱᶿ; De Moivre's theorem: zⁿ = rⁿ(cos nθ + i sin nθ); nth roots of unity"),

    ("quadratic-inequalities", "Quadratic Inequalities", [11],
     "Algebra", ["quadratic-equations", "inequalities"],
     "ax²+bx+c > 0 or < 0; sign chart method; parabola above/below x-axis; solution as union of intervals"),

    ("factorial", "Factorial Notation", [11],
     "Combinatorics", ["natural-numbers"],
     "n! = n×(n−1)×…×1; 0!=1; n! grows super-exponentially; Stirling's approximation; appears in permutations/combinations"),

    ("circular-permutations", "Circular Permutations", [11],
     "Combinatorics", ["permutations"],
     "Arrangements in a circle: (n−1)!; necklace/bracelet problems: (n−1)!/2; distinguishing clockwise/anticlockwise"),

    ("pascal-triangle", "Pascal's Triangle", [11],
     "Combinatorics", ["combinations", "binomial-theorem"],
     "Triangular array of binomial coefficients ⁿCᵣ; row sums = 2ⁿ; diagonals give figurate numbers and Fibonacci"),

    ("harmonic-progression", "Harmonic Progression", [11],
     "Sequences", ["sequences-and-series", "geometric-progressions"],
     "Sequence whose reciprocals form AP: 1/a, 1/(a+d), …; harmonic mean H = 2ab/(a+b); AM ≥ GM ≥ HM"),

    ("am-gm-inequality", "AM–GM Inequality", [11],
     "Algebra", ["sequences-and-series"],
     "(a₁+…+aₙ)/n ≥ (a₁…aₙ)^(1/n); equality when all terms equal; applications to optimisation and proving inequalities"),

    ("parabola", "Parabola", [11],
     "Coordinate Geometry", ["conic-sections"],
     "y² = 4ax: focus (a,0), directrix x=−a, vertex (0,0), latus rectum 4a; reflective property; real-world applications"),

    ("ellipse", "Ellipse", [11],
     "Coordinate Geometry", ["conic-sections"],
     "x²/a²+y²/b²=1 (a>b); foci (±c,0) with c²=a²−b²; eccentricity e=c/a < 1; latus rectum 2b²/a"),

    ("hyperbola", "Hyperbola", [11],
     "Coordinate Geometry", ["conic-sections"],
     "x²/a²−y²/b²=1; foci (±c,0) with c²=a²+b²; asymptotes y=±(b/a)x; eccentricity e > 1; rectangular hyperbola"),

    ("sandwich-theorem", "Sandwich Theorem (Squeeze Theorem)", [11],
     "Calculus", ["limits"],
     "If g(x)≤f(x)≤h(x) and lim g=lim h=L then lim f=L; proves lim(sin x/x)=1 and lim((1−cos x)/x)=0 as x→0"),

    ("angle-between-two-lines", "Angle Between Two Lines", [11],
     "Coordinate Geometry", ["straight-lines"],
     "tan φ = |(m₁−m₂)/(1+m₁m₂)|; parallel if m₁=m₂; perpendicular if m₁m₂=−1; inclination and slope"),

    ("sample-space-events", "Sample Space and Events", [11],
     "Probability", ["sets", "probability-basic"],
     "Sample space S = set of all outcomes; events as subsets; mutually exclusive; exhaustive; complementary events"),

    ("addition-theorem-probability", "Addition Theorem of Probability", [11],
     "Probability", ["axiomatic-probability", "set-operations"],
     "P(A∪B)=P(A)+P(B)−P(A∩B); mutually exclusive: P(A∪B)=P(A)+P(B); extension to three events"),

    ("standard-deviation-grouped", "Standard Deviation for Grouped Data", [11],
     "Statistics", ["measures-of-dispersion", "data-representation-grouped"],
     "σ = √(Σfᵢ(xᵢ−x̄)²/N); step-deviation shortcut; variance and SD for frequency distributions; CV = σ/x̄ × 100"),

    ("interval-notation", "Interval Notation", [11],
     "Algebra", ["real-numbers", "inequalities"],
     "Open (a,b), closed [a,b], half-open intervals; union and intersection; infinite intervals (a,∞); number line representation"),

    ("locus-of-a-point", "Locus of a Point", [11],
     "Coordinate Geometry", ["cartesian-coordinate-system", "straight-lines"],
     "Set of all points satisfying a geometric condition; deriving equations of circles, lines; locus problems"),

    # ══════════════════════════════════════════════════════════
    # GRADE 12 — NEW ADDITIONS
    # ══════════════════════════════════════════════════════════

    ("composition-of-functions", "Composition of Functions", [12],
     "Algebra", ["types-of-functions"],
     "(f∘g)(x)=f(g(x)); domain restrictions; associativity (f∘g)∘h=f∘(g∘h); (f∘g)⁻¹=g⁻¹∘f⁻¹"),

    ("invertible-functions", "Invertible Functions", [12],
     "Algebra", ["composition-of-functions"],
     "f is invertible iff it is bijective; f⁻¹∘f=I; graph of f⁻¹ is reflection of f across y=x; finding f⁻¹ explicitly"),

    ("inverse-trig-properties", "Properties of Inverse Trigonometric Functions", [12],
     "Trigonometry", ["inverse-trigonometric-functions", "trigonometric-addition-formulas"],
     "sin⁻¹x+cos⁻¹x=π/2; tan⁻¹x+cot⁻¹x=π/2; addition formulas for tan⁻¹; simplification identities"),

    ("matrix-types", "Types and Operations on Matrices", [12],
     "Linear Algebra", ["types-of-matrices"],
     "Equality; addition and subtraction; scalar multiplication; properties; symmetric A=Aᵀ, skew A=−Aᵀ; decomposition"),

    ("matrix-multiplication", "Matrix Multiplication", [12],
     "Linear Algebra", ["matrix-types"],
     "(AB)ᵢⱼ = Σₖ AᵢₖBₖⱼ; non-commutative; associative; AB=0 does not imply A=0; (AB)ᵀ=BᵀAᵀ"),

    ("cofactor-expansion", "Cofactor Expansion of Determinants", [12],
     "Linear Algebra", ["determinants"],
     "Minor Mᵢⱼ; cofactor Cᵢⱼ=(−1)^(i+j)Mᵢⱼ; expansion along any row/column; adjoint adj(A) = (Cᵢⱼ)ᵀ"),

    ("cramers-rule", "Cramer's Rule", [12],
     "Linear Algebra", ["cofactor-expansion", "inverse-of-a-matrix"],
     "x = Dₓ/D, y = Dᵧ/D, z = D_z/D; unique solution iff D≠0; inconsistent/dependent cases; consistency conditions"),

    ("implicit-differentiation", "Implicit Differentiation", [12],
     "Calculus", ["differentiation-rules"],
     "Differentiating F(x,y)=0 treating y as function of x; applying chain rule; finding dy/dx for implicit curves"),

    ("parametric-differentiation", "Parametric Differentiation", [12],
     "Calculus", ["implicit-differentiation"],
     "x=f(t), y=g(t); dy/dx=(dy/dt)/(dx/dt); d²y/dx²=d/dx(dy/dx); applications to parametric curves"),

    ("second-order-derivative", "Second Order Derivatives", [12],
     "Calculus", ["parametric-differentiation"],
     "f''(x) = d²y/dx²; concavity: f''>0 concave up, f''<0 concave down; inflection points where f'' changes sign"),

    ("rolles-mean-value-theorem", "Rolle's and Mean Value Theorems", [12],
     "Calculus", ["continuity-of-functions", "differentiation-rules"],
     "Rolle's: f(a)=f(b) implies f'(c)=0 for some c∈(a,b); MVT: f'(c)=(f(b)−f(a))/(b−a); geometric interpretation"),

    ("tangent-normal-curve", "Tangents and Normals to Curves", [12],
     "Calculus", ["differentiation-rules", "straight-lines"],
     "Tangent slope = f'(x₀); normal slope = −1/f'(x₀); equations using point-slope form; angle between curves"),

    ("rate-of-change", "Rate of Change and Related Rates", [12],
     "Calculus", ["tangent-normal-curve"],
     "Instantaneous rate = derivative; related rates linking dV/dt, dr/dt etc.; expanding sphere, sliding ladder problems"),

    ("approximation-differentials", "Approximation Using Differentials", [12],
     "Calculus", ["rate-of-change"],
     "dy = f'(x)dx; approximate f(x+Δx) ≈ f(x)+f'(x)Δx; absolute/relative/percentage error; linear approximation"),

    ("integration-standard-forms", "Standard Integration Formulas", [12],
     "Calculus", ["integration"],
     "∫xⁿ, ∫eˣ, ∫1/x, ∫sin x, ∫cos x, ∫sec²x; inverse trig forms ∫1/√(1−x²), ∫1/(1+x²); standard results"),

    ("integration-by-substitution", "Integration by Substitution", [12],
     "Calculus", ["integration-standard-forms"],
     "Let u=g(x); ∫f(g(x))g'(x)dx = ∫f(u)du; adjusting limits for definite integrals; standard substitutions"),

    ("integration-partial-fractions", "Integration by Partial Fractions", [12],
     "Calculus", ["integration-by-substitution", "polynomial-long-division"],
     "Decomposing P(x)/Q(x) for distinct linear, repeated, irreducible quadratic factors; cover-up method"),

    ("definite-integral-properties", "Properties of Definite Integrals", [12],
     "Calculus", ["definite-integrals", "integration-by-substitution"],
     "∫ₐᵃ=0; reversing limits negates; splitting at c; ∫₀ᵃf(x)=∫₀ᵃf(a−x); even/odd function integrals"),

    ("area-between-curves", "Area Between Curves", [12],
     "Calculus", ["area-under-curves", "definite-integral-properties"],
     "∫ₐᵇ|f(x)−g(x)|dx; finding intersection points; area enclosed by parametric curves; area in polar form"),

    ("order-degree-de", "Order and Degree of Differential Equations", [12],
     "Calculus", ["differential-equations"],
     "Order = highest derivative; degree = power of highest derivative when polynomial; formation of DEs"),

    ("variable-separable-de", "Variable Separable Differential Equations", [12],
     "Calculus", ["order-degree-de"],
     "dy/dx = f(x)g(y) → ∫dy/g(y) = ∫f(x)dx; general solution with arbitrary constant; particular solution"),

    ("homogeneous-de", "Homogeneous Differential Equations", [12],
     "Calculus", ["variable-separable-de"],
     "dy/dx = F(y/x); substitution y=vx transforms to variable separable form; identifying homogeneous functions"),

    ("linear-first-order-de", "Linear First-Order Differential Equations", [12],
     "Calculus", ["homogeneous-de"],
     "dy/dx + P(x)y = Q(x); integrating factor IF = e^(∫P dx); solution y·IF = ∫Q·IF dx + C"),

    ("position-vector", "Position Vectors and Vector Algebra", [12],
     "Vectors", ["vectors"],
     "Position vector of point P is OP; section formula in vectors; collinear vectors; linear combination; basis vectors"),

    ("vector-triple-product", "Scalar Triple Product", [12],
     "Vectors", ["dot-product-and-cross-product"],
     "[a,b,c] = a·(b×c); volume of parallelepiped; coplanarity condition [a,b,c]=0; cyclic property"),

    ("line-in-3d-space", "Lines in Three-Dimensional Space", [12],
     "Coordinate Geometry", ["three-dimensional-geometry", "vectors"],
     "Vector form r=a+λb; Cartesian form (x−x₁)/l=(y−y₁)/m=(z−z₁)/n; angle between lines; skew lines; shortest distance"),

    ("plane-in-3d-space", "Planes in Three-Dimensional Space", [12],
     "Coordinate Geometry", ["line-in-3d-space"],
     "Equation r·n̂=d; Cartesian ax+by+cz=d; angle between planes; plane through three points; families of planes"),

    ("distance-point-to-plane", "Distance from Point to Plane", [12],
     "Coordinate Geometry", ["plane-in-3d-space"],
     "d = |ax₁+by₁+cz₁+d|/√(a²+b²+c²); distance between parallel planes; foot of perpendicular; angle bisector planes"),

    ("mean-variance-distribution", "Mean and Variance of Random Variables", [12],
     "Probability", ["bayes-theorem", "bernoulli-trials"],
     "E(X)=Σxᵢpᵢ; Var(X)=E(X²)−[E(X)]²; mean and variance of binomial distribution: μ=np, σ²=npq"),

    ("graph-transformations", "Graph Transformations", [12],
     "Algebra", ["special-functions", "even-odd-functions"],
     "Translations f(x±a), f(x)±a; reflections f(−x), −f(x); stretches f(kx), kf(x); combined transformations"),
]


# ─── BUILD THE GRAPH ──────────────────────────────────────────────────────────

def build_graph():
    # Index by slug
    concept_index = {slug: (name, grades, area, prereqs, desc)
                     for slug, name, grades, area, prereqs, desc in CONCEPTS}

    # Validate all prerequisite slugs exist
    all_slugs = set(concept_index.keys())
    errors = []
    for slug, name, grades, area, prereqs, desc in CONCEPTS:
        for p in prereqs:
            if p not in all_slugs:
                errors.append(f"  MISSING PREREQ: '{p}' referenced by '{slug}'")
    if errors:
        print("VALIDATION ERRORS:")
        for e in errors:
            print(e)
        raise SystemExit(1)

    # Compute leads_to (reverse of prerequisites)
    leads_to = defaultdict(list)
    for slug, name, grades, area, prereqs, desc in CONCEPTS:
        for p in prereqs:
            leads_to[p].append(slug)

    # Build edges list
    edges = []
    for slug, name, grades, area, prereqs, desc in CONCEPTS:
        for p in prereqs:
            edges.append({"from": p, "to": slug, "type": "prerequisite"})

    # Build concepts dict
    concepts_out = {}
    for slug, name, grades, area, prereqs, desc in CONCEPTS:
        concepts_out[slug] = {
            "canonical_name": name,
            "slug": slug,
            "grades": sorted(grades),
            "area": area,
            "subject": "maths",
            "description": desc,
            "prerequisites": prereqs,
            "leads_to": sorted(leads_to.get(slug, [])),
            "related": [],
        }

    # Build grade_views
    grade_views = {}
    all_grades = sorted({g for _, _, grades, _, _, _ in CONCEPTS for g in grades})
    for g in all_grades:
        grade_concepts = [s for s, _, grades, _, _, _ in CONCEPTS if g in grades]
        # Entry points = concepts in this grade with no prerequisites from any earlier grade
        entry_points = []
        for s in grade_concepts:
            prereqs = concepts_out[s]["prerequisites"]
            # Check if all prereqs are from same or later grade (i.e., no earlier-grade dependency)
            has_prior_grade_prereq = any(
                any(gp < g for gp in concepts_out[p]["grades"])
                for p in prereqs
                if p in concepts_out
            )
            if not prereqs or not has_prior_grade_prereq:
                entry_points.append(s)
        grade_views[str(g)] = {
            "count": len(grade_concepts),
            "concepts": grade_concepts,
            "entry_points": entry_points,
        }

    graph = {
        "subject": "maths",
        "version": "v2-manual",
        "description": "Manually curated knowledge graph covering NCERT Grades 6-12 maths curriculum, built from 417 raw topics",
        "total_concepts": len(concepts_out),
        "total_edges": len(edges),
        "concepts": concepts_out,
        "edges": edges,
        "grade_views": grade_views,
    }

    return graph


if __name__ == "__main__":
    graph = build_graph()
    out_path = Path(__file__).parent.parent / "data" / "output" / "knowledge_graph" / "maths_v2.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)

    g = graph
    print(f"✓ Written to {out_path}")
    print(f"  Concepts : {g['total_concepts']}")
    print(f"  Edges    : {g['total_edges']}")
    print()
    print("  Grade breakdown:")
    for grade, view in g["grade_views"].items():
        print(f"    Grade {grade}: {view['count']} concepts, {len(view['entry_points'])} entry points")
    print()
    print("  Sample edges:")
    for e in g["edges"][:8]:
        src = g["concepts"][e["from"]]["canonical_name"]
        tgt = g["concepts"][e["to"]]["canonical_name"]
        print(f"    {src}  →  {tgt}")
