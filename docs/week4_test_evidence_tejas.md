# Week 4 Test Evidence – Tejas

## Test 1: High-Risk Brute Force
Input: score 90, brute_force → Output: high, block_ip → PASS

## Test 2: High-Risk Malware
Input: score 95, malware_detection → Output: high, isolate_host → PASS

## Test 3: Medium-Risk Suspicious Login
Input: score 55, suspicious_login → Output: medium, manual_review → PASS

## Test 4: Enrichment Failure
Input: score 0, source lookup_failed → Output: unknown, manual_review, pending → PASS