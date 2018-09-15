from keras.preprocessing.image import img_to_array

class ImageToArrayPreprocssor:
	def __init__(self, dataFormat=None):
		sele.dataFormat = dataFormat

	def preprocess(self, image):
		return img_to_array(image, dataFormat=self.dataFormat)

	