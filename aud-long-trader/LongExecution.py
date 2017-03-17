#!/usr/bin/env python

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

import csv
import datetime
import os
import time
import sys
import subprocess
import re
import urllib.parse
import urllib.request

#local imports
from SendSMS import SMSService
from Rule import DailyRule
from Rule import WeeklyRule


#######################
debug = False

class AppURLopener(urllib.request.FancyURLopener):
	version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'


class LongExecution:
	url = 'https://au.investing.com/currencies/aud-usd-historical-data'
	currentSpot = None	
	desc = 'AUD/USD'

	sms = SMSService()
	dailyRule = DailyRule()
	weeklyRule = WeeklyRule()

	def execute(self):
		opener = AppURLopener()
		soup = BeautifulSoup(opener.open(self.url).read(), 'html5lib')
		currTable = soup.find(id='curr_table')

		self.currentSpot = float(self.parseLastPrice(soup))
		print ('current trading price is:', str(self.currentSpot))

		if debug:
			f = open('workfile', 'w')
			f.write(str(table))
			f.close()

			self.writeCsv(dailyRecords, ["'date'", "'price'", "'open'", "'high'", "'low'", "'change'"])

		dailyRecords = self.parseDailyPriceTable(currTable)

		weeklyMsg = self.weeklyRule.execute(self.currentSpot, dailyRecords, self.desc)
		self.sms.send(weeklyMsg)
		
		dailyMsg = self.dailyRule.execute(self.currentSpot, dailyRecords, self.desc)
		self.sms.send(dailyMsg)

		print ('program ends')
		
	def writeCsv(self, records, headline):
		now = str(datetime.datetime.now())

		with open("data/price_daily." + now + ".csv", "w", newline="") as f:
			writer = csv.writer(f)
			records.insert(0, headline)
			writer.writerows(records)

	def parseDailyPriceTable(self, currTable):
		records = []
		for tr in currTable.find_all('tr')[2:]:
			tds = tr.find_all('td')
			records.append([elem.text for elem in tds])
		return records
		
	def parseLastPrice(self, soup):
		element_id = 'last_last'
		last_price = soup.find(id=element_id)
		return last_price.get_text()


def main(argv):
	print ('Starting long execution logic......', '\n')
	print ('Argument List:' + ' ' + str(len(argv)), '\n')
	if (len(argv) == 0):
		longE = LongExecution()
		longE.execute()
		return


if __name__ == "__main__":
   main(sys.argv[1:])
