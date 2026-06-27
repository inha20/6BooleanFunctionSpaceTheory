# FQ Group A — Function Space Structure (FQ-1 ~ FQ-5)

**버전:** 1.0  
**작성일:** 2026-06-22  
**위치:** `6BooleanFunctionSpaceTheory/fq/FQ_A_function_space_structure.md`  
**원출처:** `TODO.md §4-A`

---

## FQ-1. Size of Space(G) for n=2,3,4,5 — Growth Rate Patterns?

### 질문
n=2, 3, 4, 5변수에 대해 각 게이트 G의 Space(G) 크기는 어떻게 변하는가?

### 분석

**전체 함수 공간 크기:** $|\mathcal{F}_n| = 2^{2^n}$

| n | 전체 공간 $2^{2^n}$ | 아핀 $2^{n+1}$ | 아핀 비율 |
|---|-------------------|--------------|---------|
| 2 | 16 | 8 | 50.0% |
| 3 | 256 | 16 | 6.25% |
| 4 | 65,536 | 32 | 0.049% |
| 5 | 4,294,967,296 | 64 | 0.0000015% |

**단조 함수 크기 (Dedekind 수 D(n)):**

| n | D(n) | 비율 |
|---|------|-----|
| 2 | 6 | 37.5% |
| 3 | 20 | 7.8% |
| 4 | 168 | 0.26% |
| 5 | 7,581 | 0.000177% |
| 6 | 7,828,354 | — |

> D(8) = 56,130,437,228,687,557,907,788 (2023년에야 계산 완료 — Dedekind 수 문제의 어려움을 보여줌)

**핵심 관찰:**
- 아핀 공간(Space(XOR)): 선형 증가 $2^{n+1}$ → 전체 대비 비율 **이중 지수적 감소**
- 단조 공간(Space(AND/OR)): Dedekind 수 증가 → 비율 역시 급격히 감소
- **결론:** n이 커질수록 "특수한 구조를 가진 함수"는 전체 중 극히 일부 → 구조 인식의 희소성

---

## FQ-2. Post Lattice Mapping of Space(G) — Which Level in the Hierarchy?

### 질문
각 게이트 G에 대해 Space(G)는 Post 격자의 정확히 어느 클론에 대응하는가?

### 분석

**확립된 대응:**

| 게이트 G (+ 변수, 상수) | Space(G) = Post 클론 | 격자 위치 |
|----------------------|-------------------|---------|
| NAND | Ω (전체 클론) | 최상위 |
| NOR | Ω (전체 클론) | 최상위 |
| XOR (+ 0) | L (선형 클론) | 중간 (아핀 = ANF 차수 ≤ 1) |
| XOR (+ 0, 1) | L + {0,1} → L∩T₀ | T₀ 추가 제약 |
| AND (+ vars, 0, 1) | M ∩ T₀ ∩ T₁ | 단조 + 양끝 보존 |
| OR (+ vars, 0, 1) | M ∩ T₀ ∩ T₁ | AND와 쌍대 관계 |
| NOT (+ id, 0 또는 1) | S ∩ ? | 자기쌍대 클론 |

**미해결 부분:**
- NOT과 상수의 조합이 정확히 어느 Post 클론을 생성하는가?
- AND와 OR는 같은 클론을 생성하는가? (쌍대이므로 격자에서 대칭적 위치)

**격자 다이어그램 (Space(G) 매핑):**
```
Ω [NAND, NOR]
├── M∩T₀∩T₁ [AND, OR + vars + 0,1]
│     └── {상수}
├── L [XOR + 0]
│     └── L∩T₀ [XOR + 0,1]
└── S∩? [NOT + id]
```

---

## FQ-3. Intersection Space(G₁) ∩ Space(G₂) — Mathematical Structure?

### 질문
두 게이트 G₁, G₂가 있을 때, Space(G₁) ∩ Space(G₂)의 수학적 구조는 무엇인가?

### 분석

**클론 이론에서의 답:**
Space(G₁) ∩ Space(G₂) = [G₁] ∩ [G₂]

Post 격자는 교집합에 대해 닫혀 있다: 두 클론의 교집합은 클론이다.

**구체적 사례:**

| 교집합 | 결과 | 설명 |
|-------|-----|-----|
| Space(NAND) ∩ Space(XOR) | Space(XOR) = L | NAND = Ω이므로 교집합 = 작은 쪽 |
| Space(AND) ∩ Space(XOR) | L ∩ M∩T₀∩T₁ | 선형이면서 단조인 함수 |
| Space(AND) ∩ Space(OR) | 동일 (같은 클론) | AND와 OR가 같은 클론 생성 여부 확인 필요 |

**선형이면서 단조인 함수 (L ∩ M):**
- 아핀: f = a₀ ⊕ a₁A ⊕ ... ⊕ aₙD
- 단조: 계수에 음의 기여가 없어야 함
- 실제로 4변수에서: 상수 0, 상수 1, 단일 변수 A, B, C, D (6개)
  - 왜냐하면 A⊕B는 단조가 아님 (A=1,B=0→1, A=1,B=1→0 위반)

> L ∩ M = { 상수, 단일 변수 투영 } — 극히 단순한 함수들만

**K-map 시각화:** 교집합이 좁아질수록 K-map 패턴이 더 단순해짐

---

## FQ-4. Closure Properties of Space(G) — Systematic Classification

### 질문
Space(G)의 폐포(closure) 속성을 체계적으로 분류하라.

### 분석

**클론의 정의에 의한 기본 폐포:**
모든 Space(G)는 다음에 대해 닫혀 있다:
1. **합성 (Composition):** f, g ∈ Space(G) → G(f,g) ∈ Space(G)
2. **변수 동일화 (Identification):** f(x,y,...) ∈ Space(G) → f(x,x,...) ∈ Space(G)
3. **상수 대입 (Substitution):** f ∈ Space(G) → f(c,...) for c∈{0,1} ∈ Space(G)
4. **변수 치환 (Permutation):** f ∈ Space(G), σ∈Sₙ → f∘σ ∈ Space(G)

**추가 폐포 속성 (Post 클래스별):**

| Space(G) | 보수 닫힘? | 쌍대 닫힘? | 합성 닫힘 깊이 |
|---------|---------|---------|------------|
| Space(NAND) = Ω | ✅ | ✅ | 무한 |
| Space(XOR) = L | ✅ (⊕1로) | ✅ | 유한 (n+1 단계) |
| Space(AND) = M∩T₀∩T₁ | ❌ (NOT은 단조 아님) | 쌍대=Space(OR) | 유한 |
| Space(OR) | ❌ | 쌍대=Space(AND) | 유한 |

**비교 관점:**
- Space(NAND)만이 보수 연산에 닫혀 있는 유일한 "완전" 공간
- Space(XOR)는 ⊕1(XOR와 상수 1의 합성)으로 보수를 만들 수 있어 닫혀 있음
- Space(AND): NOT(A∧B) ∉ Space(AND) (단조 함수가 아님) → 보수 생성 불가

---

## FQ-5. Minimal Generating Set Size vs. Space(G) Properties

### 질문
Space(G)의 최소 생성 집합(minimal generating set) 크기와 Space(G)의 속성 사이에 어떤 관계가 있는가?

### 분석

**최소 생성 집합의 정의:**
Space(G)를 클론으로서 생성하는 최소 크기의 함수 집합 B:
$[B] = Space(G)$ 이고, 어떤 B' ⊊ B에 대해서도 $[B'] \neq Space(G)$

**알려진 결과:**

| Space(G) | 최소 생성 집합 예 | 크기 |
|---------|--------------|-----|
| Ω = Space(NAND) | {NAND} | 1 |
| Ω = Space(NOR) | {NOR} | 1 |
| L = Space(XOR) | {XOR} 또는 {XOR, NOT} | 1~2 |
| M∩T₀∩T₁ = Space(AND) | {AND} | 1 |

**관찰:**
- NAND, NOR, XOR, AND, OR는 모두 **단일 게이트가 자신의 Space(G)를 생성**
- 이는 Space(G)를 "G 하나의 클론"으로 정의한 것과 일치

**열린 질문:**
- 어떤 Space(G)는 단일 게이트로 생성되지 않을 수 있는가?
- Space(G₁) ∩ Space(G₂)의 최소 생성 집합은 {G₁, G₂}인가, 더 작을 수 있는가?
  - L ∩ M의 최소 생성 집합 = ? (단일 변수 투영 A 하나로 생성 가능?)

---

## 소결 (FQ-1~5 통합 관찰)

FQ-1~5를 통해 얻은 핵심 통찰:

1. **희소성의 법칙:** 특수 구조를 가진 함수(아핀, 단조 등)의 비율은 n 증가에 따라 이중 지수적으로 감소 → "구조 있는 함수"가 얼마나 드문지를 정량화
2. **격자 구조의 명확성:** Post 격자에서 각 Space(G)의 위치가 G의 성질(T₀, T₁, M, L, S 위반 여부)로 완전히 결정됨
3. **교집합의 단순화:** 두 Space(G)의 교집합은 항상 더 제약이 많은(더 작은) 공간 → 클론들의 격자 구조가 K-map 제약의 누적과 정확히 대응
4. **생성의 경제성:** 단 하나의 게이트가 자신의 전체 클론을 생성 → Space(G)는 G 하나에 내재된 모든 구조적 정보를 담고 있음

---

*이 문서는 탐구 과정에서 계속 업데이트될 예정입니다.*
