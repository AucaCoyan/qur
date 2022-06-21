import datetime
from enum import Enum
from typing import List


def add(
    recruiter_name: str,
    keywords: str,
    link: str,
    starting_date: datetime.datetime,
    notice: datetime.datetime,
    status: Enum,
    log: List[str] = [""],
):
    """adds the job offer to the table
    :str recruiter_name: the person to contact for this offer, empty if is a group
    :str keywords: a short description of the offer. May have special formatting like <Location, Jobtitle, keywords>
    :str link: the original link to see the offer
    :datetime starting_date: date (, and hour) of the log into the table
    :str log: a string to append into de log
        for example: Charles, sent cv. Richard, etc
    :datetime notice: date on which you will be notified if you don't get any news before
    :Enum status: general status of the offer (pending, to-do, rejected)

    """
    print(
        f"""Adding to the table:
    recruiter: {recruiter_name}
    short description: {keywords}
    link: {link}
    starting date: {starting_date}
    log:
        {log}
    next notice: {notice}
    status: {status}
    """
    )


def update_offer():
    pass
