def displayUseCases():
	output = """


	1. Get Posts By Id : 
		SELECT obj FROM table WHERE id = post_id

	2. Get Posts By Url :
		SELECT obj FROM table WHERE url = 'url'

	3. Collection Query 1
		SELECT obj FROM table WHERE country = 'x' AND tag = 'y' AND published < 'timestamp' AND site = 'site' ORDER BY published DESC LIMIT 20

	4. Collection Query 2
		SELECT obj FROM table WHERE country = 'x' AND tag = 'y' AND rank < `postRank` AND site = `site` ORDER BY rank DESC LIMIT 20

	5. Collection Query 3
		SELECT obj FROM table WHERE country = 'x' AND type = 'postType' AND rank < `postRank` AND site = 'site' ORDER BY rank DESC LIMIT 20

	"""
	print(output)