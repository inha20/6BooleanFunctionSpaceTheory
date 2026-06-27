# Q3 — Constructibility Framework

**버전:** 1.0  
**작성일:** 2026-06-22  
**위치:** `6BooleanFunctionSpaceTheory/exploration/Q3_constructibility_framework.md`  
**원출처:** `TODO.md §2, Q3`

---

## 1. 질문 진술

> **Q3:** 주어진 목표 함수(target function) f가 어떤 단일 게이트 G로 구성 가능한지 여부를 결정하는  
> **구성 가능성 프레임워크(Constructibility Framework)**를 정립하라.

이는 대수학적으로 다음과 동치이다:
> f ∈ Space(G) (= Post 클론 [G]) 인지 판별하라.

---

## 2. 핵심 개념: 구성 가능성(Constructibility)

### 2.1 정의

**Definition (Constructibility):**  
함수 f : {0,1}ⁿ → {0,1}가 게이트 G에 대해 **구성 가능(constructible)**하다  
⟺ 유한 깊이의 게이트 회로(G만으로 구성, 변수와 상수 {0,1} 사용 가능)가 존재하여 f를 구현한다.  
⟺ f ∈ Space(G) = [G] (G가 생성하는 Post 클론)

### 2.2 직관적 의미

구성 가능성 문제는 다음 세 가지 관점으로 볼 수 있다:

| 관점 | 해석 |
|-----|-----|
| **회로 관점** | G 게이트만으로 f를 구현하는 회로가 존재하는가? |
| **대수 관점** | f가 G가 생성하는 클론에 속하는가? (f ∈ [G]?) |
| **K-map 관점** | f의 K-map 패턴이 Space(G)의 시각적 시그니처를 가지는가? |

---

## 3. 판별 조건 (Constructibility Criteria)

### 3.1 Post 정리 기반 판별

f가 Space(G)에 속하지 **않기** 위한 조건:  
f가 G가 보존하는 Post 클래스 중 적어도 하나를 **위반**해야 한다.

| 게이트 G | G가 보존하는 클래스 | f ∈ Space(G) 판별 조건 |
|---------|-----------------|---------------------|
| NAND | 없음 | 항상 f ∈ Space(NAND) |
| NOR | 없음 | 항상 f ∈ Space(NOR) |
| XOR | T₀(0 보존), S(자기쌍대), L(선형) | f가 아핀 함수인지 확인 |
| AND | T₀, T₁, M(단조) | f가 AND-생성 단조 함수인지 확인 |
| OR | T₀, T₁, M(단조) | f가 OR-생성 단조 함수인지 확인 |

### 3.2 구체적 판별 알고리즘 (4변수 기준)

**Case 1: f ∈ Space(XOR) 판별**
1. f의 대수 정규형(ANF)을 계산
2. ANF에 2차 이상 항(xy, xyz 등)이 있으면 → f ∉ Space(XOR)
3. 없으면 → f ∈ Space(XOR) ✓

**Case 2: f ∈ Space(AND) 판별**
1. f가 단조(monotone)인지 확인: 모든 x ≤ y에 대해 f(x) ≤ f(y)?
2. 단조가 아니면 → f ∉ Space(AND)
3. 단조이면, f가 AND-다항식(적화 정규형, POS)으로 표현 가능한지 확인

**Case 3: f ∈ Space(NAND) = Ω** — 항상 참 (모든 함수 구성 가능)

---

## 4. 예시 분석

### 4.1 f = A⊕B (XOR 함수)

- ANF: A⊕B (1차항만) → f ∈ Space(XOR) ✓
- AND로 구성 가능? → f는 단조가 아님 (A=0,B=1→1, A=1,B=0→1, A=1,B=1→0) → f ∉ Space(AND) ✗
- NAND로 구성 가능? → 항상 가능 ✓

### 4.2 f = AB (AND 함수)

- ANF: AB (2차항 존재) → f ∉ Space(XOR) ✗
- AND로 구성 가능? → f 자체가 AND → f ∈ Space(AND) ✓
- NAND로 구성 가능? → NOT(A NAND B) → 가능 ✓

### 4.3 f = A (단일 변수)

- ANF: A (1차항) → f ∈ Space(XOR) ✓ (0 XOR A = A)
- AND로 구성 가능? → 단조, AND로 생성 가능 → f ∈ Space(AND) ✓
- NAND: 항상 가능 ✓

### 4.4 f = Majority(A,B,C,D) [입력 중 2개 이상 1일 때 1]

- ANF: AB⊕AC⊕AD⊕BC⊕BD⊕CD⊕... (2차항 이상 존재) → f ∉ Space(XOR) ✗
- 단조? → 예 (1→1 변환에 단조) → Space(AND) 후보
- 실제로는 단조 함수이고 AND/OR로 구현 가능 → f ∈ Space(AND) ✓

---

## 5. Representation Transformation Cost (FQ-11)

> **FQ-11:** 구성 가능성을 "표현 변환 비용(Representation Transformation Cost)"으로 해석할 수 있는가?  
> Paper 2(Repo 2)와의 연결점은?

해석:
- f ∈ Space(G)이면 → G-회로로 표현할 수 있음 = 변환 비용 유한
- f ∉ Space(G)이면 → G만으로는 표현 불가 = 변환 비용 무한(∞)
- 이는 SRT의 **표현 변환(H2)**와 연결됨: 어떤 표현이 가능한지가 구조 인식에 영향

---

## 6. 열린 질문

- **Q3 핵심:** 임의의 G에 대해 f ∈ Space(G) 판별을 다항 시간에 할 수 있는가?
- **FQ-12:** Space(G)에 속하지 않는 함수들의 집합 Ω \ Space(G)의 수학적 구조는?
- **FQ-5:** Space(G)의 최소 생성 집합(minimal generating set) 크기와 Space(G) 속성의 관계는?

---

*이 문서는 탐구 과정에서 계속 업데이트될 예정입니다.*
