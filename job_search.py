def search_jobs(jobs: list[dict], keyword: str) -> list[dict]:
    results = []
    keyword = keyword.lower()

    for job in jobs:
        if keyword in job["title"].lower():
            results.append(job)

    return results


if __name__ == "__main__":
    jobs = [
        {"id": 1, "title": "Python Developer", "status": "open"},
        {"id": 2, "title": "Frontend Developer", "status": "closed"},
        {"id": 3, "title": "Backend Developer", "status": "open"},
    ]

    print(search_jobs(jobs, "python"))