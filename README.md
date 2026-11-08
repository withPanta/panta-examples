# Panta Swiss job market examples

Explore source-linked Swiss job and employer data through [Panta](https://withpanta.com/data/swiss-jobs/). These examples show how to search public data, inspect source evidence and reproduce a dated workload statistic.

## Run an example

Requires Python 3.10+ and curl. No API key is needed for these small public-market examples. They do not access personal workspaces.

```sh
python3 examples/search_jobs.py --query python --location-class physical_ch --limit 5
python3 examples/company_jobs.py --query Roche
python3 examples/workload_snapshot.py
```

The Python HTTP helper requires curl. It reports HTTP failures, including 429, without automatically retrying or saving responses. API access remains subject to the current service limits.

`workload_snapshot.py` reads a dated aggregate dataset. Its output is not a live market count. The accompanying `workload_snapshot.ipynb` uses the same public aggregate and creates a chart with Python's standard library SVG output; no notebook packages are needed beyond a notebook runner.

## Connect through MCP

Use this hosted Streamable HTTP URL in a compatible MCP client:

```text
https://withpanta.com/mcp
```

Initialization, tool discovery and public market tools can work anonymously. Personal workspace tools require an approved OAuth connection. Follow the [current connection guide](https://withpanta.com/docs/mcp/) for your client.

Try this prompt:

> Find up to five physical Swiss workplace listings mentioning Python. Keep the employer, source URL, source freshness and observation time with each result. Read the source evidence before recommending a role. Mark unstated requirements unknown and distinguish indexed leads from vacancies independently verified open. Do not apply or change my workspace.

## Interpret results carefully

- `physical_ch`, `remote_ch_eligible` and `multi_country_ch` represent different location evidence.
- Headquarters country and canonical active job counts do not establish Swiss vacancies.
- `source_freshness` and observation times describe source evidence, not a hiring outcome or guaranteed application acceptance.
- Null salary/language values are unknown. Language metadata does not establish a language requirement.
- Search pages are bounded and mutable. Use `next_offset` for navigation; do not describe a search-page download as a full atomic inventory export.

See [REST documentation](https://withpanta.com/docs/), [OpenAPI](https://withpanta.com/api/v1/openapi.json), [research](https://withpanta.com/insights/) and [methodology](https://withpanta.com/insights/methodology/).

These examples are maintained by Panta. Example code is provided under the [MIT License](LICENSE). Public API access does not grant a blanket license to redistribute third-party advert text. No underlying employer descriptions are bundled here.

## Questions and contributions

For example-code issues, [open an issue](https://github.com/withPanta/panta-examples/issues). Include the command, Python/curl versions and a redacted error. Never post API keys, account details, resumes or personal workspace data. For research corrections, use the original report’s correction route.

Contributions should be small, runnable and preserve source/date context. See [CONTRIBUTING.md](CONTRIBUTING.md).
