class JobPost:
    def __init__(self, job_id, title, description, salary):
        if salary < 0:
            raise ValueError("Цалин сөрөг байж болохгүй")
        self.job_id = job_id
        self.title = title
        self.description = description
        self.salary = salary


def get_job_detail(jobs, job_id):
    """Ажлын байрны дэлгэрэнгүй мэдээллийг ID-аар авах."""
    if job_id not in jobs:
        raise ValueError("Ажлын байр олдсонгүй")
    return jobs[job_id]
