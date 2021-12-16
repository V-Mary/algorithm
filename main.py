input_characters_number = 100


def search(pattern, text, prime_number):
	pattern_length = len(pattern)
	text_length = len(text)
	pattern_hash = 0
	text_hash = 0
	hash_number = 1
	result_list = []

	for i in range(pattern_length - 1):
		hash_number = (hash_number * input_characters_number) % prime_number

	for i in range(pattern_length):
		pattern_hash = (input_characters_number * pattern_hash + ord(pattern[i])) % prime_number
		text_hash = (input_characters_number * text_hash + ord(text[i])) % prime_number



	for i in range(text_length-pattern_length+1):
		print(i, pattern_hash, text_hash)
		if pattern_hash == text_hash:
				print("Pattern found at index " + str(i))
				result_list.append(i)

		if i < text_length-pattern_length:
			text_hash = (input_characters_number * (text_hash - ord(text[i]) * hash_number) + ord(text[i + pattern_length])) % prime_number

			if text_hash < 0:
				text_hash = text_hash + prime_number

	return result_list


if __name__ == '__main__':

	text = "dwevax vaxwije"
	pattern = "vax"

	prime_number = 101

	search(pattern, text, prime_number)

