#! /usr/bin/env python

from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import csv
import sqlite3
from sqlite3 import Error

# page_url = "https://en.wikipedia.org/wiki/2019%E2%80%9321_ICC_World_Test_Championship"
#
# uClient = uReq(page_url)
#
# page_soup = soup(uClient.read(), "html.parser")
# uClient.close()

# point_table = containers = page_soup.findAll("table", {"class": "wikitable"})[0]
#
# print(point_table)
#
# exit()
#
# table_body = point_table.find('tbody')
#
# point_data = []
#
# rows = table_body.find_all('tr')
#
# for row in rows:
#     columns = row.find_all('th')
#     columns = [ele.text.strip() for ele in columns]
#     point_data.append([ele for ele in columns if ele])
#
# for row in rows:
#     cols = row.find_all('td')
#     cols = [ele.text.strip() for ele in cols]
#     point_data.append([ele for ele in cols if ele])
#
# with open('output.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows([x for x in point_data if x])


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid


def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid


def main():
    database = r"icc.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30');
        project_id = create_project(conn, project)

        # # tasks
        # task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
        # task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')
        #
        # # create tasks
        # create_task(conn, task_1)
        # create_task(conn, task_2)


if __name__ == '__main__':
    main()
#
# league_table = containers = page_soup.findAll("table", {"class": "wikitable"})[3]
#
#
# table_body = league_table.find('tbody')
#
# point_data = []
#
# rows = table_body.find_all('tr')
#
# for row in rows:
#     columns = row.find_all('th')
#     columns = [ele.text.strip() for ele in columns]
#     point_data.append([ele for ele in columns if ele])
#
# for row in rows:
#     cols = row.find_all('td')
#     cols = [ele.text.strip() for ele in cols]
#     point_data.append([ele for ele in cols if ele])
#
# #with open('output.csv', 'w') as csvfile:
# #    writer = csv.writer(csvfile)
# #    writer.writerows([x for x in point_data if x])
#
# #print([x for x in point_data if x][:-1])

