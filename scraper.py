#!/usr/bin/env python3

import requests
import csv
from bs4 import BeautifulSoup


def extract_data(content, csvwriter):
    '''
    Take html content and csv file writer object as parameter.
    Extract the needed data and write it to the csv file.
    '''
    soup = BeautifulSoup(content, 'lxml')

    # First getting the all the job blocks
    content_blocks = soup.find_all('div', {'class': 'norm-jobs-wrapper'})

    # Now extracting per job info
    for block in content_blocks:
        company = block.find('div', {'class': 'comp-name-text'}).text.strip()

        # job position
        position_a = block.find('a')    # The block contains only one link(<a>)
        position = position_a.text.strip()

        # Absolute url of the job post
        job_url = 'http://jobs.bdjobs.com/' + position_a.get('href')

        # Finding education
        education_div = block.find('div', {'class': 'edu-text-d'})
        # Sometimes education info doesn't exist
        if education_div:
            # As some are given as plain text and some are given as list (<ul>)
            education_div_li = education_div.find_all('li')
            if education_div_li:
                for count, li in enumerate(education_div_li):
                    # there should be no line break before first line
                    if not count:
                        education = li.text.strip()
                    else:
                        education += '\n' + li.text.strip()
            else:
                education = education_div.text.strip()
        else:
            education = ''

        experience = block.find('div', {'class': 'exp-text-d'}).text.strip()

        # Writing data to the csv file
        data_row = [position, company, education, experience, job_url]
        csvwriter.writerow(data_row)


if __name__ == '__main__':
    print('Input BDJOBS category ID:')
    print('[-1 for all category, see README.md for more details]')
    category_id = int(input('> '))

    print('Input search keyword: [you can leave it blank for all results.]')
    search_keyword = input('> ')

    print('Input the CSV file name: [default: bdjobs.csv]')
    csv_file_name = input('> ')

    if not csv_file_name:
        csv_file_name = 'bdjobs.csv'

    print('Working on it. Please wait...')

    url = 'http://jobs.bdjobs.com/jobsearch.asp'
    post_data = {
        'fcat': category_id,
        'txtsearch': search_keyword,
        'hidJobSearch': 'JobSearch',
    }
    webpage = requests.post(url, data=post_data)

    soup = BeautifulSoup(webpage.content, 'lxml')

    # finding out how many pages to scrap
    pagination = soup.find('div', {'class': 'pagination', 'id': 'topPagging'})
    page_list = pagination.find_all('a')
    if page_list:
        last_page = int(page_list[-1].text.lstrip('...'))
    else:
        last_page = 1

    with open(csv_file_name, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csv_column_headers = [
            'Position',
            'Company Name',
            'Education',
            'Experience',
            'Job URL'
        ]
        csvwriter.writerow(csv_column_headers)

        # Scraping every page
        for page in range(last_page):
            post_data['pg'] = page + 1
            webpage = requests.post(url, data=post_data)
            extract_data(webpage.content, csvwriter)

    print('All data extracted to the ./{} file.'.format(csv_file_name))
