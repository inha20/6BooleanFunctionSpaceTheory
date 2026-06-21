# Integration Directive for Repository 6 — Boolean Function Space Theory

**Document status:** Formal directive — v2.0 (full rewrite, supersedes v1.0 draft)
**Repository:** 6BooleanFunctionSpaceTheory-main
**Program position:** 9th repository registered in the Structure Recognition Research Program
**Architecture:** Architecture B (Empirical Foundation Model) — Branch 8
**Resolves:** `ConsistencyAuditFindings_20260612.md`, Finding 1 / Action Item 13 — researcher decision **13-C-2** (full rewrite of the five relationship sections, not a title-only patch)
**Date:** 2026-06-20

---

## Purpose

This repository is not intended as a conventional digital logic or circuit design repository.

Its role is to extend the Structure Recognition Research Program by exploring how Boolean function spaces emerge from primitive operators (gates), and how these spaces — not just individual functions — can be recognized, classified, transformed, and visualized.

Repository 6 should be developed as an **integrated extension** of Papers 1–5, not as an isolated engineering project. Every substantive contribution should make an explicit connection back to at least one of the five repositories described below.

---

## Note on Numbering

This repository was added on 2026-06-12 as the **9th repository** in the program, after Repositories 1–5 (Papers 1–5), Research-Portfolio, ANTIGRAVITY, and inha20 already existed. Its historical folder name, `6BooleanFunctionSpaceTheory`, is preserved unchanged — existing artifact names are not renamed retroactively. However, the digit "6" in that name does **not** indicate a position in the Architecture B branch list: Branches 6 and 7 were already assigned (AI Collaboration Education; Structure-Based Elementary Mathematics) before this repository existed. Within Architecture B, this repository occupies **Branch 8**. The five sections below use "Repository 1" through "Repository 5" to mean Papers 1–5 specifically, not adjacent branch numbers — this is the source of the mismatch the v1.0 draft did not resolve (see Appendix).

---

## Relationship to Repository 1 — KMap Structure Invariance

Repository 1 established the Karnaugh map as the program's primary visualization instrument and produced its founding empirical observation: the XOR/XNOR checkerboard pattern, together with a D₄ group-theoretic proof that the 24 possible four-variable axis arrangements collapse to exactly 3 independent equivalence classes (AB/CD, AC/BD, AD/BC).

Repository 6 inherits the Karnaugh map as a shared representation surface but asks a complementary question. Repository 1 asks: *for one fixed Boolean function, which axis rearrangements leave its pattern equivalent?* Repository 6 asks: *for one fixed generating gate G, what region of the 65,536-function space — and what shared visual signature across that whole region — does Space(G) occupy?* The checkerboard Repository 1 discovered empirically turns out, in Repository 6's terms, to be the visual signature of a specific algebraic object: the affine function class Space(XOR). Repository 6's Q2/Q4 supply an algebraic explanation for a pattern Repository 1 first identified by inspection.

## Relationship to Repository 2 — Symmetric Boolean Function Minor Thesis

Repository 2 reframed the Karnaugh map from a minimization tool into a visualization of Boolean space structure, using Hamming-weight layers (L₀–L₄) to classify five visual pattern types (point, corner, ring, checkerboard, double-diagonal), and showed that the XOR checkerboard is a structural consequence of selecting odd-weight layers combined with Gray-code adjacency.

Repository 6 treats this layer-based account as one representation among several in its representation-transformation theme (truth table ↔ Karnaugh map ↔ gate network ↔ algebraic normal form ↔ function-space coordinate), and generalizes it from single functions to whole gate-generated classes: which Hamming-weight layers does Space(AND) or Space(XOR) occupy collectively, and why? As recorded in `FOLLOW_UP_ANSWERS.md` (FQ-8): Paper 1 observed the phenomenon, Paper 2 explained the mechanism, Repository 6 places it inside the algebraic (clone-theoretic) framework — a third step in the same lineage, not an unrelated one.

## Relationship to Repository 3 — Variable Rearrangement Invariance Minor Thesis

Repository 3 used S₄ permutation theory to separate what changes under variable rearrangement (visual layout, apparent symmetry axis) from what is invariant (the logical function itself, Hamming weight, the causal origin of a pattern), proposing structural invariance as the program's general analytical lens.

Repository 6 introduces a second, independent partition of the same 65,536-function domain: not "which permutation-equivalence class does f fall into" but "which gate-generated clone does f belong to." These two classification systems are orthogonal — a function's variable-rearrangement class says nothing a priori about which gate can generate it, and vice versa. Repository 6's open research direction (FQ-9) is to compute their intersection: do the 32 affine functions in Space(XOR) cluster into few or many of Repository 3's rearrangement-equivalence classes? This extends Repository 3's invariance machinery to a new classification axis rather than building a separate invariance theory from scratch.

## Relationship to Repository 4 — Structure Recognition Theory

Repository 4 is the program's theoretical hub: Structure Recognition Theory (SRT v0.3, hypotheses H1–H10) models how humans discover structure, attribute meaning, and generate research questions, including how Human-AI collaboration expands what gets noticed.

Repository 6 is a direct application domain for SRT, organized around one central hypothesis: *different Boolean functions belonging to the same gate-generated function space share recognizable structural properties.* Three SRT hypotheses are operationalized concretely here (`FOLLOW_UP_ANSWERS.md`, FQ-13–15): **H4** (research-worthiness as high information content relative to description complexity) explains why the 32 affine functions — definable by one simple algebraic condition — are disproportionately interesting; **H3** (preferential noticing of high local regularity) explains why the program's earliest observed patterns were all highly symmetric functions; **H6** (AI-expanded coverage) explains why *space-level* classification, infeasible to check by hand across 65,536 functions, is precisely where Human-AI collaboration adds the most value. Repository 6 plays the same evidentiary role for SRT that Repositories 1–3 played, in an algebraic rather than purely visual domain.

## Relationship to Repository 5 — Human-AI Research Collaboration

Repository 5 is self-referential: it studies the collaboration process that produced Papers 1–4, proposing Human-AI Research Continuity Theory (HARCT) — goal preservation, distributed cognitive architecture, reconstruction cost, and externalized memory.

Repository 6 continues this self-reference in two ways. First, its own creation is a HARCT case study: the four-document structure (`INTEGRATION_DIRECTIVE.md`, `HANDOVER.md`, `RESEARCH_NOTES.md`, `FOLLOW_UP_ANSWERS.md`) exists specifically so a future AI session can reconstruct full research context without the researcher re-explaining it — a direct application of Repository 5's Reconstruction Cost Theory and Externalized Memory concepts. Second, because Boolean function space is finite and fully enumerable (2¹⁶ = 65,536 four-variable functions), it is a natural benchmark domain for testing HARCT's division-of-labor model directly (FQ-16, FQ-17): AI performs exhaustive enumeration and algebraic verification; the researcher performs pattern recognition and research-worthiness judgment. Repository 6 is positioned to feed a concrete, documented collaboration case study back into Repository 5, extending its self-referential program rather than standing apart from it.

---

## Core Research Questions

### Q1 — Universal Gate Demonstration
Demonstrate that NAND alone can generate all 65,536 four-variable Boolean functions. Demonstrate the same for NOR. (An application of Post's Functional Completeness Theorem, with educational value through Karnaugh map visualization.)

### Q2 — Gate-Generated Function Space Characterization
For each primitive gate, determine: the size of the generated function space; the characterization of the generated class; the visual patterns these functions form on Karnaugh maps.

### Q3 — Constructibility Framework
Given a target function (e.g., 3-input AND), determine which single gate types can generate it and which cannot. Generalize into a constructibility framework — equivalent to asking whether f is contained in the clone generated by G.

### Q4 — Function Space Structure (core question)
For any primitive gate G, define: the generated function space Space(G); its closure properties; its visual characteristics on Karnaugh maps; its structural invariants.

Q1–Q3 are special cases of Q4.

---

## Long-Term Goal

Develop a theory of Boolean Function Spaces analogous to how Structure Recognition Theory studies structure spaces. The focus is not gates themselves, but the relationship between representation, generation, transformation, recognition, and function-space structure.

---

## Version History

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-06-12 | Initial informal draft — a Korean planning note with an embedded example directive. Mapped Repository 1 → "Human-AI Collaboration," Repository 3 → "Context/Knowledge Preservation," etc., which do not match the actual content of Papers 1–5. Mismatch identified in `ConsistencyAuditFindings_20260612.md`, Finding 1 / Action Item 13. |
| 2.0 | 2026-06-20 | Full rewrite of all five "Relationship to Repository N" sections per researcher decision 13-C-2 (Session 26), grounded in the actual README.md of each of Papers 1–5. Numbering conflict formally resolved (9th repository · Architecture B · Branch 8). Reformatted to match `README.md` / `HANDOVER.md` conventions. Original v1.0 text preserved below for historical reference. |

*Cross-reference: `README.md`, `HANDOVER.md`, `RESEARCH_NOTES.md`, `FOLLOW_UP_ANSWERS.md`, `ConsistencyAuditFindings_20260612.md` (Finding 1 / Action Item 13).*

---

## Appendix — Original v1.0 Draft (superseded, preserved for historical reference)

> The text below is the original 2026-06-12 planning note in unedited form. It is kept here, rather than deleted, in keeping with the program's practice of preserving discovery history. It should not be read as the active directive — see the sections above instead.

```
좋다. 지금까지의 흐름을 보면 이 리포지토리는 단순한 논리회로 문제가 아니라 네 기존 연구들과 연결해야 한다.
클로드에게 넘길 문서는 "새 연구를 기존 연구 생태계에 편입하라"는 지시문 형태가 적절하다.

[원본 예시 지시문의 Repository 1–5 매핑은 실제 Papers 1–5의 내용과 일치하지 않아
ConsistencyAuditFindings_20260612.md (Finding 1)에서 문제로 지적되었고,
연구자 결정 13-C-2에 따라 위 5개 절로 전면 재작성되었음.]

이 문서의 장점은 "논리회로 리포지토리"가 아니라 네가 이미 가지고 있는 1~5번 연구 체계 속의
응용 수학 연구 리포지토리로 위치를 고정한다는 점이야. 그러면 클로드가 이후 문서를 생성할 때도
NAND 문제만 파지 않고 기존 연구들과 연결해서 확장하게 된다.
```
