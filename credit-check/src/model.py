import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv("./src/csvs/credit_risk_dataset.csv")
print(base_credit)