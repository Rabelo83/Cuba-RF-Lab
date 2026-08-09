# Scripts

Status: starter tooling available

Place project automation scripts here. Keep scripts small, documented, and reproducible.

Scripts that support design choices should preserve assumptions and outputs so another collaborator can trace RF performance, cost, and fabrication tradeoffs.

## Current Scripts

- `nec_smoke_test.py`: verifies that the Python `necpp` NEC2 solver can run a basic antenna model.

Run from the repository root:

```bash
.venv/bin/python scripts/nec_smoke_test.py
```

For scripts that import plotting libraries, use a project-local Matplotlib cache:

```bash
MPLCONFIGDIR=.cache/matplotlib .venv/bin/python <script>
```
