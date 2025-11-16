# Källa: Videor (Matplotlib), (moduler)

# Här tänkte jag samla alla grafer i en funktion som kan köras från notebook.
# Bara lite renare än att ha mycket kod där.
# Tänkte lite somm en "presentation" med tre slides.

import matplotlib.pyplot as plt

def plot_all_graphs(df):
    # Slide 1: Histogram
    print("=== FIG 1: BLODTRYCKSFÖRDELNING ===")
    print("Vi ritar histogram för att se hur blodtrycket är fördelat")
    print("Är det normalfördelat?)")
    print()
    
    plt.figure(figsize=(8, 5))
    plt.hist(df["systolic_bp"], bins=20, color="skyblue", edgecolor="black")
    plt.title("Hur ser blodtrycket ut i studien?")
    plt.xlabel("Systoliskt blodtryck (mmHg)")
    plt.ylabel("Antal personer")
    plt.show()

    # Slide 2: Boxplot
    print("=== FIG 2: VIKT PER KÖN ===")
    print("Jämför vikt mellan män och kvinnor")
    print("Finns skillnad? (median, spridning, outliers)")
    print()
    
    plt.figure(figsize=(6, 6))
    df.boxplot(column="weight", by="sex", grid=False, patch_artist=True,
               boxprops=dict(facecolor="lightgreen", color="black"),
               medianprops=dict(color="red"))
    plt.title("Vikt – skillnad mellan män och kvinnor?")
    plt.suptitle("")
    plt.xlabel("Kön")
    plt.ylabel("Vikt (kg)")
    plt.show()

    # Slide 3: Rökare
    print("=== FIG 3: ANDEL RÖKARE ===")
    print("Hur många röker egentligen?")
    print("Procentfördelning med stapeldiagram")
    print()
    
    counts = df["smoker"].value_counts(normalize=True)[["Yes", "No"]]
    plt.figure(figsize=(6, 5))
    counts.plot(kind="bar", color=["salmon", "lightgray"], edgecolor="black")
    plt.title("Hur många röker i studien?")
    plt.xlabel("Rökare")
    plt.ylabel("Andel")
    plt.xticks(rotation=0)
    plt.ylim(0, 1)
    for i, v in enumerate(counts):
        plt.text(i, v + 0.01, f"{v:.1%}", ha="center", fontweight="bold")
    plt.show()