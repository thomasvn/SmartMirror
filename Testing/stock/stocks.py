import urllib2
import time

# User Stock Follow Interests
stocksToPull = "AAPL", "GOOG", "AMZN", "EBAY"

# Method to grab data and write data to file.
def pullData(stock):
    try:
        fileLine = stock + '.txt'
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/' + stock + '/chartdata;type=quote;range=10d/csv'
        sourceCode = urllib2.urlopen(urlToVisit).read().decode()
        splitSource = sourceCode.split('\n')
        saveFile = open(fileLine, 'w')
        for eachLine in splitSource:
            splitLine = eachLine.split(',')
            if len(splitLine) == 6:
                if 'values' not in eachLine:
                    saveFile = open(fileLine, 'a')
                    lineToWrite = eachLine + '\n'
                    saveFile.write(lineToWrite)

        print 'Pulled', stock
        time.sleep(1)
    except Exception, e:
        print 'Stocks Error', str(e)
        print 'in Stock' + stock

for eachStock in stocksToPull:
    pullData(eachStock)