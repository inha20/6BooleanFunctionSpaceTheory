# 파일 정리 평가 — 6BooleanFunctionSpaceTheory

**작성일:** 2026-06-27  
**기준:** `paper.md`에 핵심 내용이 흡수되었으면 → 🗑️ 삭제 가능, 그렇지 않으면 → ✅ 유지

> **판단 기준:**
> - 🗑️ **삭제 가능**: 파일의 핵심 결론·정의·수식이 paper.md에 온전히 포함됨
> - ✅ **유지 (이유: 미래 연구)**: Phase 3·4 이관 파일 — 후속 연구에 필요
> - ✅ **유지 (이유: 운영 문서)**: 연구 관리·배포·코드 파일
> - ✅ **유지 (이유: 탐구 과정)**: 탐구 과정 기록으로 연구 이력 보존 가치 있음

---

## 루트 파일

| 파일 | 판단 | 이유 |
|-----|------|------|
| `paper.md` | ✅ **유지 (핵심 문서)** | 이번 세션에서 작성한 통합 소논문 본체 |
| `README.md` | ✅ **유지 (운영 문서)** | GitHub Pages 공개 진입점 |
| `index.html` | ✅ **유지 (운영 문서)** | GitHub Pages 배포 본문 |
| `TODO.md` | ✅ **유지 (운영 문서)** | 연구 로드맵·Phase 관리 (Deferred 상태 반영됨) |
| `SubTODO.md` | ✅ **유지 (운영 문서)** | 세부 작업 추적 (Deferred 상태 반영됨) |
| `FutureWorks.md` | 🗑️ **삭제 가능** | `FUTURE_RESEARCH.md`로 통합 완료. 기존 우선순위 표·연구 설명 모두 포함됨 |
| `FUTURE_RESEARCH.md` | ✅ **유지 (향후 연구 허브)** | 이번 세션 신규 작성. 미래 연구 4가지 전체 통합 문서. `paper.md` §7.3에서 연결됨 |
| `IntegrationMap.md` | 🗑️ **삭제 가능** | §4(선행연구 통합)가 `paper.md` §4로 완전히 흡수됨. Repo 1~5와의 통합 진술 전체 포함 |

---

## `theory/` 폴더

| 파일 | 판단 | 이유 |
|-----|------|------|
| `FunctionSpaceTheory.md` | 🗑️ **삭제 가능** | Space(G) 정의·클론 개념·계층 구조가 paper.md §2.2에 완전히 흡수됨 |
| `PostLattice.md` | 🗑️ **삭제 가능** | Post 격자·T₀/T₁/S/M/L 분류·만능성 증명이 paper.md §2.3에 완전히 흡수됨 |
| `KarnaughGeometry.md` | 🗑️ **삭제 가능** | 카르노 맵 기하학적 해석·공간별 K-map 특성이 paper.md §2.4에 흡수됨 |
| `S4GroupAnalysis.md` | ✅ **유지 (상세 원본)** | paper.md의 핵심 수학 원천 문서. OC-1~OC-5 전체 계산 과정·30궤도 완전 목록(O01~O30) 등 paper.md보다 훨씬 상세. 검증 기준 문서로 유지 필요 |
| `ResearchOriginTimeline.md` | 🗑️ **삭제 가능** | paper.md §6으로 통합됨. 단, §6 개인 서술 보완 시 이 파일 참조 가이드를 함께 볼 것 → **보완 완료 후 삭제 권장** |
| `CognitiveExperimentDesign.md` | ✅ **유지 (이유: 미래 연구)** | Phase 3(인지 실험) 이관 파일. 파일럿 실시 시 필요 |
| `KMapVisualizationSpec.md` | ✅ **유지 (이유: 미래 연구)** | Phase 3 자극 이미지 제작 표준화 명세. 파일럿 실시 시 필요 |
| `MemoryAndEducationModel.md` | ✅ **유지 (이유: 미래 연구)** | Phase 4(인간-AI 협업 교육 모델) 이관 파일. 후속 연구에서 사용 예정 |

---

## `exploration/` 폴더

| 파일 | 판단 | 이유 |
|-----|------|------|
| `NAND_universality.md` | 🗑️ **삭제 가능** | NAND 만능성·Post 완전성 정리가 paper.md §2.3에 흡수됨. 탐구 과정 기록 |
| `XOR_affine_space.md` | 🗑️ **삭제 가능** | 아핀 함수 정의·32개 목록이 paper.md §2.2·§3.1에 흡수됨. S4GroupAnalysis.md가 더 완전한 원본 |
| `Q3_constructibility_framework.md` | 🗑️ **삭제 가능** | 구성 가능성(constructibility) 프레임워크. 핵심 결론(Space(G) 계층)이 paper.md §2에 포함. 탐구 과정 기록 |
| `Q4_function_space_structure.md` | 🗑️ **삭제 가능** | Q4(함수 공간 구조) 탐구. 핵심 결론이 paper.md §2·§3에 포함. 탐구 과정 기록 |

---

## `questions/` 폴더

| 파일 | 판단 | 이유 |
|-----|------|------|
| `OQ1_kmap_visual_signatures.md` | 🗑️ **삭제 가능** | K-map 시각적 시그니처 분석이 paper.md §2.4·§5.2에 흡수됨 |
| `OQ2_axisswap_symmetry.md` | 🗑️ **삭제 가능** | 축 교환 대칭 = S₄ 작용. paper.md §2.5·§3·§4.1에 완전히 흡수됨 |
| `OQ3_post_lattice_kmap.md` | 🗑️ **삭제 가능** | Post 격자와 K-map 연결. paper.md §2.3·§2.4에 흡수됨 |
| `OQ4_gate_complexity.md` | 🗑️ **삭제 가능** | 게이트 복잡성 질문. paper.md에서 FutureWorks 영역으로 처리됨. 내용 보존 필요 없음 |
| `OQ5_manyvalued_logic.md` | ✅ **유지 (이유: 미래 연구)** | 다치 논리 확장 = FutureWorks §5에 해당. paper.md 범위 밖. 후속 연구 시 참조 |

---

## `fq/` 폴더

| 파일 | 판단 | 이유 |
|-----|------|------|
| `FQ_A_function_space_structure.md` | 🗑️ **삭제 가능** | FQ-1~5(함수 공간 구조). 핵심 결론이 paper.md §2·§3에 흡수됨 |
| `FQ_B_kmap_geometry.md` | 🗑️ **삭제 가능** | FQ-6~9(K-map 기하학). 특히 FQ-9(정제 관계)가 paper.md §4.1(정리 4.1)에 흡수됨 |
| `FQ_C_constructibility.md` | 🗑️ **삭제 가능** | FQ-10~12(구성 가능성). 핵심 결론 paper.md에 흡수됨 |
| `FQ_D_srt_connection.md` | 🗑️ **삭제 가능** | FQ-13~15(SRT 연결). H3·H4·H6 Boolean 적용이 paper.md §5에 완전히 흡수됨 |
| `FQ_E_human_ai.md` | ✅ **유지 (이유: 미래 연구)** | FQ-16~17(인간-AI 협업). Phase 4 이관 영역. MemoryAndEducationModel.md와 연관 |
| `FQ_F_generalization.md` | ✅ **유지 (이유: 미래 연구)** | FQ-18~20(일반화: n=5 확장·다치 논리·위상학적 관점). paper.md §7.3에서 향후 연구로 언급. 내용은 미포함 |

---

## `scripts/` 폴더

| 파일 | 판단 | 이유 |
|-----|------|------|
| `s4_orbit_calculator.py` | ✅ **유지 (운영 문서)** | 전체 분류 결과의 컴퓨터 검증 도구. paper.md 수식의 독립 검증 근거 |

---

## 요약

| 구분 | 파일 수 | 파일 목록 |
|-----|--------|---------|
| 🗑️ **삭제 가능** | 14개 | `IntegrationMap.md`, `FunctionSpaceTheory.md`, `PostLattice.md`, `KarnaughGeometry.md`, `ResearchOriginTimeline.md`(조건부), `NAND_universality.md`, `XOR_affine_space.md`, `Q3_constructibility_framework.md`, `Q4_function_space_structure.md`, `OQ1~OQ4`, `FQ_A~FQ_D` |
| ✅ **유지** | 14개 | `paper.md`, `README.md`, `index.html`, `TODO.md`, `SubTODO.md`, `FutureWorks.md`, `S4GroupAnalysis.md`, `CognitiveExperimentDesign.md`, `KMapVisualizationSpec.md`, `MemoryAndEducationModel.md`, `OQ5`, `FQ_E`, `FQ_F`, `s4_orbit_calculator.py` |

> **삭제 전 확인 사항:**
> - `ResearchOriginTimeline.md` — paper.md §6 개인 서술 보완 완료 후 삭제 권장
> - 삭제 전 Git commit으로 이력 보존 권장
