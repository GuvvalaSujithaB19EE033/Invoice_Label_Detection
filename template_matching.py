import math
import pytesseract
from keras.preprocessing import image
from PIL import Image

def return_text(img_path):
  img = Image.open(img_path)
  text = pytesseract.image_to_string(img)
  return text


def get_words_from_line_list(text):	
	text = text.translate(translation_table)
	word_list = text.split()
	
	return word_list

def count_frequency(word_list):
    D = {}
    for new_word in word_list:		
        if new_word in D:
            D[new_word] = D[new_word] + 1			
        else:
            D[new_word] = 1			
    return D

def word_frequencies_for_file(filename):	
	line_list = return_text(filename)
	word_list = get_words_from_line_list(line_list)
	freq_mapping = count_frequency(word_list)
	#print("File", filename, ":", )
	#print(len(line_list), "lines, ", )
	#print(len(word_list), "words, ", )
	#print(len(freq_mapping), "distinct words")
	return freq_mapping

def dotProduct(D1, D2):
	Sum = 0.0	
	for key in D1:		
		if key in D2:
			Sum += (D1[key] * D2[key])			
	return Sum

def vector_angle(D1, D2):
	numerator = dotProduct(D1, D2)
	denominator = math.sqrt(dotProduct(D1, D1)*dotProduct(D2, D2))	
	return math.acos(numerator / denominator)
 
def documentSimilarity(filename_1, filename_2):
  sorted_word_list_1 = word_frequencies_for_file(filename_1)
  sorted_word_list_2 = word_frequencies_for_file(filename_2)
  distance = vector_angle(sorted_word_list_1, sorted_word_list_2)
  #print("The distance between the documents is: % 0.6f (radians)"% distance)
  return distance
