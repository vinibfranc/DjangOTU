# from django.core.management.base import BaseCommand
# from app.models import Amostra, Taxonomia, Frequencia
# import csv
# import pandas as pd

# class Command(BaseCommand):

#     def popula_amostra(self, arquivo):
#         with open(arquivo, newline='') as tsvfile:
#             reader = csv.reader(tsvfile, delimiter="\t")
#             amostras = next(reader)
#         amostras = amostras[1:-1]
#         print(amostras)
#         for i in range(len(amostras)):
#             amostra_db = Amostra(codigo=amostras[i])
#             print(amostra_db)
#             amostra_db.save()
    
#     def popula_taxonomia(self, arquivo):
#         tax_file = pd.read_csv(arquivo, sep = '\t') 
#         tax_col = tax_file.OTU
#         tax_col = tax_col.iloc[1:]
#         print(tax_col)
#         tax_str = tax_col.values.tolist()
#         print(tax_str)
#         for i in range(len(tax_str)):
#             tax_db = Taxonomia(especie=tax_str[i])
#             print(tax_db)
#             tax_db.save()
    
#     def popula_frequencia(self, arquivo):
#         with open() as tsvfile:
#             for row in csv.reader(tsvfile, delimiter='\t'):
#                 for col in row:
#                     pass
                    
        

#     def handle(self, *args, **options):
#         self.popula_amostra("app/files/otu_table_tax_amostras.tsv")
#         self.popula_taxonomia("app/files/otu_table_tax_amostras.tsv")
#         self.popula_frequencia("app/files/otu_table_tax_amostras.tsv")

# def main():
#     command = Command()

# if __name__ == '__main__':
#     main()