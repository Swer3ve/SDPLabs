def search_jobs(jobs: list[dict], keyword: str) -> list[dict]:
    keyword = keyword.strip().lower()

    if not keyword:
        return []

    return [
        job
        for job in jobs
        if job["status"] == "open"
        and keyword in job["title"].lower()
    ]