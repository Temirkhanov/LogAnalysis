# Log Analysis

Internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

## Overview

Executing SQL queries that fetch results from a large database of a news website and then outputing it to the console in a presentable format.

### Prerequisites

Download the following:     
    Python 3
    Vagrant 
    VirtualBox
    Preconfigured vagrant folder [Download](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)
    "LogAnalysis.py" file from current repository
    "News" database [file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)



### How to run the program

1. In the terminal cd and unzip\move downloaded project files into \FSND-Virtual-Machine\vagrant
2. In the terminal run `vagrant up` 
3. After installation use `vagrant ssh` 
4. Cd into vagrant folder
5. Load the database psql -d news -f newsdata.sql
6. Create the required views. Follow few simple instructions below.
7. Then run `python LosAnalysis.py`

### Views

Creating the view that returns the list of all posts with count of views and sorted by popularity.
This query makes the code easy to read and might be very helpful for other purposes when it comes to working with popularity of the website posts. 

Create view from the terminal by running `psql -d news` and the executing 2 queries: 

Check and drop if the view is already exists: 
`
drop view if exists TOP_ARTICLES;
`

Create the view: 
`
create view TOP_ARTICLES as select a.title, count(l.id) as count 
from articles as a 
    join log as l 
        on a.slug = SUBSTRING(l.path, 10) 
where method = 'GET' and status = '200 OK' 
group by a.title order by count desc;
`




