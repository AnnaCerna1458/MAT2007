import pandas as pd

import numpy as np

import matplotlib.pyplot as plt


# ----------------------------------------------------------------------------------------------
# 1. Reading the data from the CSV file, checking its contents,
# and creating two groups for comparison: current-smokers and never-smokers.

# Read the data from the CSV file.
data = pd.read_csv("smoking_driking_dataset_Ver01.csv")


# Checking that the correct amount of rows and columns have been read.
print(f"Number of rows: {data.shape[0]}")
print(f"Number of columns: {data.shape[1]}")


# Checking how many people in the dataset are current-smokers, never-smokers, and former-smokers.
print(data["SMK_stat_type_cd"].value_counts())


# Creating two groups for comparison: current-smokers and never-smokers.
current_smokers = data[data["SMK_stat_type_cd"] == 3]
never_smokers = data[data["SMK_stat_type_cd"] == 1]


# Checking the sex proportions among current-smokers and never-smokers.
print("Sex proportions among current smokers:")
print(current_smokers["sex"].value_counts(normalize=True))

print("Sex proportions among never-smokers:")
print(never_smokers["sex"].value_counts(normalize=True))


# Creating separate groups for male and female current-smokers and never-smokers.
male_current_smokers = current_smokers[current_smokers["sex"] == "Male"]
female_current_smokers = current_smokers[current_smokers["sex"] == "Female"]
male_never_smokers = never_smokers[never_smokers["sex"] == "Male"]
female_never_smokers = never_smokers[never_smokers["sex"] == "Female"]

print(f"Male current smokers: {len(male_current_smokers)}")
print(f"Female current smokers: {len(female_current_smokers)}")
print(f"Male never smokers: {len(male_never_smokers)}")
print(f"Female never smokers: {len(female_never_smokers)}")
# ----------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------
# 2. Creating helper functions.

# A. Creating a function to calculate the mean and uncertainty of a dataset using the subsampling method.
def calculate_mean_and_uncertainty(data_values, number_of_subsamples):

    # Splitting the data into subsamples.
    subsamples = np.array_split(data_values, number_of_subsamples)

    # Calculating the mean for each subsample, and then calculating the mean of those means
    # and the standard deviation of those means.
    means = []

    for subsample in subsamples:
        means.append(np.mean(subsample))

    mean_of_means = np.mean(means)
    uncertainty = np.std(means)

    # Returning the mean, uncertainty, and the subsample means.
    return mean_of_means, uncertainty, np.array(means)


# B. Creating a function to compare the mean and uncertainty of two datasets,
# and determine whether the difference is statistically significant.
def compare_means_and_uncertainties(mean_current, subsample_means_current,
                                    mean_never, subsample_means_never):

    # Calculating the difference between the current-smoker and never-smoker
    # mean for each pair of subsamples.
    subsample_differences = subsample_means_current - subsample_means_never

    # Calculating the mean difference and the standard deviation
    # of the subsample differences.
    mean_difference = np.mean(subsample_differences)
    difference_uncertainty = np.std(subsample_differences)

    # Calculating how many sigmas the difference is away from zero.
    sigma_difference = abs(mean_difference) / difference_uncertainty

    # Determining whether the difference is statistically significant.
    if sigma_difference > 3:
        significance = "statistically significant"
    else:
        significance = "NOT statistically significant"

    # Returning the significance, mean difference, uncertainty of the difference,
    # and sigma difference.
    return significance, mean_difference, difference_uncertainty, sigma_difference
# ----------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------
# 3. Creating a function to compare the mean triglyceride levels of current-smokers and never-smokers.

def compare_triglyceride():

    # Assigning variables for the triglyceride levels of current-smokers and never-smokers.
    triglyceride_current = current_smokers["triglyceride"]
    triglyceride_never = never_smokers["triglyceride"]

    # Calculating their means and uncertainties using the helper function.
    mean_current_triglyceride, uncertainty_current_triglyceride, subsample_means_current_triglyceride = calculate_mean_and_uncertainty(
        triglyceride_current, 50
    )

    mean_never_triglyceride, uncertainty_never_triglyceride, subsample_means_never_triglyceride = calculate_mean_and_uncertainty(
        triglyceride_never, 50
    )

    # Comparing the means and uncertainties using the helper function.
    significance_triglyceride, mean_difference_triglyceride, difference_uncertainty_triglyceride, sigma_difference_triglyceride = compare_means_and_uncertainties(
        mean_current_triglyceride, subsample_means_current_triglyceride,
        mean_never_triglyceride, subsample_means_never_triglyceride
    )

    # Returning the results.
    return (
        mean_current_triglyceride,
        uncertainty_current_triglyceride,
        mean_never_triglyceride,
        uncertainty_never_triglyceride,
        mean_difference_triglyceride,
        difference_uncertainty_triglyceride,
        sigma_difference_triglyceride,
        significance_triglyceride
    )
# ----------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------
# 4. Creating a function to compare the mean height of current-smokers and never-smokers.

def compare_height():

    # Assigning variables for the height of current-smokers and never-smokers.
    height_current = current_smokers["height"]
    height_never = never_smokers["height"]

    # Calculating their means and uncertainties using the helper function.
    mean_current_height, uncertainty_current_height, subsample_means_current_height = calculate_mean_and_uncertainty(
        height_current, 50
    )

    mean_never_height, uncertainty_never_height, subsample_means_never_height = calculate_mean_and_uncertainty(
        height_never, 50
    )

    # Comparing the means and uncertainties using the helper function.
    significance_height, mean_difference_height, difference_uncertainty_height, sigma_difference_height = compare_means_and_uncertainties(
        mean_current_height, subsample_means_current_height,
        mean_never_height, subsample_means_never_height
    )

    # Returning the results.
    return (
        mean_current_height,
        uncertainty_current_height,
        mean_never_height,
        uncertainty_never_height,
        mean_difference_height,
        difference_uncertainty_height,
        sigma_difference_height,
        significance_height
    )
# ---------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------
# 5. Calling the functions and printing the results.

# Calling the function for triglyceride results and storing them in variables.
(
    mean_current_triglyceride,
    uncertainty_current_triglyceride,
    mean_never_triglyceride,
    uncertainty_never_triglyceride,
    mean_difference_triglyceride,
    difference_uncertainty_triglyceride,
    sigma_difference_triglyceride,
    significance_triglyceride
) = compare_triglyceride()


# Calling the function for height results and storing them in variables.
(
    mean_current_height,
    uncertainty_current_height,
    mean_never_height,
    uncertainty_never_height,
    mean_difference_height,
    difference_uncertainty_height,
    sigma_difference_height,
    significance_height
) = compare_height()


# Printing the results for triglyceride and height comparisons.
print("Triglyceride Results:")
print(f"Mean of current-smokers: {mean_current_triglyceride:.2f} mg/dL ± {uncertainty_current_triglyceride:.2f}")
print(f"Mean of never-smokers: {mean_never_triglyceride:.2f} mg/dL ± {uncertainty_never_triglyceride:.2f}")
print(f"Difference: {mean_difference_triglyceride:.2f} mg/dL ± {difference_uncertainty_triglyceride:.2f}")
print(f"Sigma Difference: {sigma_difference_triglyceride:.2f}")
print(f"Significance: {significance_triglyceride}")
print()  # Adding a blank line.


print("Height Results:")
print(f"Mean of current-smokers: {mean_current_height:.2f} cm ± {uncertainty_current_height:.2f}")
print(f"Mean of never-smokers: {mean_never_height:.2f} cm ± {uncertainty_never_height:.2f}")
print(f"Difference: {mean_difference_height:.2f} cm ± {difference_uncertainty_height:.2f}")
print(f"Sigma Difference: {sigma_difference_height:.2f}")
print(f"Significance: {significance_height}")
# --------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------
# 6. Doing the exact same analysis for male and female subgroups, and printing the results.

def compare_triglyceride_by_sex():

    # Assigning variables for the triglyceride levels of male and female current-smokers and never-smokers.
    triglyceride_male_current = male_current_smokers["triglyceride"]
    triglyceride_female_current = female_current_smokers["triglyceride"]
    triglyceride_male_never = male_never_smokers["triglyceride"]
    triglyceride_female_never = female_never_smokers["triglyceride"]

    # Calculating their means and uncertainties using the helper function.
    mean_male_current_triglyceride, uncertainty_male_current_triglyceride, subsample_means_male_current_triglyceride = calculate_mean_and_uncertainty(
        triglyceride_male_current, 50
    )

    mean_female_current_triglyceride, uncertainty_female_current_triglyceride, subsample_means_female_current_triglyceride = calculate_mean_and_uncertainty(
        triglyceride_female_current, 50
    )

    mean_male_never_triglyceride, uncertainty_male_never_triglyceride, subsample_means_male_never_triglyceride = calculate_mean_and_uncertainty(
        triglyceride_male_never, 50
    )

    mean_female_never_triglyceride, uncertainty_female_never_triglyceride, subsample_means_female_never_triglyceride = calculate_mean_and_uncertainty(
        triglyceride_female_never, 50
    )

    # Comparing the means and uncertainties using the helper function.
    significance_male_triglyceride, mean_difference_male_triglyceride, difference_uncertainty_male_triglyceride, sigma_difference_male_triglyceride = compare_means_and_uncertainties(
        mean_male_current_triglyceride, subsample_means_male_current_triglyceride,
        mean_male_never_triglyceride, subsample_means_male_never_triglyceride
    )

    significance_female_triglyceride, mean_difference_female_triglyceride, difference_uncertainty_female_triglyceride, sigma_difference_female_triglyceride = compare_means_and_uncertainties(
        mean_female_current_triglyceride, subsample_means_female_current_triglyceride,
        mean_female_never_triglyceride, subsample_means_female_never_triglyceride
    )

    # Returning the results.
    return (
        (mean_male_current_triglyceride, uncertainty_male_current_triglyceride,
         mean_male_never_triglyceride, uncertainty_male_never_triglyceride,
         mean_difference_male_triglyceride, difference_uncertainty_male_triglyceride,
         sigma_difference_male_triglyceride, significance_male_triglyceride),

        (mean_female_current_triglyceride, uncertainty_female_current_triglyceride,
         mean_female_never_triglyceride, uncertainty_female_never_triglyceride,
         mean_difference_female_triglyceride, difference_uncertainty_female_triglyceride,
         sigma_difference_female_triglyceride, significance_female_triglyceride)
    )


def compare_height_by_sex():

    # Assigning variables for the height of male and female current-smokers and never-smokers.
    height_male_current = male_current_smokers["height"]
    height_female_current = female_current_smokers["height"]
    height_male_never = male_never_smokers["height"]
    height_female_never = female_never_smokers["height"]

    # Calculating their means and uncertainties using the helper function.
    mean_male_current_height, uncertainty_male_current_height, subsample_means_male_current_height = calculate_mean_and_uncertainty(
        height_male_current, 50
    )

    mean_female_current_height, uncertainty_female_current_height, subsample_means_female_current_height = calculate_mean_and_uncertainty(
        height_female_current, 50
    )

    mean_male_never_height, uncertainty_male_never_height, subsample_means_male_never_height = calculate_mean_and_uncertainty(
        height_male_never, 50
    )

    mean_female_never_height, uncertainty_female_never_height, subsample_means_female_never_height = calculate_mean_and_uncertainty(
        height_female_never, 50
    )

    # Comparing the means and uncertainties using the helper function.
    significance_male_height, mean_difference_male_height, difference_uncertainty_male_height, sigma_difference_male_height = compare_means_and_uncertainties(
        mean_male_current_height, subsample_means_male_current_height,
        mean_male_never_height, subsample_means_male_never_height
    )

    significance_female_height, mean_difference_female_height, difference_uncertainty_female_height, sigma_difference_female_height = compare_means_and_uncertainties(
        mean_female_current_height, subsample_means_female_current_height,
        mean_female_never_height, subsample_means_female_never_height
    )

    # Returning the results.
    return (
        (mean_male_current_height, uncertainty_male_current_height,
         mean_male_never_height, uncertainty_male_never_height,
         mean_difference_male_height, difference_uncertainty_male_height,
         sigma_difference_male_height, significance_male_height),

        (mean_female_current_height, uncertainty_female_current_height,
         mean_female_never_height, uncertainty_female_never_height,
         mean_difference_female_height, difference_uncertainty_female_height,
         sigma_difference_female_height, significance_female_height)
    )


# Printing the results for triglyceride and height comparisons by sex.

# Printing the results for male and female triglyceride comparisons.
male_triglyceride_results, female_triglyceride_results = compare_triglyceride_by_sex()


(
    mean_male_current_triglyceride,
    uncertainty_male_current_triglyceride,
    mean_male_never_triglyceride,
    uncertainty_male_never_triglyceride,
    mean_difference_male_triglyceride,
    difference_uncertainty_male_triglyceride,
    sigma_difference_male_triglyceride,
    significance_male_triglyceride
) = male_triglyceride_results


(
    mean_female_current_triglyceride,
    uncertainty_female_current_triglyceride,
    mean_female_never_triglyceride,
    uncertainty_female_never_triglyceride,
    mean_difference_female_triglyceride,
    difference_uncertainty_female_triglyceride,
    sigma_difference_female_triglyceride,
    significance_female_triglyceride
) = female_triglyceride_results


print("Triglyceride Results by Sex:")
print(f"Male Current Smokers: {mean_male_current_triglyceride:.2f} mg/dL ± {uncertainty_male_current_triglyceride:.2f}")
print(f"Male Never Smokers: {mean_male_never_triglyceride:.2f} mg/dL ± {uncertainty_male_never_triglyceride:.2f}")
print(f"Difference: {mean_difference_male_triglyceride:.2f} mg/dL ± {difference_uncertainty_male_triglyceride:.2f}")
print(f"Sigma Difference: {sigma_difference_male_triglyceride:.2f}")
print(f"Significance: {significance_male_triglyceride}")
print()  # Adding a blank line.


print(f"Female Current Smokers: {mean_female_current_triglyceride:.2f} mg/dL ± {uncertainty_female_current_triglyceride:.2f}")
print(f"Female Never Smokers: {mean_female_never_triglyceride:.2f} mg/dL ± {uncertainty_female_never_triglyceride:.2f}")
print(f"Difference: {mean_difference_female_triglyceride:.2f} mg/dL ± {difference_uncertainty_female_triglyceride:.2f}")
print(f"Sigma Difference: {sigma_difference_female_triglyceride:.2f}")
print(f"Significance: {significance_female_triglyceride}")
print()  # Adding a blank line.


# Printing the results for male and female height comparisons.
male_height_results, female_height_results = compare_height_by_sex()


(
    mean_male_current_height,
    uncertainty_male_current_height,
    mean_male_never_height,
    uncertainty_male_never_height,
    mean_difference_male_height,
    difference_uncertainty_male_height,
    sigma_difference_male_height,
    significance_male_height
) = male_height_results


(
    mean_female_current_height,
    uncertainty_female_current_height,
    mean_female_never_height,
    uncertainty_female_never_height,
    mean_difference_female_height,
    difference_uncertainty_female_height,
    sigma_difference_female_height,
    significance_female_height
) = female_height_results


print("Height Results by Sex:")
print(f"Male Current Smokers: {mean_male_current_height:.2f} cm ± {uncertainty_male_current_height:.2f}")
print(f"Male Never Smokers: {mean_male_never_height:.2f} cm ± {uncertainty_male_never_height:.2f}")
print(f"Difference: {mean_difference_male_height:.2f} cm ± {difference_uncertainty_male_height:.2f}")
print(f"Sigma Difference: {sigma_difference_male_height:.2f}")
print(f"Significance: {significance_male_height}")
print()  # Adding a blank line.


print(f"Female Current Smokers: {mean_female_current_height:.2f} cm ± {uncertainty_female_current_height:.2f}")
print(f"Female Never Smokers: {mean_female_never_height:.2f} cm ± {uncertainty_female_never_height:.2f}")
print(f"Difference: {mean_difference_female_height:.2f} cm ± {difference_uncertainty_female_height:.2f}")
print(f"Sigma Difference: {sigma_difference_female_height:.2f}")
print(f"Significance: {significance_female_height}")
# --------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# 7. Creating plots to visualise the results.
# --------------------------------------------------------------------------------------------

# A. Triglyceride comparison plot.

# Creating a bar plot to compare the mean triglyceride levels of current-smokers and never-smokers,
# including error bars for uncertainties.

groups = ["Overall", "Male", "Female"]

x = np.arange(len(groups))


# Creating the means and uncertainties for current-smokers and never-smokers.
current_triglyceride_means = [
    mean_current_triglyceride,
    mean_male_current_triglyceride,
    mean_female_current_triglyceride
]


never_triglyceride_means = [
    mean_never_triglyceride,
    mean_male_never_triglyceride,
    mean_female_never_triglyceride
]


# Creating the uncertainties for current-smokers and never-smokers.
current_triglyceride_uncertainties = [
    uncertainty_current_triglyceride,
    uncertainty_male_current_triglyceride,
    uncertainty_female_current_triglyceride
]


never_triglyceride_uncertainties = [
    uncertainty_never_triglyceride,
    uncertainty_male_never_triglyceride,
    uncertainty_female_never_triglyceride
]


# Creating the plot with error bars for uncertainties.
plt.figure(figsize=(8, 5))


# Plotting current smokers.
plt.errorbar(
    x - 0.07,
    current_triglyceride_means,
    yerr=current_triglyceride_uncertainties,
    fmt="o",
    color="#D55E00",
    markersize=6,
    capsize=4,
    elinewidth=1.5,
    label="Current smokers"
)


# Plotting never-smokers.
plt.errorbar(
    x + 0.07,
    never_triglyceride_means,
    yerr=never_triglyceride_uncertainties,
    fmt="o",
    color="#0072B2",
    markersize=6,
    capsize=4,
    elinewidth=1.5,
    label="Never-smokers"
)


# Adding the mean values next to the current-smoker points.
for i in range(len(groups)):
    plt.text(
        x[i] - 0.07 + 0.03,
        current_triglyceride_means[i],
        f"{current_triglyceride_means[i]:.1f}",
        ha="left",
        va="center",
        color="#D55E00",
        fontsize=10
    )


# Adding the mean values next to the never-smoker points.
for i in range(len(groups)):
    plt.text(
        x[i] + 0.07 + 0.03,
        never_triglyceride_means[i],
        f"{never_triglyceride_means[i]:.1f}",
        ha="left",
        va="center",
        color="#0072B2",
        fontsize=10
    )


# Naming the axes and title and adding a legend.
plt.xticks(x, groups)
plt.xlim(-0.25, 2.35)  # making sure the x-axis limits are set to show all points and error bars clearly
plt.ylabel("Mean Triglyceride Level (mg/dL)")
plt.title("Mean Triglyceride Levels by Smoking Status")
plt.legend()
plt.grid(axis="y", alpha=0.2)

plt.tight_layout()
plt.show()
# --------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------
# B. Height comparison plot.

# Creating a point plot to compare the mean height of current-smokers
# and never-smokers, including error bars for uncertainties.


# Creating the means for current-smokers and never-smokers.
current_height_means = [
    mean_current_height,
    mean_male_current_height,
    mean_female_current_height
]


never_height_means = [
    mean_never_height,
    mean_male_never_height,
    mean_female_never_height
]


# Creating the uncertainties for current-smokers and never-smokers.
current_height_uncertainties = [
    uncertainty_current_height,
    uncertainty_male_current_height,
    uncertainty_female_current_height
]


never_height_uncertainties = [
    uncertainty_never_height,
    uncertainty_male_never_height,
    uncertainty_female_never_height
]


# Creating the plot.
plt.figure(figsize=(7, 4))


# Plotting current smokers.
plt.errorbar(
    x - 0.07,
    current_height_means,
    yerr=current_height_uncertainties,
    fmt="o",
    color="#D55E00",
    markersize=4,
    capsize=3,
    elinewidth=1.3,
    label="Current smokers"
)


# Plotting never-smokers.
plt.errorbar(
    x + 0.07,
    never_height_means,
    yerr=never_height_uncertainties,
    fmt="o",
    color="#0072B2",
    markersize=4,
    capsize=3,
    elinewidth=1.3,
    label="Never-smokers"
)


# Adding the mean values next to the current-smoker points.
for i in range(len(groups)):
    plt.text(
        x[i] - 0.07 + 0.03,
        current_height_means[i],
        f"{current_height_means[i]:.1f}",
        ha="left",
        va="center",
        color="#D55E00",
        fontsize=10
    )


# Adding the mean values next to the never-smoker points.
for i in range(len(groups)):
    plt.text(
        x[i] + 0.07 + 0.03,
        never_height_means[i],
        f"{never_height_means[i]:.1f}",
        ha="left",
        va="center",
        color="#0072B2",
        fontsize=10
    )


# Naming the axes and title and adding a legend.
plt.xticks(x, groups)
plt.xlim(-0.25, 2.35)
plt.ylabel("Mean Height (cm)")
plt.ylim(154, 170.5)
plt.title("Mean Height by Smoking Status")
plt.legend()
plt.grid(axis="y", alpha=0.2)

plt.tight_layout()
plt.show()
# --------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------
# C. Sex composition plot.

# Creating a stacked bar plot to show the sex composition of current-smokers and never-smokers.

# Getting the counts of males and females in current-smokers and never-smokers.
current_smokers_sex_counts = current_smokers["sex"].value_counts(normalize=True)
never_smokers_sex_counts = never_smokers["sex"].value_counts(normalize=True)


# Getting the proportions of males and females in current-smokers and never-smokers.
male_percentages = [
    current_smokers_sex_counts.get("Male", 0) * 100,
    never_smokers_sex_counts.get("Male", 0) * 100
]


female_percentages = [
    current_smokers_sex_counts.get("Female", 0) * 100,
    never_smokers_sex_counts.get("Female", 0) * 100
]


# Creating the plot.
plt.figure(figsize=(5, 4))


# Creating the male part of each bar.
smoking_groups = ["Current smokers", "Never-smokers"]


plt.bar(
    smoking_groups,
    male_percentages,
    width=0.55,
    color="#56B4E9",
    label="Male"
)


# Adding the female part on top of the male part.
plt.bar(
    smoking_groups,
    female_percentages,
    width=0.55,
    bottom=male_percentages,
    color="#CC79A7",
    label="Female"
)


# Naming the y-axis and title, and adding a legend.
plt.ylabel("Percentage (%)")
plt.title("Sex Composition by Smoking Status")
plt.ylim(0, 100)
plt.legend(loc="upper right")


# Adding the percentage values in the middle of each section of the bars.
for i in range(len(smoking_groups)):

    # Male percentage in the middle of the male section.
    plt.text(
        i,
        male_percentages[i] / 2,
        f"{male_percentages[i]:.1f}%",
        ha="center",
        va="center",
        fontsize=11,
        fontweight="bold"
    )

    # Female percentage in the middle of the female section.
    plt.text(
        i,
        male_percentages[i] + female_percentages[i] / 2,
        f"{female_percentages[i]:.1f}%",
        ha="center",
        va="center",
        fontsize=11,
        fontweight="bold"
    )


# Adding a light horizontal grid.
plt.grid(axis="y", alpha=0.2)

plt.tight_layout()


# Showing the plot.
plt.show()
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------