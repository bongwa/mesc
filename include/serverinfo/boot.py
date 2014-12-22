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

Copyright (c) 2014, Miguel Morillo
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
from . import config
from .operations import execute_cmd, check_file_exact,\
                        exists_read_file, OS_dist


__all__ = [
    "grub",
    "rc3",
    "initservices",
    "grubterminal"
]


def grub(__host__, __user__, __passwd__, __port__):
    """
    :returns: grub configuration.
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "Grub configuration"
    __cmd__ = "cat /boot/grub/grub.cfg"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__,
         __passwd__, __port__)
    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to load configuration'
        __check_html_message__ = 'Unable to load configuration'
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __cmd__)

#------------------------------------------------------------------------------


def rc3(__host__, __user__, __passwd__, __port__):
    """
    :returns: rc3 level.
    :param host: Target.
    """
    __help_result__ = 'Started applications in the rc3.d level'
    __help_result__ += os.linesep
    __command__ = "rc3.d level"
    __cmd__ = "ls -ltr /etc/rc3.d/S*"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__,
         __passwd__, __port__)
    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to load configuration'
        __check_html_message__ = 'Unable to load configuration'
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __cmd__)


#------------------------------------------------------------------------------


def initservices(__host__, __user__, __passwd__, __port__):
    """
    :returns: list all available services.
    :param host: Target.
    """
    __help_result__ = 'List all available services and specify in which'
    __help_result__ += ' runlevel start a service'
    __help_result__ += os.linesep
    __command__ = "List all available services"
    __distribution__ = OS_dist(__host__, __user__, __passwd__, __port__)

    if (__distribution__ == "RedHat"):
        __cmd__ = "chkconfig --list"
    elif (__distribution__ == "SuSE"):
        __cmd__ = "chkconfig --list"
    elif (__distribution__ == "debian"):
        __cmd__ = "service --status-all"
    elif (__distribution__ == "mandrake"):
        __cmd__ = "chkconfig --list"
    else:
        __cmd__ = "service --status-all"

    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__,
         __passwd__, __port__)
    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to load configuration'
        __check_html_message__ = 'Unable to load configuration'
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __cmd__)


#------------------------------------------------------------------------------


def grubterminal(__host__, __user__, __passwd__, __port__):
    """
    :returns: Disable graphical terminal
    :param host: Target.
    """
    __help_result__ = 'To see all the kernel messages fly by as it boots'
    __help_result__ += os.linesep
    __command__ = "Disable graphical terminal"
    __distribution__ = OS_dist(__host__, __user__, __passwd__, __port__)

    if (__distribution__ == "RedHat"):
        __file__ = "/etc/default/grub"
        __check__ = ['GRUB_TERMINAL=console']
    elif (__distribution__ == "SuSE"):
        __file__ = "/etc/default/grub"
        __check__ = ['GRUB_TERMINAL=console']
    elif (__distribution__ == "debian"):
        __file__ = "/etc/default/grub"
        __check__ = ['GRUB_TERMINAL=console']
    elif (__distribution__ == "mandrake"):
        __file__ = "/etc/default/grub"
        __check__ = ['GRUB_TERMINAL=console']
    else:
        __file__ = "/etc/default/grub"
        __check__ = ['GRUB_TERMINAL=console']

    __cmd_check__, __output__ = exists_read_file(__file__, __host__, __user__,
                                                 __passwd__, __port__)

    if not __cmd_check__:
        __command_check__ = config.CHECKRESULTERROR
    else:
        __command_check__, __line__, __linehtml__, __check_count__ =\
        check_file_exact(__file__, __check__, __host__, __user__, __passwd__,
                         __port__)

    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = 'Grub graphical terminal disabled'
        __check_html_message__ = 'Grub graphical terminal disabled'
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to load configuration'
        __check_html_message__ = 'Unable to load configuration'
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = 'Recomended to disable Grub graphical terminal'
        __check_message__ += ' with: ' + __check__[0]
        __check_html_message__ = 'Recomended to disable Grub graphical terminal'
        __check_html_message__ += ' with: ' + __check__[0]
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __file__)

