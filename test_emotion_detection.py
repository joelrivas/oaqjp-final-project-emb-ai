import unittest
from EmotionDetection.emotion_detection import emotion_detector

class EmotionDetectionTest(unittest.TestCase):
    """Test emotion detection"""

    def test_emotion_detector(self):
        """Test emotion_detector"""
        
        emotion = emotion_detector("I am glad this happened")
        self.assertEqual(emotion["dominant_emotion"], "joy")

        emotion = emotion_detector("I am really mad about this")
        self.assertEqual(emotion["dominant_emotion"], "anger")

        emotion = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(emotion["dominant_emotion"], "disgust")

        emotion = emotion_detector("I am so sad about this")
        self.assertEqual(emotion["dominant_emotion"], "sadness")

        emotion = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(emotion["dominant_emotion"], "fear")

unittest.main()