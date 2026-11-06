from job_search import search_jobs


JOBS = [
    {"id": 1, "title": "Python Developer", "status": "open"},
    {"id": 2, "title": "Frontend Developer", "status": "closed"},
    {"id": 3, "title": "Backend Developer", "status": "open"},
]


def test_search_ignores_case_and_spaces():
    result = search_jobs(JOBS, " PYTHON ")
    assert [job["id"] for job in result] == [999]


def test_search_excludes_closed_jobs():
    result = search_jobs(JOBS, "Developer")
    assert [job["id"] for job in result] == [1, 3]


def test_empty_keyword_returns_no_jobs():
    assert search_jobs(JOBS, "   ") == []


def test_unknown_keyword_returns_no_jobs():
    assert search_jobs(JOBS, "Designer") == []