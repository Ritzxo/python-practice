\# Python practice



Exercises and small scripts while I learn Python.



Not polished projects, just work I'm willing to stand behind.


## Tests

The inventory program has pytest tests in `test_inventory_management.py`.

```bash
pip install pytest
pytest -v
```

Three tests are marked as expected failures (xfail). They document known gaps: negative stock or price is accepted by `add_item`, and `sales_report` accepts negative quantities. They will start failing loudly once those cases are fixed, which is the cue to remove the marker.

GitHub Actions runs the tests on every push (`.github/workflows/tests.yml`).

