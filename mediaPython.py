import requests
import time
year = 2014
fileName = 0
for y in range(4):
    year = year + 1
    for m in range(12):
        m = m+1
        for d in range(31):
            date = str(year)
            d = d+1
            if m < 10:
                date = date+str(0)+str(m)
            else:
                date = date+str(m)
            if d < 10:
                date = date+str(0)+str(d)
            else:
                date = date+str(d)
            print str(date)+"\n"
            print "https://api-prod.footballindex.co.uk/buzzmedia/rankedpage/footballuk.all:"+str(date)+"?page=1&per_page=2000&sort=asc"
            data = requests.get("https://api-prod.footballindex.co.uk/buzzmedia/rankedpage/footballuk.all:"+str(date)+"?page=1&per_page=2000&sort=asc"
                                ).json()
            #print data
            items = data['items']
            for item in items:
                data1 = requests.get("https://api-prod.footballindex.co.uk/buzzmedia/footballuk/"+item['id']+ "/20190811?page=1&per_page=2000").json()
                for value in data1['items']:
                    values = value['title']
                    fileName = fileName + 1
                    file = open("/Users/sanjeev/Desktop/FootBallIndexProject/Headlines/%d.text" % fileName , "w")
                    print "/Users/sanjeev/Desktop/FootBallIndexProject/Headlines/%d.text" % fileName
                    file.write(u''.join(values).encode('utf-8').strip())
                    file.close()
                    time.sleep(1)
