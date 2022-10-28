import sys
import csv

def main():
    path_to_mails = "mails.txt"

    promo = sys.argv[1]
    print("Promo Code: " + promo)

    print(read_emails(path_to_mails))


if __name__ == '__main__':
    main()


def read_emails(path):
    emails_list = []
    with open(path) as csvfile:
        data = csvfile.readlines()

    for i in data:
        emails_list.append(i.replace("\n", "").replace(" ", ""))

    return emails_list


