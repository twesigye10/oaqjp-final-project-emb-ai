from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result1 = emotion_detector("I am glad this happened")
        self.assertIn('joy', result1)
        self.assertEqual(result1['dominant_emotion'], 'joy')

        result2 = emotion_detector("I am really mad about this")
        self.assertIn('anger', result2)
        self.assertEqual(result2['dominant_emotion'], 'anger')

        result3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertIn('disgust', result3)
        self.assertEqual(result3['dominant_emotion'], 'disgust')

        result4 = emotion_detector("I am so sad about this")
        self.assertIn('sadness', result4)
        self.assertEqual(result4['dominant_emotion'], 'sadness')

        result5 = emotion_detector("I am really afraid that this will happen")
        self.assertIn('fear', result5)
        self.assertEqual(result5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()

