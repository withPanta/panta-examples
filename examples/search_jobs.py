"""Read one bounded page of public Swiss job leads."""
import argparse
import json
from _public import get

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", default="python")
    parser.add_argument("--location-class", choices=["physical_ch", "remote_ch_eligible", "multi_country_ch"], default="physical_ch")
    parser.add_argument("--limit", type=int, choices=range(1, 51), default=5)
    args = parser.parse_args()
    page = get("/api/v1/jobs", {"q": args.query, "location_class": args.location_class, "limit": args.limit})
    fields = ["id", "company_id", "company", "title", "location_class", "source_url", "source_freshness", "source_last_synced_at"]
    print(json.dumps({"snapshot_at": page["snapshot_at"], "has_more": page["has_more"], "next_offset": page["next_offset"], "jobs": [{k: job.get(k) for k in fields} for job in page["jobs"]]}, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
