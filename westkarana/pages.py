import os
from post import postfolder, month_names
from utils import filename


def create_year_page(by_year):
    os.makedirs(postfolder, exist_ok=True)
    with open(os.path.join(postfolder, filename), 'w', encoding="utf8", newline='') as f:
        print("# West Karana Archive by year\n", file=f)
        #print (by_year)
        sorted_years = [x for x in by_year.keys()]
        sorted_years.sort(reverse=True)
        for year in sorted_years:
            print('* [{}](./{}/{}) ({})'.format(year,
                                                year, filename, by_year[year]), file=f)


def postSort(post):
    return post.post_day


def create_year_month_day_page(ymtuple, by_year_month):
    path = os.path.join(postfolder, str(ymtuple[0]), ymtuple[1])
    filepath = os.path.join(path, filename)
    os.makedirs(path, exist_ok=True)
    by_year_month.sort(key=postSort)
    with open(filepath, 'w', encoding="utf8", newline='') as f:
        print("Back to: [West Karana](/posts/{}) > [{}](/posts/{}/{})".format(
            filename, ymtuple[0], ymtuple[0], filename), file=f)
        print('# West Karana Archive for {}, {}\n'.format(
            ymtuple[1], ymtuple[0]), file=f)
        for post in by_year_month:
            print('* [{}]({}.md) <span style="color:red;">{}</span>'.format(
                post.post_title, post.ID, 'comment' if post.comments else ''), file=f)


def monthsort(m):
    return month_names.index(m)


def create_year_month_page(by_year_month):
    monthlog = {}
    for ymtupl in by_year_month:
        year = ymtupl[0]
        month = ymtupl[1]
        if year in monthlog:
            monthlog[year].append(month)
        else:
            monthlog[year] = [month]
    for year in monthlog:
        path = os.path.join(postfolder, str(year))
        filepath = os.path.join(path, filename)
        os.makedirs(path, exist_ok=True)
        with open(filepath, 'w', encoding="utf8", newline='') as f:
            months = [m for m in monthlog[year]]
            months.sort(key=monthsort)
            print("Back to: [West Karana](../westkarana.md)", file=f)
            print("# West Karana Archive for {}\n".format(year), file=f)
            for m in months:
                print("* [{}](./{}/{})".format(m, m, filename), file=f)
