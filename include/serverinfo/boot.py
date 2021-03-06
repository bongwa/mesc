#!/usr/bin/env python
# -*- coding: utf-8 -*-

__license__ = """

███╗   ███╗███████╗███████╗ ██████╗
████╗ ████║██╔════╝██╔════╝██╔════╝
██╔████╔██║█████╗  ███████╗██║
██║╚██╔╝██║██╔══╝  ╚════██║██║
██║ ╚═╝ ██║███████╗███████║╚██████╗
╚═╝     ╚═╝╚══════╝╚══════╝ ╚═════╝

MESC: Minimun Essential Security Checks

Author: https://twitter.com/1_mod_m/

Project site: https://github.com/1modm/mesc

Copyright (c) 2007-2015, Miguel Morillo
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. Neither the name of copyright holders nor the names of its
   contributors may be used to endorse or promote products derived
   from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
''AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL COPYRIGHT HOLDERS OR CONTRIBUTORS
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""

#------------------------------------------------------------------------------
# Modules
#------------------------------------------------------------------------------

import os
import json
from . import config
from .operations import execute_cmd, check_file_exact,\
                        exists_read_file, OS_dist


__all__ = [
    "fire"
]



#------------------------------------------------------------------------------
def fire(__host__, __user__, __passwd__, __port__, __jsonfile__, __subfolder__):
    """
    :returns: Output security check from json file
    :params: Target, User, Passwd, Port and Json file
    """
    
    if (__subfolder__ == "include/serverinfo/boot/"):
        __file__ = __subfolder__+__jsonfile__
    else:
        __file__ = __subfolder__+"/"+__jsonfile__

    with open(__file__) as data_file:
        data = json.loads(data_file.read())
        __help_result__ = data["help_result"]
        __command__ = data["command"]
        __distribution__, __env_shell__ = OS_dist(__host__, __user__, __passwd__, __port__)
        __type__ = data["type"]

        if __type__ == "execute_cmd":
            __cmd__ = data["distribution"][__distribution__]["cmd"]
            __output__, __command_check__ = execute_cmd(__cmd__, __env_shell__, __host__, __user__, __passwd__, __port__)

        if __type__ == "exists_read_file":
            __file__ = data["distribution"][__distribution__]["file"]
            __cmd_check__, __output__ = exists_read_file(__file__, __env_shell__, __host__, __user__, __passwd__, __port__)
        
            if (__cmd_check__):
                __command_check__ = config.CHECKRESULTOK
                __cmd__ = __file__
            else:
                __command_check__ = config.CHECKRESULTERROR
                __cmd__ = __file__

        if __type__ == "check_file_exact":
            __file__ = data["distribution"][__distribution__]["file"]
            __check__ = [data["distribution"][__distribution__]["chk"]]
            __cmd_check__, __output__ = exists_read_file(__file__, __env_shell__, __host__, __user__, __passwd__, __port__)
            
            if not __cmd_check__:
                __command_check__ = config.CHECKRESULTERROR
                __cmd__ = __file__
            else:
                __command_check__, __line__, __linehtml__, __check_count__ =\
                check_file_exact(__file__, __check__, __env_shell__, __host__, __user__, __passwd__,
                                 __port__)
                if (data["level"] != ""):
                    __level__ = int(data["level"])  
                    if (__command_check__ == config.CHECKRESULTWARNING and __level__ > config.VALUECRITICAL):
                        __command_check__ = config.CHECKRESULTCRITICAL

                __recommendations__ = data["recommendations"]

                if __command_check__ == config.CHECKRESULTCRITICAL:
                    __output__ = __recommendations__
                else:
                    __output__ = config.CHECKRESULTOK

                __cmd__ = __file__

        if __type__ == "check_file_exact_load":
            __file__ = data["distribution"][__distribution__]["file"]
            __check__ = [data["distribution"][__distribution__]["chk"]]
            __cmd_check__, __output__ = exists_read_file(__file__, __env_shell__, __host__, __user__, __passwd__, __port__)
            
            if not __cmd_check__:
                __command_check__ = config.CHECKRESULTERROR
                __cmd__ = __file__
            else:
                __command_check__, __line__, __linehtml__, __check_count__ =\
                check_file_exact(__file__, __check__, __env_shell__, __host__, __user__, __passwd__,
                                 __port__)
                __cmd__ = __file__
                
        if __command_check__ == config.CHECKRESULTOK:
            __check_message__ = data["result"]["checkresultok"]["check_message"]
            __check_html_message__ = data["result"]["checkresultok"]["check_html_message"]
        elif __command_check__ == config.CHECKRESULTWARNING:
            __check_message__ = data["result"]["checkresultwarning"]["check_message"]
            __check_html_message__ = data["result"]["checkresultwarning"]["check_html_message"]
        elif __command_check__ == config.CHECKRESULTCRITICAL:
            __check_message__ = data["result"]["checkresultcritical"]["check_message"]
            __check_html_message__ = data["result"]["checkresultcritical"]["check_html_message"]
        elif __command_check__ == config.CHECKRESULTERROR:
            __check_message__ = data["result"]["checkresulterror"]["check_message"]
            __check_html_message__ = data["result"]["checkresulterror"]["check_html_message"]

    return (__output__.decode("ascii", "ignore"), __help_result__, __command_check__, __check_message__,
            __check_html_message__, __command__, __cmd__)

