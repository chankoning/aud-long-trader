import datetime

BASE_MSG = 'No suggestion to BUY, does not meet requirement'
def percentDiff(current, last):
	return round((current-last)*1.0/last*100,3)
		

class WeeklyRule:

	# compare current price and last 3 week's close price
	def execute(self, currentSpot, dailyRecords):

		now = str(datetime.datetime.now())
		msg = now + '\n'
		msg += 'Weekly percentChanges: '
		
		weekDaysGap = [4, 9, 14, 19]

		weeklyPrices = []
		for i in weekDaysGap:
			if (i > len(dailyRecords)):
				weeklyPrices.append(float(dailyRecords[len(dailyRecords)-1][1]))
			else:
				weeklyPrices.append(float(dailyRecords[i][1]))

		
		weeklyChange = []			 

		tempSpot = currentSpot
		for last in weeklyPrices:
			weeklyChange.append(percentDiff(tempSpot, last))
			tempSpot = last

		percentChange = weeklyChange[0]
		lastWeeklyChange = weeklyChange[1]

		msg += str(percentChange) + '%\n' + 'currentSpot: ' + str(currentSpot) + '\n'
		msg += 'last weekly change: ' + str(lastWeeklyChange) + '\n'

		if (percentChange <= -2.5 and lastWeeklyChange <= 0):
			msg += 'suggest to BUY: 2500 AUD'
		elif (percentChange <= -2.0 and lastWeeklyChange <= 0):
			msg += 'suggest to BUY: 2000 AUD'
		elif (percentChange <= -1.5 and lastWeeklyChange <= 0):
			msg += 'suggest to BUY: 1500 AUD'
		else:
			msg += BASE_MSG

		msg += '\n'
		return msg


class DailyRule:

	def execute(self, currentSpot, dailyRecords):
		now = str(datetime.datetime.now())

		lastDailyClosePrice = float(dailyRecords[0][1])

		msg = now + '\n'
		msg += 'last close price is: ' + str(lastDailyClosePrice) + '\n'
		msg += 'Daily percentChange: '

		percentChange = percentDiff(currentSpot, lastDailyClosePrice)
	
		msg += str(percentChange) + '%\n' + 'currentSpot: ' + str(currentSpot) + '\n'
		if (percentChange <= -1.5):
			msg += 'suggest to BUY: 2000 AUD'
		elif (percentChange <= -1.0):
			msg += 'suggest to BUY: 1000 AUD'
		elif (percentChange <= -0.5):
			msg += 'suggest to BUY: 100 AUD'
		else:
			msg += BASE_MSG

		msg += '\n'
		return msg
