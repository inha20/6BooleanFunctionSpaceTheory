# FQ Group C — Constructibility and Complexity (FQ-10 ~ FQ-12)

**버전:** 1.0  
**작성일:** 2026-06-22  
**위치:** `6BooleanFunctionSpaceTheory/fq/FQ_C_constructibility.md`  
**원출처:** `TODO.md §4-C`  
**관련 문서:** `exploration/Q3_constructibility_framework.md`, `exploration/Q4_function_space_structure.md`

---

## FQ-10. Gate Complexity and Space(G) Properties

### 질문
게이트 복잡성(Gate Complexity)과 Space(G)의 구조적 속성 사이에 어떤 체계적 관계가 있는가?

### 분석

#### 10.1 게이트 복잡성의 정의

**회로 복잡성 (Circuit Complexity):**  
함수 f를 구현하는 최소 게이트 회로(depth 또는 size 기준)의 크기.

| 복잡성 측도 | 정의 | 예시 |
|-----------|-----|-----|
| **크기(Size)** | 회로 내 게이트 총 수 | AND 1개 → size=1 |
| **깊이(Depth)** | 입력에서 출력까지 가장 긴 경로의 게이트 수 | 병렬 계산 최소 단계 |
| **팬인(Fan-in)** | 게이트 하나가 받는 최대 입력 수 | NAND-2: 팬인=2 |

**Space(G)와의 연결:**
- f ∈ Space(G) ⟹ G로 구성된 회로가 존재 → 최소 크기/깊이가 정의됨
- f ∉ Space(G) ⟹ G 회로 없음 → 복잡성 = ∞ (불가)

#### 10.2 Space(G) 위치와 게이트 복잡성의 관계

**직관:** Post 격자에서 Space(G)가 더 작은(더 제약된) 클론일수록, 그 안의 함수는 더 단순한 구조를 가진다.

| Space(G) | 최소 회로 크기(대표 함수) | 비고 |
|---------|----------------------|-----|
| Ω (NAND, NOR) | 1 게이트(자명 함수부터) ~ 지수적 | 모든 함수 포함, 최악=지수 |
| L (XOR) | 최대 n 게이트 (n-variable XOR) | 선형 — ANF 차수가 깊이를 결정 |
| M∩T₀∩T₁ (AND) | 최대 n-1 게이트 | AND-트리 구조 |
| L ∩ M (선형+단조) | 1 게이트 또는 상수 | 극히 단순: 변수 투영 또는 상수 |

**관찰 1 (복잡성 단조성):**  
Space(G₁) ⊆ Space(G₂)이면, Space(G₁) 안에서의 최대 회로 복잡성 ≤ Space(G₂)에서의 최대 복잡성.  
→ 더 작은 공간 = 더 낮은 (또는 같은) 복잡성 한계

**관찰 2 (공간 크기와 복잡성의 역비례):**

| 공간 크기 | 최대 복잡성 | 설명 |
|---------|----------|-----|
| 65,536 (Ω) | 지수적 | 임의 함수 — 복잡할 수 있음 |
| 32 (아핀) | 선형(n) | ANF 차수 ≤ 1 → 단순 |
| 6 (L∩M) | 상수(0 또는 1 게이트) | 단일 변수 투영 수준 |

→ **Space(G)가 작을수록 그 안의 함수는 더 단순한 복잡성 한계를 가진다.**

#### 10.3 Space(G)별 복잡성 최악 사례

**Space(NAND) = Ω:**
- 최악 복잡성 함수: 예를 들어 Parity(A,B,C,D) = A⊕B⊕C⊕D
  - NAND 회로: 14 NAND 게이트 (4변수 XOR를 NAND로 구현 시)
- 복잡성 하한(Shannon): n변수 함수의 대부분은 최소 $2^n / n$ 크기의 회로가 필요

**Space(XOR) = L:**
- 아핀 함수 f = a₀ ⊕ a₁A ⊕ a₂B ⊕ a₃C ⊕ a₄D
- XOR 트리로 최대 n-1=3개의 XOR 게이트로 구현 가능
- 최대 깊이 = ⌈log₂(n)⌉ (병렬 트리)

**Space(AND) = M∩T₀∩T₁ 부분:**
- AND-트리로 최대 n-1개의 AND 게이트로 구현
- 단조 함수 전체의 최대 복잡성은 더 클 수 있음

#### 10.4 Post 클래스 위반 수 vs. 복잡성

**OQ-4에서 도입된 개념:**  
포스트 클래스 위반 수 V(f) = {f가 T₀, T₁, M, L, S 중 몇 가지를 위반하는가}

| V(f) | 해석 | 예시 |
|-----|-----|-----|
| 0 | 모든 5개 클래스에 속함 (상수 0 또는 1, 단일 변수) | 최소 복잡성 |
| 1 | 4개에 속함 | XOR, AND 등 기본 게이트 |
| 5 | 어느 클래스에도 속하지 않음 (만능) | NAND, NOR |

**가설 (FQ-10):** V(f)가 클수록 일반적으로 복잡성이 높다.  
→ NAND/NOR (V=5)는 모든 함수를 만들 수 있는 "최대 복잡성 허용 공간"

#### 10.5 미해결 질문

- n=4에서 각 Space(G)의 함수 복잡성 분포(histogram)는?
- L ∩ M과 같은 교집합 공간에서 복잡성은 어떻게 변하는가?

---

## FQ-11. Constructibility as Representation Transformation Cost — Connection to Paper 2

### 질문
구성 가능성(f ∈ Space(G))을 "표현 변환 비용(Representation Transformation Cost)"으로 해석할 수 있는가?  
이 해석은 Paper 2(2SymmetricBooleanFunctionMinorThesis)와 어떻게 연결되는가?

### 분석

#### 11.1 표현 변환 비용 개념

**SRT 가설 H2 (Representation Transformation):**  
"어떤 문제는 계산을 줄이는 것이 아니라 표현을 바꿈으로써 해결 가능해진다."

이를 Space(G)에 적용하면:

**정의 (표현 변환 비용):**  
함수 f의 게이트 G에 대한 표현 변환 비용 TC(f, G)는:
- f ∈ Space(G)이면: TC(f, G) = f를 G-회로로 표현하는 최소 비용 (유한)
- f ∉ Space(G)이면: TC(f, G) = ∞ (G-회로로는 표현 불가)

#### 11.2 표현 변환 비용의 계층

```
표현 변환 비용 계층:

TC(f, NAND) = TC(f, NOR) ≤ TC(f, XOR) ≤ TC(f, AND) ≤ ∞
               (모든 f에 유한)    (아핀 f만 유한)  (단조 f만 유한)
```

**해석:**
- NAND 표현: 모든 함수에 대해 유한 비용 → "범용 언어"
- XOR 표현: 아핀 함수에만 유한 → "선형 언어"
- AND 표현: 단조 함수에만 유한 → "단조 언어"

#### 11.3 Paper 2와의 연결

**Paper 2 (2SymmetricBooleanFunctionMinorThesis):**  
대칭 Boolean 함수의 시각적 패턴 연구.

**연결 고리:**
1. 대칭 함수(Symmetric Boolean Function)는 입력 변수의 순열에 불변인 함수
2. 대칭 함수는 특정 Space(G)에 속하는지 분류될 수 있다:
   - 대칭 함수 중 아핀(선형)인 것 = {0, 1, A⊕B⊕C⊕D, ¬(A⊕B⊕C⊕D)} (4개)
   - 대칭 함수 중 단조인 것 = {0, A∧B∧C∧D, A∨B∨C∨D, 1, Majority 등}

3. **표현 변환 비용 관점:**  
   Paper 2에서 관찰된 "시각적 패턴의 다양성" = 서로 다른 Space(G) 표현에서의 복잡성 차이
   - 체커보드 패턴(XOR-게이트 표현) = TC(f, XOR) 최소 사례
   - 링/코너 패턴(AND/OR-게이트 표현) = TC(f, AND) 최소 사례

#### 11.4 SRT H2와의 연결

H2의 핵심 주장: "표현 변환이 문제를 해결 가능하게 만든다"

Space(G) 관점에서:
- 진리표 표현 → 구성 가능성 직접 판단 어려움
- ANF 표현 → Space(XOR) 판단 즉시 가능 (2차 항 존재 여부)
- K-map 표현 → Space(AND) 판단 즉시 가능 (단조 패턴 시각 확인)

**→ 표현 방식 선택이 구성 가능성 판단 비용을 결정한다**

이것이 SRT H2("표현 변환이 새로운 구조를 드러낸다")의 Boolean 함수 공간 버전이다.

#### 11.5 SRT 가설과의 통합

| SRT 가설 | Boolean 함수 공간에서의 대응 |
|---------|--------------------------|
| H2: 표현 변환 | 진리표 → ANF → K-map 변환으로 Space(G) 판단 용이성 변화 |
| H6: 설명적 유의미성 | "이 함수가 XOR-표현 가능"이라는 인식이 연구 가치를 창출 |
| H4: 의미 필터 | Space(G) 분류가 함수의 "설명 가능한 구조"를 선별하는 필터 역할 |

---

## FQ-12. Mathematical Structure of "Functions Not Constructible from Gate G"

### 질문
게이트 G로 구성 불가능한 함수들의 집합 Ω \ Space(G)의 수학적 구조는 무엇인가?

### 분석

#### 12.1 여집합(Complement)의 정의

**정의:**  
$\overline{\text{Space}(G)} = \mathcal{F}_4 \setminus \text{Space}(G)$  
= G만으로는 구성 불가능한 함수들의 집합

#### 12.2 여집합의 기본 성질

**성질 1 (비-클론):**  
$\overline{\text{Space}(G)}$는 클론이 아니다 (합성에 닫혀 있지 않음).  
→ 두 "구성 불가 함수"의 합성이 "구성 가능"이 될 수 있음.

**예시:**  
Space(AND)에 속하지 않는 NOT(A) ∉ Space(AND)  
그러나 NOT(A) AND NOT(B) → 이것도 Space(AND)에 속하지 않음 (NOT이 필요)  
하지만 만약 G=XOR이면: NOT(A)∉Space(XOR)이지만 이런 예외적 합성이 생길 수 있음.

**성질 2 (크기):**  

| Space(G) | $|\overline{\text{Space}(G)}|$ | 비율 |
|---------|-------------------------------|-----|
| Space(XOR) = 32 | 65,504 | ~99.95% |
| Space(AND) 부분집합 | 65,536 - (작은 수) | ~99.7% |
| Space(NAND) = Ω | 0 | 0% |

**관찰:** Space(G)가 작을수록 여집합이 거의 전체 공간을 차지한다.

#### 12.3 여집합의 Post 클래스 구조

$\overline{\text{Space}(G)}$는 직접적인 대수적 구조보다는 **Post 클래스 위반 조건**으로 특성화된다.

**Space(XOR)의 여집합 특성화:**  
$f \notin \text{Space}(XOR)$  
⟺ f의 ANF에 2차 이상의 항이 존재 (AND 항을 포함)  
⟺ f의 K-map이 "아핀 패턴"이 아님 (2×2 부분격자 조건 위반)

**Space(AND)의 여집합 특성화:**  
$f \notin \text{Space}(AND)$  
⟺ f가 단조 함수가 아님  
⟺ 어떤 x ≤ y에 대해 f(x) > f(y)인 쌍이 존재  
⟺ K-map에서 인접 칸 1→0 전환(입력 증가에 출력 감소)이 존재

#### 12.4 여집합의 계층 구조

```
Ω = Space(NAND)
├── Space(XOR) (32개)
│     └── Space(XOR) ∩ Space(AND) = 선형+단조 (6개)
└── Ω \ Space(XOR) (65,504개)  ← FQ-12의 관심 대상
      ├── (단조이지만 비선형인 함수들)
      ├── (자기쌍대이지만 비선형인 함수들)
      └── (어느 특수 클래스에도 속하지 않는 함수들) ← 대다수
```

#### 12.5 "구성 불가 함수"의 분류

$\overline{\text{Space}(XOR)}$ = 65,504개 함수를 Post 클래스 기준으로 분류:

| 추가 속성 | 해당 개수 (추정) | 설명 |
|---------|--------------|-----|
| 단조(M) but 비선형 | ~162개 | 단조이지만 XOR 구성 불가 |
| 자기쌍대(S) but 비선형 | ~224개 | 자기쌍대이지만 XOR 구성 불가 |
| T₀∩T₁ but 비선형 | ~많음 | 양끝 보존이지만 XOR 구성 불가 |
| 어느 특수 클래스도 아님 | 대다수 | "일반적" 비선형 함수 |

#### 12.6 K-map 기하학적 관점

$\overline{\text{Space}(XOR)}$의 K-map 특성:
- "불규칙한" 패턴: 2×2 부분격자 조건을 적어도 하나 위반
- 체커보드, 줄무늬, 균일 블록과 다른 "비선형적 복잡한" 패턴
- [그림 플레이스홀더: FQ12_Figure01_nonlinear_kmap_gallery.png]  
  *명세: 비선형 함수 K-map 8개 예시, 아핀 조건 위반 위치 표시*

#### 12.7 SRT 연결 (H4 — 의미 필터)

$\overline{\text{Space}(G)}$는 "흥미로운 구조가 없는 함수들"이 아니라:
- 오히려 특정 게이트로는 표현이 불가능한 → "더 풍부한 구조"를 가진 함수들

이 역설이 SRT H4(의미 필터)와 연결된다:
- H4: 인간은 무의식적으로 "설명 가능한 구조"에 주의를 기울임
- $\overline{\text{Space}(XOR)}$의 함수들은 XOR 표현으로는 설명 불가 → 다른 표현(NAND 등)을 요구
- 어떤 $\overline{\text{Space}(G)}$ 원소가 인간의 주의를 끄는가? = FQ-14와 연결

---

## 소결 (FQ-10~12 통합 관찰)

1. **복잡성과 공간 크기의 역비례:** Space(G)가 클수록 더 복잡한 함수를 포함하지만, 더 작은 공간의 함수들은 상한이 낮은 복잡성을 가진다.
2. **표현 변환 비용으로서의 구성 가능성:** f ∈ Space(G)는 TC(f, G) < ∞를 의미하며, 이는 SRT H2의 Boolean 함수 공간 버전이다.
3. **여집합의 풍부한 구조:** $\overline{\text{Space}(G)}$는 단순히 "구성 불가 집합"이 아니라 Post 클래스 위반 조건으로 세밀하게 분류되며, K-map 기하학적 관점에서 "더 복잡한 구조"를 가진다.

---

*이 문서는 탐구 과정에서 계속 업데이트될 예정입니다.*
