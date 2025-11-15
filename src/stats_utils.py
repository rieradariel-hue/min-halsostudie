# Källa: Video (funktioner)

def calculate_descriptive_stats(df, columns):
    
 # Räknar medel, median, min, max för relevanta kolumner.

 # df (pd.DataFrame): Data
 # columns (list): Lista med kolumnnamn
    
 # dict: Resultat per kolumn
    
    results = {}
    for col in columns:
        results[col] = {
            "mean": df[col].mean(),
            "median": df[col].median(),
            "min": df[col].min(),
            "max": df[col].max()
        }
    return results