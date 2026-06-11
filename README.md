# LeetCode Python Solutions: Math & Strings

Welcome to my repository containing clean, optimized, and thoroughly tested solutions for algorithmic problems. 

Instead of just writing raw functions, every solution here is built as an independent script featuring its own **isolated test suite**. This allows you to clone the repository and verify the logic locally right out of the box.

---

## 🛠️ Solutions Included

### 1. Reverse Integer (LeetCode 7 - Medium)
* **File:** `reverse_integer.py`
* **Core Concepts:** 32-bit integer boundaries, sign preservation, overflow emulation.
* **Overview:** Reverses the digits of a signed 32-bit integer. The algorithm strictly adheres to the constraint of not utilizing 64-bit integer types by validating boundaries mathematically before finishing execution.

### 2. String to Integer / atoi (LeetCode 8 - Medium)
* **File:** `string_to_integer_atoi.py`
* **Core Concepts:** String parsing, pointer management (`while` loops), look-ahead overflow checking.
* **Overview:** Simulates the classic C/C++ `atoi` function. It safely processes messy strings containing leading whitespace, optional signs, and trailing non-digit characters, seamlessly clamping the results to 32-bit limits.

---

## 📐 Engineering Standard: Code Guarding

A major highlight of this repository is the use of the Python industry convention:
```python
if __name__ == "__main__":
    # Test suite logic...
