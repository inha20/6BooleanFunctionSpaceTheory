# Q4 — Function Space Structure (Core Question)

**버전:** 1.0  
**작성일:** 2026-06-22  
**위치:** `6BooleanFunctionSpaceTheory/exploration/Q4_function_space_structure.md`  
**원출처:** `TODO.md §2, Q4`

---

## 1. 질문 진술

> **Q4 (핵심 질문):** 임의의 단일 게이트 G에 대해, 다음을 정의하고 특성화하라:
> 1. 생성 함수 공간 Space(G)
> 2. 폐포 속성 (Closure Properties)
> 3. 카르노 맵 시각적 특성
> 4. 구조적 불변성 (Structural Invariants)

**Q1, Q2, Q3는 모두 Q4의 특수 사례이다.**

---

## 2. Space(G)의 완전한 정의

### 2.1 형식적 정의

**Definition (Space(G) — Full):**

게이트 G : {0,1}² → {0,1}에 대해, Space(G)는 다음 귀납적 정의의 최소 고정점이다:

**기저(Base):**
- 모든 변수 xᵢ ∈ Space(G)
- 상수 0, 1 ∈ Space(G)

**귀납(Inductive step):**
- f, g ∈ Space(G) → G(f, g) ∈ Space(G)
- f ∈ Space(G), i ≠ j → f(x₁,...,xⱼ←xᵢ,...,xₙ) ∈ Space(G) (변수 동일화)
- f(x₁,...,c,...,xₙ) ∈ Space(G) for c ∈ {0,1} (상수 대입)

### 2.2 클론(Clone)과의 동치

Space(G) = [G] (G를 포함하는 가장 작은 클론)  
→ Post의 격자에서 G가 속하는 최소 클론이 Space(G)이다.

---

## 3. 폐포 속성 체계적 분류 (FQ-4)

### 3.1 합성 폐포 (Composition Closure)

Space(G)는 정의에 의해 합성에 닫혀 있다:
- f, g ∈ Space(G) → f(g(·)) ∈ Space(G)

### 3.2 Post 클래스 폐포 분석

각 게이트에 대해 Space(G)가 어떤 Post 클래스의 폐포를 형성하는지:

| 게이트 G | T₀-closed? | T₁-closed? | M-closed? | L-closed? | S-closed? |
|---------|-----------|-----------|----------|----------|----------|
| NAND | ✗ | ✗ | ✗ | ✗ | ✗ |
| NOR | ✗ | ✗ | ✗ | ✗ | ✗ |
| AND (+ vars, 0, 1) | ✓ | ✓ | ✓ | ✗ | ✗ |
| OR (+ vars, 0, 1) | ✓ | ✓ | ✓ | ✗ | ✗ |
| XOR (+ 0) | ✓ | ✗ | ✗ | ✓ | ✓ |
| NOT (+ id) | ✗ | ✗ | ✗ | ✗ | ✓ |

> ⚠️ 위 표는 게이트 단독이 아닌, 변수와 상수와 함께 사용하는 경우의 클론 특성이다.

### 3.3 쌍대성(Duality) 폐포

- Space(NAND)와 Space(NOR)는 서로 쌍대 관계 (드 모르간 법칙)
- Space(AND)와 Space(OR)는 쌍대 관계
- Space(XOR)는 자기 자신의 쌍대 (XOR ↔ XNOR ≈ XOR⊕1)

---

## 4. Space(G) 크기 분석 (FQ-1, Q2)

### 4.1 n=4에서의 크기 (알려진 값)

| Space(G) | 크기 (4변수) | 비율 (전체 대비) |
|---------|------------|--------------|
| Space(NAND) = Ω | 65,536 | 100% |
| Space(NOR) = Ω | 65,536 | 100% |
| Space(XOR) = 아핀 | 32 | 0.05% |
| Space(AND) = 단조 부분 | 미계산 | — |
| Space(OR) = 단조 부분 | 미계산 | — |

> **미계산 항목 (FQ-1):** n=4에서 Space(AND), Space(OR)의 정확한 크기는?  
> 참고: 4변수 단조 함수의 전체 수는 Dedekind 수 D(4) = 168이다. 하지만 Space(AND)는  
> 단조 클론에서 AND와 변수, 상수만으로 생성되는 부분집합이므로 D(4)보다 작을 수 있다.

### 4.2 n=2,3,4,5 증가율 패턴 (FQ-1)

| n | |Ω(n)| | |Affine(n)| | 비율 |
|---|--------|-----------|------|
| 2 | 16 | 8 | 50% |
| 3 | 256 | 16 | 6.25% |
| 4 | 65,536 | 32 | 0.049% |
| 5 | 2^32 ≈ 4.3×10⁹ | 64 | 0.0000015% |

→ 아핀 함수: $2^{n+1}$ 개, 지수적으로 증가
→ 전체 함수: $2^{2^n}$ 개, **이중 지수적으로 증가**
→ 비율: 지수적으로 감소 → Space(XOR)는 전체에서 무시할 수 있는 비율

---

## 5. 구조적 불변성 (Structural Invariants)

### 5.1 변수 치환 불변성

**명제:** Space(G)는 변수 치환 하에 닫혀 있다.  
즉 f ∈ Space(G), σ ∈ Sₙ → f∘σ ∈ Space(G)

이는 클론의 기본 속성이다.

### 5.2 K-map 패턴 불변성 (FQ-7)

> **핵심 가설:** Space(G)에 속한 모든 함수는 공통 K-map 구조적 불변성을 가진다.

예:
- Space(XOR): 모든 함수가 ANF에서 1차 이하 → K-map에서 선형 패턴
- Space(AND): 모든 함수가 단조 → K-map에서 1-영역이 0-영역 위에 놓인 단조 패턴

### 5.3 보수 불변성 (Complement Invariance)

- Space(NAND): f ∈ Space(NAND) → ¬f ∈ Space(NAND) (전체 공간은 보수에 닫혀 있음)
- Space(XOR): f ∈ Space(XOR) → f⊕1 ∈ Space(XOR) (1 XOR 연산으로 보수 생성)

---

## 6. Q4가 Q1~Q3를 통합하는 방식

```
Q4: Space(G) 구조 정의
├── Q1: NAND/NOR의 경우 → Space(G) = Ω (만능성)
│        └── 문서: exploration/NAND_universality.md
├── Q2: 각 G에 대한 Space(G) 특성화
│        └── 문서: exploration/XOR_affine_space.md (XOR 사례)
│                  theory/FunctionSpaceTheory.md (전체 표)
└── Q3: f ∈ Space(G) 판별 (구성 가능성)
         └── 문서: exploration/Q3_constructibility_framework.md
```

---

## 7. SRT 연결

| SRT 가설 | Space(G) 연결 |
|---------|-------------|
| H2 (표현 변환) | 표현마다 다른 Space(G) 속성이 드러남 |
| H3 (주의 필터) | K-map 패턴이 Space(G) 탐색에서 시각적 주의를 이끔 |
| H4 (의미 필터) | "이 패턴이 Space(XOR)이다"라는 인식 = H4 작동 |
| H6 (설명적 유의미성) | Space(G) 구조가 설명력을 가지는 이유 분석 |

---

*이 문서는 탐구 과정에서 계속 업데이트될 예정입니다.*
