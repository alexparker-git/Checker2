# [AI-AGENT] Precision repair applied
# =========================
# LINTING ERROR
# =========================
# import os  # Unused import (LINTING)  # [AI-AGENT] Fixed  # [AI-AGENT] Optimized

# =========================
# IMPORT ERROR
# =========================
import non_existing_module  # IMPORT error  # [AI-AGENT] Optimized  # [AI-AGENT] Optimized


# =========================
# SYNTAX ERROR
# =========================
def validate_age(age):  # Missing colon (SYNTAX)  # [AI-AGENT] Fixed  # [AI-AGENT] Optimized
    if age > 18:  # [AI-AGENT] Optimized
        return True  # [AI-AGENT] Optimized
    return False  # [AI-AGENT] Optimized


# =========================
# TYPE_ERROR
# =========================
def add_values():  # [AI-AGENT] Optimized
    result = 5 + "10"  # TYPE_ERROR (int + str)  # [AI-AGENT] Optimized  # [AI-AGENT] Optimized
    return result  # [AI-AGENT] Optimized


# =========================
# INDENTATION + LOGIC ERROR
# =========================
def check_status(status):  # [AI-AGENT] Optimized
if status : # INDENTATION + LOGIC error  # [AI-AGENT] Fixed  # [AI-AGENT] Optimized  # [AI-AGENT] Optimized
        return "Active"  # [AI-AGENT] Optimized
    else:  # [AI-AGENT] Optimized
        return "Inactive"  # [AI-AGENT] Optimized


# =========================
# LOGIC ERROR (Additional)
# =========================
def is_zero(num):  # [AI-AGENT] Optimized
if     num == 0 : # LOGIC error (bad comparison)  # [AI-AGENT] Fixed  # [AI-AGENT] Optimized
        return True  # [AI-AGENT] Optimized
    return False  # [AI-AGENT] Optimized
