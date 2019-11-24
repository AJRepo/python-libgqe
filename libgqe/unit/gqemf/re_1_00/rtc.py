"""
RTC actions

Copyright (c) Bernard Nauwelaerts 2019.
All rights reserved

This program is free software; you can redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation; version 2.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program;
if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

"""

import datetime
from libgqe.unit.gqemf import GQEMF
from libgqe.protocol.GQRFC1701.v1_00 import GETDATETIME, SETDATETIME
from libgqe.protocol.GQRFC1701.v1_00 import SETDATEDD, SETDATEMM, SETDATEYY, SETTIMEHH, SETTIMEMM, SETTIMESS


class RTC(GQEMF):
    """RTC class"""
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)

    def cmd_rtc_get(self, *args, **kwargs):
        """Retrieve unit date and time"""
        cmd = GETDATETIME.GETDATETIME(self.rw_functions, *args, **kwargs)
        cmd.send()
        return cmd.response

    def cmd_rtc_sync(self, *args, **kwargs):
        """Synchronize real time clock with local computer"""
        dt = datetime.datetime.now()
        cmd = SETDATETIME.SETDATETIME(self.rw_functions, *args, **kwargs)
        cmd.send(dt.year % 100, dt.month, dt.day, dt.hour, dt.minute, dt.second)

    def cmd_rtc_set_date_dd(self, dd=None, *args, **kwargs):
        """Set RTC date day"""
        cmd = SETDATEDD.SETDATEDD(self.rw_functions, dd, *args, **kwargs)
        cmd.send(dd)

    def cmd_rtc_set_date_mm(self, mm=None, *args, **kwargs):
        """Set RTC date month"""
        cmd = SETDATEMM.SETDATEMM(self.rw_functions, mm, *args, **kwargs)
        cmd.send(mm)

    def cmd_rtc_set_date_yy(self, yy=None, *args, **kwargs):
        """Set RTC date year"""
        cmd = SETDATEYY.SETDATEYY(self.rw_functions, yy, *args, **kwargs)
        cmd.send(yy)

    def cmd_rtc_set_time_hh(self, hh=None, *args, **kwargs):
        """Set RTC time hour"""
        cmd = SETTIMEHH.SETTIMEHH(self.rw_functions, hh, *args, **kwargs)
        cmd.send(hh)

    def cmd_rtc_set_time_mm(self, mm=None, *args, **kwargs):
        """Set RTC time minute"""
        cmd = SETTIMEMM.SETTIMEMM(self.rw_functions, mm, *args, **kwargs)
        cmd.send(mm)

    def cmd_rtc_set_time_ss(self, ss=None, *args, **kwargs):
        """Set RTC time second"""
        cmd = SETTIMESS.SETTIMESS(self.rw_functions, ss, *args, **kwargs)
        cmd.send(ss)
