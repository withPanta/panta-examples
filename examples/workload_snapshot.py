"""Reproduce one aggregate from the dated 4 November 2026 Panta study."""
from _public import get

def main():
    data = get("/insights/data/eighty-percent-careers-2026-11-04.json")
    main = data["main"]
    categories = main["categories"]
    compatible = categories["exact_80"] + categories["range_including_80"] + categories["discrete_80_option"]
    assert compatible == main["includes_80"]
    print(f"Snapshot: {data['snapshot_at']}")
    print(f"Observed main cohort: {main['records']:,} records")
    print(f"80%-compatible signals: {compatible:,}; continuous ranges: {categories['range_including_80']:,} ({100 * categories['range_including_80'] / compatible:.1f}% of compatible signals)")
    print("Recorded title/employment-field wording; not a national estimate, agreed schedule or four-day-week count.")

if __name__ == "__main__":
    main()
