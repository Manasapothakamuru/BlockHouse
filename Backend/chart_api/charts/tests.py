from django.test import TestCase
from django.urls import reverse
import json

class ChartViewsTestCase(TestCase):
    def test_candlestick_data_view(self):
        response = self.client.get(reverse('candlestick-data'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('datasets', data)
        self.assertIsInstance(data['datasets'], list)

    def test_line_chart_data_view(self):
        response = self.client.get(reverse('line-chart-data'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('labels', data)
        self.assertIn('data', data)

    def test_bar_chart_data_view(self):
        response = self.client.get(reverse('bar-chart-data'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('labels', data)
        self.assertIn('data', data)

    def test_pie_chart_data_view(self):
        response = self.client.get(reverse('pie-chart-data'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('labels', data)
        self.assertIn('data', data)