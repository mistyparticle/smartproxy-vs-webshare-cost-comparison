#!/usr/bin/env python3
"""
Smartproxy (Decodo) vs Webshare Cost Benchmark Calculator 2026.
Compares dedicated datacenter and rotating residential proxy plan tiers.
"""
import argparse

def evaluate_smartproxy_vs_webshare(ip_count, smartproxy_monthly, webshare_monthly):
    savings_monthly = smartproxy_monthly - webshare_monthly
    savings_annual = savings_monthly * 12.0
    return {
        "ip_count": ip_count,
        "smartproxy_monthly": smartproxy_monthly,
        "webshare_monthly": webshare_monthly,
        "savings_monthly": savings_monthly,
        "savings_annual": savings_annual
    }

def main():
    parser = argparse.ArgumentParser(description="Smartproxy vs Webshare Datacenter Cost Calculator")
    parser.add_argument("--ips", type=int, default=100, help="Dedicated datacenter IP count (default: 100)")
    parser.add_argument("--smartproxy-cost", type=float, default=50.00, help="Smartproxy 100-IP monthly fee (default: $50.00)")
    parser.add_argument("--webshare-cost", type=float, default=6.00, help="Webshare 100-IP monthly fee (default: $6.00)")
    args = parser.parse_args()

    res = evaluate_smartproxy_vs_webshare(args.ips, args.smartproxy_cost, args.webshare_cost)
    print(f"Dedicated IP Pool:       {res['ip_count']} IPs")
    print(f"Smartproxy Monthly:      ${res['smartproxy_monthly']:.2f}")
    print(f"Webshare Monthly:        ${res['webshare_monthly']:.2f}")
    print(f"Monthly Cost Difference: ${res['savings_monthly']:.2f}")
    print(f"Annual Projected Savings:${res['savings_annual']:.2f}")

if __name__ == "__main__":
    main()
