#
# @lc app=leetcode id=1185 lang=python3
#
# [1185] Day of the Week
#

# @lc code=start


from datetime import datetime

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        date_str = str(year) + '-' + str(month) + '-' + str(day)
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')

        weekday_name = date_obj.strftime('%A')

        return weekday_name

# @lc code=end

