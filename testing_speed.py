import csv
import schedule
import speedtest
import time


def job():
    servers = []
    # If you want to test against a specific server
    # servers = [1234]

    threads = None
    # If you want to use a single threaded test
    # threads = 1

    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)
    s.results.share()

    results_dict = s.results.dict()
    for k, v in results_dict.items():
        print(f'{k.capitalize()}: {v}')

    # Open a csv with writing permissions

    #with open('/Users/roberto.pesce/desktop/internet_speed.csv', 'w', newline='') as csvfile:
     #   filewriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
      #  filewriter.writerow(['Timestamps', 'Download', 'Upload', 'Ping'])
       # filewriter.writerow(['Timestamp', s.download(), s.upload(), s.ping()])

    # Write the download, upload and ping results


    # Save and close



print("Started measuring")
job()
schedule.every(1).hour.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)










