"""Input validation helpers for the Personal Budget Tracker CLI.

This module provides small, focused validation functions used by the
interactive CLI. Each function attempts to coerce/validate the provided
value and returns either the cleaned value (e.g. float for amounts) or
None to indicate invalid input.

The helpers are intentionally permissive and simple to keep the code
easy to understand and test. They do not raise exceptions for invalid
user input; instead they return None so the caller can re-prompt the
user.
"""

from __future__ import annotations

from typing import Optional
import re


def validate_user_id(value: str) -> Optional[str]:
    """Validate that the user id is a non-empty string.

    Returns the stripped string on success or None on failure.
    """

    if value is None:
        return None
    val = str(value).strip()
    return val if val else None


def validate_user_name(value: str) -> Optional[str]:
    """Validate that the user name is a non-empty string.

    Returns the stripped string on success or None on failure.
    """

    if value is None:
        return None
    val = str(value).strip()
    return val if val else None


def validate_spending_category(value: str) -> Optional[str]:
    """Validate that a spending category is provided.

    Returns the stripped category name or None.
    """

    if value is None:
        return None
    val = str(value).strip()
    return val if val else None


def validate_amount(value: str) -> Optional[float]:
    """Validate and convert an amount to float.

    Accepts strings or numeric types. Returns a float on success or None
    if the value cannot be converted or is negative.
    """

    if value is None:
        return None
    try:
        amt = float(str(value).strip())
    except (ValueError, TypeError):
        return None
    return amt if amt >= 0 else None


_DATE_RE = re.compile(r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$")


def validate_date(value: str) -> Optional[str]:
    """Validate a date string in the format dd/mm/yyyy.

    The function only checks the format (via a regex). It returns the
    original stripped string on success or None on failure.
    """

    if value is None:
        return None
    val = str(value).strip()
    return val if _DATE_RE.match(val) else None


def validate_description(value: str) -> Optional[str]:
    """Validate the transaction description as a non-empty string."""

    if value is None:
        return None
    val = str(value).strip()
    return val if val else None
