import io
import unittest
from app import create_app


class CVUploadTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def upload(self, filename, content=b'test'):
        data = {'cv': (io.BytesIO(content), filename)}
        return self.client.post(
            '/cv/upload', data=data,
            content_type='multipart/form-data')

    def test_accepts_pdf(self):
        response = self.upload('cv.pdf')
        self.assertEqual(response.status_code, 200)
        self.assertIn('амжилттай', response.get_data(as_text=True))

    def test_accepts_docx(self):
        response = self.upload('cv.docx')
        self.assertEqual(response.status_code, 200)

    def test_rejects_wrong_type(self):
        response = self.upload('cv.exe')
        self.assertEqual(response.status_code, 400)

    def test_rejects_large_file(self):
        big = b'x' * (5 * 1024 * 1024 + 1)
        response = self.upload('cv.pdf', big)
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()