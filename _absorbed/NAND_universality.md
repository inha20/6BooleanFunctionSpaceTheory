# NAND Universality — Demonstration and Karnaugh Map Visualization

**버전:** 1.0  
**작성일:** 2026-06-22  
**위치:** `6BooleanFunctionSpaceTheory/exploration/NAND_universality.md`  
**관련 질문:** Q1 (TODO.md §2), FQ-1, FQ-2

---

## 1. 탐구 목표

이 문서는 **Q1**을 탐구한다:

> NAND 게이트만을 사용하여 모든 4변수 Boolean 함수(65,536개)를 생성할 수 있음을 입증하고,  
> 이를 카르노 맵을 통해 시각화하라.

---

## 2. NAND 만능성 증명 (Q1 — Theoretical Argument)

### 2.1 핵심 전략: NOT과 AND를 NAND로 구성하기

NAND 게이트의 정의: `A NAND B = ¬(A ∧ B)`

**Step 1: NOT 구성**
```
NOT(A) = A NAND A = ¬(A ∧ A) = ¬A  ✓
```

**Step 2: AND 구성**
```
AND(A, B) = NOT(A NAND B) = (A NAND B) NAND (A NAND B)
          = ¬(¬(A∧B)) = A∧B  ✓
```

**Step 3: OR 구성 (드 모르간 법칙 활용)**
```
OR(A, B) = NOT(NOT(A) AND NOT(B))
         = (A NAND A) NAND (B NAND B)  ✓
```

### 2.2 함수적 완전성 (Post 정리 적용)

Post의 완전성 정리에 의해 {NOT, AND}는 함수적으로 완전하다.  
NAND로 NOT과 AND를 구성할 수 있으므로, NAND 하나만으로도 함수적으로 완전하다.  
따라서 **Space(NAND) = Ω (65,536개 전체)**.

### 2.3 4변수 구체 예시: XOR 구성

XOR(A, B) = (A ∨ ¬B) ∧ (¬A ∨ B) — 이를 NAND 게이트만으로 구성:

```
Step 1: G1 = A NAND B
Step 2: G2 = A NAND G1
Step 3: G3 = B NAND G1
Step 4: XOR = G2 NAND G3
```

[그림 플레이스홀더: Figure04_NAND_XOR_circuit.png]  
*명세: XOR를 NAND 4개로 구성한 회로도, 게이트별 출력 값 표시*

---

## 3. 카르노 맵을 통한 시각화 (Q1 — Visualization)

### 3.1 NAND(A, B)의 카르노 맵

```
        CD
        00  01  11  10
AB  00 | 1 | 1 | 1 | 1 |   ← A=0, B=0일 때 항상 1
    01 | 1 | 1 | 1 | 1 |   ← A=0, B=1일 때 항상 1
    11 | 1 | 1 | 0 | 1 |   ← A=1, B=1일 때 C,D 무관 단 C=1,D=1이면 0
    10 | 1 | 1 | 1 | 1 |   ← A=1, B=0일 때 항상 1
```

> 참고: 위의 예는 A NAND B를 4변수 함수로 확장한 것 (C, D는 don't-care).  
> 실제로는 입력 쌍 (A, B)만 사용하는 2변수 함수가 4변수 공간에 투영된 것.

[그림 플레이스홀더: Figure05_NAND_AB_kmap.png]  
*명세: A NAND B의 4×4 K-map, 0 칸 1개 위치 강조*

### 3.2 NOT(A)의 카르노 맵

```
        CD
        00  01  11  10
AB  00 | 1 | 1 | 1 | 1 |
    01 | 1 | 1 | 1 | 1 |
    11 | 0 | 0 | 0 | 0 |
    10 | 0 | 0 | 0 | 0 |
```

[그림 플레이스홀더: Figure06_NOT_A_kmap.png]  
*명세: ¬A의 4×4 K-map, 위 2행=1, 아래 2행=0으로 구성*

### 3.3 Space(NAND) = 전체 공간 시각화 아이디어

- 65,536개 함수 전부를 NAND로 생성 가능하다는 것은
  → K-map의 임의의 0/1 패턴이 NAND 게이트 회로로 실현 가능하다는 의미
- 실제로 임의의 진리표 = Σmin-terms로 OR 결합 = NOT + AND 결합 = NAND만으로 구성 가능

---

## 4. NOR 만능성 (대칭적 논증)

NAND와 쌍대(dual) 관계:

```
NOT(A) = A NOR A = ¬(A∨A) = ¬A  ✓
OR(A, B) = NOT(A NOR B)  ✓
AND(A, B) = (A NOR A) NOR (B NOR B)  ✓  (드 모르간 적용)
```

→ Space(NOR) = Ω = 전체 Boolean 공간 (65,536개)

---

## 5. 열린 탐구 질문

- **FQ-1:** n=2,3,4,5에 대해 Space(G)의 크기 증가율 패턴은? (NAND/NOR은 항상 최대)
- **FQ-10:** 게이트 복잡성(NAND 게이트 수)과 생성 가능한 함수 수의 관계는?
- **OQ-1:** NAND로 생성된 중간 함수들(NOT, AND, OR, XOR)의 K-map 패턴 시퀀스로 '생성 경로'를 시각화할 수 있는가?

---

## 6. 연구 프로그램 연계

| 연계 저장소 | 연결 지점 |
|------------|---------|
| Repo 1 (KMapStructureInvariance) | 체커보드 패턴 = XOR의 K-map → NAND로 생성 가능 |
| Repo 4 (SRT) | H1(구조 발견): NAND만능성 증명은 어떤 인지적 구조를 드러내는가? |
| Repo 5 (HARCT) | AI가 임의의 K-map 패턴을 NAND 회로로 합성하는 과정 → 인간-AI 분업 모델 |

---

*이 문서는 탐구 과정에서 계속 업데이트될 예정입니다.*
