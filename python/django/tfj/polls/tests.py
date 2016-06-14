import datetime

from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your tests here.
from .models import Question


def create_question(question_text, days):
    time = timezone.now()
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionMethodTests(TestCase):

    def test_was_publshed_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_index_view_with_now_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'no polls are available.')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_a_past_questions(self):
        create_question(question_text='past question.', days=-30)
        response = self.client.get(reverse('polls:index'))

        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: past question.>']
        )


def QuestionIndexDetailTests(TestCase):

    def test_detail_view_with_a_future_question(self):
        future_question = create_question(question_text='future question', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
