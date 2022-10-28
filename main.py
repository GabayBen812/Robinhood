import sys
import csv
import pandas as pd

def main():
    path_to_mails = "mails.txt"
    emails = []

    promo = sys.argv[1]
    print("Promo Code: " + promo)

    print(read_emails(path_to_mails))
    
    write_to_logs("exmail@gmail.com")


if __name__ == '__main__':
    main()


def read_emails(path):
    emails_list = []
    with open(path) as csvfile:
        data = csvfile.readlines()

    for i in data:
        emails_list.append(i.replace("\n", "").replace(" ", ""))

    return emails_list


# Use This Func Everytime User Is Ready. Arg: "mail"
def write_to_logs(completedEmail):
    print("Email Is Ready To Use: " + completedEmail)
    emails.append(completedEmail)
    d = {'Emails': emails}
    df = pd.DataFrame(data=d)
    df.to_csv("exfile", sep='\t', encoding='utf-8')


