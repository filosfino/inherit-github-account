import requests
import argparse
import getpass


GITHUB_API_PROXY = 'https://api.github.com'


def parse_command_line():
    parser = argparse.ArgumentParser(
        description='Follow who he follow, star what he star',
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument('-a', '--auth',
                        metavar='USERNAME',
                        help='your github account username')
    parser.add_argument('target',
                        metavar='TARGET',
                        help='the target you want to copy')

    args = parser.parse_args()

    password = getpass.getpass('Enter your Github account password: ') if args.auth else None
    return args.auth, password, args.target


def follow_him(s, target):
    print('>> ******\n>> He followed ...')
    resp = s.get(GITHUB_API_PROXY + '/users/%s/following' % target)
    following_list = [following['url'].split('/')[-1] for following in resp.json()]
    for user in following_list:
        if USERNAME:
            s.put(GITHUB_API_PROXY + '/user/following/%s' % user)
        print(user)
    if USERNAME:
        print('>> following done\n')


def star_him(s, target):
    print('>> ******\n>> He starred ...')
    resp = s.get(GITHUB_API_PROXY + '/users/%s/starred' % target)
    starred_list = [repo['full_name'] for repo in resp.json()]
    for repo in starred_list:
        if USERNAME:
            s.put(GITHUB_API_PROXY + '/user/starred/%s' % repo)
        print(repo)
    if USERNAME:
        print('>> starring done\n')


def main():
    s = requests.Session()
    if USERNAME and PASSWORD:
        s.auth = (USERNAME, PASSWORD)

    follow_him(s, TARGET)
    star_him(s, TARGET)


if __name__ == '__main__':
    USERNAME, PASSWORD, TARGET = parse_command_line()
    main()
