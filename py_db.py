#! /usr/bin/env python

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re

'''
This is the test script that is used to prove scraping is correct before being added
to the server.py file.
'''

def get_league_positions():

    page_url = "https://en.wikipedia.org/wiki/2019%E2%80%9321_ICC_World_Test_Championship"

    uClient = uReq(page_url)

    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    league_table = page_soup.findAll("table", {"class": "wikitable"})[3]

    table_body = league_table.find('tbody')

    point_data = []

    rows = table_body.find_all('tr')

    for row in rows:
        columns = row.find_all('th')
        columns = [ele.text.strip() for ele in columns]
        point_data.append([ele for ele in columns if ele])

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        point_data.append([ele for ele in cols if ele])

    n = 2

    return [x for x in point_data if x][n:][:-1]

def most_runs():

    page_url = "https://en.wikipedia.org/wiki/2019%E2%80%9321_ICC_World_Test_Championship"

    uClient = uReq(page_url)

    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    most_runs_table = page_soup.findAll("table", {"class": "wikitable"})[4]

    table_body = most_runs_table.find('tbody')

    most_runs_data = []

    rows = table_body.find_all('tr')

    for row in rows:
         columns = row.find_all('th')
         columns = [ele.text.strip() for ele in columns]
         most_runs_data.append([ele for ele in columns if ele])

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        most_runs_data.append([ele for ele in cols if ele])

    n = 1

    return [x for x in most_runs_data if x][n:][:-1]


def most_wickets():

    page_url = "https://en.wikipedia.org/wiki/2019%E2%80%9321_ICC_World_Test_Championship"

    uClient = uReq(page_url)

    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    most_wickets_table = page_soup.findAll("table", {"class": "wikitable"})[5]

    table_body = most_wickets_table.find('tbody')

    most_runs_data = []

    rows = table_body.find_all('tr')

    for row in rows:
        columns = row.find_all('th')
        columns = [ele.text.strip() for ele in columns]
        most_runs_data.append([ele for ele in columns if ele])

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        most_runs_data.append([ele for ele in cols if ele])

    n = 1

    return [x for x in most_runs_data if x][n:][:-1]

def highest_ind_score():

    page_url = "https://en.wikipedia.org/wiki/2019%E2%80%9321_ICC_World_Test_Championship"

    uClient = uReq(page_url)

    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    highest_ind_score_table = page_soup.findAll("table", {"class": "wikitable"})[6]

    table_body = highest_ind_score_table.find('tbody')

    most_runs_data = []

    rows = table_body.find_all('tr')

    for row in rows:
        columns = row.find_all('th')
        columns = [ele.text.strip() for ele in columns]
        most_runs_data.append([ele for ele in columns if ele])

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        most_runs_data.append([ele for ele in cols if ele])

    n = 1

    return [x for x in most_runs_data if x][n:][:-1]


def best_bowling_fig():

    page_url = "https://en.wikipedia.org/wiki/2019%E2%80%9321_ICC_World_Test_Championship"

    uClient = uReq(page_url)

    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    best_bowling_fig_table = page_soup.findAll("table", {"class": "wikitable"})[7]

    table_body = best_bowling_fig_table.find('tbody')

    most_runs_data = []

    rows = table_body.find_all('tr')

    for row in rows:
        columns = row.find_all('th')
        columns = [ele.text.strip() for ele in columns]
        most_runs_data.append([ele for ele in columns if ele])

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        most_runs_data.append([ele for ele in cols if ele])

    n = 1

    return [x for x in most_runs_data if x][n:][:-1]

def highest_team_totals():

    page_url = "https://en.wikipedia.org/wiki/2019%E2%80%9321_ICC_World_Test_Championship"

    uClient = uReq(page_url)

    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    highest_team_totals_table = page_soup.findAll("table", {"class": "wikitable"})[8]

    table_body = highest_team_totals_table.find('tbody')

    most_runs_data = []

    rows = table_body.find_all('tr')

    for row in rows:
        columns = row.find_all('th')
        columns = [ele.text.strip() for ele in columns]
        most_runs_data.append([ele for ele in columns if ele])

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        most_runs_data.append([ele for ele in cols if ele])

    n = 1

    return [x for x in most_runs_data if x][n:][:-1]

def lowest_team_totals():

    page_url = "https://en.wikipedia.org/wiki/2019%E2%80%9321_ICC_World_Test_Championship"

    uClient = uReq(page_url)

    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    lowest_team_totals_table = page_soup.findAll("table", {"class": "wikitable"})[9]

    table_body = lowest_team_totals_table.find('tbody')

    most_runs_data = []

    rows = table_body.find_all('tr')

    for row in rows:
        columns = row.find_all('th')
        columns = [ele.text.strip() for ele in columns]
        most_runs_data.append([ele for ele in columns if ele])

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        most_runs_data.append([ele for ele in cols if ele])

    n = 1

    return [x for x in most_runs_data if x][n:][:-1]



def get_about():

    page_url = "https://en.wikipedia.org/wiki/2019%E2%80%9321_ICC_World_Test_Championship"

    uClient = uReq(page_url)

    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    about = []

    about1 = page_soup.findAll("p")[1]
    about2 = page_soup.findAll("p")[2]
    about3 = page_soup.findAll("p")[3]
    about4 = page_soup.findAll("p")[4]

    about.append(about1.text)
    about.append(about2.text)
    about.append(about3.text)
    about.append(about4.text)

    #about_text = ''.join(about)

    #about_text = re.sub(r'\W[\w\W]]', '', about_text)


    about = [re.sub(r'\W[\w\W]]', '', i) for i in about]

    #[re.sub(r'\d\.fa$', '', file) for file in file_lst]


    #print(''.join(about).replace('[ ]', ''))

    print(about)


def get_point_scoring():
    page_url = "https://en.wikipedia.org/wiki/2019%E2%80%9321_ICC_World_Test_Championship"

    uClient = uReq(page_url)

    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    point_scoring = []

    point1 = page_soup.findAll("p")[5]
    point2 = page_soup.findAll("p")[6]
    point3 = page_soup.findAll("p")[7]

    point_scoring.append(point1.text)
    point_scoring.append(point2.text)
    point_scoring.append(point3.text)

    point_scoring = [re.sub(r'\W[\w\W]]', '', i) for i in point_scoring]

    print(point_scoring)


def get_teams():
    page_url = "https://en.wikipedia.org/wiki/2019%E2%80%9321_ICC_World_Test_Championship"

    uClient = uReq(page_url)

    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    teams = page_soup.findAll("div", {"class": "div-col"})[0]

    results = [[i.img for i in b.find_all('li')] for b in teams.find_all('ul')]

    for i in results:
        print(i[1]['src'])

def get_schedules():
    page_url = "https://en.wikipedia.org/wiki/2019%E2%80%9321_ICC_World_Test_Championship"

    uClient = uReq(page_url)

    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    years_html = [ page_soup.findAll("h3")[3], page_soup.findAll("h3")[4],
              page_soup.findAll("h3")[5], page_soup.findAll("h3")[6]
            ]


    schedule_2019_team1 = {}
    schedule_2019_team2 = {}
    schedule_2019_team3 = {}
    schedule_2019_20_team1 = {}
    schedule_2019_20_team2 = {}
    schedule_2019_20_team3 = {}
    schedule_2019_20_team4 = {}
    schedule_2019_20_team5 = {}
    schedule_2019_20_team6 = {}
    schedule_2019_20_team7 = {}
    schedule_2019_20_team8 = {}
    schedule_2019_20_team9 = {}
    schedule_2020_team10 = {}
    schedule_2020_team11 = {}
    schedule_2020_team12 = {}
    schedule_2020_team13 = {}
    schedule_2020_team14 = {}
    schedule_2020_team15 = {}
    schedule_2020_21_team1 = {}
    schedule_2020_21_team2 = {}
    schedule_2020_21_team3 = {}
    schedule_2020_21_team4 = {}
    schedule_2020_21_team5 = {}
    schedule_2020_21_team6 = {}
    schedule_2020_21_team7 = {}
    schedule_2020_21_team8 = {}
    schedule_2020_21_team9 = {}

    years = [i.text.replace('[edit]', '') for i in years_html]

    vs_teams_html = page_soup.findAll("h4")

    vs_teams = [i.text.replace('[edit]', '') for i in vs_teams_html]

    vs_teams1 = vs_teams[:1]
    vs_teams2 = vs_teams[1:2]
    vs_teams3 = vs_teams[2:3]
    vs_teams4 = vs_teams[3:4]
    vs_teams5 = vs_teams[4:5]
    vs_teams6 = vs_teams[5:6]
    vs_teams7 = vs_teams[6:7]
    vs_teams8 = vs_teams[7:8]
    vs_teams9 = vs_teams[8:9]
    vs_teams10 = vs_teams[9:10]
    vs_teams11 = vs_teams[10:11]
    vs_teams12 = vs_teams[11:12]
    vs_teams13 = vs_teams[12:13]
    vs_teams14 = vs_teams[13:14]
    vs_teams15 = vs_teams[14:15]
    vs_teams16 = vs_teams[15:16]
    vs_teams17 = vs_teams[16:17]
    vs_teams18 = vs_teams[17:18]
    vs_teams19 = vs_teams[18:19]
    vs_teams20 = vs_teams[19:20]
    vs_teams21 = vs_teams[20:21]
    vs_teams22 = vs_teams[21:22]
    vs_teams23 = vs_teams[22:23]
    vs_teams24 = vs_teams[23:24]
    vs_teams25 = vs_teams[24:25]
    vs_teams26 = vs_teams[25:26]
    vs_teams27 = vs_teams[26:27]

    #print(vs_teams1)
    #print(vs_teams2)
    #print(vs_teams3)
    #print(vs_teams4)
    #print(vs_teams5)

    # schedule.update({years[0]: vs_teams[:3]})
    # schedule.update({years[1]: vs_teams[4:12]})
    # schedule.update({years[2]: vs_teams[5:18]})
    # schedule.update({years[3]: vs_teams[19:27]})

    ###2019 TEAM1####

    ###MATCH1###
    t1match1_date = page_soup.findAll("table")[5]
    #print(t1match1_date)
    #exit()
    t1match1_date = t1match1_date.text.rstrip().strip().replace('Scorecard', '')

    t1match1_score = page_soup.find_all(["table"])[6].find_all('td')
    t1m1 = []
    for i in t1match1_score:
        t1m1.append(i.text.rstrip().strip())
    t1match1_score = ' '.join(t1m1).replace('&', 'and ')

    t1match1_result = page_soup.findAll("table")[7]
    #print(t1match1_result)
    #exit()
    t1match1_result = ' '.join(t1match1_result.td.b.text.rstrip().strip().split(' ')[:5])

    t1m1lst = [t1match1_date, t1match1_score, t1match1_result]

    ###MATCH2###
    t1match2_date = page_soup.findAll("table")[8]
    t1match2_date = t1match2_date.text.rstrip().strip().replace('Scorecard', '')

    t1match2_score = page_soup.find_all(["table"])[9].find_all('td')
    t1m2 = []
    for i in t1match2_score:
        t1m2.append(i.text.rstrip().strip())
    t1match2_score = ' '.join(t1m2).replace('&', 'and ')

    t1match2_result = page_soup.findAll("table")[10]
    t1match2_result = ' '.join(t1match2_result.td.b.text.rstrip().strip().split(' ')[:5])

    t1m2lst = [t1match2_date, t1match2_score, t1match2_result]

    ###MATCH3###
    t1match3_date = page_soup.findAll("table")[11]
    t1match3_date = t1match3_date.text.rstrip().strip().replace('Scorecard', '')

    t1match3_score = page_soup.find_all(["table"])[12].find_all('td')
    t1m3 = []
    for i in t1match3_score:
        t1m3.append(i.text.rstrip().strip())
    t1match3_score = ' '.join(t1m3).replace('&', 'and ')

    t1match3_result = page_soup.findAll("table")[13]
    t1match3_result = ' '.join(t1match3_result.td.b.text.rstrip().strip().split(' ')[:5])

    t1m3lst = [t1match3_date, t1match3_score, t1match3_result]

    ###MATCH4###
    t1match4_date = page_soup.findAll("table")[14]
    t1match4_date = t1match4_date.text.rstrip().strip().replace('Scorecard', '')

    t1match4_score = page_soup.find_all(["table"])[15].find_all('td')
    t1m4 = []
    for i in t1match4_score:
        t1m4.append(i.text.rstrip().strip())
    t1match4_score = ' '.join(t1m4).replace('&', 'and ')

    t1match4_result = page_soup.findAll("table")[16]
    t1match4_result = ' '.join(t1match4_result.td.b.text.rstrip().strip().split(' ')[:5])

    t1m4lst = [t1match4_date, t1match4_score, t1match4_result]


    ###MATCH5###
    t1match5_date = page_soup.findAll("table")[17]
    t1match5_date = t1match5_date.text.rstrip().strip().replace('Scorecard', '')

    t1match5_score = page_soup.find_all(["table"])[18].find_all('td')
    t1m5 = []
    for i in t1match5_score:
        t1m5.append(i.text.rstrip().strip())
    t1match5_score = ' '.join(t1m5).replace('&', 'and ')

    t1match5_result = page_soup.findAll("table")[19]
    t1match5_result = ' '.join(t1match5_result.td.b.text.rstrip().strip().split(' ')[:5])

    t1m5lst = [t1match5_date, t1match5_score, t1match5_result]

    schedule_2019_team1.update({years[0]: ' '.join(vs_teams1), 'match1': t1m1lst, 'match2': t1m2lst, 'match3': t1m3lst,
                     'match4': t1m4lst, 'match5': t1m5lst})

    ###END 2019 TEAM1####


    ###2019 TEAM2####

    ###MATCH1###
    t2match1_date = page_soup.findAll("table")[20]
    t2match1_date = t2match1_date.text.rstrip().strip().replace('Scorecard', '')

    t2match1_score = page_soup.find_all(["table"])[21].find_all('td')
    t2m1 = []
    for i in t2match1_score:
        t2m1.append(i.text.rstrip().strip())
    t2match1_score = ' '.join(t2m1).replace('&', 'and ')

    t2match1_result = page_soup.findAll("table")[22]
    t2match1_result = ' '.join(t2match1_result.td.b.text.rstrip().strip().split(' ')[:5])

    t2m1lst = [t2match1_date, t2match1_score, t2match1_result]

    ###MATCH2###
    t2match2_date = page_soup.findAll("table")[23]
    t2match2_date = t2match2_date.text.rstrip().strip().replace('Scorecard', '')

    t2match2_score = page_soup.find_all(["table"])[24].find_all('td')
    t2m2 = []
    for i in t2match2_score:
        t2m2.append(i.text.rstrip().strip())
    t2match2_score = ' '.join(t2m2).replace('&', 'and ')

    t2match2_result = page_soup.findAll("table")[25]
    t2match2_result = ' '.join(t2match2_result.td.b.text.rstrip().strip().split(' ')[:5])

    t2m2lst = [t2match2_date, t2match2_score, t2match2_result]

    schedule_2019_team2.update({years[0]: ' '.join(vs_teams2), 'match1': t2m1lst, 'match2': t2m2lst})

    ###END 2019 TEAM2####

    ###2019 TEAM3####

    ###MATCH1###
    t3match1_date = page_soup.findAll("table")[26]
    t3match1_date = t3match1_date.text.rstrip().strip().replace('Scorecard', '')

    t3match1_score = page_soup.find_all(["table"])[27].find_all('td')
    t3m1 = []
    for i in t3match1_score:
        t3m1.append(i.text.rstrip().strip())
    t3match1_score = ' '.join(t3m1).replace('&', 'and ')

    t3match1_result = page_soup.findAll("table")[28]
    t3match1_result = ' '.join(t3match1_result.td.b.text.rstrip().strip().split(' ')[:5])

    t3m1lst = [t3match1_date, t3match1_score, t3match1_result]

    ###MATCH2###
    t3match2_date = page_soup.findAll("table")[29]
    t3match2_date = t3match2_date.text.rstrip().strip().replace('Scorecard', '')

    t3match2_score = page_soup.find_all(["table"])[30].find_all('td')
    t3m2 = []
    for i in t3match2_score:
        t3m2.append(i.text.rstrip().strip())
    t3match2_score = ' '.join(t3m2).replace('&', 'and ')

    t3match2_result = page_soup.findAll("table")[31]
    t3match2_result = ' '.join(t3match2_result.td.b.text.rstrip().strip().split(' ')[:5])

    t3m2lst = [t3match2_date, t3match2_score, t3match2_result]

    schedule_2019_team3.update({years[0]: ' '.join(vs_teams3), 'match1': t3m1lst, 'match2': t3m2lst})

    ###END 2019 TEAM3####


    ###2019-20 TEAM1####

    ###MATCH1###
    t4match1_date = page_soup.findAll("table")[32]
    t4match1_date = t4match1_date.text.rstrip().strip().replace('Scorecard', '')

    t4match1_score = page_soup.find_all(["table"])[33].find_all('td')
    t4m1 = []
    for i in t4match1_score:
        t4m1.append(i.text.rstrip().strip())
    t4match1_score = ' '.join(t4m1).replace('&', 'and ')

    t4match1_result = page_soup.findAll("table")[34]
    t4match1_result = ' '.join(t4match1_result.td.b.text.rstrip().strip().split(' ')[:5])

    t4m1lst = [t4match1_date, t4match1_score, t4match1_result]

    ###MATCH2###
    t4match2_date = page_soup.findAll("table")[35]
    t4match2_date = t4match2_date.text.rstrip().strip().replace('Scorecard', '')

    t4match2_score = page_soup.find_all(["table"])[36].find_all('td')
    t4m2 = []
    for i in t4match2_score:
        t4m2.append(i.text.rstrip().strip())
    t4match2_score = ' '.join(t4m2).replace('&', 'and ')

    t4match2_result = page_soup.findAll("table")[37]
    t4match2_result = ' '.join(t4match2_result.td.b.text.rstrip().strip().split(' ')[:9])

    t4m2lst = [t4match2_date, t4match2_score, t4match2_result]

    ###MATCH3###
    t4match3_date = page_soup.findAll("table")[38]
    t4match3_date = t4match3_date.text.rstrip().strip().replace('Scorecard', '')

    t4match3_score = page_soup.find_all(["table"])[39].find_all('td')
    t4m3 = []
    for i in t4match3_score:
        t4m3.append(i.text.rstrip().strip())
    t4match3_score = ' '.join(t4m3).replace('&', 'and ')

    t4match3_result = page_soup.findAll("table")[40]
    t4match3_result = ' '.join(t4match3_result.td.b.text.rstrip().strip().split(' ')[:9])

    t4m3lst = [t4match3_date, t4match3_score, t4match3_result]

    schedule_2019_20_team1.update({years[1]: ' '.join(vs_teams4), 'match1': t4m1lst, 'match2': t4m2lst, 'match3':
        t4m3lst})

    ###END 2019-20 TEAM1####

    ###2019-20 TEAM2####

    ###MATCH1###
    t5match1_date = page_soup.findAll("table")[41]
    t5match1_date = t5match1_date.text.rstrip().strip().replace('Scorecard', '')

    t5match1_score = page_soup.find_all(["table"])[42].find_all('td')
    t5m1 = []
    for i in t5match1_score:
        t5m1.append(i.text.rstrip().strip())
    t5match1_score = ' '.join(t5m1).replace('&', 'and ')

    t5match1_result = page_soup.findAll("table")[43]
    t5match1_result = ' '.join(t5match1_result.td.b.text.rstrip().strip().split(' ')[:9])

    t5m1lst = [t5match1_date, t5match1_score, t5match1_result]

    ###MATCH2###
    t5match2_date = page_soup.findAll("table")[44]
    t5match2_date = t5match2_date.text.rstrip().strip().replace('Scorecard', '')

    t5match2_score = page_soup.find_all(["table"])[45].find_all('td')
    t5m2 = []
    for i in t5match2_score:
        t5m2.append(i.text.rstrip().strip())
    t5match2_score = ' '.join(t5m2).replace('&', 'and ')

    t5match2_result = page_soup.findAll("table")[46]
    t5match2_result = ' '.join(t5match2_result.td.b.text.rstrip().strip().split(' ')[:9])

    t5m2lst = [t5match2_date, t5match2_score, t5match2_result]

    schedule_2019_20_team2.update({years[1]: ' '.join(vs_teams5), 'match1': t5m1lst, 'match2': t5m2lst})

    ###END 2019-20 TEAM2####

    ###2019-20 TEAM3####

    ###MATCH1###
    t6match1_date = page_soup.findAll("table")[47]
    t6match1_date = t6match1_date.text.rstrip().strip().replace('Scorecard', '')

    t6match1_score = page_soup.find_all(["table"])[48].find_all('td')
    t6m1 = []
    for i in t6match1_score:
        t6m1.append(i.text.rstrip().strip())
    t6match1_score = ' '.join(t6m1).replace('&', 'and ')

    t6match1_result = page_soup.findAll("table")[49]
    t6match1_result = ' '.join(t6match1_result.td.b.text.rstrip().strip().split(' ')[:9])

    t6m1lst = [t6match1_date, t6match1_score, t6match1_result]

    ###MATCH2###
    t6match2_date = page_soup.findAll("table")[50]
    t6match2_date = t6match2_date.text.rstrip().strip().replace('Scorecard', '')

    t6match2_score = page_soup.find_all(["table"])[51].find_all('td')
    t6m2 = []
    for i in t6match2_score:
        t6m2.append(i.text.rstrip().strip())
    t6match2_score = ' '.join(t6m2).replace('&', 'and ')

    t6match2_result = page_soup.findAll("table")[52]
    try:
       t6match2_result = ' '.join(t6match2_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t6match2_result = 'TBD'

    t6m2lst = [t6match2_date, t6match2_score, t6match2_result]

    schedule_2019_20_team3.update({years[1]: ' '.join(vs_teams6), 'match1': t6m1lst, 'match2': t6m2lst})

    ###END 2019-20 TEAM3####

    ###2019-20 TEAM4####

    ###MATCH1###
    t7match1_date = page_soup.findAll("table")[53]
    t7match1_date = t7match1_date.text.rstrip().strip().replace('Scorecard', '')

    t7match1_score = page_soup.find_all(["table"])[54].find_all('td')
    t7m1 = []
    for i in t7match1_score:
        t7m1.append(i.text.rstrip().strip())
    t7match1_score = ' '.join(t7m1).replace('&', 'and ')

    t7match1_result = page_soup.findAll("table")[55]
    try:
        t7match1_result = ' '.join(t7match1_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t7match1_result = 'TBD'

    t7m1lst = [t7match1_date, t7match1_score, t7match1_result]

    ###MATCH2###
    t7match2_date = page_soup.findAll("table")[56]
    t7match2_date = t7match2_date.text.rstrip().strip().replace('Scorecard', '')

    t7match2_score = page_soup.find_all(["table"])[57].find_all('td')
    t7m2 = []
    for i in t7match2_score:
        t7m2.append(i.text.rstrip().strip())
    t7match2_score = ' '.join(t7m2).replace('&', 'and ')

    t7match2_result = page_soup.findAll("table")[58]
    try:
        t7match2_result = ' '.join(t7match2_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t7match2_result = 'TBD'

    t7m2lst = [t7match2_date, t7match2_score, t7match2_result]

    schedule_2019_20_team4.update({years[1]: ' '.join(vs_teams7), 'match1': t7m1lst, 'match2': t7m2lst})

    ###END 2019-20 TEAM4####

    ###2019-20 TEAM5####

    ###MATCH1###
    t8match1_date = page_soup.findAll("table")[59]
    t8match1_date = t8match1_date.text.rstrip().strip().replace('Scorecard', '')

    t8match1_score = page_soup.find_all(["table"])[60].find_all('td')
    t8m1 = []
    for i in t8match1_score:
        t8m1.append(i.text.rstrip().strip())
    t8match1_score = ' '.join(t8m1).replace('&', 'and ')

    t8match1_result = page_soup.findAll("table")[61]
    try:
        t8match1_result = ' '.join(t8match1_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t8match1_result = 'TBD'

    t8m1lst = [t8match1_date, t8match1_score, t8match1_result]

    ###MATCH2###
    t8match2_date = page_soup.findAll("table")[62]
    t8match2_date = t8match2_date.text.rstrip().strip().replace('Scorecard', '')

    t8match2_score = page_soup.find_all(["table"])[63].find_all('td')
    t8m2 = []
    for i in t8match2_score:
        t8m2.append(i.text.rstrip().strip())
    t8match2_score = ' '.join(t8m2).replace('&', 'and ')

    t8match2_result = page_soup.findAll("table")[64]
    try:
        t8match2_result = ' '.join(t8match2_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t8match2_result = 'TBD'

    t8m2lst = [t8match2_date, t8match2_score, t8match2_result]

    ###MATCH3###
    t8match3_date = page_soup.findAll("table")[65]
    t8match3_date = t8match3_date.text.rstrip().strip().replace('Scorecard', '')

    t8match3_score = page_soup.find_all(["table"])[66].find_all('td')
    t8m3 = []
    for i in t8match3_score:
        t8m3.append(i.text.rstrip().strip())
    t8match3_score = ' '.join(t8m3).replace('&', 'and ')

    t8match3_result = page_soup.findAll("table")[67]
    try:
        t8match3_result = ' '.join(t8match3_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t8match3_result = 'TBD'

    t8m3lst = [t8match3_date, t8match3_score, t8match3_result]

    schedule_2019_20_team5.update({years[1]: ' '.join(vs_teams8), 'match1': t8m1lst, 'match2': t8m2lst,
                                   'match3': t8m3lst})

    ###END 2019-20 TEAM5####

    ###2019-20 TEAM6####

    ###MATCH1###
    t9match1_date = page_soup.findAll("table")[68]
    t9match1_date = t9match1_date.text.rstrip().strip().replace('Scorecard', '')

    t9match1_score = page_soup.find_all(["table"])[69].find_all('td')
    t9m1 = []
    for i in t9match1_score:
        t9m1.append(i.text.rstrip().strip())
    t9match1_score = ' '.join(t9m1).replace('&', 'and ')

    t9match1_result = page_soup.findAll("table")[70]
    try:
        t9match1_result = ' '.join(t9match1_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t9match1_result = 'TBD'

    t9m1lst = [t9match1_date, t9match1_score, t9match1_result]

    ###MATCH2###
    t9match2_date = page_soup.findAll("table")[71]
    t9match2_date = t9match2_date.text.rstrip().strip().replace('Scorecard', '')

    t9match2_score = page_soup.find_all(["table"])[72].find_all('td')
    t9m2 = []
    for i in t9match2_score:
        t9m2.append(i.text.rstrip().strip())
    t9match2_score = ' '.join(t9m2).replace('&', 'and ')

    t9match2_result = page_soup.findAll("table")[73]
    try:
        t9match2_result = ' '.join(t9match2_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t9match2_result = 'TBD'

    t9m2lst = [t9match2_date, t9match2_score, t9match2_result]

    ###MATCH3###
    t9match3_date = page_soup.findAll("table")[74]
    t9match3_date = t9match3_date.text.rstrip().strip().replace('Scorecard', '')

    t9match3_score = page_soup.find_all(["table"])[75].find_all('td')
    t9m3 = []
    for i in t9match3_score:
        t9m3.append(i.text.rstrip().strip())
    t9match3_score = ' '.join(t9m3).replace('&', 'and ')

    t9match3_result = page_soup.findAll("table")[76]
    try:
        t9match3_result = ' '.join(t9match3_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t9match3_result = 'TBD'

    t9m3lst = [t9match3_date, t9match3_score, t9match3_result]


    ###MATCH4###
    t9match4_date = page_soup.findAll("table")[77]
    t9match4_date = t9match4_date.text.rstrip().strip().replace('Scorecard', '')

    t9match4_score = page_soup.find_all(["table"])[78].find_all('td')
    t9m4 = []
    for i in t9match4_score:
        t9m4.append(i.text.rstrip().strip())
    t9match4_score = ' '.join(t9m4).replace('&', 'and ')

    t9match4_result = page_soup.findAll("table")[79]
    try:
        t9match4_result = ' '.join(t9match4_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t9match4_result = 'TBD'

    t9m4lst = [t9match4_date, t9match4_score, t9match4_result]

    schedule_2019_20_team6.update({years[1]: ' '.join(vs_teams9), 'match1': t9m1lst, 'match2': t9m2lst,
                                   'match3': t9m3lst, 'match4': t9m4lst })

    ###END 2019-20 TEAM6####

    ###2019-20 TEAM7####

    ###MATCH1###
    t10match1_date = page_soup.findAll("table")[80]
    t10match1_date = t10match1_date.text.rstrip().strip().replace('Scorecard', '')

    t10match1_score = page_soup.find_all(["table"])[81].find_all('td')
    t10m1 = []
    for i in t10match1_score:
        t10m1.append(i.text.rstrip().strip())
    t10match1_score = ' '.join(t10m1).replace('&', 'and ')

    t10match1_result = page_soup.findAll("table")[82]
    try:
        t10match1_result = ' '.join(t10match1_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t10match1_result = 'TBD'

    t10m1lst = [t10match1_date, t10match1_score, t10match1_result]

    ###MATCH2###
    t10match2_date = page_soup.findAll("table")[83]
    t10match2_date = t10match2_date.text.rstrip().strip().replace('Scorecard', '')

    t10match2_score = page_soup.find_all(["table"])[84].find_all('td')
    t10m2 = []
    for i in t10match2_score:
        t10m2.append(i.text.rstrip().strip())
    t10match2_score = ' '.join(t10m2).replace('&', 'and ')

    t10match2_result = page_soup.findAll("table")[85]
    try:
        t10match2_result = ' '.join(t10match2_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t10match2_result = 'TBD'

    t10m2lst = [t10match2_date, t10match2_score, t10match2_result]

    schedule_2019_20_team7.update({years[1]: ' '.join(vs_teams10), 'match1': t10m1lst, 'match2': t10m2lst})

    ###END 2019-20 TEAM7####

    ###2019-20 TEAM8####

    ###MATCH1###
    t11match1_date = page_soup.findAll("table")[86]
    t11match1_date = t11match1_date.text.rstrip().strip().replace('Scorecard', '')

    t11match1_score = page_soup.find_all(["table"])[87].find_all('td')
    t11m1 = []
    for i in t11match1_score:
        t11m1.append(i.text.rstrip().strip())
    t11match1_score = ' '.join(t11m1).replace('&', 'and ')

    t11match1_result = page_soup.findAll("table")[88]
    try:
        t11match1_result = ' '.join(t11match1_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t11match1_result = 'TBD'

    t11m1lst = [t11match1_date, t11match1_score, t11match1_result]

    ###MATCH2###
    t11match2_date = page_soup.findAll("table")[89]
    t11match2_date = t11match2_date.text.rstrip().strip().replace('Scorecard', '')

    t11match2_score = page_soup.find_all(["table"])[90].find_all('td')
    t11m2 = []
    for i in t11match2_score:
        t11m2.append(i.text.rstrip().strip())
    t11match2_score = ' '.join(t11m2).replace('&', 'and ')

    t11match2_result = page_soup.findAll("table")[91]
    try:
        t11match2_result = ' '.join(t11match2_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t11match2_result = 'TBD'

    t11m2lst = [t11match2_date, t11match2_score, t11match2_result]

    schedule_2019_20_team8.update({years[1]: ' '.join(vs_teams11), 'match1': t11m1lst, 'match2': t11m2lst})

    ###END 2019-20 TEAM8####

    ###2019-20 TEAM9####

    ###MATCH1###
    t12match1_date = page_soup.findAll("table")[92]
    t12match1_date = t12match1_date.text.rstrip().strip().replace('Scorecard', '')

    t12match1_score = page_soup.find_all(["table"])[93].find_all('td')
    t12m1 = []
    for i in t12match1_score:
        t12m1.append(i.text.rstrip().strip())
    t12match1_score = ' '.join(t12m1).replace('&', 'and ')

    t12match1_result = page_soup.findAll("table")[94]
    try:
        t12match1_result = ' '.join(t12match1_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t12match1_result = 'TBD'

    t12m1lst = [t12match1_date, t12match1_score, t12match1_result]

    ###MATCH2###
    t12match2_date = page_soup.findAll("table")[95]
    t12match2_date = t12match2_date.text.rstrip().strip().replace('Scorecard', '')

    t12match2_score = page_soup.find_all(["table"])[96].find_all('td')
    t12m2 = []
    for i in t12match2_score:
        t12m2.append(i.text.rstrip().strip())
    t12match2_score = ' '.join(t12m2).replace('&', 'and ')

    t12match2_result = page_soup.findAll("table")[97]
    try:
        t12match2_result = ' '.join(t12match2_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t12match2_result = 'TBD'

    t12m2lst = [t12match2_date, t12match2_score, t12match2_result]

    schedule_2019_20_team9.update({years[1]: ' '.join(vs_teams12), 'match1': t12m1lst, 'match2': t12m2lst})

    ###END 2019-20 TEAM9####


    ###2020 TEAM1####

    ###MATCH1###
    t13match1_date = page_soup.findAll("table")[98]
    t13match1_date = t13match1_date.text.rstrip().strip().replace('Scorecard', '')

    t13match1_score = page_soup.find_all(["table"])[99].find_all('td')
    t13m1 = []
    for i in t13match1_score:
        t13m1.append(i.text.rstrip().strip())
    t13match1_score = ' '.join(t13m1).replace('&', 'and ')

    t13match1_result = page_soup.findAll("table")[100]
    try:
        t13match1_result = ' '.join(t13match1_result.td.b.text.rstrip().strip().split(' ')[:5])
    except AttributeError:
        t13match1_result = 'TBD'

    t13m1lst = [t13match1_date, t13match1_score, t13match1_result]

    ###MATCH2###
    t13match2_date = page_soup.findAll("table")[101]
    t13match2_date = t13match2_date.text.rstrip().strip().replace('Scorecard', '')

    t13match2_score = page_soup.find_all(["table"])[102].find_all('td')
    t13m2 = []
    for i in t13match2_score:
        t13m2.append(i.text.rstrip().strip())
    t13match2_score = ' '.join(t13m2).replace('&', 'and ')

    t13match2_result = page_soup.findAll("table")[103]
    try:
        t13match2_result = ' '.join(t13match2_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t13match2_result = 'TBD'

    t13m2lst = [t13match2_date, t13match2_score, t13match2_result]

    schedule_2020_team10.update({years[2]: ' '.join(vs_teams13), 'match1': t13m1lst, 'match2': t13m2lst})

    ###END 2020 TEAM1####

    ###2020 TEAM2####

    ###MATCH1###
    t14match1_date = page_soup.findAll("table")[104]
    t14match1_date = t14match1_date.text.rstrip().strip().replace('Scorecard', '')

    t14match1_score = page_soup.find_all(["table"])[105].find_all('td')
    t14m1 = []
    for i in t14match1_score:
        t14m1.append(i.text.rstrip().strip())
    t14match1_score = ' '.join(t14m1).replace('&', 'and ')

    t14match1_result = page_soup.findAll("table")[106]
    try:
        t14match1_result = ' '.join(t14match1_result.td.b.text.rstrip().strip().split(' ')[:5])
    except AttributeError:
        t14match1_result = 'TBD'

    t14m1lst = [t14match1_date, t14match1_score, t14match1_result]

    ###MATCH2###
    t14match2_date = page_soup.findAll("table")[107]
    t14match2_date = t14match2_date.text.rstrip().strip().replace('Scorecard', '')

    t14match2_score = page_soup.find_all(["table"])[108].find_all('td')
    t14m2 = []
    for i in t14match2_score:
        t14m2.append(i.text.rstrip().strip())
    t14match2_score = ' '.join(t14m2).replace('&', 'and ')

    t14match2_result = page_soup.findAll("table")[109]
    try:
        t14match2_result = ' '.join(t14match2_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t14match2_result = 'TBD'

    t14m2lst = [t14match2_date, t14match2_score, t14match2_result]

    ###MATCH3###
    t14match3_date = page_soup.findAll("table")[110]
    t14match3_date = t14match3_date.text.rstrip().strip().replace('Scorecard', '')

    t14match3_score = page_soup.find_all(["table"])[110].find_all('td')
    t14m3 = []
    for i in t14match3_score:
        t14m3.append(i.text.rstrip().strip())
    t14match3_score = ' '.join(t14m3).replace('&', 'and ')

    t14match3_result = page_soup.findAll("table")[111]
    try:
        t14match3_result = ' '.join(t14match3_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t14match3_result = 'TBD'

    t14m3lst = [t14match3_date, t14match3_score, t14match3_result]

    schedule_2020_team11.update({years[2]: ' '.join(vs_teams14), 'match1': t14m1lst, 'match2': t14m2lst,
                                 'match3': t14m3lst})


    ###END 2020 TEAM2####


    ###2020 TEAM3####

    ###MATCH1###
    t15match1_date = page_soup.findAll("table")[113]
    t15match1_date = t15match1_date.text.rstrip().strip().replace('Scorecard', '')

    t15match1_score = page_soup.find_all(["table"])[114].find_all('td')
    t15m1 = []
    for i in t15match1_score:
        t15m1.append(i.text.rstrip().strip())
    t15match1_score = ' '.join(t15m1).replace('&', 'and ')

    t15match1_result = page_soup.findAll("table")[115]
    try:
        t15match1_result = ' '.join(t15match1_result.td.b.text.rstrip().strip().split(' ')[:5])
    except AttributeError:
        t15match1_result = 'TBD'

    t15m1lst = [t15match1_date, t15match1_score, t15match1_result]

    ###MATCH2###
    t15match2_date = page_soup.findAll("table")[116]
    t15match2_date = t15match2_date.text.rstrip().strip().replace('Scorecard', '')

    t15match2_score = page_soup.find_all(["table"])[117].find_all('td')
    t15m2 = []
    for i in t15match2_score:
        t15m2.append(i.text.rstrip().strip())
    t15match2_score = ' '.join(t15m2).replace('&', 'and ')

    t15match2_result = page_soup.findAll("table")[118]
    try:
        t15match2_result = ' '.join(t15match2_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t15match2_result = 'TBD'

    t15m2lst = [t15match2_date, t15match2_score, t15match2_result]

    ###MATCH3###
    t15match3_date = page_soup.findAll("table")[119]
    t15match3_date = t15match3_date.text.rstrip().strip().replace('Scorecard', '')

    t15match3_score = page_soup.find_all(["table"])[120].find_all('td')
    t15m3 = []
    for i in t15match3_score:
        t15m3.append(i.text.rstrip().strip())
    t15match3_score = ' '.join(t15m3).replace('&', 'and ')

    t15match3_result = page_soup.findAll("table")[121]
    try:
        t15match3_result = ' '.join(t15match3_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t15match3_result = 'TBD'

    t15m3lst = [t15match3_date, t15match3_score, t15match3_result]

    schedule_2020_team12.update({years[2]: ' '.join(vs_teams15), 'match1': t15m1lst, 'match2': t15m2lst,
                                 'match3': t15m3lst})

    ###END 2020 TEAM3####

    ###2020 TEAM4####

    ###MATCH1###
    t16match1_date = page_soup.findAll("table")[122]
    t16match1_date = t16match1_date.text.rstrip().strip().replace('Scorecard', '')

    t16match1_score = page_soup.find_all(["table"])[123].find_all('td')
    t16m1 = []
    for i in t16match1_score:
        t16m1.append(i.text.rstrip().strip())
    t16match1_score = ' '.join(t16m1).replace('&', 'and ')

    t16match1_result = page_soup.findAll("table")[124]
    try:
        t16match1_result = ' '.join(t16match1_result.td.b.text.rstrip().strip().split(' ')[:5])
    except AttributeError:
        t16match1_result = 'TBD'

    t16m1lst = [t16match1_date, t16match1_score, t16match1_result]

    ###MATCH2###
    t16match2_date = page_soup.findAll("table")[125]
    t16match2_date = t16match2_date.text.rstrip().strip().replace('Scorecard', '')

    t16match2_score = page_soup.find_all(["table"])[126].find_all('td')
    t16m2 = []
    for i in t16match2_score:
        t16m2.append(i.text.rstrip().strip())
    t16match2_score = ' '.join(t16m2).replace('&', 'and ')

    t16match2_result = page_soup.findAll("table")[127]
    try:
        t16match2_result = ' '.join(t16match2_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t16match2_result = 'TBD'

    t16m2lst = [t16match2_date, t16match2_score, t16match2_result]

    schedule_2020_team13.update({years[2]: ' '.join(vs_teams16), 'match1': t16m1lst, 'match2': t16m2lst})

    ###END 2020 TEAM4####


    ###2020 TEAM5####

    ###MATCH1###
    t17match1_date = page_soup.findAll("table")[128]
    t17match1_date = t17match1_date.text.rstrip().strip().replace('Scorecard', '')

    t17match1_score = page_soup.find_all(["table"])[129].find_all('td')
    t17m1 = []
    for i in t17match1_score:
        t17m1.append(i.text.rstrip().strip())
    t17match1_score = ' '.join(t17m1).replace('&', 'and ')

    t17match1_result = page_soup.findAll("table")[130]
    try:
        t17match1_result = ' '.join(t17match1_result.td.b.text.rstrip().strip().split(' ')[:5])
    except AttributeError:
        t17match1_result = 'TBD'

    t17m1lst = [t17match1_date, t17match1_score, t17match1_result]

    ###MATCH2###
    t17match2_date = page_soup.findAll("table")[131]
    t17match2_date = t17match2_date.text.rstrip().strip().replace('Scorecard', '')

    t17match2_score = page_soup.find_all(["table"])[132].find_all('td')
    t17m2 = []
    for i in t17match2_score:
        t17m2.append(i.text.rstrip().strip())
    t17match2_score = ' '.join(t17m2).replace('&', 'and ')

    t17match2_result = page_soup.findAll("table")[133]
    try:
        t17match2_result = ' '.join(t17match2_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t17match2_result = 'TBD'

    t17m2lst = [t17match2_date, t17match2_score, t17match2_result]

    ###MATCH3###
    t17match3_date = page_soup.findAll("table")[134]
    t17match3_date = t17match3_date.text.rstrip().strip().replace('Scorecard', '')

    t17match3_score = page_soup.find_all(["table"])[135].find_all('td')
    t17m3 = []
    for i in t17match3_score:
        t17m3.append(i.text.rstrip().strip())
    t17match3_score = ' '.join(t17m3).replace('&', 'and ')

    t17match3_result = page_soup.findAll("table")[136]
    try:
        t17match3_result = ' '.join(t17match3_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t17match3_result = 'TBD'

    t17m3lst = [t17match3_date, t17match3_score, t17match3_result]


    schedule_2020_team14.update({years[2]: ' '.join(vs_teams17), 'match1': t17m1lst, 'match2': t17m2lst, 'match3': t17m3lst})

    ###END 2020 TEAM5####

    ###2020 TEAM6####

    ###MATCH1###
    t18match1_date = page_soup.findAll("table")[137]
    t18match1_date = t18match1_date.text.rstrip().strip().replace('Scorecard', '')

    t18match1_score = page_soup.find_all(["table"])[138].find_all('td')
    t18m1 = []
    for i in t18match1_score:
        t18m1.append(i.text.rstrip().strip())
    t18match1_score = ' '.join(t18m1).replace('&', 'and ')

    t18match1_result = page_soup.findAll("table")[139]
    try:
        t18match1_result = ' '.join(t18match1_result.td.b.text.rstrip().strip().split(' ')[:5])
    except AttributeError:
        t18match1_result = 'TBD'

    t18m1lst = [t18match1_date, t18match1_score, t18match1_result]

    ###MATCH2###
    t18match2_date = page_soup.findAll("table")[140]
    t18match2_date = t18match2_date.text.rstrip().strip().replace('Scorecard', '')

    t18match2_score = page_soup.find_all(["table"])[141].find_all('td')
    t18m2 = []
    for i in t18match2_score:
        t18m2.append(i.text.rstrip().strip())
    t18match2_score = ' '.join(t18m2).replace('&', 'and ')

    t18match2_result = page_soup.findAll("table")[142]
    try:
        t18match2_result = ' '.join(t18match2_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t18match2_result = 'TBD'

    t18m2lst = [t18match2_date, t18match2_score, t18match2_result]

    schedule_2020_team15.update({years[2]: ' '.join(vs_teams18), 'match1': t18m1lst, 'match2': t18m2lst})

    ###END 2020 TEAM6####

    ###2020-21 TEAM1####


    ###MATCH1###
    t19match1_date = page_soup.findAll("table")[143]
    t19match1_date = t19match1_date.text.rstrip().strip().replace('Scorecard', '')

    t19match1_score = page_soup.find_all(["table"])[144].find_all('td')
    t19m1 = []
    for i in t19match1_score:
        t19m1.append(i.text.rstrip().strip())
    t19match1_score = ' '.join(t19m1).replace('&', 'and ')

    t19match1_result = page_soup.findAll("table")[145]
    try:
        t19match1_result = ' '.join(t19match1_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t19match1_result = 'TBD'

    t19m1lst = [t19match1_date, t19match1_score, t19match1_result]

    ###MATCH2###
    t19match2_date = page_soup.findAll("table")[146]
    t19match2_date = t19match2_date.text.rstrip().strip().replace('Scorecard', '')

    t19match2_score = page_soup.find_all(["table"])[147].find_all('td')
    t19m2 = []
    for i in t19match2_score:
        t19m2.append(i.text.rstrip().strip())
    t19match2_score = ' '.join(t19m2).replace('&', 'and ')

    t19match2_result = page_soup.findAll("table")[148]
    try:
        t19match2_result = ' '.join(t19match2_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t19match2_result = 'TBD'

    t19m2lst = [t19match2_date, t19match2_score, t19match2_result]

    schedule_2020_21_team1.update({years[3]: ' '.join(vs_teams19), 'match1': t19m1lst, 'match2': t19m2lst})

    ###END 2020-21 TEAM1####


    ###2020-21 TEAM2####


    ###MATCH1###
    t20match1_date = page_soup.findAll("table")[149]
    t20match1_date = t20match1_date.text.rstrip().strip().replace('Scorecard', '')

    t20match1_score = page_soup.find_all(["table"])[150].find_all('td')
    t20m1 = []
    for i in t20match1_score:
        t20m1.append(i.text.rstrip().strip())
    t20match1_score = ' '.join(t20m1).replace('&', 'and ')

    t20match1_result = page_soup.findAll("table")[151]
    try:
        t20match1_result = ' '.join(t20match1_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t20match1_result = 'TBD'

    t20m1lst = [t20match1_date, t20match1_score, t20match1_result]

    ###MATCH2###
    t20match2_date = page_soup.findAll("table")[152]
    t20match2_date = t20match2_date.text.rstrip().strip().replace('Scorecard', '')

    t20match2_score = page_soup.find_all(["table"])[153].find_all('td')
    t20m2 = []
    for i in t20match2_score:
        t20m2.append(i.text.rstrip().strip())
    t20match2_score = ' '.join(t20m2).replace('&', 'and ')

    t20match2_result = page_soup.findAll("table")[154]
    try:
        t20match2_result = ' '.join(t20match2_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t20match2_result = 'TBD'

    t20m2lst = [t20match2_date, t20match2_score, t20match2_result]

    ###MATCH3###
    t20match3_date = page_soup.findAll("table")[155]
    t20match3_date = t20match3_date.text.rstrip().strip().replace('Scorecard', '')

    t20match3_score = page_soup.find_all(["table"])[156].find_all('td')
    t20m3 = []
    for i in t20match3_score:
        t20m3.append(i.text.rstrip().strip())
    t20match3_score = ' '.join(t20m3).replace('&', 'and ')

    t20match3_result = page_soup.findAll("table")[157]
    try:
        t20match3_result = ' '.join(t20match3_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t20match3_result = 'TBD'

    t20m3lst = [t20match3_date, t20match3_score, t20match3_result]

    ###MATCH4###
    t20match4_date = page_soup.findAll("table")[158]
    t20match4_date = t20match4_date.text.rstrip().strip().replace('Scorecard', '')

    t20match4_score = page_soup.find_all(["table"])[159].find_all('td')
    t20m4 = []
    for i in t20match4_score:
        t20m4.append(i.text.rstrip().strip())
    t20match4_score = ' '.join(t20m4).replace('&', 'and ')

    t20match4_result = page_soup.findAll("table")[160]
    try:
        t20match4_result = ' '.join(t20match4_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t20match4_result = 'TBD'

    t20m4lst = [t20match4_date, t20match4_score, t20match4_result]

    schedule_2020_21_team2.update({years[3]: ' '.join(vs_teams20), 'match1': t20m1lst, 'match2': t20m2lst,
                                   'match3': t20m3lst, 'match4': t20m4lst})

    ###END 2020-21 TEAM2####


    ###2020-21 TEAM3####


    ###MATCH1###
    t21match1_date = page_soup.findAll("table")[161]
    t21match1_date = t21match1_date.text.rstrip().strip().replace('Scorecard', '')

    t21match1_score = page_soup.find_all(["table"])[162].find_all('td')
    t21m1 = []
    for i in t21match1_score:
        t21m1.append(i.text.rstrip().strip())
    t21match1_score = ' '.join(t21m1).replace('&', 'and ')

    t21match1_result = page_soup.findAll("table")[163]
    try:
        t21match1_result = ' '.join(t21match1_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t21match1_result = 'TBD'

    t21m1lst = [t21match1_date, t21match1_score, t21match1_result]

    ###MATCH2###
    t21match2_date = page_soup.findAll("table")[164]
    t21match2_date = t21match2_date.text.rstrip().strip().replace('Scorecard', '')

    t21match2_score = page_soup.find_all(["table"])[165].find_all('td')
    t21m2 = []
    for i in t21match2_score:
        t21m2.append(i.text.rstrip().strip())
    t21match2_score = ' '.join(t21m2).replace('&', 'and ')

    t21match2_result = page_soup.findAll("table")[166]
    try:
        t21match2_result = ' '.join(t21match2_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t21match2_result = 'TBD'

    t21m2lst = [t21match2_date, t21match2_score, t21match2_result]

    schedule_2020_21_team3.update({years[3]: ' '.join(vs_teams21), 'match1': t21m1lst, 'match2': t21m2lst})

    ###END 2020-21 TEAM3####

    ###2020-21 TEAM4####


    ###MATCH1###
    t22match1_date = page_soup.findAll("table")[167]
    t22match1_date = t22match1_date.text.rstrip().strip().replace('Scorecard', '')

    t22match1_score = page_soup.find_all(["table"])[168].find_all('td')
    t22m1 = []
    for i in t22match1_score:
        t22m1.append(i.text.rstrip().strip())
    t22match1_score = ' '.join(t22m1).replace('&', 'and ')

    t22match1_result = page_soup.findAll("table")[169]
    try:
        t22match1_result = ' '.join(t22match1_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t22match1_result = 'TBD'

    t22m1lst = [t22match1_date, t22match1_score, t22match1_result]

    ###MATCH2###
    t22match2_date = page_soup.findAll("table")[170]
    t22match2_date = t22match2_date.text.rstrip().strip().replace('Scorecard', '')

    t22match2_score = page_soup.find_all(["table"])[171].find_all('td')
    t22m2 = []
    for i in t22match2_score:
        t22m2.append(i.text.rstrip().strip())
    t22match2_score = ' '.join(t22m2).replace('&', 'and ')

    t22match2_result = page_soup.findAll("table")[172]
    try:
        t22match2_result = ' '.join(t22match2_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t22match2_result = 'TBD'

    t22m2lst = [t22match2_date, t22match2_score, t22match2_result]

    ###MATCH3###
    t22match3_date = page_soup.findAll("table")[173]
    t22match3_date = t22match3_date.text.rstrip().strip().replace('Scorecard', '')

    t22match3_score = page_soup.find_all(["table"])[174].find_all('td')
    t22m3 = []
    for i in t22match3_score:
        t22m3.append(i.text.rstrip().strip())
    t22match3_score = ' '.join(t22m3).replace('&', 'and ')

    t22match3_result = page_soup.findAll("table")[175]
    try:
        t22match3_result = ' '.join(t22match3_result.td.b.text.rstrip().strip().split(' ')[:9])
    except AttributeError:
        t22match3_result = 'TBD'

    t22m3lst = [t22match3_date, t22match3_score, t22match3_result]

    schedule_2020_21_team4.update({years[3]: ' '.join(vs_teams22), 'match1': t22m1lst, 'match2': t22m2lst,
                                   'match3': t22m3lst})


    ###2020-21 TEAM5####


    ###MATCH1###
    t23match1_date = page_soup.findAll("table")[176]
    t23match1_date = t23match1_date.text.rstrip().strip().replace('Scorecard', '')


    t23match1_score = page_soup.find_all(["table"])[177].find_all('td')
    t23m1 = []
    for i in t23match1_score:
        t23m1.append(i.text.rstrip().strip())
    t23match1_score = ' '.join(t23m1).replace('&', 'and ')

    t23match1_result = page_soup.findAll("table")[178]
    try:
        t23match1_result = ' '.join(t23match1_result.td.b.text.rstrip().strip().split(' ')[:5])
    except AttributeError:
        t23match1_result = 'TBD'


    t23m1lst = [t23match1_date, t23match1_score, t23match1_result]

    ###MATCH2###
    t23match2_date = page_soup.findAll("table")[179]
    t23match2_date = t23match2_date.text.rstrip().strip().replace('Scorecard', '')

    t23match2_score = page_soup.find_all(["table"])[180].find_all('td')
    t23m2 = []
    for i in t23match2_score:
        t23m2.append(i.text.rstrip().strip())
    t23match2_score = ' '.join(t23m2).replace('&', 'and ')

    t23match2_result = page_soup.findAll("table")[181]
    try:
        t23match2_result = ' '.join(t23match2_result.td.b.text.rstrip().strip().split(' ')[:5])
    except AttributeError:
        t23match2_result = 'TBD'


    t23m2lst = [t23match2_date, t23match2_score, t23match2_result]

    ###MATCH3###
    t23match3_date = page_soup.findAll("table")[182]
    t23match3_date = t23match3_date.text.rstrip().strip().replace('Scorecard', '')

    t23match3_score = page_soup.find_all(["table"])[183].find_all('td')
    t23m3 = []
    for i in t23match3_score:
        t23m3.append(i.text.rstrip().strip())
    t23match3_score = ' '.join(t23m3).replace('&', 'and ')

    t23match3_result = page_soup.findAll("table")[184]
    try:
        t23match3_result = ' '.join(t23match3_result.td.b.text.rstrip().strip().split(' ')[:5])
    except AttributeError:
        t23match3_result = 'TBD'


    t23m3lst = [t23match3_date, t23match3_score, t23match3_result]

    ###MATCH4###
    t23match4_date = page_soup.findAll("table")[185]
    t23match4_date = t23match4_date.text.rstrip().strip().replace('Scorecard', '')

    t23match4_score = page_soup.find_all(["table"])[186].find_all('td')
    t23m4 = []
    for i in t23match4_score:
        t23m4.append(i.text.rstrip().strip())
    t23match4_score = ' '.join(t23m4).replace('&', 'and ')

    t23match4_result = page_soup.findAll("table")[187]
    try:
        t23match4_result = ' '.join(t23match4_result.td.b.text.rstrip().strip().split(' ')[:5])
    except AttributeError:
        t23match4_result = 'TBD'


    t23m4lst = [t23match4_date, t23match4_score, t23match4_result]


    ###MATCH5###
    t23match5_date = page_soup.findAll("table")[188]
    t23match5_date = t23match5_date.text.rstrip().strip().replace('Scorecard', '')

    t23match5_score = page_soup.find_all(["table"])[189].find_all('td')
    t23m5 = []
    for i in t23match5_score:
        t23m5.append(i.text.rstrip().strip())
    t23match5_score = ' '.join(t23m5).replace('&', 'and ')

    t23match5_result = page_soup.findAll("table")[190]
    try:
        t23match5_result = ' '.join(t23match5_result.td.b.text.rstrip().strip().split(' ')[:5])
    except AttributeError:
        t23match5_result = 'TBD'

    t23m5lst = [t23match5_date, t23match5_score, t23match5_result]

    schedule_2020_21_team5.update({years[3]: ' '.join(vs_teams23), 'match1': t23m1lst, 'match2': t23m2lst,
                                   'match3': t23m3lst, 'match4': t23m4lst, 'match5': t23m5lst})

    ###END 2020-21 TEAM5####


    ###2020-21 TEAM6####

    ###MATCH1###
    t24match1_date = page_soup.findAll("table")[191]
    t24match1_date = t24match1_date.text.rstrip().strip().replace('Scorecard', '')

    t24match1_score = page_soup.find_all(["table"])[192].find_all('td')
    t24m1 = []
    for i in t24match1_score:
        t24m1.append(i.text.rstrip().strip())
    t24match1_score = ' '.join(t24m1).replace('&', 'and ')

    t24match1_result = page_soup.findAll("table")[193]
    try:
        t24match1_result = ' '.join(t24match1_result.td.b.text.rstrip().strip().split(' ')[:5])
    except AttributeError:
        t24match1_result = 'TBD'

    t24m1lst = [t24match1_date, t24match1_score, t24match1_result]

    ###MATCH2###
    t24match2_date = page_soup.findAll("table")[194]
    t24match2_date = t24match2_date.text.rstrip().strip().replace('Scorecard', '')

    t24match2_score = page_soup.find_all(["table"])[195].find_all('td')
    t24m2 = []
    for i in t24match2_score:
        t24m2.append(i.text.rstrip().strip())
    t24match2_score = ' '.join(t24m2).replace('&', 'and ')

    t24match2_result = page_soup.findAll("table")[196]
    try:
        t24match2_result = ' '.join(t24match2_result.td.b.text.rstrip().strip().split(' ')[:5])
    except AttributeError:
        t24match2_result = 'TBD'

    t24m2lst = [t24match2_date, t24match2_score, t24match2_result]

    schedule_2020_21_team6.update({years[3]: ' '.join(vs_teams24), 'match1': t24m1lst, 'match2': t24m2lst})

    ###END 2020-21 TEAM6####


    ###2020-21 TEAM7####

    ###MATCH1###
    t25match1_date = page_soup.findAll("table")[197]
    t25match1_date = t25match1_date.text.rstrip().strip().replace('Scorecard', '')

    t25match1_score = page_soup.find_all(["table"])[198].find_all('td')
    t25m1 = []
    for i in t25match1_score:
        t25m1.append(i.text.rstrip().strip())
    t25match1_score = ' '.join(t25m1).replace('&', 'and ')

    t25match1_result = page_soup.findAll("table")[199]
    try:
        t25match1_result = ' '.join(t25match1_result.td.b.text.rstrip().strip().split(' ')[:5])
    except AttributeError:
        t25match1_result = 'TBD'

    t25m1lst = [t25match1_date, t25match1_score, t25match1_result]

    ###MATCH2###
    t25match2_date = page_soup.findAll("table")[200]
    t25match2_date = t25match2_date.text.rstrip().strip().replace('Scorecard', '')

    t25match2_score = page_soup.find_all(["table"])[201].find_all('td')
    t25m2 = []
    for i in t25match2_score:
        t25m2.append(i.text.rstrip().strip())
    t25match2_score = ' '.join(t25m2).replace('&', 'and ')

    t25match2_result = page_soup.findAll("table")[202]
    try:
        t25match2_result = ' '.join(t25match2_result.td.b.text.rstrip().strip().split(' ')[:5])
    except AttributeError:
        t25match2_result = 'TBD'

    t25m2lst = [t25match2_date, t25match2_score, t25match2_result]

    schedule_2020_21_team7.update({years[3]: ' '.join(vs_teams25), 'match1': t25m1lst, 'match2': t25m2lst})

    ###END 2020-21 TEAM7####

    ###2020-21 TEAM8####

    ###MATCH1###
    t26match1_date = page_soup.findAll("table")[203]
    t26match1_date = t26match1_date.text.rstrip().strip().replace('Scorecard', '')

    t26match1_score = page_soup.find_all(["table"])[204].find_all('td')
    t26m1 = []
    for i in t26match1_score:
        t26m1.append(i.text.rstrip().strip())
    t26match1_score = ' '.join(t26m1).replace('&', 'and ')

    t26match1_result = page_soup.findAll("table")[205]
    try:
        t26match1_result = ' '.join(t26match1_result.td.b.text.rstrip().strip().split(' ')[:5])
    except AttributeError:
        t26match1_result = 'TBD'

    t26m1lst = [t26match1_date, t26match1_score, t26match1_result]

    ###MATCH2###
    t26match2_date = page_soup.findAll("table")[206]
    t26match2_date = t26match2_date.text.rstrip().strip().replace('Scorecard', '')

    t26match2_score = page_soup.find_all(["table"])[207].find_all('td')
    t26m2 = []
    for i in t26match2_score:
        t26m2.append(i.text.rstrip().strip())
    t26match2_score = ' '.join(t26m2).replace('&', 'and ')

    t26match2_result = page_soup.findAll("table")[208]
    try:
        t26match2_result = ' '.join(t26match2_result.td.b.text.rstrip().strip().split(' ')[:5])
    except AttributeError:
        t26match2_result = 'TBD'

    t26m2lst = [t26match2_date, t26match2_score, t26match2_result]


    ###MATCH3###
    t26match3_date = page_soup.findAll("table")[209]
    t26match3_date = t26match3_date.text.rstrip().strip().replace('Scorecard', '')

    t26match3_score = page_soup.find_all(["table"])[210].find_all('td')
    t26m3 = []
    for i in t26match3_score:
        t26m3.append(i.text.rstrip().strip())
    t26match3_score = ' '.join(t26m3).replace('&', 'and ')

    t26match3_result = page_soup.findAll("table")[211]
    try:
        t26match3_result = ' '.join(t26match3_result.td.b.text.rstrip().strip().split(' ')[:5])
    except AttributeError:
        t26match3_result = 'TBD'

    t26m3lst = [t26match3_date, t26match3_score, t26match3_result]

    schedule_2020_21_team8.update({years[3]: ' '.join(vs_teams26), 'match1': t26m1lst, 'match2': t26m2lst,
                                   'match3': t26m3lst})

    ###END 2020-21 TEAM8####


    ###2020-21 TEAM9####

    ###MATCH1###
    t27match1_date = page_soup.findAll("table")[212]
    t27match1_date = t27match1_date.text.rstrip().strip().replace('Scorecard', '')

    t27match1_score = page_soup.find_all(["table"])[213].find_all('td')
    t27m1 = []
    for i in t27match1_score:
        t27m1.append(i.text.rstrip().strip())
    t27match1_score = ' '.join(t27m1).replace('&', 'and ')

    t27match1_result = page_soup.findAll("table")[214]
    try:
        t27match1_result = ' '.join(t27match1_result.td.b.text.rstrip().strip().split(' ')[:5])
    except AttributeError:
        t27match1_result = 'TBD'

    t27m1lst = [t27match1_date, t27match1_score, t27match1_result]

    ###MATCH2###
    t27match2_date = page_soup.findAll("table")[215]
    t27match2_date = t27match2_date.text.rstrip().strip().replace('Scorecard', '')

    t27match2_score = page_soup.find_all(["table"])[216].find_all('td')
    t27m2 = []
    for i in t27match2_score:
        t27m2.append(i.text.rstrip().strip())
    t27match2_score = ' '.join(t27m2).replace('&', 'and ')

    t27match2_result = page_soup.findAll("table")[217]
    try:
        t27match2_result = ' '.join(t27match2_result.td.b.text.rstrip().strip().split(' ')[:5])
    except AttributeError:
        t27match2_result = 'TBD'

    t27m2lst = [t27match2_date, t27match2_score, t27match2_result]

    schedule_2020_21_team9.update({years[3]: ' '.join(vs_teams27), 'match1': t27m1lst, 'match2': t27m2lst})

    ###END 2020-21 TEAM9####



    #print(schedule_2019_team1)
    # print(schedule_2019_team2)
    # print(schedule_2019_team3)
    #print(schedule_2019_20_team1)
    #print(schedule_2019_20_team2)
    #print(schedule_2019_20_team3)
    #print(schedule_2019_20_team4)
    #print(schedule_2019_20_team5)
    #print(schedule_2019_20_team6)
    #print(schedule_2019_20_team7)
    #print(schedule_2019_20_team8)
    #print(schedule_2019_20_team9)
    #print(schedule_2020_team10)
    #print(schedule_2020_team11)
    #print(schedule_2020_team12)
    #print(schedule_2020_team13)
    #print(schedule_2020_team14)
    #print(schedule_2020_team15)
    #print(schedule_2020_21_team1)
    #print(schedule_2020_21_team2)
    #print(schedule_2020_21_team3)
    #print(schedule_2020_21_team4)
    #print(schedule_2020_21_team5)
    #print(schedule_2020_21_team6)
    #print(schedule_2020_21_team7)
    #print(schedule_2020_21_team8)
    #print(schedule_2020_21_team9)
    #print(schedule['2019'])
    #print(schedule['match1'])
    #print(schedule['match2'])
    #print(schedule['match3'])
    #print(schedule['match4'])





def main():

    x = lowest_team_totals()
    print(x)

    #x = highest_team_totals()
    #print(x)

    #x = best_bowling_fig()
    #print(x)
    #x = highest_ind_score()
    #print(x)

    #x = most_wickets()
    #print(x)
    #x = most_runs()
    #print(x)
    #x = get_league_positions()
    #print(x)
    #get_schedules()
    #get_teams()
    #get_point_scoring()
    #get_about()

    #positions = get_league_positions()

    #print(positions)




if __name__ == '__main__':
    main()