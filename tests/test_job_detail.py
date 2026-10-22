import pytest
from app.job_detail import JobPost, get_job_detail


def test_get_job_detail_returns_job():
    jobs = {1: JobPost(1, "Python хөгжүүлэгч", "Тайлбар", 2000000)}
    job = get_job_detail(jobs, 1)
    assert job.title == "Python хөгжүүлэгч"
    assert job.salary == 2000000


def test_get_job_detail_not_found():
    with pytest.raises(ValueError):
        get_job_detail({}, 99)


def test_job_post_negative_salary():
    with pytest.raises(ValueError):
        JobPost(1, "A", "B", -100)
