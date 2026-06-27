"""
s4_orbit_calculator.py
======================
S₄ Orbit Calculator for 4-Variable Boolean Function Spaces
Structure Recognition Research Program — Repo 6: BooleanFunctionSpaceTheory

목적:
    4변수 Boolean 함수 공간 (Space(XOR), Space(AND), Space(NOT), L∩M)에 대해
    S₄ 군 작용 하의 궤도(orbit)를 완전 열거하고, Burnside 보조정리로 검증한다.

사용법:
    python s4_orbit_calculator.py                # 전체 결과 출력
    python s4_orbit_calculator.py --space XOR    # 특정 공간만 분석
    python s4_orbit_calculator.py --verify       # 결과 검증만 수행

의존성:
    Python 3.8+, 표준 라이브러리만 사용 (외부 패키지 불필요)

결과 검증 기준 (theory/S4GroupAnalysis.md v1.2):
    Space(XOR) : 32개 함수 → 10개 궤도
    Space(AND) : 168개 함수 → 30개 궤도
    Space(NOT) : 256개 함수 → 32개 궤도
    L ∩ M      : 6개 함수  → 3개 궤도

작성일: 2026-06-23
저장소: 6BooleanFunctionSpaceTheory
관련 문서: theory/S4GroupAnalysis.md
"""

import sys
import itertools
from collections import defaultdict
from typing import FrozenSet, List, Set, Tuple, Dict


# ─────────────────────────────────────────────────────────────────────────────
# 0. 기본 설정 및 상수
# ─────────────────────────────────────────────────────────────────────────────

N_VARS = 4                     # 변수 개수 (A, B, C, D)
N_INPUTS = 2 ** N_VARS         # 입력 조합 수 = 16
N_FUNCTIONS = 2 ** N_INPUTS    # 전체 함수 수 = 65,536
VAR_NAMES = ['A', 'B', 'C', 'D']

# 모든 입력 조합 (0000 ~ 1111), 각각 길이 4의 튜플
ALL_INPUTS: List[Tuple[int, ...]] = list(itertools.product([0, 1], repeat=N_VARS))

# Boolean 함수 표현: int (0~65535)
# 비트 i는 입력 ALL_INPUTS[i]에 대한 출력값 (LSB = ALL_INPUTS[0])
# 즉 f(ALL_INPUTS[i]) = (func_int >> i) & 1


# ─────────────────────────────────────────────────────────────────────────────
# 1. 함수 유틸리티
# ─────────────────────────────────────────────────────────────────────────────

def evaluate(func_int: int, input_tuple: Tuple[int, ...]) -> int:
    """함수 func_int를 주어진 입력에서 평가한다."""
    idx = ALL_INPUTS.index(input_tuple)
    return (func_int >> idx) & 1


def func_to_table(func_int: int) -> List[int]:
    """진리표 벡터 반환 (인덱스 0~15에 대한 출력값 리스트)."""
    return [(func_int >> i) & 1 for i in range(N_INPUTS)]


def table_to_func(table: List[int]) -> int:
    """진리표 벡터를 정수로 변환."""
    result = 0
    for i, bit in enumerate(table):
        result |= (bit << i)
    return result


def func_name(func_int: int) -> str:
    """함수를 간략한 이름으로 표현 (진리표 hex)."""
    return f"f[{func_int:04X}]"


def func_description(func_int: int) -> str:
    """진리표를 바이너리 문자열로 표현 (MSB = 입력 1111)."""
    bits = ''.join(str((func_int >> i) & 1) for i in range(N_INPUTS - 1, -1, -1))
    return f"0b{bits}"


# ─────────────────────────────────────────────────────────────────────────────
# 2. S₄ 군 및 켤레류 정의
# ─────────────────────────────────────────────────────────────────────────────

def apply_permutation(func_int: int, perm: Tuple[int, ...]) -> int:
    """
    순열 perm을 함수 func_int에 적용한다.
    perm[i] = j 는 "원래 변수 i번이 j번으로 이동"을 의미.
    (σ·f)(x₀,x₁,x₂,x₃) = f(x_{perm[0]}, x_{perm[1]}, x_{perm[2]}, x_{perm[3]})
    
    즉 입력의 변수를 perm에 따라 재배열한다.
    """
    result_table = []
    for inp in ALL_INPUTS:
        # 순열 적용: perm이 [1,0,2,3]이면 (A,B,C,D) → (B,A,C,D)
        permuted_inp = tuple(inp[perm[i]] for i in range(N_VARS))
        permuted_idx = ALL_INPUTS.index(permuted_inp)
        result_table.append((func_int >> permuted_idx) & 1)
    return table_to_func(result_table)


def generate_s4() -> List[Tuple[int, ...]]:
    """S₄의 모든 24개 원소(순열)를 생성한다."""
    return list(itertools.permutations(range(N_VARS)))


def get_conjugacy_classes() -> Dict[str, List[Tuple[int, ...]]]:
    """
    S₄의 5개 켤레류를 반환한다.
    각 켤레류는 대표원 리스트로 표현.
    """
    s4 = generate_s4()
    classes = {
        'identity':      [],   # 항등원 (1개)
        'transposition': [],   # 호환 (6개)
        '3-cycle':       [],   # 3-순환 (8개)
        '4-cycle':       [],   # 4-순환 (6개)
        'double_trans':  [],   # 이중 호환 (3개)
    }
    
    for perm in s4:
        cycle_type = get_cycle_type(perm)
        if cycle_type == (1, 1, 1, 1):
            classes['identity'].append(perm)
        elif cycle_type == (2, 1, 1):
            classes['transposition'].append(perm)
        elif cycle_type == (3, 1):
            classes['3-cycle'].append(perm)
        elif cycle_type == (4,):
            classes['4-cycle'].append(perm)
        elif cycle_type == (2, 2):
            classes['double_trans'].append(perm)
    
    return classes


def get_cycle_type(perm: Tuple[int, ...]) -> Tuple[int, ...]:
    """순열의 순환 분해를 정렬된 튜플로 반환한다 (내림차순)."""
    visited = [False] * len(perm)
    cycle_lengths = []
    for start in range(len(perm)):
        if not visited[start]:
            cycle_len = 0
            current = start
            while not visited[current]:
                visited[current] = True
                current = perm[current]
                cycle_len += 1
            cycle_lengths.append(cycle_len)
    return tuple(sorted(cycle_lengths, reverse=True))


# ─────────────────────────────────────────────────────────────────────────────
# 3. Boolean 함수 공간 생성
# ─────────────────────────────────────────────────────────────────────────────

def generate_affine_functions() -> Set[int]:
    """
    Space(XOR) = 아핀(Affine) 함수 집합 생성.
    f(A,B,C,D) = a0 ⊕ a1·A ⊕ a2·B ⊕ a3·C ⊕ a4·D  (ai ∈ {0,1})
    총 2^5 = 32개
    """
    affine_funcs = set()
    for a0, a1, a2, a3, a4 in itertools.product([0, 1], repeat=5):
        table = []
        for inp in ALL_INPUTS:
            A, B, C, D = inp
            output = a0 ^ (a1 & A) ^ (a2 & B) ^ (a3 & C) ^ (a4 & D)
            table.append(output)
        affine_funcs.add(table_to_func(table))
    return affine_funcs


def generate_monotone_functions() -> Set[int]:
    """
    Space(AND) = 단조(Monotone) 함수 집합 생성.
    f가 단조 ⟺ x ≤ y (점별) → f(x) ≤ f(y)
    전수 열거: 65536개 함수 중 단조인 것 필터링
    기대 개수: D(4) = 168 (Dedekind 수)
    """
    monotone_funcs = set()
    for func_int in range(N_FUNCTIONS):
        if is_monotone(func_int):
            monotone_funcs.add(func_int)
    return monotone_funcs


def is_monotone(func_int: int) -> bool:
    """함수가 단조인지 확인한다."""
    for i, x in enumerate(ALL_INPUTS):
        for j, y in enumerate(ALL_INPUTS):
            # x ≤ y (점별) 이면 f(x) ≤ f(y)
            if all(x[k] <= y[k] for k in range(N_VARS)):
                fx = (func_int >> i) & 1
                fy = (func_int >> j) & 1
                if fx > fy:
                    return False
    return True


def generate_self_dual_functions() -> Set[int]:
    """
    Space(NOT) = 자기쌍대(Self-dual) 함수 집합 생성.
    f 자기쌍대 ⟺ f(x) = ¬f(¬x) for all x
    기대 개수: 2^8 = 256
    """
    self_dual_funcs = set()
    for func_int in range(N_FUNCTIONS):
        if is_self_dual(func_int):
            self_dual_funcs.add(func_int)
    return self_dual_funcs


def is_self_dual(func_int: int) -> bool:
    """함수가 자기쌍대인지 확인한다."""
    for i, x in enumerate(ALL_INPUTS):
        # ¬x = 비트 반전
        neg_x = tuple(1 - xi for xi in x)
        neg_x_idx = ALL_INPUTS.index(neg_x)
        fx = (func_int >> i) & 1
        f_neg_x = (func_int >> neg_x_idx) & 1
        if fx == f_neg_x:   # f(x) ≠ ¬f(¬x) → ¬f(¬x) = 1-f(¬x) 이어야
            return False
    return True


def generate_affine_monotone_intersection(
    affine: Set[int], monotone: Set[int]
) -> Set[int]:
    """L ∩ M = 아핀이면서 단조인 함수 집합."""
    return affine & monotone


# ─────────────────────────────────────────────────────────────────────────────
# 4. 궤도 계산 및 Burnside 적용
# ─────────────────────────────────────────────────────────────────────────────

def compute_orbits(space: Set[int], s4: List[Tuple[int, ...]]) -> List[FrozenSet[int]]:
    """
    주어진 함수 공간에서 S₄ 작용 하의 궤도들을 반환한다.
    Union-Find를 사용하지 않고 BFS 방식으로 각 궤도를 탐색.
    """
    remaining = set(space)
    orbits = []
    while remaining:
        start = min(remaining)  # 재현성을 위해 최솟값 선택
        orbit = set()
        queue = [start]
        while queue:
            f = queue.pop()
            if f in orbit:
                continue
            orbit.add(f)
            for perm in s4:
                pf = apply_permutation(f, perm)
                if pf in space and pf not in orbit:
                    queue.append(pf)
        orbits.append(frozenset(orbit))
        remaining -= orbit
    return sorted(orbits, key=lambda o: (len(o), min(o)))


def compute_burnside(
    space: Set[int],
    conj_classes: Dict[str, List[Tuple[int, ...]]]
) -> int:
    """
    Burnside의 보조정리로 궤도 수를 계산한다.
    |Orbits| = (1/|S₄|) × Σ_{σ∈S₄} |Fix(σ, Space)|
    """
    total_fix = 0
    class_info = {}
    
    for class_name, perms in conj_classes.items():
        if not perms:
            continue
        # 켤레류 내 한 대표원에 대해 Fix 계산
        rep = perms[0]
        fix_count = sum(
            1 for f in space if apply_permutation(f, rep) == f
        )
        total_fix += len(perms) * fix_count
        class_info[class_name] = (len(perms), fix_count, len(perms) * fix_count)
    
    return total_fix // 24, class_info


# ─────────────────────────────────────────────────────────────────────────────
# 5. 함수 명칭 및 설명 생성
# ─────────────────────────────────────────────────────────────────────────────

KNOWN_FUNCTIONS = {
    # 상수
    0x0000: "0 (상수 0)",
    0xFFFF: "1 (상수 1)",
    # 단일 변수 투영
    0x00FF: "A",
    0x0F0F: "B",
    0x3333: "C",
    0x5555: "D",
    # 보수
    0xFF00: "¬A",
    0xF0F0: "¬B",
    0xCCCC: "¬C",
    0xAAAA: "¬D",
    # XOR 체커보드
    0x6996: "A⊕B⊕C⊕D (체커보드)",
    0x9669: "¬(A⊕B⊕C⊕D) (체커보드 보수)",
    # AND
    0x0001: "A∧B∧C∧D",
    0x0101: "A∧B∧C",
    0x0303: "A∧B",
    0x0F0F & 0x00FF: None,  # placeholder
    0x1111: "A∧D",
    0x0055: "A∧B (= f[0055])",  # 다를 수 있음
    # OR
    0xFFFE: "A∨B∨C∨D",
    0xFEFE: "A∨B∨C",
    0xFCFC: "A∨B",
    # 임계값 함수
    0x7FFF & 0xFFFF: None,  # placeholder
    # XOR 변형
    0x0FF0: "A⊕B",
    0x00F0: "A⊕B⊕C",  # 재확인 필요
}

def get_function_label(func_int: int) -> str:
    """알려진 함수에 대해 의미 있는 라벨을 반환한다."""
    # 상수
    if func_int == 0:
        return "f=0"
    if func_int == 0xFFFF:
        return "f=1"
    
    table = func_to_table(func_int)
    
    # 단일 변수 투영
    for i, var in enumerate(VAR_NAMES):
        proj_table = [ALL_INPUTS[j][i] for j in range(N_INPUTS)]
        if table == proj_table:
            return var
    
    # XOR 체커보드 계열
    xor_all_table = [
        sum(ALL_INPUTS[j]) % 2 for j in range(N_INPUTS)
    ]
    if table == xor_all_table:
        return "A⊕B⊕C⊕D"
    if table == [1 - b for b in xor_all_table]:
        return "A⊕B⊕C⊕D⊕1"
    
    # 2변수 XOR
    for i, j in itertools.combinations(range(N_VARS), 2):
        xor_table = [ALL_INPUTS[k][i] ^ ALL_INPUTS[k][j] for k in range(N_INPUTS)]
        if table == xor_table:
            return f"{VAR_NAMES[i]}⊕{VAR_NAMES[j]}"
        if table == [1-b for b in xor_table]:
            return f"{VAR_NAMES[i]}⊕{VAR_NAMES[j]}⊕1"
    
    # 3변수 XOR
    for combo in itertools.combinations(range(N_VARS), 3):
        xor3_table = [
            sum(ALL_INPUTS[k][i] for i in combo) % 2 for k in range(N_INPUTS)
        ]
        if table == xor3_table:
            return "⊕".join(VAR_NAMES[i] for i in combo)
        if table == [1-b for b in xor3_table]:
            return "⊕".join(VAR_NAMES[i] for i in combo) + "⊕1"
    
    # AND 계열
    for r in range(1, N_VARS + 1):
        for combo in itertools.combinations(range(N_VARS), r):
            and_table = [
                1 if all(ALL_INPUTS[k][i] == 1 for i in combo) else 0
                for k in range(N_INPUTS)
            ]
            if table == and_table:
                return "∧".join(VAR_NAMES[i] for i in combo)
    
    # OR 계열
    for r in range(1, N_VARS + 1):
        for combo in itertools.combinations(range(N_VARS), r):
            or_table = [
                1 if any(ALL_INPUTS[k][i] == 1 for i in combo) else 0
                for k in range(N_INPUTS)
            ]
            if table == or_table:
                return "∨".join(VAR_NAMES[i] for i in combo)
    
    # 임계값 함수 (Hamming weight ≥ k)
    for k in range(N_VARS + 1):
        thresh_table = [
            1 if sum(ALL_INPUTS[j]) >= k else 0 for j in range(N_INPUTS)
        ]
        if table == thresh_table:
            return f"Threshold-{k} (HW≥{k})"
    
    # 알 수 없는 함수
    return f"f[{func_int:04X}]"


# ─────────────────────────────────────────────────────────────────────────────
# 6. 메인 분석 함수
# ─────────────────────────────────────────────────────────────────────────────

def analyze_space(name: str, space: Set[int], expected_orbits: int, verbose: bool = True):
    """주어진 공간을 분석하고 결과를 출력한다."""
    s4 = generate_s4()
    conj_classes = get_conjugacy_classes()
    
    # 궤도 열거
    orbits = compute_orbits(space, s4)
    
    # Burnside 검증
    burnside_count, class_info = compute_burnside(space, conj_classes)
    
    # S₄-불동점 찾기
    s4_fixed = {f for f in space if all(apply_permutation(f, perm) == f for perm in s4)}
    
    if verbose:
        print(f"\n{'='*70}")
        print(f"  공간: Space({name})")
        print(f"{'='*70}")
        print(f"  함수 수         : {len(space):,}")
        print(f"  궤도 수 (열거)   : {len(orbits)}")
        print(f"  궤도 수 (Burnside): {burnside_count}")
        print(f"  기대 궤도 수     : {expected_orbits}")
        
        status = "✅ 일치" if (len(orbits) == expected_orbits == burnside_count) else "❌ 불일치"
        print(f"  검증 결과        : {status}")
        
        print(f"\n  ── Burnside 계산 상세 ──")
        print(f"  {'켤레류':<20} {'원소수':>5} {'Fix':>8} {'기여':>10}")
        print(f"  {'-'*50}")
        class_order = ['identity', 'transposition', '3-cycle', '4-cycle', 'double_trans']
        class_labels = {
            'identity': '항등원',
            'transposition': '호환',
            '3-cycle': '3-순환',
            '4-cycle': '4-순환',
            'double_trans': '이중 호환',
        }
        total = 0
        for cls in class_order:
            if cls in class_info:
                n, fix, contrib = class_info[cls]
                total += contrib
                print(f"  {class_labels[cls]:<20} {n:>5} {fix:>8} {contrib:>10}")
        print(f"  {'-'*50}")
        print(f"  {'합계 / 24':<20} {'24':>5} {total:>8} → {total}÷24 = {total//24}")
        
        print(f"\n  ── S₄-불동점 ({len(s4_fixed)}개) ──")
        for f in sorted(s4_fixed):
            print(f"    {get_function_label(f):<35} [{func_description(f)}]")
        
        print(f"\n  ── 궤도 목록 ({len(orbits)}개) ──")
        print(f"  {'#':>3} {'크기':>5}  대표 함수")
        print(f"  {'-'*50}")
        for i, orbit in enumerate(orbits, 1):
            rep = min(orbit)
            label = get_function_label(rep)
            fixed_mark = " ◆" if rep in s4_fixed else ""
            print(f"  {i:>3}   [{len(orbit):>3}]  {label}{fixed_mark}")
        
        # 크기별 분포
        size_dist = defaultdict(int)
        for orbit in orbits:
            size_dist[len(orbit)] += 1
        print(f"\n  ── 궤도 크기 분포 ──")
        total_funcs = 0
        for size in sorted(size_dist):
            count = size_dist[size]
            subtotal = size * count
            total_funcs += subtotal
            print(f"    크기 {size:>3}: {count:>3}개 궤도 × {size:>3} = {subtotal:>5}")
        print(f"    {'합계':>8}: {'':>3}      {'':>5}   {total_funcs:>5} ({'✅' if total_funcs == len(space) else '❌'})")
    
    return orbits, burnside_count, s4_fixed


def run_all_analyses(verbose: bool = True) -> bool:
    """모든 공간에 대한 분석을 실행하고 최종 검증 결과를 반환한다."""
    print("="*70)
    print("  S₄ Orbit Calculator — Structure Recognition Research Program")
    print("  Repo 6: BooleanFunctionSpaceTheory")
    print("  이론 기준: theory/S4GroupAnalysis.md v1.2")
    print("="*70)
    
    # 공간 생성
    print("\n[생성 중] 함수 공간 생성...")
    affine = generate_affine_functions()
    print(f"  Space(XOR) : {len(affine)}개 생성 완료")
    monotone = generate_monotone_functions()
    print(f"  Space(AND) : {len(monotone)}개 생성 완료")
    self_dual = generate_self_dual_functions()
    print(f"  Space(NOT) : {len(self_dual)}개 생성 완료")
    lm = generate_affine_monotone_intersection(affine, monotone)
    print(f"  L ∩ M      : {len(lm)}개 생성 완료")
    
    # 크기 검증
    size_checks = [
        (len(affine),   32,  "Space(XOR) 크기"),
        (len(monotone), 168, "Space(AND) 크기 [Dedekind D(4)]"),
        (len(self_dual),256, "Space(NOT) 크기 [2^8]"),
        (len(lm),       6,   "L∩M 크기"),
    ]
    print("\n[검증] 함수 공간 크기 확인:")
    all_ok = True
    for actual, expected, label in size_checks:
        ok = actual == expected
        if not ok:
            all_ok = False
        print(f"  {label:<35} {actual:>5} == {expected:<5} {'✅' if ok else '❌'}")
    
    # 각 공간 분석
    results = {}
    spaces = [
        ("XOR (아핀)",        affine,    10),
        ("AND (단조)",        monotone,  30),
        ("NOT (자기쌍대)",    self_dual, 32),
        ("L∩M (아핀∧단조)",   lm,         3),
    ]
    
    for name, space, expected in spaces:
        orbits, burnside, fixed = analyze_space(name, space, expected, verbose)
        results[name] = {
            'orbits_enum': len(orbits),
            'orbits_burn': burnside,
            'expected':    expected,
            'fixed':       len(fixed),
            'ok':          (len(orbits) == expected == burnside),
        }
    
    # 최종 요약
    print(f"\n{'='*70}")
    print("  최종 검증 요약")
    print(f"{'='*70}")
    print(f"  {'공간':<25} {'열거':>6} {'Burnside':>9} {'기대':>6} {'결과':>6}")
    print(f"  {'-'*55}")
    overall = True
    for name, res in results.items():
        ok = res['ok']
        overall = overall and ok
        print(
            f"  {name:<25} {res['orbits_enum']:>6} {res['orbits_burn']:>9} "
            f"{res['expected']:>6} {'✅' if ok else '❌'}"
        )
    print(f"  {'-'*55}")
    print(f"  {'전체 검증':>55} {'✅ 통과' if overall else '❌ 실패'}")
    print(f"\n  참고 문서: theory/S4GroupAnalysis.md v1.2 (OC-1~OC-5)")
    print(f"{'='*70}\n")
    
    return overall


# ─────────────────────────────────────────────────────────────────────────────
# 7. n=5 확장 — 이론적 스캐폴드 (2026-06-27 FR-3 실제 계산으로 검증 완료)
# ─────────────────────────────────────────────────────────────────────────────

def scaffold_n5_affine():
    """
    n=5 변수 아핀 함수에 대한 S₅-궤도 분석 이론적 스캐폴드.
    Burnside 이론 계산 경로 제시 + 실제 열거 계산으로 검증 완료.
    
    아핀 함수 수: 2^(5+1) = 64개
    검증 결과 (2026-06-27 FR-3): Space(XOR)_n5 = 12궤도 ✅
    """
    print("\n" + "="*70)
    print("  n=5 이론적 스캐폴드 (Space(XOR), S₅ 작용) — 검증 완료")
    print("="*70)
    print("""
  5변수 아핀 함수: f(A,B,C,D,E) = a₀ ⊕ a₁A ⊕ a₂B ⊕ a₃C ⊕ a₄D ⊕ a₅E
  계수 벡터: (a₀,...,a₅) ∈ {0,1}^6 → 총 2^6 = 64개

  S₅의 켤레류 (순환 타입과 원소 수):
  ┌──────────────┬───────┬─────────────────────────────────────┐
  │ 순환 타입     │ 원소수 │ Fix(σ, L₅) 계산 원리                │
  ├──────────────┼───────┼─────────────────────────────────────┤
  │ (1⁵) 항등원  │   1   │ 6개 자유 계수 → Fix = 2^6 = 64       │
  │ (2,1³) 호환  │  10   │ 한 쌍 동일 조건: 5개 자유 → Fix = 2^5 = 32 │
  │ (3,1²) 3-순환│  20   │ 세 변수 동일: 4개 자유 → Fix = 2^4 = 16   │
  │ (4,1) 4-순환 │  30   │ 네 변수 동일: 3개 자유 → Fix = 2^3 = 8    │
  │ (5) 5-순환   │  24   │ 다섯 변수 모두 동일: 2개 자유 → Fix = 2^2 = 4 │
  │ (2²,1) 이중호환│ 15  │ 두 쌍 각각 동일: 4개 자유 → Fix = 2^4 = 16 │
  │ (3,2) 3+2순환│  20   │ 3-궤도+2-궤도: 3개 자유 → Fix = 2^3 = 8  │
  └──────────────┴───────┴─────────────────────────────────────┘

  Burnside 계산:
    합계 = (1×64) + (10×32) + (20×16) + (30×8) + (24×4) + (15×16) + (20×8)
         = 64 + 320 + 320 + 240 + 96 + 240 + 160
         = 1440
    궤도 수 = 1440 / |S₅| = 1440 / 120 = 12

  ✅ 검증 완료 (2026-06-27 FR-3 실제 열거):
    Space(XOR)_n5: 64개 함수 → 12궤도 (Burnside 이론값과 일치)
    Space(AND)_n5: 7581개 함수 → 210궤도 (열거↔Burnside 일치)
    Space(XOR)_n5 S₅-불동점: 4개 (f=0, A⊕B⊕C⊕D⊕E, 보수, f=1)
    Space(XOR)_n5 궤도 크기 분포: 크기1×4개, 크기5×4개, 크기10×4개

  n=4 vs n=5 비교:
    Space(XOR): n=4 → 10궤도, n=5 → 12궤도
    Space(AND): n=4 → 30궤도, n=5 → 210궤도 (Dedekind 수 급증 반영)

  실제 계산을 실행하려면: python s4_orbit_calculator.py --n5-compute
  (Space(AND)_n5 열거에 약 60초 소요)
""")


# ─────────────────────────────────────────────────────────────────────────────
# 8. n=5 완전 계산 함수 (FR-3, 2026-06-27 추가)
# ─────────────────────────────────────────────────────────────────────────────

_N5 = 5
_ALL_INPUTS_5 = list(itertools.product([0, 1], repeat=_N5))


def _table_to_func_n5(table):
    result = 0
    for i, bit in enumerate(table):
        result |= (bit << i)
    return result


def _apply_perm_n5(func_int, perm):
    result_table = []
    for inp in _ALL_INPUTS_5:
        permuted = tuple(inp[perm[i]] for i in range(_N5))
        idx = _ALL_INPUTS_5.index(permuted)
        result_table.append((func_int >> idx) & 1)
    return _table_to_func_n5(result_table)


def _compute_orbits_n5(space, s5):
    remaining = set(space)
    orbits = []
    while remaining:
        start = min(remaining)
        orbit = set()
        queue = [start]
        while queue:
            f = queue.pop()
            if f in orbit:
                continue
            orbit.add(f)
            for perm in s5:
                pf = _apply_perm_n5(f, perm)
                if pf in space and pf not in orbit:
                    queue.append(pf)
        orbits.append(frozenset(orbit))
        remaining -= orbit
    return sorted(orbits, key=lambda o: (len(o), min(o)))


def _burnside_n5(space, s5):
    total = sum(1 for perm in s5 for f in space if _apply_perm_n5(f, perm) == f)
    return total // len(s5)


def _generate_n5_affine():
    """5변수 아핀 함수 64개 생성"""
    funcs = set()
    for coeffs in itertools.product([0, 1], repeat=_N5 + 1):
        table = []
        for inp in _ALL_INPUTS_5:
            val = coeffs[0]
            for k in range(_N5):
                val ^= (coeffs[k + 1] & inp[k])
            table.append(val)
        funcs.add(_table_to_func_n5(table))
    return funcs


def _generate_n5_monotone():
    """
    5변수 단조 함수 7581개 생성 (Dedekind D(5)).
    백트래킹: 해밍 무게 순서로 입력을 처리하며 단조성 제약 적용.
    """
    sorted_inputs = sorted(range(32), key=lambda i: bin(i).count('1'))
    predecessors = {}
    for i, idx in enumerate(sorted_inputs):
        preds = []
        a = _ALL_INPUTS_5[idx]
        for j in range(i):
            pred_idx = sorted_inputs[j]
            b = _ALL_INPUTS_5[pred_idx]
            if all(b[k] <= a[k] for k in range(_N5)) and pred_idx != idx:
                preds.append(pred_idx)
        predecessors[idx] = preds

    monotone_funcs = set()
    assignment = [None] * 32

    def backtrack(pos):
        if pos == 32:
            monotone_funcs.add(_table_to_func_n5([assignment[i] for i in range(32)]))
            return
        idx = sorted_inputs[pos]
        min_val = 1 if any(assignment[p] == 1 for p in predecessors[idx]) else 0
        for val in range(min_val, 2):
            assignment[idx] = val
            backtrack(pos + 1)
            assignment[idx] = None

    backtrack(0)
    return monotone_funcs


def run_n5_full_analysis():
    """
    n=5 Space(XOR)와 Space(AND)의 S₅-궤도를 실제로 열거하고 검증한다.
    FR-3 후속 연구 — 2026-06-27 추가.
    주의: Space(AND)_n5 열거에 약 60초 소요.
    """
    import time
    s5 = list(itertools.permutations(range(_N5)))
    print("\n" + "="*70)
    print("  n=5 완전 계산 — FR-3 (2026-06-27)")
    print("="*70)
    print(f"  |S₅| = {len(s5)}")

    # Space(XOR)_n5
    print("\n[1/2] Space(XOR)_n5 — 5변수 아핀 함수")
    aff5 = _generate_n5_affine()
    print(f"  함수 수: {len(aff5)} (기대: 64)")
    orbs_xor = _compute_orbits_n5(aff5, s5)
    burn_xor  = _burnside_n5(aff5, s5)
    ok_xor = len(orbs_xor) == burn_xor == 12
    print(f"  궤도 수 (열거): {len(orbs_xor)}  (Burnside): {burn_xor}  {'✅' if ok_xor else '❌'}")
    size_dist = defaultdict(int)
    for o in orbs_xor: size_dist[len(o)] += 1
    for sz in sorted(size_dist):
        print(f"    크기 {sz:>3}: {size_dist[sz]:>2}개 궤도")
    fixed5 = [f for f in aff5 if all(_apply_perm_n5(f, p) == f for p in s5)]
    print(f"  S₅-불동점: {len(fixed5)}개")

    # Space(AND)_n5
    print("\n[2/2] Space(AND)_n5 — 5변수 단조 함수 (D(5)=7581)")
    print("  단조 함수 생성 중... ", end='', flush=True)
    t0 = time.time()
    mono5 = _generate_n5_monotone()
    print(f"완료 ({time.time()-t0:.1f}초)")
    print(f"  함수 수: {len(mono5)} {'✅' if len(mono5)==7581 else '❌'}")
    print("  궤도 열거 중... ", end='', flush=True)
    t1 = time.time()
    orbs_and = _compute_orbits_n5(mono5, s5)
    burn_and  = _burnside_n5(mono5, s5)
    print(f"완료 ({time.time()-t1:.1f}초)")
    ok_and = len(orbs_and) == burn_and
    print(f"  궤도 수 (열거): {len(orbs_and)}  (Burnside): {burn_and}  {'✅' if ok_and else '❌'}")
    size_dist2 = defaultdict(int)
    for o in orbs_and: size_dist2[len(o)] += 1
    for sz in sorted(size_dist2):
        print(f"    크기 {sz:>4}: {size_dist2[sz]:>3}개 궤도")

    print("\n" + "="*70)
    print("  최종 요약")
    print("="*70)
    print(f"  {'공간':<25} {'함수 수':>8} {'S₅-궤도 수':>12}")
    print(f"  {'-'*50}")
    print(f"  {'Space(XOR)_n5':<25} {len(aff5):>8} {len(orbs_xor):>12}")
    print(f"  {'Space(AND)_n5':<25} {len(mono5):>8} {len(orbs_and):>12}")
    print(f"\n  n=4: Space(XOR)=10궤도, Space(AND)=30궤도")
    print(f"  n=5: Space(XOR)={len(orbs_xor)}궤도, Space(AND)={len(orbs_and)}궤도")
    print("="*70)


# ─────────────────────────────────────────────────────────────────────────────
# 9. 진입점
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    args = sys.argv[1:]
    
    if '--n5-compute' in args:
        run_n5_full_analysis()
    elif '--n5' in args:
        scaffold_n5_affine()
    elif '--verify' in args:
        # 간소화된 검증만 수행 (출력 억제)
        print("간소화 검증 모드...")
        affine = generate_affine_functions()
        monotone = generate_monotone_functions()
        self_dual = generate_self_dual_functions()
        lm = affine & monotone
        s4 = generate_s4()
        conj_classes = get_conjugacy_classes()
        
        checks = [
            ("Space(XOR)",  affine,    10),
            ("Space(AND)",  monotone,  30),
            ("Space(NOT)",  self_dual, 32),
            ("L∩M",         lm,         3),
        ]
        all_ok = True
        for name, space, expected in checks:
            orbits = compute_orbits(space, s4)
            ok = len(orbits) == expected
            all_ok = all_ok and ok
            print(f"  {name:<15}: {len(orbits):>3}궤도 (기대 {expected}) {'✅' if ok else '❌'}")
        
        print(f"\n전체: {'✅ 모두 통과' if all_ok else '❌ 일부 실패'}")
        sys.exit(0 if all_ok else 1)
    elif '--space' in args:
        idx = args.index('--space')
        if idx + 1 < len(args):
            target = args[idx + 1].upper()
            affine = generate_affine_functions()
            monotone = generate_monotone_functions()
            self_dual = generate_self_dual_functions()
            lm = affine & monotone
            space_map = {
                'XOR': (affine,    10, "XOR (아핀)"),
                'AND': (monotone,  30, "AND (단조)"),
                'NOT': (self_dual, 32, "NOT (자기쌍대)"),
                'LM':  (lm,         3, "L∩M (아핀∧단조)"),
            }
            if target in space_map:
                space, expected, label = space_map[target]
                analyze_space(label, space, expected, verbose=True)
            else:
                print(f"알 수 없는 공간: {target}. XOR / AND / NOT / LM 중 하나를 선택하세요.")
        else:
            print("사용법: python s4_orbit_calculator.py --space [XOR|AND|NOT|LM]")
    else:
        # 기본: 전체 분석
        success = run_all_analyses(verbose=True)
        scaffold_n5_affine()
        sys.exit(0 if success else 1)
