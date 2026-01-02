# ref: https://towardsdatascience.com/outlier-detection-in-regression-using-cooks-distance-f5e4954461a0#:~:text=Outliers%20are%20defined%20as%20abnormal,right%20insight%20from%20the%20data.

# setup
"""_summary_
pip install shapash # for the house_prices data
"""
from shapash.data.data_loader import data_loading
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import OLSInfluence
import plotly.express as px

house_df, house_dict = data_loading('house_prices')
X_df = house_df

# model building/training
predictors = ['OverallQual', 'GrLivArea', 'TotalBsmtSF', 
              'YearBuilt', 'FullBath',	'HalfBath', 'GarageArea']
target = 'SalePrice'
model = sm.OLS(X_df[target], X_df[predictors].assign(const=1))
results = model.fit()
print(results.summary())

# influence
influence = OLSInfluence(results)
p = sm.graphics.influence_plot(results, criterion="cooks")
p.show()

# standized residuals
sresiduals = influence.resid_studentized_internal
df = pd.DataFrame(dict(ID=sresiduals.index, sresidual=sresiduals.values))
fig = px.box(df, y="sresidual", notched=True, hover_data=df.columns)
fig.show()

# Cooks distance
cooks = influence.cooks_distance[0]
df = pd.DataFrame(dict(ID=cooks.index, cooksd=cooks.values))
fig = px.violin(df, y="cooksd", box=True, points="outliers", hover_data=df.columns)
#fig = px.box(df, y="cooksd", notched=True, hover_data=df.columns)
fig.show()

# print the outlier
print(cooks.idxmax(), cooks.max())
print(X_df.iloc[cooks.idxmax(), :]) #[predictors])


