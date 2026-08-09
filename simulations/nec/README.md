# NEC Models

Status: planned

Place NEC-compatible antenna model files here. Include notes that explain every geometry parameter and feed assumption.

Use NEC models to compare candidate topologies with realistic local conductor diameters, boom materials, and construction tolerances before any dimensions are promoted to a blueprint.

First-pass queue:

- `first_pass_queue.md`

The queue starts with 900 MHz and 1800 MHz Yagi seeds, then LPDA and biquad references. Python `necpp` is installed in `.venv` and is the first working NEC2 path for this project.

Smoke test:

```bash
.venv/bin/python scripts/nec_smoke_test.py
```
