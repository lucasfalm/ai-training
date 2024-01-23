import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import helpers.custom_print as print_helpers

#
# NOTE: loading the data
#

base_credit = pd.read_csv("./src/csvs/credit_risk_dataset.csv")

#
# NOTE: visualizing the data
#

print_helpers.custom_print(base_credit.columns, printing=False)

print_helpers.custom_print(base_credit, printing=False)

print_helpers.custom_print(base_credit.head(), printing=False)

print_helpers.custom_print(base_credit.tail(), printing=False)

print_helpers.custom_print(base_credit.describe(), printing=False)

print_helpers.custom_print(
  base_credit[base_credit["person_income"] >= 100000],
  printing=False
)

print_helpers.custom_print(
  base_credit[
    (base_credit["cb_person_default_on_file"] != "N") &
    (base_credit["cb_person_default_on_file"] != "Y")
  ],
  printing=False
)

plt.hist(base_credit["person_income"])
# plt.show()

chart = px.scatter_matrix(
  base_credit,
  dimensions=["person_age", "person_income"],
  color="cb_person_default_on_file"
)
# chart.show()

#
# NOTE: treating invalid values
#

treated_base_credit = base_credit

#
# options:
#

#
# 1) can drop the entire column if there are many wrong records
#
# treated_base_credit = base_credit.drop("person_age", axis=1)

#
# 2) can drop only the records with wrong values
#
# wrong_records       = base_credit.loc[base_credit["person_age"] >= 100]
# treated_base_credit = base_credit.drop(wrong_records.index)

#
#  3) fix the values manually
#
average_age   = base_credit[base_credit["person_age"] < 100]["person_age"].mean()
wrong_records = base_credit.loc[base_credit["person_age"] >= 100]

treated_base_credit.loc[wrong_records.index] = average_age

print_helpers.custom_print(
  treated_base_credit[treated_base_credit["person_age"] > 100],
  printing=False
)
