# -*- coding: utf-8 -*-
"""Demanda de Oxigenio.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sBeW3EBmnHyI4X_LVsHsPlF3FwNqwlnh
"""

#   "j": "A água apresenta OD > 4mg/L O2? "   fonte: https://www.siam.mg.gov.br/sla/download.pdf?idNorma=2747
od = input("Digite o valor de Demanda de oxigenio(OD m/L): ")
if od  > 4:
  print("Esta apropriada")
elif od <= 4:
  print("Não é apropriada")
else:
  print("valor invalido")