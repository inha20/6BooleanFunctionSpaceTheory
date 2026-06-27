# 6BooleanFunctionSpaceTheory — 통합 작업 관리 문서

**저장소:** 6BooleanFunctionSpaceTheory  
**버전:** 2.0 (2026-06-27 통합 — TODO.md + SubTODO.md + FUTURE_RESEARCH.md 병합)

> **AI 에이전트 및 공동 연구자를 위한 안내:**  
> 이 문서는 Phase별 거시적 로드맵, 현재 스프린트 상태, 미래 연구 계획을 **단일 파일로 통합** 관리합니다.  
> 실행 규칙: **작업 완료 → 파일 재확인 → 그 다음에만 체크** (Work-Then-Record Protocol)

---

## 📋 현재 스프린트 상태

### ✅ 완료된 작업 (2026-06-27 기준)

| 항목 | 완료일 |
|------|--------|
| Phase 5: `index.html` 논문 통합 배포 (paper.md → index.html 전면 재작성) | 2026-06-27 |
| Phase 5: `inha20-main` 중앙 허브 Repo 6 카드 갱신 | 2026-06-27 |
| 본문 흡수 완료 파일 18개 → `_absorbed/` 폴더 정리 | 2026-06-27 |
| 저장소 단순화 (파일 수 최소화) | 2026-06-27 |
| SESSION_START.md Session 48 기록 및 Health 표 갱신 | 2026-06-27 |
| inha20-main/index.html Repo 6 카드 상태 갱신 | 2026-06-27 |

### 🔴 잔여 작업 (연구자 직접)

- [ ] **`index.html` §6 개인 경험 서술 5개 섹션 작성** (Phase 0~5 placeholder 채우기)
  - `#phase0-placeholder` — 어린 시절 수학 패턴 경험
  - `#phase1-placeholder` — Karnaugh map 체커보드 발견 계기
  - `#phase2-placeholder` — 대칭 함수 / Hamming weight 발견
  - `#phase3-placeholder` — 변수 재배열 군론적 분류 발상
  - `#phase4-placeholder` — SRT 메타 이론 통합 계기
  - `#phase5-placeholder` — Burnside 보조정리 적용 경위
- [x] **`SESSION_START.md` Phase 5 체크 갱신** (`inha20-main/SESSION_START.md`) ← Session 48에서 완료, 현황판에 Phase 1·2·5 Complete 반영됨

---

## 📁 현재 저장소 파일 구조

```
6BooleanFunctionSpaceTheory-main/
├── index.html                   ← 메인 논문 (웹 배포)
├── paper.md                     ← 메인 논문 소스
├── README.md                    ← GitHub Pages 진입점
├── SubTODO.md                   ← 이 파일 (통합 작업 관리)
├── _absorbed/                   ← 본문 흡수 완료 파일 보관 (삭제 가능)
├── scripts/
│   └── s4_orbit_calculator.py  ← S₄ 궤도 계산 Python 스크립트 (검증 코드)
└── theory/
    └── S4GroupAnalysis.md       ← 핵심 수학 원본 (OC-1~OC-5 전체 계산)
```

---

## 🗺 Phase 로드맵

### Phase 1 · 기반 정립 ✅ 완료
- 탐구 노트(exploration/), 미해결 질문(questions/), 후속 질문(fq/) — 모두 paper.md에 흡수

### Phase 2 · S₄ 군론적 분류 ✅ 완료
- Space(XOR) 10궤도, Space(AND) 30궤도, Space(NOT) 32궤도, L∩M 3궤도 — 완전 분류
- Burnside 이론 계산 + Python 컴퓨터 검증 양쪽 완료
- `theory/S4GroupAnalysis.md` — 세부 계산 원본 유지

### Phase 3 · SRT 인지 실험 ⏸️ 후속 연구 이관
→ 아래 **미래 연구** 섹션 참조

### Phase 4 · Human-AI 협업 모델 ⏸️ 후속 연구 이관
→ 아래 **미래 연구** 섹션 참조

### Phase 5 · 논문 통합 및 배포 ✅ 완료
- `paper.md` 작성 완료 (§1~§7, §6 개인 서술 placeholder 제외)
- `index.html` 전면 재작성 — KaTeX 수식, 섹션 구조 완성
- `inha20-main` 허브 Repo 6 카드 갱신

---

## 🔭 미래 연구 (FutureWorks)

> 이 섹션은 구 `FUTURE_RESEARCH.md`, `theory/CognitiveExperimentDesign.md`,
> `theory/KMapVisualizationSpec.md`, `theory/MemoryAndEducationModel.md`,
> `questions/OQ5_manyvalued_logic.md`, `fq/FQ_E_human_ai.md`, `fq/FQ_F_generalization.md`
> 의 핵심 내용을 통합한 것입니다.

---

### FR-1 · SRT 인지 실험 (Phase 3) 🔜 후속 연구

**목표:** `paper.md` §5에서 제시한 수학적 예측 — "S₄ 불동점 함수가 주의를 먼저 끈다"(H3), "궤도 크기가 작을수록 연구 가치 있게 판단한다"(H4) — 를 실제 인간 실험으로 검증한다.

**완료된 준비 작업:**

| 항목 | 상태 |
|------|------|
| Exp-1: K-map 주의 순서 측정 자극 50개 선정 (S₄ 궤도 크기별 층화) | ✅ 완료 |
| Exp-2: 연구 가치 판단 설문지 초안 (H4 기준 4항목 × 7점 척도) | ✅ 완료 |
| Exp-3: 설명적 의미성 감지 시점 프로토콜 초안 | ✅ 완료 |
| 자극 시각화 표준화 명세 v1.0 (400×400px, Gray code, 색상 팔레트) | ✅ 완료 |

**후속 연구 과제 (현재 미착수):**
- 자극 이미지 실제 제작 (F01–F08 V2·V3, 통제 자극, `stimuli/manifest.csv`)
  - 제작 규칙: PowerPoint/Draw.io 사용, AI 자동 생성 금지 (IMAGE CREATION RULE)
- 소규모 파일럿 실시 (N=3), 프로토콜 피드백 수집
- IRB 심의 여부 확인 (현 소속기관 또는 공용기관생명윤리위원회)
- (선택) 동일 자극을 LLM에 제시 — 인간-AI 구조 발견 비교 실험 (H1/H7)

**자극 세트 구성 (50개):**

| 자극 범주 | 기반 | 발굴 수 |
|---------|-----|--------|
| S₄ 불동점 (Space(XOR): O₉·O₁₀·O₃·O₄) | 궤도 크기 1 | 4개 |
| S₄ 불동점 (Space(AND): 대칭적 단조 함수 6개) | 궤도 크기 1 | 6개 |
| 소궤도 (크기 3~4) | 부분 선택 | 7개 |
| 중궤도 (크기 6) | 부분 선택 | 6개 |
| 대궤도 (크기 12) | 역선택 | 7개 |
| Space(NOT) 샘플 (크기 4·12 궤도) | 자기쌍대 | 10개 |
| 기준점 (무작위 비구조적) | 통제 조건 | 10개 |
| **합계** | | **50개** |

**paper.md 통합 지점:** 실험 결과 → §5.2 (H3 수정/보완), §5.3 (H4 수치화 검증)

---

### FR-2 · Human-AI 협업 모델 및 교육 프레임워크 (Phase 4) ⏸️ 우선순위 2

**목표:** 이 연구 프로그램에서 관찰된 인간-AI 협업 패턴을 형식화하고, 교육 시나리오로 발전시킨다.

**완료된 준비 작업:**
- 기억 분담 모델 수식화: $K(t) = M_H(t) \cup M_{doc}(t)$
- Level 1~3 교육 시나리오 초안 작성 완료

**기억 분담 모델:**

| 기억 주체 | 특성 | 한계 |
|---------|-----|------|
| $M_H(t)$ (연구자) | 지속적, 맥락 이해, 직관 포함 | 부정확, 망각 |
| $M_{doc}(t)$ (문서) | 대용량, 정확, 빠른 검색 | 세션 종료 후 $M_{AI}$ 소멸 |

**최적 역할 분담 루프:**
```
[인간] 새로운 패턴 식별 / 질문 생성
    → [AI] 해당 패턴의 Space(G) 분류 계산 + 유사 패턴 전체 열거
    → [인간] 결과 해석 + 새로운 질문 추출
    → [AI] 이론적 근거 탐색 + 문서화
    → [인간] 연구 방향 결정 + 가설 정제
    → (루프 반복)
```

**AI 협업 교육 프레임워크 (Level 1~3):**

| Level | AI 활용 방식 | 협업 질 | 이 연구에서의 예 |
|-------|-----------|---------|--------------|
| Level 1 | 도구/계산기 | 낮음 | Space(G) 크기 계산, K-map 생성 |
| Level 2 | 검증자/교차검토 | 중간 | Burnside 결과 반례 탐색 |
| Level 3 | 공동 탐구자 | 높음 | FQ-1~20 질문 생성 과정 전체 |

**잔여 작업:**
- [ ] Level 1~3 시나리오를 실제 학생 대상 파일럿 실습 계획 수립
- [ ] 협업 수준(Level) 전이 조건 연구

**paper.md 통합 지점:** 기억 분담 모델 공식화 결과 → §5.4(H8-H9-H10) 강화 / 교육 프레임워크 → 별도 논문(Repo 5 확장) 또는 paper.md 부록

---

### FR-3 · 차원 확장 (n=5 이상) ✅ Space(XOR)+Space(AND) 계산 완료 (2026-06-27)

**n=5 계산 결과 (2026-06-27 Session 49 — Python 완전 계산 완료):**

| 공간 | 함수 수 | S₅-궤도 수 | 검증 |
|------|---------|-----------|------|
| Space(XOR)_n5 | 64 | **12** | ✅ Burnside 이론값(12)과 일치 |
| Space(AND)_n5 | 7,581 (D(5)) | **210** | ✅ 열거↔Burnside 일치 |

**Space(XOR)_n5 궤도 크기 분포:**
- 크기 1 × 4개 궤도 (S₅-불동점: f=0, A⊕B⊕C⊕D⊕E, 보수, f=1)
- 크기 5 × 4개 궤도
- 크기 10 × 4개 궤도

**Space(AND)_n5 궤도 크기 분포:**
- 크기1(7), 크기5(14), 크기10(28), 크기12(2), 크기15(14), 크기20(21), 크기30(43), 크기60(74), 크기120(7)

**n=4 vs n=5 비교 요약:**
- Space(XOR): n=4 → 10궤도, n=5 → 12궤도
- Space(AND): n=4 → 30궤도, n=5 → 210궤도 (Dedekind 수 급증 반영)

**구현:** `scripts/s4_orbit_calculator.py` 섹션 8 추가 (`run_n5_full_analysis()`, `_generate_n5_monotone()` 등)
실행 명령: `python scripts/s4_orbit_calculator.py --n5-compute` (약 60초)

**목표:** `paper.md` 신규 소절 추가

**변수별 함수 수 규모:**

| n | 전체 함수 수 | 단조 함수 수 (Dedekind) | 비고 |
|---|-----------|---------------------|------|
| 4 | 65,536 | 168 | **본 연구 완결** |
| 5 | 4.3×10⁹ | 7,581 | 5변수 K-map 분석 불가, 샘플링 필요 |
| 6 | 1.8×10¹⁹ | 7,828,354 | 이론 분석만 가능 |

**잔여 작업:**
- [x] n=5 Space(XOR), Space(AND) 궤도 수 Python으로 완전 계산 ✅ (2026-06-27: XOR=12, AND=210)
- [ ] n=5 결과 → paper.md §3에 소절 추가

**paper.md 통합 지점:** n=5 결과 → §3 말미 소절, §7.3 갱신

---

### FR-4 · 다치 논리로의 확장 ⏸️ 우선순위 4

**목표:** Boolean(2값) → Ternary(3값) → k값 논리로 Space(G) 이론을 확장한다.

**보존되는 구조:** Space(G) 정의(클론 개념), 함수의 완전성(Rosenberg 정리), 변수 치환 군론(Sₙ)

**사라지는 구조:** K-map 기하학(9×9 격자 등), 아핀 공간(GF(k) 위 선형 구조), 만능 게이트 구조 변화

$$|\mathcal{F}_{n,k}| = k^{k^n}$$

n=2, k=3: 19,683개 — 본격 연구가 가능한 규모.

**잔여 작업:**
- [ ] 3값 논리에서의 Rosenberg 완전성 정리 적용 검토
- [ ] Ternary Space(G) 개념 정의 및 예시 산출

---

### FR-5 · 위상수학적 관점 (장기)

**목표:** Boolean 함수 공간을 위상 공간으로 보면: 함수 간 거리 = Hamming 거리(진리표 비교 → 다른 비트 수). S₄ 궤도는 이 위상에서 연결 성분을 이룬다.

**미해결 질문:** Space(G)의 Hamming 거리 기반 위상의 성질은 무엇인가?

**잔여 작업:**
- [ ] Hamming 거리 기반 Space(G) 위상 탐색 (초기 단계)

---

### FR-6 · 연구 기원 타임라인 완성 (연구자 직접)

**목표:** `index.html` §6 및 `paper.md` §6의 개인 서술 placeholder를 완성한다.

**참고 초안:** `_absorbed/ResearchOriginTimeline.md` (Phase 0~5 보완 가이드 포함)

| 섹션 | 중요도 | 가이드 |
|-----|-------|--------|
| Phase 0 (어린 시절) | 높음 | 수학 패턴에서 "왜"가 처음 생긴 구체적 경험 |
| Phase 1 (체커보드 발견) | 높음 | 카르노 맵 최초 접촉 상황, 발견 계기 |
| Phase 2 (Repo 2) | 중간 | Phase 1 이후 개념이 연결된 과정 |
| Phase 3 (Repo 3) | 중간 | 수학적 파라미터(R-3, A-7) 도출 맥락 |
| Phase 4 (SRT) | 중간 | Repo 1–3을 메타 이론으로 통합한 계기 |
| Phase 5 (Repo 6) | 높음 | Burnside 보조정리 적용 경위 |

---

## 🔧 검증 코드

`scripts/s4_orbit_calculator.py`:
```bash
# 기본 실행 (n=4 전체 분류)
python scripts/s4_orbit_calculator.py

# n=5 이론 스캐폴드 (검증 완료 요약 표시)
python scripts/s4_orbit_calculator.py --n5

# n=5 완전 계산 (실제 열거 + Burnside 검증, 약 60초)
python scripts/s4_orbit_calculator.py --n5-compute
```

**검증 결과 (2026-06-23 n=4) + FR-3 계산 결과 (2026-06-27 n=5):**

| 공간 | 궤도 수 | Python 검증 |
|------|--------|------------|
| Space(XOR) = L (n=4) | 10 | ✅ |
| Space(AND) = M (n=4) | 30 | ✅ |
| Space(NOT) = D (n=4) | 32 | ✅ |
| L ∩ M (n=4) | 3 | ✅ |
| Space(XOR)_n5 (n=5) | **12** | ✅ (2026-06-27) |
| Space(AND)_n5 (n=5) | **210** | ✅ (2026-06-27) |

---

## 📌 Work-Then-Record Protocol

**절대 원칙:** 작업 완료 → 파일 재확인 → 그 다음에만 이 문서 갱신  
**적용 대상:** 이 문서의 모든 체크리스트 항목

*Last Updated: 2026-06-27 (FR-3 n=5 계산 완료: Space(XOR)=12궤도, Space(AND)=210궤도 검증; 체크박스 정리)*
