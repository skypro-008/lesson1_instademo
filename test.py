import json
import unittest

from config import TestConfig
from webapp import app, db, views  # noqa F401
from webapp.models import Comment, Post

POST_DATA = {
    'author': 'test_post_author',
    'content': 'test_post_content',
    'image': 'test_post_image'
}
COMMENT_DATA = {
    'author': 'test_comment_author',
    'content': 'test_comment_content'
}


class MainTestCase(unittest.TestCase):
    def setUp(self):
        app.config.from_object(TestConfig)
        db.create_all()
        self.client = app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_posts(self):
        url = '/posts/'
        post = Post(**POST_DATA).add()
        Comment(post_id=post.id, **COMMENT_DATA).add()

        with self.client as client:
            resp = client.get(url)
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.access_control_allow_origin, '*')
            self.assertListEqual(resp.access_control_allow_headers._headers, ['*'])

            resp_list = resp.get_json()
            self.assertTrue(isinstance(resp_list, list))
            self.assertTrue(len(resp_list) == 1)

            first_record = resp_list[0]
            self.assertTrue(isinstance(first_record, dict))
            self.assertEqual(first_record['id'], post.id)
            self.assertEqual(first_record['author'], POST_DATA['author'])
            self.assertEqual(first_record['content'], POST_DATA['content'])
            self.assertEqual(first_record['image'], POST_DATA['image'])
            self.assertEqual(first_record['views'], 0)
            self.assertEqual(first_record['likes'], 0)
            self.assertEqual(first_record['dislikes'], 0)
            self.assertListEqual(first_record['comments'], [{'id': 1}])

    def test_like_posts(self):
        url = '/posts/{}/like/'
        Post(**POST_DATA).add()

        with self.client as client:
            resp = client.post(url.format('qwe'))
            self.assertEqual(resp.status_code, 404)

            resp = client.post(url.format('2'))
            self.assertEqual(resp.status_code, 404)

            resp = client.post(url.format('1'))
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.access_control_allow_origin, '*')
            self.assertListEqual(resp.access_control_allow_headers._headers, ['*'])
            data: dict = resp.get_json()
            self.assertEqual(data['likes'], 1)

    def test_dislike_posts(self):
        url = '/posts/{}/dislike/'
        Post(**POST_DATA).add()

        with self.client as client:
            resp = client.post(url.format('qwe'))
            self.assertEqual(resp.status_code, 404)

            resp = client.post(url.format('2'))
            self.assertEqual(resp.status_code, 404)

            resp = client.post(url.format('1'))
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.access_control_allow_origin, '*')
            self.assertListEqual(resp.access_control_allow_headers._headers, ['*'])
            data: dict = resp.get_json()
            self.assertEqual(data['dislikes'], 1)

    def test_get_comments(self):
        url = '/posts/{}/comments/'
        post = Post(**POST_DATA).add()
        Comment(post_id=post.id, **COMMENT_DATA).add()

        with self.client as client:
            resp = client.get(url.format('qwe'))
            self.assertEqual(resp.status_code, 404)

            resp = client.get(url.format('2'))
            self.assertEqual(resp.status_code, 404)

            resp = client.get(url.format('1'))
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.access_control_allow_origin, '*')
            self.assertListEqual(resp.access_control_allow_headers._headers, ['*'])

            resp_list = resp.get_json()
            self.assertTrue(isinstance(resp_list, list))
            self.assertTrue(len(resp_list) == 1)

            first_record = resp_list[0]
            self.assertTrue(isinstance(first_record, dict))
            self.assertEqual(first_record['id'], 1)
            self.assertEqual(first_record['author'], COMMENT_DATA['author'])
            self.assertEqual(first_record['content'], COMMENT_DATA['content'])
            self.assertEqual(first_record['post_id'], 1)

    def test_add_comment(self):
        url = '/posts/{}/comments/'
        Post(**POST_DATA).add()
        with self.client as client:
            resp = client.post(url.format('qwe'))
            self.assertEqual(resp.status_code, 404)

            resp = client.post(url.format('2'))
            self.assertEqual(resp.status_code, 404)

            resp = client.post(
                path=url.format('1'),
                data=json.dumps({'author': 'author'}),
                headers={'Content-Type': 'application/json'}
            )
            self.assertEqual(resp.status_code, 400)

            resp = client.post(
                path=url.format('1'),
                data=json.dumps(COMMENT_DATA),
                headers={'Content-Type': 'application/json'}
            )
            self.assertEqual(resp.status_code, 201)
            self.assertEqual(resp.access_control_allow_origin, '*')
            self.assertListEqual(resp.access_control_allow_headers._headers, ['*'])
            data: dict = resp.get_json()
            self.assertEqual(data['id'], 1)
            self.assertEqual(data['author'], COMMENT_DATA['author'])
            self.assertEqual(data['content'], COMMENT_DATA['content'])
            self.assertEqual(data['post_id'], 1)

        comment = Comment.query.get(1)
        self.assertEqual(comment.post_id, 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
