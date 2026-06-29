"""Command-line interface for QGUST."""

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="QGUST — Quantum Gravity Unified Simulation Toolkit")
    parser.add_argument("--version", action="store_true", help="Show version")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # `qgust modular` — run modular spectrum test
    mod_parser = subparsers.add_parser("modular", help="Run modular spectrum test on 2D diamond")
    mod_parser.add_argument("--N", type=int, default=200, help="Number of points")
    mod_parser.add_argument("--L", type=float, default=1.0, help="Diamond half-size")
    mod_parser.add_argument("--runs", type=int, default=5, help="Number of independent runs")
    mod_parser.add_argument("--seed", type=int, default=42, help="Random seed")
    
    # `qgust gue` — run GUE statistics test
    gue_parser = subparsers.add_parser("gue", help="Run GUE statistics test on SJ spectrum")
    gue_parser.add_argument("--N", type=int, default=200, help="Points per realization")
    gue_parser.add_argument("--runs", type=int, default=50, help="Number of independent realizations")
    gue_parser.add_argument("--L", type=float, default=1.0, help="Diamond half-size")
    gue_parser.add_argument("--seed", type=int, default=42, help="Random seed")
    
    # Parse
    args = parser.parse_args()
    
    if args.version:
        from . import __version__
        print(f"qgust v{__version__}")
        return
    
    if args.command == "modular":
        from .core.modular import analyze_diamond
        from .core.causal_set import CausalSet
        import numpy as np
        import math
        
        rng = np.random.default_rng(args.seed)
        all_results = []
        
        for run_i in range(args.runs):
            seed_i = rng.integers(0, 2**31)
            cs_rng = np.random.default_rng(seed_i)
            cs = CausalSet.sprinkle_diamond_2d(args.N, args.L, rng=cs_rng)
            
            # Spatial split at x=0
            R_idx, _ = cs.split_by_coordinate(coord_idx=1, threshold=0.0)
            
            if len(R_idx) < 10:
                print(f"  Run {run_i+1}: too few points in R (n={len(R_idx)}), skipping")
                continue
            
            result = analyze_diamond(cs, R_idx, label=f"run {run_i+1}")
            all_results.append(result)
        
        if all_results:
            S_vals = [r["S_total"] for r in all_results]
            br_vals = [r["beta_ratio"] for r in all_results if not math.isnan(r["beta_ratio"])]
            import math
            print(f"\nSummary ({len(all_results)} runs):")
            print(f"  S     = {np.mean(S_vals):.4f} ± {np.std(S_vals):.4f}")
            if br_vals:
                print(f"  β₂/β₁ = {np.mean(br_vals):.4f} ± {np.std(br_vals):.4f}")
            print(f"  LQG ref = 1.633, U(1) ref = 2.0, flat ref = 1.0")
    
    elif args.command == "gue":
        from .pred3_gue_statistics.run import run_test
        
        result = run_test(N=args.N, n_realizations=args.runs, seed=args.seed)
    
    else:
        parser.print_help()
