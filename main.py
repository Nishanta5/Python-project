from flask import Flask, render_template

import csv
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

app = Flask(__name__)

# access the drive
gauth = GoogleAuth()
drive = GoogleDrive(gauth)

@app.route('/')
def home():
    csv_list = []
    # 1wSc7KIwTg38b-n_sbEdk84PnkRxpWcSP
    # f = drive.CreateFile({'id': '1wSc7KIwTg38b-n_sbEdk84PnkRxpWcSP'})
    f = drive.CreateFile({'id': '1nguc57jsFO_m-xOXWhNhji6NNLrub070'})
    f.GetContentFile('sample.csv')

    print('title: %s, mimeType: %s' % (f['title'], f['mimeType']))

    with open('sample.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            csv_list.append(row)
    file.close()
    return render_template('index.html', len = len(csv_list), items = csv_list)

@app.route('/upload')
def upload():
    # the file you want to upload, here simple example
    f = drive.CreateFile({'sample_file': 'sample.csv'})  

    # f = drive.CreateFile({'id': '1wSc7KIwTg38b-n_sbEdk84PnkRxpWcSP'})
    # f = drive.CreateFile({'id': '1nguc57jsFO_m-xOXWhNhji6NNLrub070'})

    f.SetContentFile('sample.csv')

    # upload the file
    f.Upload()
    print('title: %s, mimeType: %s' % (f['title'], f['mimeType']))

    return "success"


if __name__ == '__main__':
   app.run(debug=True)