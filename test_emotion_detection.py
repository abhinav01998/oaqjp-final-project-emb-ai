import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        # Testing to check if the emotion of joy is detected
        test1 = emotion_detector("I am glad this happened")
        self.assertEqual(test1['dominant_emotion'], 'joy')

        # Testing to check if the emotion of anger is detected
        test2 = emotion_detector("I am really mad about this")
        self.assertEqual(test2['dominant_emotion'], 'anger')

        # Testing to check if the emotion of disgust is detected
        test3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(test3['dominant_emotion'], 'disgust')

        # Testing to check if the emotion of sadness is detected
        test4 = emotion_detector("I am so sad about this")
        self.assertEqual(test4['dominant_emotion'], 'sadness')

        # Testing to check if the emotion of fear is detected
        test5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(test5['dominant_emotion'], 'fear')

unittest.main()
