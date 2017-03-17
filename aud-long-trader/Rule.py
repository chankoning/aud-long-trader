import datetime

class DailyRule:

	def execute(self, currentSpot, lastDailyClosePrice, lastDailyChange):


		now = str(datetime.datetime.now())

		msg = now + '\n'
		msg += 'last close price is: ' + lastDailyClosePrice + '\n'
		msg += 'Daily percentChange: '

		percentChange = round((float(currentSpot) - float(lastDailyClosePrice))/float(lastDailyClosePrice) * 100, 3)

		msg += str(percentChange) + '%\n currentSpot: ' + currentSpot + '\n'
		if (percentChange <= -1.5):
			msg += 'suggest to BUY: 2000 AUD'
		elif (percentChange <= -1.0):
			msg += 'suggest to BUY: 1000 AUD'
		elif (percentChange <= -0.5):
			msg += 'suggest to BUY: 100 AUD'
		else:
			msg += 'No suggestion to BUY, does not meet requirement'

		return msg
