# DefenseKit

> Small building blocks for defensive security analysis and reporting.

DefenseKit provides dependency-free helpers for turning security findings into normalized, grouped and report-friendly data.

## Features

- Normalize findings
- Group findings by severity
- Produce compact defensive summaries
- Keep processing local and deterministic
- Designed to compose with other security tooling

## Workflow

```text
findings
   ↓
normalize
   ↓
group
   ↓
prioritize
   ↓
summarize
```

## Example

```python
from defensekit import normalize_findings, summarize

findings = normalize_findings(raw_findings)
report = summarize(findings)
print(report)
```

The source and tests define the currently supported API.

## Scope

DefenseKit is intended for authorized defensive analysis and reporting. It does not provide exploitation or unauthorized-access functionality.

## Development

```bash
python -m pytest
```

## License

MIT. See `LICENSE`.

## Author

Built by **Medu** · https://guns.lol/meduu