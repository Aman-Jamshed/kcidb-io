"""Kernel CI reporting I/O schema"""

from inspect import stack
from warnings import warn
from kcidb_io.schema.abstract import Version as VA  # noqa: F401
from kcidb_io.schema.v01_01 import Version as V1_1  # noqa: F401
from kcidb_io.schema.v02_00 import Version as V2_0  # noqa: F401
from kcidb_io.schema.v03_00 import Version as V3_0  # noqa: F401
from kcidb_io.schema.v04_00 import Version as V4_0  # noqa: F401
from kcidb_io.schema.v04_01 import Version as V4_1  # noqa: F401

# Legacy versions
V1 = V1_1  # noqa: F401
V2 = V2_0  # noqa: F401
V3 = V3_0  # noqa: F401
V4 = V4_0  # noqa: F401

# Latest version of the schema
LATEST = V4_1


def _warn_deprecated(new_func=None):
    """
    Issue a warning about the calling module's function being deprecated.

    Args:
        func:   The name of the schema.V* object method to direct the
                caller to, instead of the method named the same as the caller.
    """
    func = stack()[1].function
    warn(
        f"{__name__}.{func}() is deprecated, "
        f"use {__name__}.V*.{new_func or func}() instead",
        category=DeprecationWarning,
        stacklevel=3
    )


def validate(data):
    """
    Validate I/O data against one of the schema versions.

    Args:
        data:   The data to validate. Will not be changed.

    Returns:
        The validated (but unchanged) data.

    Raises:
        `jsonschema.exceptions.ValidationError` if the data did not adhere
        to any of the schema versions.
    """
    _warn_deprecated()
    return LATEST.validate(data)


def is_valid(data):
    """
    Check if I/O data is valid according to a schema version.

    Args:
        data:   The data to check.

    Returns:
        True if the data is valid, false otherwise.
    """
    _warn_deprecated()
    return LATEST.is_valid(data)


def validate_latest(data):
    """
    Validate I/O data against the latest schema version only.

    Args:
        data:   The data to validate. Will not be changed.

    Returns:
        The validated (but unchanged) data.

    Raises:
        `jsonschema.exceptions.ValidationError` if the data did not adhere
        to the latest schema version.
    """
    _warn_deprecated("validate_exactly")
    return LATEST.validate_exactly(data)


def is_valid_latest(data):
    """
    Check if I/O data is valid according to the latest schema version.

    Args:
        data:   The data to check.

    Returns:
        True if the data is valid, false otherwise.
    """
    _warn_deprecated("is_valid_exactly")
    return LATEST.is_valid_exactly(data)


def count(data):
    """
    Calculate number of objects of any type in an I/O data set.

    Args:
        data:   The data set to count the objects in.

    Returns:
        The number of objects in the data set.
    """
    _warn_deprecated()
    return LATEST.count(data)


def upgrade(data, copy=True):
    """
    Upgrade the data to the latest schema version from any of the previous
    versions. Validates the data. Has no effect if the data already adheres to
    the latest schema version.

    Args:
        data:   The data to upgrade and validate.
                Must adhere to a version of the schema.
        copy:   True, if the data should be copied before upgrading.
                False, if the data should be upgraded in-place.
                Optional, default is True.

    Returns:
        The upgraded and validated data.
    """
    _warn_deprecated()
    return LATEST.upgrade(data, copy)
