import os
import pandas
import pandas as pd
import snscrape.modules.twitter as sntwitter
import seaborn as sns
import matplotlib.pyplot as plt


user_list = []


def main():
    print("ok")
    # load_user()
    # auto_search_all_user()
    generate_graphical_view()
    # searchtwittsforuser("vadiabaiana")
    return 0


def searchtwittsforuser(user):
    diretorio = fr"C:\\Users\\leona\\PycharmProjects\\pythonProject1\\Retornos\\{user}"
    if not os.path.exists(f'{diretorio}.csv'):
        tweets_list1 = []
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{user}').get_items()):
            if i > 3000:
                break
            tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.media, tweet.user.username])

        if tweets_list1.__len__() > 0:
            df = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Tweet', 'Media', 'Username'])

            df.to_csv(f'{diretorio}.csv', index=None, sep=',')
        else:
            return
    else:
        print(f"{user} já foi executado!")


def load_user():
    with open("users-twitter.txt", 'r') as f:
        cont = f.readlines()
        for us in cont:
            diretorio = fr"C:\\Users\\leona\\PycharmProjects\\pythonProject1\\Retornos\\{us}"
            if not os.path.exists(f'{diretorio}.csv'):
                user_list.append(us.strip())
            else:
                print("Não possui novos usuarios cadastrados no arquivo!")


def show_user():
    for user in user_list:
        print(user)


def auto_search_all_user():
    for user in user_list:
        searchtwittsforuser(user)


def generate_graphical_view():
    # Getting currently and destination dir:
    patlocate = os.getcwd()
    final_locate = os.path.join(patlocate + "\\Graphics")
    # the patch for dir with csv files
    patlocate += os.path.join("\\Retornos")
    print(patlocate)
    try:
        os.chdir(patlocate)
        for filename in os.listdir(patlocate):
            sns.set(style='whitegrid')
            f = os.path.join(patlocate, filename)
            if os.path.isfile(f):
                data_tt = pandas.read_csv(filename)
                sns.countplot(data_tt['Username'], data_tt['DateTime'])
                plt.savefig(f'{final_locate}{data_tt["Username"]}.png', dpi=300)
    except RecursionError:
        print("Falha na leitura do diretorio")


if __name__ == '__main__':
    main()
