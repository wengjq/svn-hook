#!/usr/bin/python
# coding=utf-8
import sys
import os
import commands
import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='dat/svnadmin/fai-site/log/log.log',
                filemode='w')

def do_cmd(cmd):
    (status, output) = commands.getstatusoutput(cmd)
  
    # python 的小 bug，返回值要右移 8 位
    # http://bbs.chinaunix.net/thread-3666310-1-1.html
    return status >> 8

def get_file_list(repo, rev):
    """svnlook changed -r REV REPOS 获得发生变更的文件
    """
    cmd = '%s changed -r %s %s' % (svnlook_bin_path, rev, repo)
    output = os.popen(cmd).read()
    return output

def get_diff(repo, rev):
    """svnlook diff REV REPOS 获得文件变动
    """
    cmd = '%s diff -r %s %s' % (svnlook_bin_path, rev, repo)
    output = os.popen(cmd).read()
    return output 

def main(repo, rev):
    file_list = get_file_list(repo, rev)
    
    logging.info(file_list)
    
    if file_list.find("xxx") != -1 or file_list.find("xxx") != -1:
        content = get_diff(repo, rev).replace('"', "&quot;")
        logging.info(content)
        cmd = "curl -m 5 'xxx' -H 'Content-Type: application/json' -d '{\"msgtype\": \"text\", \"text\": {\"content\": \"" + content + "\"}}'"
        logging.info(cmd)
        do_cmd(cmd)

global svnlook_bin_path
if  __name__ =="__main__":
    svnlook_bin_path = '/usr/bin/svnlook' 
    main(sys.argv[1], sys.argv[2])
