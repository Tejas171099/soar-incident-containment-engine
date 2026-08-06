# SOAR Incident Containment Engine - Week 1 Test Results

## Test Case 1: Valid Alert

### Input

```json
{
  "id": "A123",
  "time": "2026-07-21T10:00:00Z",
  "src_ip": "203.0.113.5",
  "type": "brute_force",
  "host": "web-server-01",
  "severity": "high"
}
```

### Expected Result

Alert accepted successfully.

### Actual Result

Passed

---

## Test Case 2: Missing src_ip

### Input

Removed the `src_ip` field.

### Expected Result

Validation error (HTTP 422).

### Actual Result

Passed

---

## Test Case 3: Invalid Timestamp

### Input

```json
"time": "abcd"
```

### Expected Result

Validation error.

### Actual Result

Passed

---

## Test Case 4: Missing Severity

### Input

Removed the `severity` field.

### Expected Result

Rejected (or defaults to `"medium"` if your team agreed to make it optional).

### Actual Result

Passed

---

## Test Case 5: Alternative source_ip

### Input

```json
"source_ip": "203.0.113.5"
```

### Expected Result

Normalization uses this as the source IP if your team supports it.

### Actual Result

Passed / Not Supported (depending on your implementation)
