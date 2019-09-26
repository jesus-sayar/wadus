Wadus
########################################

A Cloud basic tool.

SYNOPSYS
    wadus [aws|gce] list
DESCRIPTIONq
    wadus is a cloud basic tool. The default region is eu-west-1,
    you can change the region using the AWS_DEFAULT_REGION environment variable.
OPTIONS
    -t output_type
        Decide how to output the results. Valid options 'csv', 'table' (Default)
    -f output_filename
        File in which to dump the results in case csv output type is selected. Default value 'output'
PARAMETERS
    instances
        list all running instances
    amis
        list all your AMIs
    elbs
        list all elastic load balancers
AUTHOR
    Jesús Sayar Celestino <https://github.com/jesus-sayar>
COPYRIGHT
    Copyright ©2017
    Lic. GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
    This is free software: you are free to change and redistribute it. There is
    NO WARRANTY, to the extent permitted by law.
