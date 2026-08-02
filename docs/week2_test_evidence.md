# Week 2 Test Evidence

## Test 1: High-risk alert
Input score: 90
Expected risk: high
Expected action: block_ip
Actual result: high / block_ip

## Test 2: Medium-risk alert
Input score: 50
Expected risk: medium
Expected action: manual_review
Actual result: medium / manual_review

## Test 3: Low-risk alert
Input score: 0
Expected risk: low
Expected action: no_action
Actual result: low / no_action
