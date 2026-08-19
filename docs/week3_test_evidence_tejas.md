# Week 3 Test Evidence – Tejas

## Test 1: High-Risk Brute Force

### Input

- Alert Type: `brute_force`
- Reputation Score: `90`

### Expected Result

- Risk Level: `high`
- Recommended Action: `block_ip`

### Result

To be verified after running tests.

---

## Test 2: High-Risk Malware Detection

### Input

- Alert Type: `malware_detection`
- Reputation Score: `95`

### Expected Result

- Risk Level: `high`
- Recommended Action: `isolate_host`

### Result

To be verified after running tests.

---

## Test 3: Medium-Risk Suspicious Login

### Input

- Alert Type: `suspicious_login`
- Reputation Score: `55`

### Expected Result

- Risk Level: `medium`
- Recommended Action: `manual_review`

### Result

To be verified after running tests.

---

## Test 4: Enrichment Failure

### Input

- Alert Type: `brute_force`
- Reputation Score: `0`
- Source: `lookup_failed`

### Expected Result

- Risk Level: `unknown`
- Recommended Action: `manual_review`
- Action Status: `pending`

### Result

To be verified after running tests.
