from pathlib import Path
from numpy import number
import pandas as pd
import pprint
import scipy.stats as st

import matplotlib.pyplot as plt

def main():

	csv_path = Path("./df_factors.csv")
	orig_df = pd.read_csv(csv_path)


	working_df = orig_df.groupby("country")["mental_health_severity"].value_counts().unstack(fill_value=0)

	working_df["n_points"] = working_df.sum(axis=1)

	columns = working_df.columns.tolist()
	for elem in columns:
		if elem in working_df.columns:
			working_df_prop = working_df.div(working_df[elem], axis=0)

	country_prop_dict = {}

	for country in working_df_prop.index:
		country_weighted_total = 0;
		for i in range(len(working_df_prop.loc[country]) - 1):

			country_weighted_total += i * working_df_prop.loc[country].iloc[i]

		country_prop_dict[country] = country_weighted_total
		country_weighted_total = 0

	results_df = pd.DataFrame(country_prop_dict.items(), columns=["country", "severity"])

	n_points_list = working_df["n_points"].to_list()
	results_df["n_points"] = n_points_list

	n_points_total = results_df["n_points"].sum(axis=0)

	results_df["n_points_prop"] = results_df["n_points"].div(n_points_total, axis=0)

	weighted_severity_list = results_df["severity"].to_list()
	n_points_prop_list = results_df["n_points_prop"].to_list()

	for i in range(len(weighted_severity_list)):
		weighted_severity_list[i] = weighted_severity_list[i] * n_points_prop_list[i]

	results_df["weighted_severity"] = weighted_severity_list

	#pprint.pp(results_df)

	n_rows = len(results_df)
	#print(n_rows)

	us_severity = results_df.values[n_rows - 1][4]
	non_us_severity = 0

	for i in range(n_rows - 2):
		non_us_severity += results_df.values[i][4]

	pprint.pp(orig_df["country"])

	country_score_slices_df = pd.DataFrame()
	country_score_slices_df["country"] = orig_df["country"].copy()
	country_score_slices_df["severity"] = orig_df["mental_health_severity"].copy()

	pprint.pp(country_score_slices_df)

	us_df = country_score_slices_df[country_score_slices_df.country == "United States"]
	non_us_df = country_score_slices_df[country_score_slices_df.country != "United States"]

	pprint.pp(us_df)
	pprint.pp(non_us_df)

	us_avg = us_df[["severity"]].mean()
	non_us_avg = non_us_df[["severity"]].mean()
	print("us: "+ str(us_avg))
	print("non-us: " + str(non_us_avg))

	us_zscore = st.zscore(us_df[["severity"]])
	non_us_zscore = st.zscore(non_us_df[["severity"]])

	us_severity_list = us_df["severity"].to_list()
	non_us_severity_list = non_us_df["severity"].to_list()

	print(st.normaltest(us_df[["severity"]]))

	print(st.mannwhitneyu(us_severity_list, non_us_severity_list, alternative="less", axis=0, nan_policy="raise"))

	#print("us: " + str(us_severity))
	#print("non-us: " + str(non_us_severity))

	plt.hist(us_severity_list, bins=12, edgecolor="black", color="dodgerblue", alpha=0.7)
	plt.hist(non_us_severity_list, bins=12, edgecolor="black", color="tomato", alpha=0.7)

	plt.xlabel("Mental Health Severity Metric")
	plt.ylabel("# of Measurements")
	plt.title("Comparison of US and non-US Mental Health Severity Scores")
	#plt.legend()

	plt.show()

	#plt.violinplot([us_severity_list, non_us_severity_list])

	fig, ax = plt.subplots()

	parts = ax.violinplot([us_severity_list, non_us_severity_list], showmeans=False, showmedians=True)

	# Customizing colors
	colors = ['skyblue', 'salmon', 'lightgreen']
	for i, pc in enumerate(parts['bodies']):
	    pc.set_facecolor(colors[i])

	# Add labels and title
	ax.set_xlabel('Dataset')
	ax.set_ylabel('Value')
	ax.set_title('Customized Violin Plots')

	# Customize x-axis labels
	ax.set_xticks([1, 2])
	ax.set_xticklabels(['US Scores', 'Non-US Scores'])

	plt.show()

	return results_df

if __name__ == "__main__":
	main()