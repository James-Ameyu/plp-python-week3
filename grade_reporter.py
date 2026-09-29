```python
# Grade Reporter

scores = [72, 45, 90, 61, 38]

passed = 0
failed = 0
total = 0

for score in scores:
    total = total + score

    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    print(f"Score: {score}, Grade: {grade}")

    if score >= 50:
        passed = passed + 1
    else:
        failed = failed + 1

average = total / len(scores)

print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Average: {round(average, 1)}")
```

**Expected output:**

```text
Score: 72, Grade: B
Score: 45, Grade: F
Score: 90, Grade: A
Score: 61, Grade: C
Score: 38, Grade: F
Passed: 3
Failed: 2
Average: 61.2
```
