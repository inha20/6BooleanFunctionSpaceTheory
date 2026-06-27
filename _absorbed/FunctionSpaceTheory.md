# Function Space Theory — Gate-Generated Boolean Function Spaces

**버전:** 1.0  
**작성일:** 2026-06-22  
**위치:** `6BooleanFunctionSpaceTheory/theory/FunctionSpaceTheory.md`  
**관련 저장소:** [4StructureRecognitionTheory](https://github.com/inha20/4StructureRecognitionTheory)

---

## 1. 기본 정의 (Definitions)

### 1.1 Boolean Function Space

**4변수 Boolean 함수 전체 공간:**

$$\mathcal{F}_4 = \{ f : \{0,1\}^4 \to \{0,1\} \}$$

이 공간의 크기는 $|\mathcal{F}_4| = 2^{2^4} = 2^{16} = 65536$ 이다.

### 1.2 Gate G로 생성된 함수 공간 Space(G)

단일 게이트 G에 대해, G만을 사용하여 구성할 수 있는 모든 Boolean 함수의 집합을 **Space(G)** 로 정의한다.

> **Definition 1.1 (Space(G)):**  
> Space(G) = { f ∈ F₄ | f는 게이트 G와 입력 변수 및 상수 {0, 1}만으로 구성 가능 }

이는 대수학의 **클론(clone)** 개념과 동치이다: Space(G) = [G] (G가 생성하는 Post 클론).

### 1.3 생성(Generation)과 폐포(Closure)

Space(G)는 다음 세 가지 연산에 대해 닫혀 있다:
1. **합성(Composition):** g, h ∈ Space(G) → g(h(·)) ∈ Space(G)
2. **변수 동일화(Identification):** f(x,y) ∈ Space(G) → f(x,x) ∈ Space(G)
3. **상수 대입(Substitution):** f ∈ Space(G), c ∈ {0,1} → f(c, ·) ∈ Space(G)

---

## 2. 주요 게이트별 Space(G) 특성

| 게이트 G | Space(G) | 크기 (4변수) | Post 격자 위치 |
|---------|---------|------------|-------------|
| NAND | 전체 Boolean 공간 | 65,536 | 최상위 (Ω) |
| NOR | 전체 Boolean 공간 | 65,536 | 최상위 (Ω) |
| XOR | 아핀(Affine) 함수 공간 | 256 | 선형 클론 |
| AND | 단조(Monotone) 함수의 부분공간 | < 65,536 | 단조 클론 |
| OR | 단조(Monotone) 함수의 부분공간 | < 65,536 | 단조 클론 |
| NOT | 자기쌍대(Self-dual) 함수 공간 | 미정 | 쌍대 클론 |

> **핵심 미해결 질문 (Q4):** 각 Space(G)의 정확한 크기, 폐포 속성, Karnaugh 맵 시각적 특성, 그리고 구조적 불변성은 무엇인가?

---

## 3. Space(G)의 계층 구조

```
Ω (전체 공간: NAND, NOR)
├── 단조 클론 (Monotone Clone: AND, OR)
│   └── 상수 (0, 1)
├── 선형 클론 (Linear Clone: XOR)
│   └── 상수 (0)
└── 쌍대 클론 (Self-dual Clone: NOT)
```

이 계층은 Post의 격자(Post's Lattice)의 핵심 부분이며, 자세한 내용은 `PostLattice.md`를 참조한다.

---

## 4. 표현 변환 (Representation Transformation)

Space(G)의 동일한 함수는 여러 표현으로 볼 수 있다:

| 표현 방식 | 설명 | 시각화 |
|---------|-----|------|
| 진리표 (Truth Table) | 16비트 벡터 | - |
| 카르노 맵 (Karnaugh Map) | 4×4 격자 | 직접 시각화 가능 |
| 게이트 회로 (Gate Network) | G만으로 구성된 회로 | 그래프 |
| 대수 정규형 (ANF) | XOR+AND 다항식 | 수식 |

> **SRT 연결 (H2 — Representation Transformation):**  
> Space(G)의 구조는 표현 변환에 따라 다르게 드러난다. 카르노 맵은 특히 시각적 패턴을 명시화하는 데 유리하다.

---

## 5. 열린 연구 질문

- **Q1:** NAND/NOR의 만능성(Universality)을 4변수 카르노 맵으로 시각화하는 방법은?
- **Q2:** 각 게이트의 Space(G) 크기를 n변수(n=2,3,4,5)에 대해 정확히 계산할 수 있는가?
- **Q3:** 목표 함수 f가 Space(G)에 속하는지 판별하는 효율적인 기준(Constructibility Framework)은?
- **Q4:** Space(G)에 속한 함수들이 카르노 맵 위에서 공통 시각적 시그니처를 가지는가?

---

## 6. 연구 프로그램 연계

이 문서는 [Structure Recognition Research Program](https://github.com/inha20)의 일부로:
- **Paper 1 (Repo 1):** 카르노 맵 구조 불변성 — Space(G)의 K-map 기하학 기초
- **Paper 3 (Repo 3):** 변수 재배열 불변성 — Space(G) 분류와 S₄ 대칭군의 관계
- **Paper 4 (Repo 4 — SRT):** 구조 인식 이론 — Space(G) 탐색에서 H3(주의 필터), H4(의미 필터) 적용

---

*이 문서는 스캐폴드 버전입니다. 각 섹션은 연구 진행에 따라 구체화될 예정입니다.*
