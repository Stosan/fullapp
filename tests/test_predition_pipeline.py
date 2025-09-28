import unittest
import pytest
from src.services.prediction_pipeline import PredictionPipeline


class TestPredictionPipeline(unittest.TestCase):
    def test_predict_returns_string(self):
        pipeline = PredictionPipeline()
        result = pipeline.predict()
        self.assertIsInstance(result, str)