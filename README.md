# BDJOBS scraper
----------------

This simple scraper crawl through bdjobs.com according to category and keyword,
extract job position, company name, education, experience and job url to a csv file.


## Installing requirements
```
pip install -r requirements.txt
```

## Usage
```
python3 scraper.py
```
Then follow the interactive prompt.

## BDJOBS category IDs
| Category Name                    | ID | Category Name                     | ID  |
| -------------------------------- |:--:| --------------------------------- |:---:|
| All Category                     | -1 | Accounting/Finance                |   1 |
| Bank/ Non-Bank Fin. Institution  |  2 | Commercial/Supply Chain           |   3 |
| Education/Training               |  4 | Engineer/Architects               |   5 |
| Garments/Textile                 |  6 | Gen Mgt/Admin                     |   7 |
| IT & Telecommunication           |  8 | Marketing/Sales                   |   9 |
| Media/Ad./Event Mgt.             | 10 | Medical/Pharma                    |  11 |
| NGO/Development                  | 12 | Research/Consultancy              |  13 |
| Secretary/Receptionist           | 14 | Data Entry/Operator/BPO           |  15 |
| Customer Support/Call Centre     | 16 | HR/Org. Development               |  17 |
| Design/Creative                  | 18 | Production/Operation              |  19 |
| Hospitality/ Travel/ Tourism     | 20 | Beauty Care/ Health & Fitness     |  21 |
| Law/Legal                        | 22 | Electrician/ Construction/ Repair |  23 |
| Security/Support Service         | 24 | Driving/Motor Technician          |  25 |
| Agro (Plant/Animal/Fisheries)    | 26 | Others                            | -10 |

-----------------------------------------------------------------------------------

This is an educational purpose project. Commercial use of the bdjobs.com data
may require permission from the authority.

As of 12 October 2016, this project works quite nicely. Any future change in bdjobs website may break this project's compatibility.
