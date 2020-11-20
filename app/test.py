import os, json, csv
import pandas as pd
import requests

# return dictionary of filenames that are in the library
def getFolderPath():
    return os.path.dirname(os.path.abspath(__file__))

def getFnames():
    fnames = os.listdir(getFolderPath() + r'/static/lib')
    return fnames;
    #return { "libCsvMenu": fnames }
    # return(dict)

def getLibCsvInfo():
    libCsvInfo = getFolderPath() + r'/static/meta.json'
    with open ( libCsvInfo ) as file:
        return json.load(file)

def getLibCsv():
    filename = 'test.csv'
    libCsv = getFolderPath() + r'/static/lib/' + filename
    csvHeaders = []
    csvData = []
    with open(libCsv)as file:
      data = csv.reader(file)
      row = 0
      for record in data:
        if row == 0:
            csvHeaders = record
        csvData.append(record)
        row += 1

    dict = { "csvHeaders": csvHeaders,
             "csvData": csvData }

    return dict

def getFileSize(filename):
    libCsv = getFolderPath() + r'/static/lib/' + filename
    fileSize = os.stat(libCsv).st_size/1000  # get filesize
    if fileSize < 1:
        fileSize = str(round(fileSize, 2)) + ' KB'
    else:
        fileSize = str(round(fileSize)) + 'KB'

    return fileSize

def getSimpleFileSize(filename):
    libCsv = getFolderPath() + r'/static/lib/' + filename
    return os.stat(libCsv).st_size/1000  # get filesize

def addCsvToLibrary():
    # rem data object looks like: {'results': results.data, 'filename': self.csvFilename}
    filename = 'test_1.csv'
    data = [ ['h1', 'h2', 'h3'], ['1','2','3'], ['4', '5', '6'] ]
    file = getFolderPath() + '/static/lib/' + filename  # define save path
    csvfile = open(file, 'w', newline='')
    obj = csv.writer(csvfile, delimiter='|')
    for item in data:
        obj.writerow(item)
    csvfile.close()

def updateLibCsvInfo():
    #data = request.get_json()  # get the data
    filename = 'census_2009b.csv'
    description = 'Testing the File Update Again!'
    libCsvInfo = getFolderPath() + '/static/meta.json'
    #print(libCsvInfo)
    with open ( libCsvInfo, 'r' ) as file:
        data = json.load(file)  # get the json out of the file
        data['info'][filename] = description  # update the json

    with open ( libCsvInfo, 'w' ) as file:
        json.dump(data, file)  # dump the updated json object back into the json file

    return data

    # data['filename']
    # data['results']

def getBenfordAnalysis(data):
    #data = request.get_json()

    df = pd.DataFrame(data['data'])  # turn data into pandas dataFrame
    df.dropna()  # remove empty records
    print(df)

    #data = data.astype(str)  # cast int to string to allow easy char parsing
    #data = data.str[0]  # extract first char from each string
    data = data.value_counts(normalize=True)  ## count dist of unique values
    data = data.tolist()  ## cast data back to list (from series) to allow jsonify

def updateJsonFile():
    file = "testing.csv"
    field = "apifield"
    chart = "column"
    series = [9,8,7,6,5,4,3,2,1]

    # create a new chart entry
    nuchart = {}
    nuchart['filename'] = file
    nuchart['fieldname'] = field
    nuchart['chartType'] = chart
    nuchart['seriesData'] = series

    # get json object
    locfile = r'C:\Users\stcyb\Desktop\Docker\benapp_bstrap\00_TakeTwo\benapp_bstrap\bennyChartsTest.json'
    with open(locfile, 'r+') as file:
        data = json.load(file) # read json
        data.append(nuchart) # update json object
        file.seek(0) # reset iterator so that file can be re-written
        json.dump(data, file) # overwrite file with new object

def addCsvToLibrary( filename ):
    # rem data object looks like: {'results': results.data, 'filename': self.csvFilename}
    #data = request.get_json() # get data

    if filename in getFnames():
        name, ext = os.path.splitext(filename)
        filename = name + '0' + ext

    return filename

    #file = getFolderPath() + '/static/lib/' + data['filename']  # define save path

    csvfile = open(file, 'w', newline='')
    obj = csv.writer(csvfile, delimiter='|')
    for item in data['results']:
        obj.writerow(item)
    csvfile.close()

    #return jsonify( {'msg': 'CSV was added to Library.'} )

    return filename

#addInfo('widgets0.csv');
def addInfo(filename):
    libCsvInfo = getFolderPath() + r'/static/meta.json'
    description = 'No description.'

    # read the info object and update it
    with open ( libCsvInfo, 'r' ) as file:
        fileObj = json.load(file)
        fileObj['info'][filename] = description

    # dump the info object back into the file
    with open ( libCsvInfo, 'w' ) as file:
        json.dump( fileObj, file)

    return 'Good job!'


def getBenfordAnalysis( data ):
    df = pd.DataFrame(data)  # turn column into pandas dataframe
    df = df.dropna()  # remove null records
    # df['bNums'] = df['7_2009'].astype(str).str[0]  # extract 1st letters into new column
    dist = df['7_2009'].astype(str).str[0]  # extract 1st letters into new column
    dist = dist.value_counts(normalize=True)
    print(dist)
    #return df['bNums']
    return df


def getColDataForBenford(file):
    data = pd.read_csv(file, sep='|', usecols=['7_2009'])
    return data

# file = r'C:\Users\stcyb\Desktop\Docker\benapp_bstrap\00_TakeTwo\benapp_bstrap\app\static\lib\census_2009b.csv'
# print( getBenfordAnalysis( getColDataForBenford(file) ))


# def addToS3():
#     var params = {
# 	file: 'testingNewFile.csv',
#   field: 'testingNewField',
#   chart: 'scatterPlotThing',
#   series: [5,5,5,5,5,5,5,5,0]
# }

# response = requests.get("https://1z7u04v9vg.execute-api.us-east-2.amazonaws.com/init/bennyappgetgallerydata", {
# 	params: params
# })
# .then( (res) => {
# 	console.log('res: ', res.data);
# });
def getS3Contents():
    response = requests.get("https://1z7u04v9vg.execute-api.us-east-2.amazonaws.com/init/bennyappgetgallerydata")
    return response.json()

def setS3Contents():
    params = {
        'queryStringParameters':{
            'file': 'testingNewFile.csv',
            'field': 'testingNewField',
            'chart': 'scatterPlotThing',
            'series': [5,5,5,5,5,5,5,5,0]
        }
    }
    response = requests.post("https://1z7u04v9vg.execute-api.us-east-2.amazonaws.com/init/bennyappgetgallerydata", params=params)
    return response.json()

print( 'get: ', getS3Contents() )
print( 'set: ', setS3Contents() )
