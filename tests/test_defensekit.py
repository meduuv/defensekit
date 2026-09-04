from defensekit import normalize, summary

def test_defense():
    assert normalize({"title": " Finding ", "severity": "HIGH"})["title"] == "Finding"
    assert summary([{"severity": "high"}, {"severity": "low"}])["total"] == 2
