# Post's Lattice — Boolean Clone Hierarchy and Space(G) Mapping

**버전:** 1.0  
**작성일:** 2026-06-22  
**위치:** `6BooleanFunctionSpaceTheory/theory/PostLattice.md`  
**관련 문서:** `FunctionSpaceTheory.md`, `KarnaughGeometry.md`

---

## 1. Post의 완전성 정리 (Post's Functional Completeness Theorem)

### 1.1 정리 진술

**Theorem (Post, 1941):**  
Boolean 함수의 집합 F ⊆ F₄가 함수적으로 완전(Functionally Complete)하기 위한 필요충분조건:  
F는 다음 5가지 Post 클래스 중 어느 것에도 포함되지 않아야 한다:
1. **T₀** — 0을 보존하는 함수 (f(0,...,0) = 0)
2. **T₁** — 1을 보존하는 함수 (f(1,...,1) = 1)
3. **S** — 자기쌍대(Self-dual) 함수 (f(¬x) = ¬f(x))
4. **M** — 단조(Monotone) 함수
5. **L** — 선형(Linear/Affine) 함수 (ANF에서 AND 항 없음)

### 1.2 NAND와 NOR의 만능성

| 게이트 | T₀ | T₁ | S | M | L | 만능? |
|-------|----|----|---|---|---|------|
| NAND | ✗ (0,0→1) | ✗ (1,1→0) | ✗ | ✗ | ✗ | ✅ |
| NOR | ✗ | ✗ | ✗ | ✗ | ✗ | ✅ |
| AND | ✓ | ✓ | ✗ | ✓ | ✗ | ❌ |
| XOR | ✓ | ✗ | ✓ | ✗ | ✓ | ❌ |

NAND는 5가지 클래스 중 어느 것도 보존하지 않으므로 만능 게이트이다.

---

## 2. Post 격자의 구조 (Post's Lattice)

Post의 격자는 모든 클론(닫혀 있는 연산 클래스)의 집합에 포함 관계를 통해 격자 구조를 부여한 것이다.

```
          Ω (전체 공간)
         /           \
  T₀ ∩ Ω           T₁ ∩ Ω
      |                |
    M (단조)         S (자기쌍대)
      |                |
  M ∩ T₀           S ∩ L
      |                |
    L (선형)        M ∩ S ∩ L
      |                |
  L ∩ T₀ ∩ T₁      ...
      |
   {0, 1, id}
       |
      {} (상수)
```

> ⚠️ 이 다이어그램은 간략화된 버전입니다. 완전한 Post 격자는 무한히 많은 클론을 포함하나, 주요 유한 클래스만 표시하였습니다.

---

## 3. Space(G)의 Post 격자 위치 (Q2와의 연결)

각 게이트 G에 대해 Space(G)는 Post 격자의 특정 클론과 대응된다:

| 게이트 G | Space(G) = Post 클론 | 설명 |
|---------|-------------------|-----|
| NAND | Ω | 전체 Boolean 공간 |
| NOR | Ω | 전체 Boolean 공간 |
| XOR | L (Linear/Affine) | 아핀 함수 공간 |
| AND (+ 변수, 0, 1) | M (Monotone) 부분집합 | 단조 함수 중 AND로 생성 가능한 것 |
| NOT (+ 0 또는 1) | ? | 연구 대상 |

**FQ-2:** Space(G)가 Post 격자의 어느 레벨에 위치하는지 각 G에 대해 정확히 결정하는 것이 후속 연구 과제이다.

---

## 4. Karnaugh 맵과의 연결 (OQ-3)

Post 격자의 각 클래스는 카르노 맵 위에서 특정 기하학적 패턴을 보여줄 것으로 예상된다:

| Post 클래스 | K-map 예상 특성 |
|------------|--------------|
| L (선형) | 체커보드 또는 선형 경계 패턴 |
| M (단조) | "아래에서 위" 단조 패턴 (1은 상위 연결 영역에만) |
| S (자기쌍대) | 보수 관계: 180° 회전 시 0↔1 교환 |
| T₀ | 모든 입력 0일 때 출력 0 (특정 코너 값 고정) |
| T₁ | 모든 입력 1일 때 출력 1 (특정 코너 값 고정) |

> **연결 (OQ-3):**  
> Post 격자의 카르노 맵 기하학 시각화는 이 저장소의 핵심 탐구 과제 중 하나이다.  
> `KarnaughGeometry.md`에서 더 자세히 다룬다.

---

## 5. 미해결 질문

- **FQ-2:** 각 Space(G)가 Post 격자에서 정확히 어느 위치(클론)에 매핑되는가?
- **FQ-3:** Space(G₁) ∩ Space(G₂)의 수학적 구조는 무엇인가?
- **FQ-4:** Space(G)의 폐포 속성을 체계적으로 분류하는 방법은?

---

## 6. 참고 문헌

- Post, E. L. (1941). *The Two-Valued Iterative Systems of Mathematical Logic.* Annals of Mathematical Studies, 5.
- Lau, D. (2006). *Function Algebras on Finite Sets.* Springer.
- [Boolean Function Space Theory 개요] — `README.md` (이 저장소)

---

*이 문서는 스캐폴드 버전입니다. 각 섹션은 연구 진행에 따라 구체화될 예정입니다.*
