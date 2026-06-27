# 6BooleanFunctionSpaceTheory — Master Roadmap (TODO)

본 문서는 파편화된 문서들을 연결하는 **마스터 내비게이션 허브**이자, 추상적인 미래 계획(`FutureWorks.md`)을 실행 가능한 단위 행동(Actionable Tasks)으로 분할한 **상세 할 일 목록**입니다.

> [!TIP]
> **AI 에이전트 및 공동 연구자를 위한 안내:** 
> 본 문서(`TODO.md`)는 거시적인 로드맵(Phase 단위)을 관리합니다. 현재 **당장 실행해야 할 미시적인 세부 작업(Micro-tasks, 스크립트 작성, 수식 전개 등)**은 [SubTODO.md](./SubTODO.md)에서 관리하고 있으니, 실제 작업 전 반드시 해당 문서를 확인하세요.

---

## Phase 1: 기반 정립 및 탐구 노트 (✅ 완료 아카이브)

초기 설정 및 파편화된 탐구/질문 파일들을 카테고리별로 모아둔 아카이브입니다. 필요 시 아래 링크를 통해 원본 문서로 이동하세요.

### 1.1 기본 구조 및 프레임워크 탐구 (`exploration/`, `theory/`)
- [x] [FunctionSpaceTheory.md](theory/FunctionSpaceTheory.md): 게이트 공간 이론 기초
- [x] [PostLattice.md](theory/PostLattice.md), [KarnaughGeometry.md](theory/KarnaughGeometry.md)
- [x] **Q1~Q4 해결:** NAND 만능성, XOR 아핀 공간, 구성 가능성 파악 (`exploration/` 폴더 내 문서)

### 1.2 미해결 질문 (Open Questions, `questions/`)
- [x] [OQ1: K-map 시각적 시그니처](questions/OQ1_kmap_visual_signatures.md)
- [x] [OQ2: 축 교환 대칭](questions/OQ2_axisswap_symmetry.md)
- [x] [OQ3: 포스트 격자 K-map 시각화](questions/OQ3_post_lattice_kmap.md)
- [x] [OQ4: 게이트 복잡성](questions/OQ4_gate_complexity.md)
- [x] [OQ5: 다치 논리 확장](questions/OQ5_manyvalued_logic.md)

### 1.3 후속 세부 질문 (Follow-up Questions, `fq/`)
- [x] FQ-1~5: Function Space Structure (`fq/FQ_A_function_space_structure.md`)
- [x] FQ-6~9: Karnaugh Map Geometry (`fq/FQ_B_kmap_geometry.md`)
- [x] FQ-10~12: Constructibility (`fq/FQ_C_constructibility.md`)
- [x] FQ-13~15: SRT Connection (`fq/FQ_D_srt_connection.md`)
- [x] FQ-16~17: Human-AI Collaboration (`fq/FQ_E_human_ai.md`)
- [x] FQ-18~20: Generalization (`fq/FQ_F_generalization.md`)

### 1.4 통합 지침 및 문서 병합 완료
- [x] [FutureWorks.md](FutureWorks.md): 미래 아이디어 통합본
- [x] [IntegrationMap.md](IntegrationMap.md): Repo 1~5와의 통합 지점 명시

---

## Phase 2: S₄ 군론적 분류 심화 (✅ 완료)

Repo 3(변수 재배열 불변)과 Repo 6(게이트 공간)을 수학적으로 완전히 통일하는 단계. (`FutureWorks.md §1`)

### 2.1 군론적 분류 (`theory/S4GroupAnalysis.md`)
- [x] **OC-1~OC-5 완료:** Space(XOR) 10궤도, Space(AND) 30궤도(168개), Space(NOT) 32궤도, L∩M 3궤도 완전 분류 완료 (2026-06-23)

### 2.2 파이썬 스크립트 공식화 (코드 보존)
- [x] **[Code]** `scripts/` 디렉토리 생성 *(2026-06-23)*
- [x] **[Code]** `s4_orbit_calculator.py` 스크립트 작성 및 검증 완료 *(2026-06-23 — 전체 통과)*
- [x] **[Code]** README.md에 스크립트 실행 방법 및 활용법 가이드 추가 *(2026-06-23)*
- [x] **[Audit]** `inha20-main` 및 `6BooleanFunctionSpaceTheory` 전역 대상 이론 검증용 파이썬 코드 누락 감사 수행 — 전체 유실 없이 정상 보존 확인 *(2026-06-23)*

### 2.3 군론적 분류 후속 확장
- [x] **[Math]** Space(NOT)의 S₄-궤도 분류 — 32궤도, 불동점 부재(정리 3.5.2) *(OC-4)*
- [x] **[Math]** L ∩ M 공간의 궤도 확인 — {0,1,A,B,C,D} 6개, 3궤도 *(OC-5)*
- [x] **[Math]** n=5 확장 기초 스캐폴드 — 아핀 함수 S₅-궤도 12개 예측, 이론 계산 완료

---

## Phase 3: SRT 인지 실험 설계 (⏸️ Deferred to FutureWorks)

핵심 문서: [`theory/CognitiveExperimentDesign.md`](theory/CognitiveExperimentDesign.md)

- [x] **[Exp-1]** K-map 패턴 주의 순서(H3) 측정을 위한 자극(Stimuli) 샘플 세트 구성 — S₄-궤도 기반 50개 자극 선정 *(2026-06-23)*
- [x] **[Exp-2]** 연구 가치 판단(H4) 측정용 질문/설문지 초안 작성 — H4 세부 기준(압축·예측·일반화·설명 인력)별 7점 척도 문항 *(2026-06-23)*
- [x] **[Exp-3]** "설명적 유의미성(H6)" 감지 시점 측정을 위한 대조군 설계 및 프로토콜 뼈대 구축 *(2026-06-23)*
- [ ] **[Deferred]** 소규모 파일럿 테스트 (N=3) 진행 및 프로토콜 피드백 수집 *(후속 연구 이관)*
- [ ] **[Deferred]** 자극 정련(K-map 시각화 표준화) 및 현재 소속기관 또는 공용 IRB 심의 필요 여부 검토 *(후속 연구 이관)*
- [ ] **[Deferred]** (선택) 동일 K-map 자극을 LLM(AI)에 제시하여 대조 실험(H1/H7) *(후속 연구 이관)*

---

## Phase 4: Human-AI 협업 모델 (HARCT) 구체화 (🟢 Active)

장기 연구에서의 기억 분담 및 연구 협업 교육 프레임워크 수립. (`FutureWorks.md §3, §4`)

핵심 문서: [`theory/MemoryAndEducationModel.md`](theory/MemoryAndEducationModel.md)

### 4.1 기억 분담 모델 (Memory Model)
- [x] **[Model]** M_AI(t)와 M_H(t)를 활용한 인간-AI 기억 분담 수학적/인지적 모델링 정리 문서화 *(2026-06-23)*
- [x] **[Review]** SESSION_START.md의 현황판 구조가 이 모델에서 가지는 의의 분석 *(2026-06-23)*

### 4.2 AI 협업 교육 (Education Framework)
- [x] **[Edu]** Level 1 (도구/계산기 활용) 실습 시나리오 작성 *(2026-06-23)*
- [x] **[Edu]** Level 2 (검증자 활용 — 가설 교차검증) 실습 시나리오 작성 *(2026-06-23)*
- [x] **[Edu]** Level 3 (질문 생성 및 공동 탐구자) 실습 시나리오 작성 *(2026-06-23)*
- [ ] **[Deferred]** 작성된 Level 1~3 교육 시나리오를 바탕으로 실제 학생 대상 파일럿 실습 또는 워크숍 진행 계획 수립 *(후속 연구 이관)*

---

## Phase 5: 연구 기원 타임라인 및 이론 통합 (🟢 Active)

핵심 문서: [`theory/ResearchOriginTimeline.md`](theory/ResearchOriginTimeline.md)

- [x] **[History]** Phase 0 (초등학생) ~ Phase 5 (현재 Repo 6)에 이르는 개인 연구 인지 발달 타임라인 텍스트 초안 작성 *(2026-06-23)*
- [x] **[Theory]** Repo 6의 핵심 수학적 성과(S₄ 불동점 ↔ SRT H8·H9의 관계)를 Repo 4 논문에 병합하기 위한 개요 작성 *(2026-06-23)*
- [ ] **[Publish]** 도출된 수학적 성과와 이론 개요를 Repo 6 자체 메인 본문(`index.html` 또는 `README.md` 등)으로 공식 통합 및 배포
- [ ] **[Hub]** 6번 저장소의 완료 상태 및 핵심 성과를 `inha20-main` 중앙 허브에 반영
