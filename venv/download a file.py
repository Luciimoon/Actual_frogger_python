from urllib import  request
goog_url = "http://spatialkeydocs.s3.amazonaws.com/FL_insurance_sample.csv"
def dowload_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url, "w")
    for lines in lines:
        fx.write(line + "\n")
    fx.close()
download_stock_data(goog_url)
