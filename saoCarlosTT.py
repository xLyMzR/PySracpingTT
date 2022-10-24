import os
import pandas as pd
import snscrape.modules.twitter as sntwitter
import seaborn as sns
import matplotlib.pyplot as plt
from PIL._imaging import display
dicionario = {}
user_list = []
data_treat_for_graph = []
anos = ['2016', '2017', '2018', '2019', '2020', '2021', '2022']
def main():
    print("ok")
    executar_menu()
    return 0


def executar_menu():
    # searchtwittsforuser("arturdmartins", 0)
    # dicionario_dump_to()
    # auto_search_all_user
     generate_graphical_view()
    # read_csv_treat_data()


def searchtwittsforuser(user, num_user):
    diretorio = fr"C:\\Users\\leona\\PycharmProjects\\pythonProject1\\Retornos\\{user}"
    if not os.path.isfile(f'{diretorio}.csv'):
        tweets_list1 = []
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{user}').get_items()):
            if i > 3000:
                break
            tweets_list1.append([tweet.date.year, tweet.id, tweet.content, tweet.media, tweet.user.username])

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
    for i, user in user_list:
        searchtwittsforuser(user, i)


def generate_graphical_view():
    # Getting currently and destination dir:
    patlocate = os.getcwd()
    final_locate = os.path.join(patlocate + "\\Graphics")
    # the patch for dir with csv files
    patlocate += os.path.join("\\RetornosTratados")
    print(patlocate)
    try:
        os.chdir(patlocate)
        for filename in os.listdir(patlocate):
            sns.set(style='whitegrid')
            f = os.path.join(patlocate, filename)
            if os.path.isfile(f):
                data_tt = pandas.read_csv(filename)
                data_tt.plot(x='Datetime', y='Freq', kind = 'bar')
                nome_arq_final = filename.replace('.csv', '.png')
                nome_arq_final = nome_arq_final.replace("tratado-", "graphic-")
                print(nome_arq_final)
                arch_save_file = os.path.join(final_locate + f"\\{nome_arq_final}")
                plt.savefig(f"{arch_save_file}")

    except RecursionError:
        print("Falha na leitura do diretorio")


def read_csv_treat_data():
    pat_locate = os.getcwd()
    pat_search = os.path.join(pat_locate + "\\Retornos")
    pat_save_file = os.path.join(pat_locate+"\\RetornosTratados")
    os.chdir(pat_search)
    print(pat_search)
    for filename in os.listdir(pat_search):
        if os.path.isfile(filename):
            dataf = pd.read_csv(filename)
            data = pd.DataFrame(dataf,columns=['Datetime'])
            data['Freq'] = data.groupby('Datetime')['Datetime'].transform('count')
            data = data.drop_duplicates()
            arch_name = os.path.join(pat_save_file +f"\\tratado-{filename}")
            data.to_csv(f"{arch_name}", sep=',')

        else:
            continue


if __name__ == '__main__':
    main()
