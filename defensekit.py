"""Defensive finding normalization helpers."""
def normalize(finding):
    return {"title": str(finding.get("title", "Untitled")).strip(), "severity": str(finding.get("severity", "unknown")).lower(), "status": str(finding.get("status", "open")).lower()}
def by_severity(findings):
    result = {}
    for finding in findings:
        item = normalize(finding)
        result.setdefault(item["severity"], []).append(item)
    return result
def summary(findings):
    grouped = by_severity(findings)
    return {"total": len(findings), "counts": {k: len(v) for k, v in grouped.items()}}
