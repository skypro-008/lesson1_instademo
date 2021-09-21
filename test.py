import unittest

from config import TestConfig
from webapp import app, cli, db, views  # noqa
from webapp.models import Comment, Post  # noqa


class MainTestCase(unittest.TestCase):
    def setUp(self):
        app.config.from_object(TestConfig)
        db.create_all()
        self.client = app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_posts(self):
        test_post_data = {
            'author': 'test_post_author',
            'content': 'test_post_content',
            'image': 'test_post_image'
        }
        test_comment_data = {
            'author': 'test_comment_author',
            'content': 'test_comment_content'
        }
        with self.client as client:
            post = Post(**test_post_data).add()
            comment = Comment(post_id=post.id, **test_comment_data).add()

            resp = client.get('/posts/')
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.access_control_allow_origin, '*')

            resp_list = resp.get_json()
            self.assertTrue(isinstance(resp_list, list))
            self.assertTrue(len(resp_list) == 1)

            first_record = resp_list[0]
            self.assertTrue(isinstance(first_record, dict))
            self.assertDictEqual(first_record, post.to_dict())
            self.assertTrue('comments' in first_record)

            first_record_comments = first_record['comments']
            self.assertTrue(isinstance(first_record_comments, list))
            self.assertListEqual(first_record_comments, [comment.id])


if __name__ == '__main__':
    unittest.main(verbosity=2)
