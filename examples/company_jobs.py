"""Resolve an employer ID before requesting its bounded public job page."""
import argparse
import json
from urllib.parse import quote
from _public import get

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", default="Roche")
    args = parser.parse_args()
    companies = get("/api/v1/companies", {"q": args.query, "swiss_jobs": "true", "limit": 5})["companies"]
    if len(companies) != 1:
        print(json.dumps({"message": "Resolve the exact employer before selecting its jobs; no first-result guess made.", "candidates": [{k: c.get(k) for k in ["id", "canonical_name", "domain"]} for c in companies]}, indent=2))
        return
    company = companies[0]
    page = get("/api/v1/companies/" + quote(company["id"], safe="") + "/jobs", {"status": "active", "limit": 5})
    print(json.dumps({"company": {k: company.get(k) for k in ["id", "canonical_name", "domain"]}, "snapshot_at": page["snapshot_at"], "has_more": page["has_more"], "jobs": [{k: j.get(k) for k in ["id", "title", "source_url", "source_freshness", "location_class"]} for j in page["jobs"]]}, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
