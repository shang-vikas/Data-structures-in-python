import requests
import pandas as pd
import numpy as np
import json


def get_url(URL,args=None):
    '''
    This function downloads the URL and returns response.content
    '''
    if args is None:
        resp = requests.get(URL)
    else:
        resp = requests.get(URL,params=args)
    return resp.content

def main():
    import argparse
    # from tabulate import tabulate
    parser = argparse.ArgumentParser(description="Simply returns urls response")
    arguments = parser.add_argument_group("required params")
    arguments.add_argument('-u','--URL',dest='URL',type=str,required=True,help="URL to download")
    
    parser.add_arguments("-a","--args",dest='args',default=None)

    argss = parser.parse_args()

    resp = get_url(argss.URL,argss.args)
    print(f'this is the response - {resp.content}')

if __name__=='__main__':
    main()
