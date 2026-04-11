import importlib
import inspect
from pathlib import Path

from .driver_api import CameraDriver, validate_driver_class


def iter_driver_classes():
    for path in Path(__file__).parent.glob("*.py"):
        if path.name.startswith("_") or path.name in {
            "driver_api.py",
            "validate_driver_contract.py",
            "__init__.py",
        }:
            continue

        module = importlib.import_module(f"drivers.{path.stem}")
        for _, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, CameraDriver) and obj.__name__ not in {"CameraDriver", "GPhoto2CameraDriver", "GPhoto2CandidateDriver"}:
                if obj.__module__ == module.__name__:
                    yield path.name, obj


def main() -> int:
    errors = []
    for file_name, driver_cls in iter_driver_classes():
        for err in validate_driver_class(driver_cls):
            errors.append(f"{file_name}:{driver_cls.__name__}: {err}")

    if errors:
        for err in errors:
            print(err)
        return 1

    print("Driver contract validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
